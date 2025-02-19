import pandas as pd
import json
import re
from fuzzywuzzy import process

def load_schema(schema_path):
    with open(schema_path) as f:
        schema = json.load(f)
    return schema

def extract_currency(col_name):
    currency_pattern = re.compile(r'\(([A-Z]{3})\)|_([A-Z]{3})$')
    match = currency_pattern.search(col_name)
    return match.group(1) or match.group(2) if match else None

def extract_unit(col_name):
    unit_pattern = re.compile(r'_([a-z]{2,3})$', re.IGNORECASE)
    match = unit_pattern.search(col_name)
    return match.group(1).lower() if match else None

def convert_to_kg(value, unit):
    unit_conversion = {'lb': 0.453592, 'g': 0.001, 'kg': 1.0}
    return value * unit_conversion.get(unit, 1.0)

def normalize_category(input_category, allowed_categories):
    if not input_category or pd.isna(input_category):
        return None
    best_match, score = process.extractOne(str(input_category), allowed_categories)
    return best_match if score >= 80 else input_category

def harmonize_data(input_csv, schema_path, output_csv, log_file):
    schema = load_schema(schema_path)
    standard_fields = [field['name'] for field in schema['fields']]
    allowed_categories = next((f['allowed_values'] for f in schema['fields'] if f['name'] == 'category'), [])
    
    df = pd.read_csv(input_csv)
    log = []
    cleaned_data = {field: [] for field in standard_fields}
    
    column_mapping = {}
    currency_col = None
    weight_col = None

    for col in df.columns:
        col_lower = col.lower()
        if 'price' in col_lower or 'cost' in col_lower:
            currency = extract_currency(col)
            column_mapping[col] = ('price', currency)
            currency_col = col
        elif 'weight' in col_lower:
            unit = extract_unit(col)
            column_mapping[col] = ('weight_kg', unit)
            weight_col = col
        else:
            best_match = process.extractOne(col, standard_fields, score_cutoff=70)
            if best_match:
                column_mapping[col] = (best_match[0], None)

    for index, row in df.iterrows():
        cleaned_row = {field: None for field in standard_fields}
        
        # Process mapped columns
        for src_col, (tgt_field, extra) in column_mapping.items():
            value = row[src_col]
            if pd.isna(value):
                continue
            if tgt_field == 'price':
                try:
                    cleaned_row['price'] = float(re.sub(r'[^\d.]', '', str(value)))
                    if extra:
                        cleaned_row['currency'] = extra
                except:
                    log.append(f"Row {index}: Invalid price value '{value}'")
            elif tgt_field == 'weight_kg':
                try:
                    weight = float(value)
                    cleaned_row['weight_kg'] = convert_to_kg(weight, extra)
                except:
                    log.append(f"Row {index}: Invalid weight value '{value}'")
            else:
                cleaned_row[tgt_field] = value
        
   
        if 'category' in cleaned_row:
            cleaned_row['category'] = normalize_category(cleaned_row['category'], allowed_categories)
        
        for field in standard_fields:
            cleaned_data[field].append(cleaned_row.get(field))
    
    cleaned_df = pd.DataFrame(cleaned_data)
    cleaned_df.drop_duplicates(inplace=True)
    cleaned_df.to_csv(output_csv, index=False)
    
    with open(log_file, 'w') as f:
        f.write('\n'.join(log))

if __name__ == "__main__":
    input_csv_file= input("[ENTER INPUT CSV FILE PATH]: ")
    output_csv_file=input("[ENTER OUTPUT CSV FILE PATH]: ")
    harmonize_data(
        input_csv=input_csv_file,
        schema_path='data.json',
        output_csv=output_csv_file,
        log_file='transformations.log'
    )