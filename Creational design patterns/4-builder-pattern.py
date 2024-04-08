"""
Builder Design Pattern

Builder is a creational design pattern that lets you construct complex
objects step by step. The pattern allows you to produce different types
and representations of an object using the same construction code.

Link: https://refactoring.guru/design-patterns/builder
"""

from abc import ABC, abstractmethod


class Desktop:

    monitor: str
    keyboard: str
    mouse: str
    speaker: str
    ram: str
    processor: str
    motherboard: str

    def set_monitor(self, monitor: str) -> None:
        self.monitor: str = monitor

    def set_keyboard(self, keyboard: str) -> None:
        self.keyboard: str = keyboard

    def set_mouse(self, mouse: str) -> None:
        self.mouse: str = mouse

    def set_speaker(self, speaker: str) -> None:
        self.speaker: str = speaker

    def set_ram(self, ram: str) -> None:
        self.ram: str = ram

    def set_processor(self, processor: str) -> None:
        self.processor: str = processor

    def set_motherboard(self, motherboard: str) -> None:
        self.motherboard: str = motherboard

    def show_spec(self) -> None:
        print("-----------------------------------------------------------")
        print("Monitor", self.monitor)
        print("Keyboard", self.keyboard)
        print("Mouse", self.mouse)
        print("Speaker", self.speaker)
        print("Ram", self.ram)
        print("Processor", self.processor)
        print("Motherboard", self.motherboard)
        print("-----------------------------------------------------------")


class DesktopBuilder(ABC):

    desktop: Desktop

    def __init__(self):
        self.desktop = Desktop()

    @abstractmethod
    def build_monitor(self) -> None:
        ...

    @abstractmethod
    def build_keyboard(self) -> None:
        ...

    @abstractmethod
    def build_mouse(self) -> None:
        ...

    @abstractmethod
    def build_speaker(self) -> None:
        ...

    @abstractmethod
    def build_ram(self) -> None:
        ...

    @abstractmethod
    def build_processor(self) -> None:
        ...

    @abstractmethod
    def build_motherboard(self) -> None:
        ...

    def get_desktop(self) -> Desktop:
        return self.desktop


class DesktopDirector:

    desktop_builder: DesktopBuilder

    def __init__(self, desktop_builder: DesktopBuilder) -> None:
        self.desktop_builder = desktop_builder

    def build_desktop(self) -> Desktop:
        self.desktop_builder.build_monitor()
        self.desktop_builder.build_keyboard()
        self.desktop_builder.build_mouse()
        self.desktop_builder.build_speaker()
        self.desktop_builder.build_ram()
        self.desktop_builder.build_processor()
        self.desktop_builder.build_motherboard()
        return self.desktop_builder.get_desktop()


class DellDesktopBuilder(DesktopBuilder):

    def build_monitor(self) -> None:
        self.desktop.set_monitor("Dell Monitor.")

    def build_keyboard(self) -> None:
        self.desktop.set_keyboard("Dell Keyboard.")

    def build_mouse(self) -> None:
        self.desktop.set_mouse("Dell Mouse.")

    def build_speaker(self) -> None:
        self.desktop.set_speaker("Dell Speaker.")

    def build_ram(self) -> None:
        self.desktop.set_ram("Dell RAM.")

    def build_processor(self) -> None:
        self.desktop.set_processor("Dell Processor.")

    def build_motherboard(self) -> None:
        self.desktop.set_motherboard("Dell Motherboard.")


class HPDesktopBuilder(DesktopBuilder):

    def build_monitor(self) -> None:
        self.desktop.set_monitor("HP Monitor.")

    def build_keyboard(self) -> None:
        self.desktop.set_keyboard("HP Keyboard.")

    def build_mouse(self) -> None:
        self.desktop.set_mouse("HP Mouse.")

    def build_speaker(self) -> None:
        self.desktop.set_speaker("HP Speaker.")

    def build_ram(self) -> None:
        self.desktop.set_ram("HP RAM.")

    def build_processor(self) -> None:
        self.desktop.set_processor("HP Processor.")

    def build_motherboard(self) -> None:
        self.desktop.set_motherboard("HP Motherboard.")


dell_desktop: Desktop = DesktopDirector(DellDesktopBuilder()).build_desktop()
dell_desktop.show_spec()

hp_desktop: Desktop = DesktopDirector(HPDesktopBuilder()).build_desktop()
hp_desktop.show_spec()
