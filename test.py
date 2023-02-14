from pathlib import Path
import sys

cwd = Path(__file__).parent.resolve()
#print('%s\stubs' % cwd)
#print('%s\descriptors' % cwd)
#print(sys.path)
#sys.path.append(cwd)
sys.path.append('%s\stubs' % cwd)
sys.path.append('%s\descriptors' % cwd)
#sys.path.append('%s\implementations' % cwd)
#print(sys.path)


import ipAddress_pb2,_shared_pb2
import ipAddress_pb2_grpc
import grpc

print('This is a test of the of the gRPC Server...')

with grpc.insecure_channel('localhost:55555') as channel:
    stub = ipAddress_pb2_grpc.IpAddressServiceStub(channel)
    response = stub.GetIpAddressById(_shared_pb2.id(id='0f3e5474-854b-41a6-9ade-0e12e171dd59'))

print('Response = %s' % response.IpAddress)


