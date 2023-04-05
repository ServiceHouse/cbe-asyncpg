import codecs
import typing
import uuid

class CodecContext:
    def get_text_codec(self) -> codecs.CodecInfo: ...

class ReadBuffer: ...
class WriteBuffer: ...
class BufferError(Exception): ...

class UUID(uuid.UUID):
    def __init__(self, inp: typing.AnyStr) -> None: ...