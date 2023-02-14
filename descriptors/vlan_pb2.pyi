import _shared_pb2 as __shared_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

from _shared_pb2 import ResponseStatus
from _shared_pb2 import id
from _shared_pb2 import name
DESCRIPTOR: _descriptor.FileDescriptor

class vLANResponse(_message.Message):
    __slots__ = ["status", "vlan"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    status: __shared_pb2.ResponseStatus
    vlan: vlan
    def __init__(self, vlan: _Optional[_Union[vlan, _Mapping]] = ..., status: _Optional[_Union[__shared_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class vlan(_message.Message):
    __slots__ = ["dataLastSeen", "dateLastEdited", "description", "id", "name", "vlanNumber"]
    DATALASTSEEN_FIELD_NUMBER: _ClassVar[int]
    DATELASTEDITED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VLANNUMBER_FIELD_NUMBER: _ClassVar[int]
    dataLastSeen: str
    dateLastEdited: str
    description: str
    id: str
    name: str
    vlanNumber: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., vlanNumber: _Optional[int] = ..., description: _Optional[str] = ..., dataLastSeen: _Optional[str] = ..., dateLastEdited: _Optional[str] = ...) -> None: ...
