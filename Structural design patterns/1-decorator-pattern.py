"""
Decorator Design Pattern Module

The Decorator Design Pattern is a structural design pattern that
allows behavior to be added to individual objects dynamically, without
affecting the behavior of other objects from the same class. It involves
creating a set of decorator classes that are used to wrap concrete components.

Link: https://www.youtube.com/watch?v=GCraGHx6gso&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=3
"""

from abc import ABC, abstractmethod


# Define your interfaces.

class Beverage(ABC):

    @abstractmethod
    def cost(self) -> int:
        ...

class AddOnDecorator(Beverage):

    @abstractmethod
    def cost(self) -> int:
        ...

# Define your concrete classes.

class Espresso(Beverage):

    def cost(self) -> int:
        return 1

class Caramel(AddOnDecorator):

    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage

    def cost(self) -> int:
        return self.beverage.cost() + 2


beverage = Caramel(Espresso())
print(beverage.cost())
