"""
Observer Design Pattern Module

The Observer Design Pattern is a behavioral design pattern that defines
a one-to-many dependency between objects so that when one object (the subject)
changes state, all its dependents (observers) are notified and updated automatically.

Link: https://www.youtube.com/watch?v=_BpmfnqjgzQ&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=2
"""

from abc import ABC, abstractmethod


# Define your interfaces.

class IObserver(ABC):

    @abstractmethod
    def update(self):
        ...

class ISubject(ABC):

    @abstractmethod
    def register(self, observer: IObserver):
        ...

    @abstractmethod
    def unregister(self, observer: IObserver):
        ...

    @abstractmethod
    def notify(self):
        ...

# Define your concrete classes.

class WeatherStation(ISubject):

    def __init__(self) -> None:
        self.observers: list[IObserver] = []
        self.temperature: int = 10  # There should be a method to get latest temperature.

    def register(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def unregister(self, observer: IObserver) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update()

    def get_temperature(self) -> int:
        return self.temperature

class PhoneDisplay(IObserver):

    def __init__(self, weather_station: WeatherStation) -> None:
       self.weather_station = weather_station

    def update(self) -> None:
        print(self.weather_station.get_temperature())  # You can do whatever operation needs to be performed.
