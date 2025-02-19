class Train:
    def __init__(self, train_id, train_name, total_seats):
        self.train_id = train_id
        self.train_name = train_name
        self.total_seats = total_seats
        self.seats = [False] * total_seats

    def is_seat_available(self):
        return any(not seat for seat in self.seats)

    def book_seat(self):
        for i in range(self.total_seats):
            if not self.seats[i]:
                self.seats[i] = True
                return i + 1
        return -1

    def cancel_seat(self, seat_number):
        if 0 < seat_number <= self.total_seats:
            self.seats[seat_number - 1] = False


class Booking:
    def __init__(self, booking_id, train_id, seat_number):
        self.booking_id = booking_id
        self.train_id = train_id
        self.seat_number = seat_number


class RailwayReservationSystem:
    def __init__(self):
        self.trains = {}
        self.bookings = {}
        self.booking_counter = 1

    def add_train(self, train_id, train_name, total_seats):
        self.trains[train_id] = Train(train_id, train_name, total_seats)
        print(f"Train {train_name} added successfully.")

    def book_ticket(self, train_id):
        if train_id not in self.trains:
            return "Train not found"
        
        train = self.trains[train_id]
        if not train.is_seat_available():
            return "No seats available"
        
        seat_number = train.book_seat()
        booking_id = f"B{self.booking_counter}"
        self.booking_counter += 1
        self.bookings[booking_id] = Booking(booking_id, train_id, seat_number)
        return f"Booking successful. Booking ID: {booking_id}, Seat Number: {seat_number}"

    def cancel_ticket(self, booking_id):
        if booking_id not in self.bookings:
            return "Booking ID not found"
        
        booking = self.bookings[booking_id]
        if booking.train_id in self.trains:
            self.trains[booking.train_id].cancel_seat(booking.seat_number)
        
        del self.bookings[booking_id]
        return f"Cancellation successful for Booking ID: {booking_id}"

    def check_ticket_status(self, booking_id):
        if booking_id not in self.bookings:
            return "Booking ID not found"
        
        booking = self.bookings[booking_id]
        return f"Booking ID: {booking.booking_id}, Train ID: {booking.train_id}, Seat Number: {booking.seat_number}"


def main():
    system = RailwayReservationSystem()
    while True:
        print("\nRailway Reservation System")
        print("1. Add Train")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Check Ticket Status")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            train_id = input("Enter Train ID: ")
            train_name = input("Enter Train Name: ")
            total_seats = int(input("Enter Total Seats: "))
            system.add_train(train_id, train_name, total_seats)
        elif choice == '2':
            train_id = input("Enter Train ID: ")
            print(system.book_ticket(train_id))
        elif choice == '3':
            booking_id = input("Enter Booking ID: ")
            print(system.cancel_ticket(booking_id))
        elif choice == '4':
            booking_id = input("Enter Booking ID: ")
            print(system.check_ticket_status(booking_id))
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "_main_":
    main()