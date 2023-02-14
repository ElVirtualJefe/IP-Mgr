from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseStatus(_message.Message):
    __slots__ = ["errorMessage", "responseMessage", "statusCode"]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    errorMessage: str
    responseMessage: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., responseMessage: _Optional[str] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class id(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class name(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
