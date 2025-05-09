import Pyro4

def main():
    with open("server_uri.txt", "r") as f:
        uri = f.read()  # Read server URI from file

    server = Pyro4.Proxy(uri)  # Connect to remote server

    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    result = server.concatenate_strings(str1, str2)  # Call remote method
    print("Concatenated Result:", result)

if __name__ == "__main__":
    main()


""" ---------------------- To Run This Code ------------------------------------
Step 1: Install Pyro4
Run the following command in the terminal:
    pip install Pyro4

Step 2:Start Pyro Nameserver
Before running the server, start the Pyro Nameserver using:
    pyro4-ns

    This registers the server in the distributed system.

Step 3: Run the Server
In a new terminal window, navigate to the folder where server.py is saved and run:
    python server.py
    It will display the server URI.



Step 4: Copy Server URI
Copy the URI displayed in the server terminal.

Paste it inside server_uri.txt (located in the same folder).

Step 5: Run the Client
Now, open another terminal window and run:
    python client.py

"""