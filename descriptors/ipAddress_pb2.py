# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ipAddress.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import _shared_pb2 as __shared__pb2

from _shared_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fipAddress.proto\x1a\r_shared.proto\"\xf0\x01\n\tipAddress\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12\x11\n\tipAddress\x18\x03 \x01(\t\x12\x12\n\nis_gateway\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x10\n\x08hostname\x18\x06 \x01(\t\x12\x12\n\nmacAddress\x18\x07 \x01(\t\x12\r\n\x05owner\x18\x08 \x01(\t\x12\x10\n\x08state_id\x18\t \x01(\t\x12\x14\n\x0c\x64\x61taLastSeen\x18\n \x01(\t\x12\x16\n\x0e\x64\x61teLastEdited\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x61teCreated\x18\x0c \x01(\t\"S\n\x11IpAddressResponse\x12\x1d\n\tipAddress\x18\x01 \x01(\x0b\x32\n.ipAddress\x12\x1f\n\x06status\x18\x02 \x01(\x0b\x32\x0f.ResponseStatus2\xb9\x02\n\x10IpAddressService\x12-\n\x10GetIpAddressById\x12\x03.id\x1a\x12.IpAddressResponse\"\x00\x12\x31\n\x12GetIpAddressByName\x12\x05.name\x1a\x12.IpAddressResponse\"\x00\x12\x31\n\x14GetIpAddressBySubnet\x12\x03.id\x1a\x12.IpAddressResponse\"\x00\x12\x30\n\x0c\x41\x64\x64IpAddress\x12\n.ipAddress\x1a\x12.IpAddressResponse\"\x00\x12\x33\n\x0fUpdateIpAddress\x12\n.ipAddress\x1a\x12.IpAddressResponse\"\x00\x12)\n\x0f\x44\x65leteIpAddress\x12\x03.id\x1a\x0f.ResponseStatus\"\x00P\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ipAddress_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IPADDRESS._serialized_start=35
  _IPADDRESS._serialized_end=275
  _IPADDRESSRESPONSE._serialized_start=277
  _IPADDRESSRESPONSE._serialized_end=360
  _IPADDRESSSERVICE._serialized_start=363
  _IPADDRESSSERVICE._serialized_end=676
# @@protoc_insertion_point(module_scope)
