import pyfiglet
import socket
import sys
from datetime import datetime

# create the Port Scanner in pyfiglet
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

# Ask for target input IP address
target = input(str("Target IP: "))

# target IP validation check
if target < 1 or target > 65535:
  print("Invalid port range.")
  sys.exit()

# some extra features
# Specify a range of ports to scan
# start_port = int(input("Enter the starting port: "))
# end_port = int(input("Enter the ending port: "))

# Add a check for valid port range
# if start_port < 1 or end_port > 65535 or start_port > end_port:
#   print("Invalid port range.")
#   sys.exit()

# # Add a counter for open ports
# open_ports = []

# Scan ports within the specified range
for port in range(start_port, end_port + 1):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(1)
  result = s.connect_ex((target, port))

  # If port is open, add it to the list of open ports
  if result == 0:
    # open_ports.append(port)
    print("Port {} is open".format(port))
  s.close()



# # Print the list of open ports
# if open_ports:
#   print("Open ports: ", open_ports)
# else:
#   print("No open ports found.")

# Add a pretty banner
print("_" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("_" * 50)

try:
  # Scan ports between 1 and 65,535
  for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))

    # If port is open, print it
    if result == 0:
      print("Port {} is open".format(port))
    s.close()

# exception handling
except KeyboardInterrupt:
  print("\nExit program.")
  sys.exit()

except socket.gaierror:
  print("\nHostname could not be resolved.")
  sys.exit()

except socket.error:
  print("\nServer not responding.")
  sys.exit()