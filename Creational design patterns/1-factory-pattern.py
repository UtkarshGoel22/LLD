"""
Factory Design Pattern Module

Factory Method is a creational design pattern that provides an
interface for creating objects in a superclass, but allows
subclasses to alter the type of objects that will be created.

Link: https://www.youtube.com/watch?v=EcFVTgRHJLM&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=4
"""

from abc import ABC, abstractmethod

# Define interface.

class Vehicle(ABC):

    @abstractmethod
    def create_vehicle(self):
        ...

# Define concrete classes.

class Bike(Vehicle):

    def create_vehicle(self) -> None:
        print("Creating bike.")

class Car(Vehicle):

    def create_vehicle(self) -> None:
        print("Creating car.")

VEHICLE_CLASS_MAPPER = {
    "car": Car,
    "bike": Bike,
}

# Define factory

class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        return VEHICLE_CLASS_MAPPER[vehicle_type]()


vehicle1: Vehicle = VehicleFactory.get_vehicle("bike")
vehicle1.create_vehicle()

vehicle2: Vehicle = VehicleFactory.get_vehicle("car")
vehicle2.create_vehicle()
