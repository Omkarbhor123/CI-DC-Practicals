import xmlrpc.client

# Create an RPC client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# Get user input
input_value = int(input("Enter a number: "))

try:
    result = proxy.calculate_factorial(input_value)
    print(f"Factorial of {input_value} is: {result}")
except Exception as e:
    print(f"Error: {e}")



"""
Step 1: Start the Server
Open Command Prompt or Terminal.

Navigate to the folder where Factserver.py is located.

Run the command:
    python Factserver.py



Step 2: Run the Client
Open another Command Prompt window.

Navigate to the folder where Factclient.py is located.

Run the command:
    python Factclient.py

"""