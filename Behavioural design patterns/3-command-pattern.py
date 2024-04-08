"""
Command Design Pattern

Command is a behavioral design pattern that turns a request into a
stand-alone object that contains all information about the request.
This transformation lets you pass requests as a method arguments,
delay or queue a request’s execution, and support undoable operations.

Link: https://www.youtube.com/watch?v=9qA5kw8dcSU&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=7
"""

from abc import ABC, abstractmethod


class ICommand(ABC):

    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def unexecute(self):
        ...

class Light:

    def on(self):
        print("Turn on light.")

    def off(self):
        print("Turn off light.")

class LightOnCommand(ICommand):

    def __init__(self):
        self.light = Light()  # We can also pass the object as arguments.

    def execute(self):
        self.light.on()

    def unexecute(self):
        self.light.off()

class Invoker:

    def __init__(self):
        self.on = LightOnCommand()  # We can also pass the object as arguments.

    def click_on(self):
        self.on.execute()
