import random
import time
from collections import deque

class Server:
    def __init__(self, name):
        self.name = name
        self.current_load = 0  # Keeps track of active connections

    def handle_request(self):
        """ Simulates handling a request by increasing load """
        self.current_load += 1

    def complete_request(self):
        """ Simulates completing a request and decreasing load """
        self.current_load = max(0, self.current_load - 1)

    def __str__(self):
        return f"{self.name} (Load: {self.current_load})"


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.round_robin_queue = deque(self.servers)

    def round_robin(self):
        """ Distributes requests using the Round Robin method """
        server = self.round_robin_queue.popleft()
        server.handle_request()
        self.round_robin_queue.append(server)
        return server

    def least_connections(self):
        """ Distributes requests using the Least Connections method """
        server = min(self.servers, key=lambda s: s.current_load)
        server.handle_request()
        return server


# Creating Servers
servers = [Server(f"Server {i}") for i in range(3)]
lb = LoadBalancer(servers)

# Simulating Requests
print("Distributing requests using Round Robin:")
for i in range(6):
    server = lb.round_robin()
    print(f"Request {i + 1} handled by {server}")

print("\nDistributing requests using Least Connections:")
for i in range(6):
    server = lb.least_connections()
    print(f"Request {i + 1} handled by {server}")

# Completing some requests randomly
print("\nCompleting random requests...")
for server in servers:
    server.complete_request()
    print(server)
