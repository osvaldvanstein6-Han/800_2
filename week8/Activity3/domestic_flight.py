# Activity 8 - Activity 3
# Single Inheritance - Air New Zealand Domestic Flight System

# Parent class
class GeneralFlight:
    def __init__(self, flight_number, airline, departure, destination, departure_time):
        # These attributes are shared by all flights
        self.flight_number = flight_number
        self.airline = airline
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time

    # This method can be used by the parent class and inherited by the subclass
    def display_flight_info(self):
        print("Flight Information")
        print("------------------")
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")

    # Shared method
    def check_status(self):
        print(f"Flight {self.flight_number} is scheduled on time.")


# Subclass
# DomesticFlight inherits from GeneralFlight
class DomesticFlight(GeneralFlight):
    def __init__(
        self,
        flight_number,
        airline,
        departure,
        destination,
        departure_time,
        aircraft_type,
        gate_number
    ):
        # super() calls the parent class constructor
        super().__init__(flight_number, airline, departure, destination, departure_time)

        # These attributes are specific to domestic flights
        self.aircraft_type = aircraft_type
        self.gate_number = gate_number

    # Method specific to DomesticFlight
    def display_domestic_details(self):
        print("Domestic Flight Details")
        print("-----------------------")
        print(f"Aircraft Type: {self.aircraft_type}")
        print(f"Gate Number: {self.gate_number}")

    # Method specific to DomesticFlight
    def boarding_announcement(self):
        print(
            f"Air New Zealand flight {self.flight_number} from "
            f"{self.departure} to {self.destination} is now boarding at {self.gate_number}."
        )


# Main program
def main():
    # Create an object from the subclass
    domestic_flight = DomesticFlight(
        "NZ123",
        "Air New Zealand",
        "Auckland",
        "Wellington",
        "10:30 AM",
        "Airbus A320",
        "Gate 12"
    )

    # These methods are inherited from GeneralFlight
    domestic_flight.display_flight_info()
    domestic_flight.check_status()

    print()

    # These methods belong to DomesticFlight
    domestic_flight.display_domestic_details()
    domestic_flight.boarding_announcement()


if __name__ == "__main__":
    main()