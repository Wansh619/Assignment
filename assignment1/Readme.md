# Railway Reservation System

## Overview
The Railway Reservation System is a simple Python program that allows users to manage train reservations. It provides functionalities such as adding trains, booking tickets, canceling tickets, and checking ticket status.

## Features
- Add new trains with a unique ID, name, and total seats.
- Book tickets for a train, automatically assigning the next available seat.
- Cancel tickets by providing the booking ID.
- Check ticket status using the booking ID.
- Console-based menu for user interaction.

## Installation
1. Ensure you have Python installed (version 3.x recommended).
2. Download or clone the repository.
3. Navigate to the project directory.

## Usage
Run the program using the following command:
```sh
python railway_reservation.py
```

## Menu Options
Upon running the program, the following options will be displayed:
1. **Add Train**: Enter the train ID, name, and total seats.
2. **Book Ticket**: Provide the train ID to book a ticket.
3. **Cancel Ticket**: Enter the booking ID to cancel a reservation.
4. **Check Ticket Status**: Enter the booking ID to view the reservation details.
5. **Exit**: Close the program.

## Example Usage
### Adding a Train:
```sh
Enter Train ID: 123
Enter Train Name: Express Train
Enter Total Seats: 10
Train Express Train added successfully.
```

### Booking a Ticket:
```sh
Enter Train ID: 123
Booking successful. Booking ID: B1, Seat Number: 1
```

### Canceling a Ticket:
```sh
Enter Booking ID: B1
Cancellation successful for Booking ID: B1
```

### Checking Ticket Status:
```sh
Enter Booking ID: B1
Booking ID not found
```

## Known Issues
- No GUI interface (currently console-based only).
- No persistence (data is lost when the program exits).

## Future Improvements
- Implement a database to store booking details permanently.
- Develop a web-based or GUI application for better user experience.
- Add more train management features, such as schedule tracking.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## Author
Wansh Singh

