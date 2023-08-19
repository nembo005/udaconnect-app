import grpc
import location_pb2
import location_pb2_grpc

# Create channel and stub
channel = grpc.insecure_channel("127.0.0.1:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Create payload
payload =  location_pb2.LocationMessage(person_id=7, latitude=8, longitude=18) 

# SEnd sample payload to server
response = stub.Create(payload)
print(f"Response from gRPC server: {response}")