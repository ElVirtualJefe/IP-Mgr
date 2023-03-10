# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import _shared_pb2 as __shared__pb2
import vlan_pb2 as vlan__pb2


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
