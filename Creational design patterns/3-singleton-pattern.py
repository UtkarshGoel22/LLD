"""
Singleton Design Pattern

Singleton Method or Singleton Design Patterns ensure a class
only has one instance and provide glocal point of access to it.

Link: https://www.youtube.com/watch?v=hUE_j6q0LTQ&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=6
"""

class Singleton:

    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
