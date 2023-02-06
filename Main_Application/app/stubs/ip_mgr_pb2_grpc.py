# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.descriptors._shared_pb2 as __shared__pb2
import app.descriptors.ipAddress_pb2 as ipAddress__pb2
import app.descriptors.subnet_pb2 as subnet__pb2
import app.descriptors.vlan_pb2 as vlan__pb2


class IpAddressServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetIpAddressById = channel.unary_unary(
                '/IpAddressService/GetIpAddressById',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.GetIpAddressByName = channel.unary_unary(
                '/IpAddressService/GetIpAddressByName',
                request_serializer=__shared__pb2.name.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.GetIpAddressBySubnet = channel.unary_unary(
                '/IpAddressService/GetIpAddressBySubnet',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.AddIpAddress = channel.unary_unary(
                '/IpAddressService/AddIpAddress',
                request_serializer=ipAddress__pb2.ipAddress.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.UpdateIpAddress = channel.unary_unary(
                '/IpAddressService/UpdateIpAddress',
                request_serializer=ipAddress__pb2.ipAddress.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.DeleteIpAddress = channel.unary_unary(
                '/IpAddressService/DeleteIpAddress',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=__shared__pb2.ResponseStatus.FromString,
                )


class IpAddressServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetIpAddressById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIpAddressByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIpAddressBySubnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IpAddressServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetIpAddressById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIpAddressById,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'GetIpAddressByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIpAddressByName,
                    request_deserializer=__shared__pb2.name.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'GetIpAddressBySubnet': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIpAddressBySubnet,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'AddIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.AddIpAddress,
                    request_deserializer=ipAddress__pb2.ipAddress.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'UpdateIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateIpAddress,
                    request_deserializer=ipAddress__pb2.ipAddress.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'DeleteIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIpAddress,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=__shared__pb2.ResponseStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'IpAddressService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IpAddressService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetIpAddressById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IpAddressService/GetIpAddressById',
            __shared__pb2.id.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIpAddressByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IpAddressService/GetIpAddressByName',
            __shared__pb2.name.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIpAddressBySubnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IpAddressService/GetIpAddressBySubnet',
            __shared__pb2.id.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IpAddressService/AddIpAddress',
            ipAddress__pb2.ipAddress.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IpAddressService/UpdateIpAddress',
            ipAddress__pb2.ipAddress.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IpAddressService/DeleteIpAddress',
            __shared__pb2.id.SerializeToString,
            __shared__pb2.ResponseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SubnetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSubnetById = channel.unary_unary(
                '/SubnetService/GetSubnetById',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=subnet__pb2.SubnetResponse.FromString,
                )
        self.GetSubnetByName = channel.unary_unary(
                '/SubnetService/GetSubnetByName',
                request_serializer=__shared__pb2.name.SerializeToString,
                response_deserializer=subnet__pb2.SubnetResponse.FromString,
                )
        self.GetSubnetByIpAddress = channel.unary_unary(
                '/SubnetService/GetSubnetByIpAddress',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=subnet__pb2.SubnetResponse.FromString,
                )
        self.AddSubnet = channel.unary_unary(
                '/SubnetService/AddSubnet',
                request_serializer=subnet__pb2.subnet.SerializeToString,
                response_deserializer=subnet__pb2.SubnetResponse.FromString,
                )
        self.UpdateSubnet = channel.unary_unary(
                '/SubnetService/UpdateSubnet',
                request_serializer=subnet__pb2.subnet.SerializeToString,
                response_deserializer=subnet__pb2.SubnetResponse.FromString,
                )
        self.DeleteSubnet = channel.unary_unary(
                '/SubnetService/DeleteSubnet',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=__shared__pb2.ResponseStatus.FromString,
                )


class SubnetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSubnetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubnetByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubnetByIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSubnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSubnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSubnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubnetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSubnetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubnetById,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=subnet__pb2.SubnetResponse.SerializeToString,
            ),
            'GetSubnetByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubnetByName,
                    request_deserializer=__shared__pb2.name.FromString,
                    response_serializer=subnet__pb2.SubnetResponse.SerializeToString,
            ),
            'GetSubnetByIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubnetByIpAddress,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=subnet__pb2.SubnetResponse.SerializeToString,
            ),
            'AddSubnet': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSubnet,
                    request_deserializer=subnet__pb2.subnet.FromString,
                    response_serializer=subnet__pb2.SubnetResponse.SerializeToString,
            ),
            'UpdateSubnet': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSubnet,
                    request_deserializer=subnet__pb2.subnet.FromString,
                    response_serializer=subnet__pb2.SubnetResponse.SerializeToString,
            ),
            'DeleteSubnet': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSubnet,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=__shared__pb2.ResponseStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SubnetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubnetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSubnetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubnetService/GetSubnetById',
            __shared__pb2.id.SerializeToString,
            subnet__pb2.SubnetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSubnetByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubnetService/GetSubnetByName',
            __shared__pb2.name.SerializeToString,
            subnet__pb2.SubnetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSubnetByIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubnetService/GetSubnetByIpAddress',
            __shared__pb2.id.SerializeToString,
            subnet__pb2.SubnetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSubnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubnetService/AddSubnet',
            subnet__pb2.subnet.SerializeToString,
            subnet__pb2.SubnetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSubnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubnetService/UpdateSubnet',
            subnet__pb2.subnet.SerializeToString,
            subnet__pb2.SubnetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSubnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubnetService/DeleteSubnet',
            __shared__pb2.id.SerializeToString,
            __shared__pb2.ResponseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class vLANServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVlanById = channel.unary_unary(
                '/vLANService/GetVlanById',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=vlan__pb2.vLANResponse.FromString,
                )
        self.GetVlanByName = channel.unary_unary(
                '/vLANService/GetVlanByName',
                request_serializer=__shared__pb2.name.SerializeToString,
                response_deserializer=vlan__pb2.vLANResponse.FromString,
                )
        self.GetVlanByIpAddress = channel.unary_unary(
                '/vLANService/GetVlanByIpAddress',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=vlan__pb2.vLANResponse.FromString,
                )
        self.AddVlan = channel.unary_unary(
                '/vLANService/AddVlan',
                request_serializer=vlan__pb2.vlan.SerializeToString,
                response_deserializer=vlan__pb2.vLANResponse.FromString,
                )
        self.UpdateVlan = channel.unary_unary(
                '/vLANService/UpdateVlan',
                request_serializer=vlan__pb2.vlan.SerializeToString,
                response_deserializer=vlan__pb2.vLANResponse.FromString,
                )
        self.DeleteVlan = channel.unary_unary(
                '/vLANService/DeleteVlan',
                request_serializer=__shared__pb2.id.SerializeToString,
                response_deserializer=__shared__pb2.ResponseStatus.FromString,
                )


class vLANServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetVlanById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVlanByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVlanByIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddVlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_vLANServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVlanById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVlanById,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=vlan__pb2.vLANResponse.SerializeToString,
            ),
            'GetVlanByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVlanByName,
                    request_deserializer=__shared__pb2.name.FromString,
                    response_serializer=vlan__pb2.vLANResponse.SerializeToString,
            ),
            'GetVlanByIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVlanByIpAddress,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=vlan__pb2.vLANResponse.SerializeToString,
            ),
            'AddVlan': grpc.unary_unary_rpc_method_handler(
                    servicer.AddVlan,
                    request_deserializer=vlan__pb2.vlan.FromString,
                    response_serializer=vlan__pb2.vLANResponse.SerializeToString,
            ),
            'UpdateVlan': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateVlan,
                    request_deserializer=vlan__pb2.vlan.FromString,
                    response_serializer=vlan__pb2.vLANResponse.SerializeToString,
            ),
            'DeleteVlan': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVlan,
                    request_deserializer=__shared__pb2.id.FromString,
                    response_serializer=__shared__pb2.ResponseStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vLANService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class vLANService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetVlanById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vLANService/GetVlanById',
            __shared__pb2.id.SerializeToString,
            vlan__pb2.vLANResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVlanByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vLANService/GetVlanByName',
            __shared__pb2.name.SerializeToString,
            vlan__pb2.vLANResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVlanByIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vLANService/GetVlanByIpAddress',
            __shared__pb2.id.SerializeToString,
            vlan__pb2.vLANResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddVlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vLANService/AddVlan',
            vlan__pb2.vlan.SerializeToString,
            vlan__pb2.vLANResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateVlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vLANService/UpdateVlan',
            vlan__pb2.vlan.SerializeToString,
            vlan__pb2.vLANResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteVlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vLANService/DeleteVlan',
            __shared__pb2.id.SerializeToString,
            __shared__pb2.ResponseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
