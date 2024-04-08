"""
Facade Design Pattern

Facade method or Facade Design Pattern it provide a unified interface
to a set of interfaces in a subsystem. Facade defines a higher-level
interface that makes the subsystem easier to use. The facade pattern
is like that outer wall. It hides the complexity of the underlying system
and provides a simple interface that clientscan use to interact with the system.

Link: https://www.youtube.com/watch?v=K4FkHVO5iac&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=9
"""

class VideoFile:

    def __init__(self, filename: str):
        self.filename: str = filename

class OggCompressionCodec:
    ...

class MPEG4CompressionCodec:
    ...

class VideoConverter:

    def convert(self, filename: str, format: str):
        file = VideoFile(filename)
        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()
