"""
Parking Lot.

Requirements:
A parking lot system manages vehicles parking in and out, with different
parking spot sizes and rates. Key requirements include:
    - Parking Space Management: Track the availability of parking spaces.
    - Vehicle Management: Handle the entry and exit of vehicles.
    - Fee Calculation: Calculate parking fees based on parking duration.
    - Parking Lot Capacity: Support different types of vehicles with designated spots (e.g., compact, large, handicapped).

Core Use Cases:
    - Parking a Vehicle: Assigning spots to vehicles and recording entry time.
    - Unparking a Vehicle: Removing a vehicle and calculating the fee.
    - Spot Availability Check: Checking for available spots for specific vehicles.
    - Handling Different Vehicle Types.
"""

from abc import ABC
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class VehicleType(Enum):

    COMPACT = "compact"
    LARGE = "large"
    HANDICAPPED = "handicapped"


class Vehicle(ABC):

    license_number: str
    vehicle_type: str

    def __init__(self, license_number: str, vechicle_type: VehicleType) -> None:
        self.license_number = license_number
        self.vehicle_type = vechicle_type.value

    # Other attributes and methods.


class Car(Vehicle):
    # Car specific attributes.
    ...


class ParkingSpot:

    spot_id: str
    vehicle_type: str
    is_occupied: bool

    def __init__(self, spot_id: str, vehicle_type: VehicleType) -> None:
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type.value
        self.is_occupied = False

    def occupy_spot(self) -> None:
        self.is_occupied = True

    def free_spot(self) -> None:
        self.is_occupied = False

    # Other getter and setter methods.


class CarSpot(ParkingSpot):
    ...


class ParkingTicket:

    ticket_id: str
    issued_at: datetime
    paid_at: datetime
    fee: float

    def __init__(self, ticket_id: str) -> None:
        self.ticket_id = ticket_id
        self.issued_at = datetime.now(timezone.utc)

    def mark_paid(self, paid_at: datetime, fee: float) -> None:
        self.paid_at = paid_at
        self.fee = fee

    # Other getter and setter methods.


class FeeCalculator:

    def calculate_fee(self, issued_at: datetime, paid_at: datetime) -> float:
        # Logic for calculating fee based on the visit duration.
        ...


class ParkingLot:

    parking_spots: list[ParkingSpot]
    parking_tickets: list[ParkingTicket]

    def __init__(self, parking_spots: list[ParkingSpot]) -> None:
        self.parking_spots = parking_spots
        self.parking_tickets = []

    def find_free_spots(self, vehicle_type: VehicleType) -> Optional[ParkingSpot]:
        # Logic for finding parking spot based on the vehicle type.
        ...

    def issue_ticket(self, vehicle_type: VehicleType) -> Optional[ParkingTicket]:
        spot = self.find_free_spots(vehicle_type)

        if not spot:
            return None

        spot.occupy_spot()
        ticket = ParkingTicket(self.generate_ticket_id())
        self.parking_tickets.append(ticket)
        return ticket

    def process_payment(self, ticket: ParkingTicket):
        current_datetime = datetime.now(timezone.utc)
        fee: float = FeeCalculator().calculate_fee(ticket.issued_at, current_datetime)
        ticket.mark_paid(current_datetime, fee)

    def generate_ticket_id(self) -> str:
        # Logic for generating a unique ticket id.
        # "TICKET" + current time in milliseconds
        ...

    # Other necessary methods.


class ParkingFloor:
    spots: list[ParkingSpot]
    ...
