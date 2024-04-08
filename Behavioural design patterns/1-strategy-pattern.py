"""
Strategy Design Pattern Module

The Strategy Design Pattern defines a family of algorithms,
encapsulates each one, and makes them interchangeable, allowing
clients to switch algorithms dynamically without altering the code structure.

Link: https://www.youtube.com/watch?v=v9ejT8FO-7I&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc
"""

from abc import ABC, abstractmethod


# Define your interfaces i.e abstract strategies.

class IQuackStrategy(ABC):

    @abstractmethod
    def quack(self):
        ...

class IDisplayStrategy(ABC):

    @abstractmethod
    def display(self):
        ...

class IFlyingStrategy(ABC):

    @abstractmethod
    def fly(self):
        ...

# Define your concrete strategies.

class SimpleQuack(IQuackStrategy):

    def quack(self) -> None:
        print("Simple quack.")

class NoQuack(IQuackStrategy):

    def quack(self) -> None:
        print("No quack.")

class DisplayGraphically(IDisplayStrategy):

    def display(self) -> None:
        print("Display graphically.")

class DisplayAsText(IDisplayStrategy):

    def display(self) -> None:
        print("Display as text.")

class SimpleFlying(IFlyingStrategy):

    def fly(self) -> None:
        print("Simple flying.")

class JetFlying(IFlyingStrategy):

    def fly(self) -> None:
        print("Jet flying.")

# Define your base class.

class Duck:

    def __init__(
        self,
        quack_instance: IQuackStrategy,
        display_instance: IDisplayStrategy,
        flying_instance: IFlyingStrategy
    ) -> None:
        self.quack_instance: IQuackStrategy = quack_instance
        self.display_instance: IDisplayStrategy = display_instance
        self.flying_instance: IFlyingStrategy = flying_instance

    def quack(self) -> None:
        self.quack_instance.quack()

    def display(self) -> None:
        self.display_instance.display()

    def fly(self) -> None:
        self.flying_instance.fly()

class Duck1(Duck):

    def __init__(self) -> None:
        super().__init__(SimpleQuack(), DisplayGraphically(), SimpleFlying())

class Duck2(Duck):

    def __init__(self) -> None:
        super().__init__(NoQuack(), DisplayAsText(), JetFlying())

duck1 = Duck1()
duck1.quack()
duck1.display()
duck1.fly()

duck2 = Duck2()
duck2.quack()
duck2.display()
duck2.fly()
