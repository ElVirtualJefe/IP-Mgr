import _shared_pb2 as __shared_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

from _shared_pb2 import ResponseStatus
from _shared_pb2 import id
from _shared_pb2 import name
DESCRIPTOR: _descriptor.FileDescriptor

class SubnetResponse(_message.Message):
    __slots__ = ["status", "subnet"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    status: __shared_pb2.ResponseStatus
    subnet: subnet
    def __init__(self, subnet: _Optional[_Union[subnet, _Mapping]] = ..., status: _Optional[_Union[__shared_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class subnet(_message.Message):
    __slots__ = ["dataLastSeen", "dateLastEdited", "description", "hostname", "id", "ipAddress", "is_gateway", "macAddress", "owner", "state_id", "subnet_id", "vlan_id"]
    DATALASTSEEN_FIELD_NUMBER: _ClassVar[int]
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
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    dataLastSeen: str
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
    vlan_id: str
    def __init__(self, id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., vlan_id: _Optional[str] = ..., ipAddress: _Optional[str] = ..., is_gateway: bool = ..., description: _Optional[str] = ..., hostname: _Optional[str] = ..., macAddress: _Optional[str] = ..., owner: _Optional[str] = ..., state_id: _Optional[str] = ..., dataLastSeen: _Optional[str] = ..., dateLastEdited: _Optional[str] = ...) -> None: ...
