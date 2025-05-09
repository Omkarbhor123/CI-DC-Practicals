import Pyro4

# Expose the class for remote invocation
@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        return str1 + str2  # Concatenating strings

# Initialize Pyro4 server
def main():
    daemon = Pyro4.Daemon()  # Create Pyro daemon
    ns = Pyro4.locateNS()  # Locate Pyro nameserver

    server = StringConcatenationServer()  # Create server object
    uri = daemon.register(server)  # Register server object
    ns.register("string.concatenation", uri)  # Register name in Pyro nameserver

    print(f"Server URI: {uri}")
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))  # Save URI to file for client reference

    daemon.requestLoop()  # Run server loop

if __name__ == "__main__":
    main()
