"""
Abstract Factory Design Pattern Module

Abstract Factory is a creational design pattern that lets you produce
families of related objects without specifying their concrete classes.
In simpler terms the Abstract Factory Pattern is a way of organizing
how you create groups of things that are related to each other.

Link: https://www.youtube.com/watch?v=v-GiuMmsXj4&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=5
"""

from abc import ABC, abstractmethod

# Define interfaces.

class IButton(ABC):

    @abstractmethod
    def press(self):
        ...

class ITextBox(ABC):

    @abstractmethod
    def show_text(self):
        ...

class IFactory(ABC):

    @abstractmethod
    def create_button(self) -> IButton:
        ...

    @abstractmethod
    def create_textbox(self) -> ITextBox:
        ...

# Define concrete classes.

class MacButton(IButton):

    def press(self) -> None:
        print("Mac button pressed.")

class WindowsButton(IButton):

    def press(self) -> None:
        print("Windows button pressed.")

class MacTextBox(ITextBox):

    def show_text(self) -> None:
        print("Mac text box.")

class WindowsTextBox(ITextBox):

    def show_text(self) -> None:
        print("Windows text box.")

class MacFactory(IFactory):

    def create_button(self) -> IButton:
        return MacButton()

    def create_textbox(self) -> ITextBox:
        return MacTextBox()

class WindowsFactory(IFactory):

    def create_button(self) -> IButton:
        return WindowsButton()

    def create_textbox(self) -> ITextBox:
        return WindowsTextBox()

class GUIAbstractFactory:

    @staticmethod
    def create_factory(os_type: str) -> IFactory:
        if (os_type == "mac"):
            return MacFactory()
        elif (os_type == "windows"):
            return WindowsFactory()
        else:
            return WindowsFactory()

factory1: IFactory = GUIAbstractFactory.create_factory("mac")
button1: IButton = factory1.create_button()
textbox1: ITextBox = factory1.create_textbox()

button1.press()
textbox1.show_text()
