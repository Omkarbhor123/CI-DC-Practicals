from xmlrpc.server import SimpleXMLRPCServer

# Define the server class
class FactorialServer:
    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Create the RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(FactorialServer())

print("Factorial Server is running...")

# Start the server
server.serve_forever()
