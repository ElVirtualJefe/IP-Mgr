import _shared_pb2 as __shared_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

from _shared_pb2 import ResponseStatus
from _shared_pb2 import id
from _shared_pb2 import name
DESCRIPTOR: _descriptor.FileDescriptor

class IpAddressResponse(_message.Message):
    __slots__ = ["ipAddress", "status"]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ipAddress: ipAddress
    status: __shared_pb2.ResponseStatus
    def __init__(self, ipAddress: _Optional[_Union[ipAddress, _Mapping]] = ..., status: _Optional[_Union[__shared_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class ipAddress(_message.Message):
    __slots__ = ["dataLastSeen", "dateCreated", "dateLastEdited", "description", "hostname", "id", "ipAddress", "is_gateway", "macAddress", "owner", "state_id", "subnet_id"]
    DATALASTSEEN_FIELD_NUMBER: _ClassVar[int]
    DATECREATED_FIELD_NUMBER: _ClassVar[int]
    DATELASTEDITED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    dataLastSeen: str
    dateCreated: str
    dateLastEdited: str
    description: str
    hostname: str
    id: str
    ipAddress: str
    is_gateway: bool
    macAddress: str
    owner: str
    state_id: str
    subnet_id: str
    def __init__(self, id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., ipAddress: _Optional[str] = ..., is_gateway: bool = ..., description: _Optional[str] = ..., hostname: _Optional[str] = ..., macAddress: _Optional[str] = ..., owner: _Optional[str] = ..., state_id: _Optional[str] = ..., dataLastSeen: _Optional[str] = ..., dateLastEdited: _Optional[str] = ..., dateCreated: _Optional[str] = ...) -> None: ...
