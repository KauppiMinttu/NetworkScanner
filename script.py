from datetime import datetime
import sys
import socket
from colorama import Fore, init
import termios
import tty

# Initialize colorama
init(autoreset=True)

# Disable terminal echoing
def disable_echo():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    return old_settings

# Restore terminal settings
def restore_echo(old_settings):
    fd = sys.stdin.fileno()
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Function to get user input for target and port range
def get_user_input():
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    return target, start_port, end_port

# Get user input for target and port range
target, start_port, end_port = get_user_input()

# Resolve the hostname
try:
    target = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

# Display scan information
print("-" * 40)
print(f"Scan started on target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 40)

# Calculate the total number of ports to scan
total_ports = end_port - start_port + 1  # Include the end port

# Define the width of the progress bar (in characters)
progress_bar_width = 50

# Print the initial progress bar once, without a leading empty bar
print(f"\r{Fore.CYAN}{' ' * progress_bar_width} 0.00% 0/{total_ports} ports scanned", end="", flush=True)

try:
    # Disable terminal echo
    old_settings = disable_echo()

    # Buffer for open ports
    open_ports_buffer = []

    # Scan ports in the specified range
    for i, port in enumerate(range(start_port, end_port + 1)):  # Include the end port in the range
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout for the connection attempt
        result = s.connect_ex((target, port))  # Check if the port is open
        
        # Calculate percentage done
        percent_done = ((i + 1) / total_ports) * 100
        
        # Scale the progress to fit the fixed width
        blocks = "█" * int((percent_done / 100) * progress_bar_width)

        # Update the progress bar without printing it again unnecessarily
        print(f"\r{Fore.CYAN}{blocks.ljust(progress_bar_width)} {percent_done:.2f}% {i + 1}/{total_ports} ports scanned", end="", flush=True)

        if result == 0:
            open_ports_buffer.append(f"Port {port} is open")

        s.close()

    # Restore terminal settings
    restore_echo(old_settings)

    # Print open ports after completing the progress bar
    for port_msg in open_ports_buffer:
        print("\n" + port_msg)

    # Final message after scanning
    print("\nScan complete.")

except KeyboardInterrupt:
    restore_echo(old_settings)
    print("\n")
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    restore_echo(old_settings)
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    restore_echo(old_settings)
    print("Could not connect to server.")
    sys.exit()