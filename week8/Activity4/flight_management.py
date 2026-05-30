# Week 8 - Activity 4
# Hybrid Inheritance - Air New Zealand Flight Management System


class Flight:
    def __init__(self, flight_number, airline, departure, destination):
        self.flight_number = flight_number
        self.airline = airline
        self.departure = departure
        self.destination = destination

    def display_basic_info(self):
        print("Basic Flight Information")
        print("------------------------")
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")

    def check_status(self):
        print(f"Flight {self.flight_number} is currently scheduled.")

    def update_destination(self, new_destination):
        self.destination = new_destination
        print(f"Destination updated to {self.destination}.")


class DomesticFlight(Flight):
    def __init__(self, flight_number, airline, departure, destination, domestic_gate):
        super().__init__(flight_number, airline, departure, destination)
        self.domestic_gate = domestic_gate

    def display_domestic_info(self):
        print("Domestic Flight Information")
        print("---------------------------")
        print(f"Domestic Gate: {self.domestic_gate}")

    def boarding_domestic(self):
        print(f"Domestic flight {self.flight_number} is boarding at {self.domestic_gate}.")

    def domestic_baggage_rule(self):
        print("Domestic baggage allowance is 1 checked bag.")


class InternationalFlight(Flight):
    def __init__(self, flight_number, airline, departure, destination, passport_required, international_terminal):
        super().__init__(flight_number, airline, departure, destination)
        self.passport_required = passport_required
        self.international_terminal = international_terminal

    def display_international_info(self):
        print("International Flight Information")
        print("--------------------------------")
        print(f"Passport Required: {self.passport_required}")
        print(f"International Terminal: {self.international_terminal}")

    def check_passport_requirement(self):
        print(f"Passport required: {self.passport_required}")

    def international_baggage_rule(self):
        print("International baggage allowance is 2 checked bags.")


class ManagedFlight(DomesticFlight, InternationalFlight):
    def __init__(
        self,
        flight_number,
        airline,
        departure,
        destination,
        domestic_gate,
        passport_required,
        international_terminal,
        manager_name
    ):
        Flight.__init__(self, flight_number, airline, departure, destination)
        self.domestic_gate = domestic_gate
        self.passport_required = passport_required
        self.international_terminal = international_terminal
        self.manager_name = manager_name

    def display_management_info(self):
        print("Managed Flight Information")
        print("--------------------------")
        print(f"Flight Manager: {self.manager_name}")

    def assign_manager(self, new_manager):
        self.manager_name = new_manager
        print(f"New manager assigned: {self.manager_name}")

    def display_complete_flight_info(self):
        self.display_basic_info()
        print()
        self.display_domestic_info()
        print()
        self.display_international_info()
        print()
        self.display_management_info()


def main():
    managed_flight = ManagedFlight(
        "NZ789",
        "Air New Zealand",
        "Auckland",
        "Sydney",
        "Domestic Gate 5",
        True,
        "International Terminal A",
        "Han"
    )

    managed_flight.display_complete_flight_info()
    print()

    managed_flight.check_status()
    managed_flight.boarding_domestic()
    managed_flight.check_passport_requirement()
    managed_flight.domestic_baggage_rule()
    managed_flight.international_baggage_rule()


if __name__ == "__main__":
    main()