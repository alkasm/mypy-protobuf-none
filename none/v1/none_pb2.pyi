"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NONE_FIELD_NUMBER: builtins.int

    @property
    def none(self) -> global___None: ...

    def __init__(self,
        *,
        none : typing.Optional[global___None] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"none",b"none"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"none",b"none"]) -> None: ...
global___Message = Message

class OtherMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NONE_FIELD_NUMBER: builtins.int

    def __init__(self,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"None",b"None"]) -> None: ...
global___OtherMessage = OtherMessage
