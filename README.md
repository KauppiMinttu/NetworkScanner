# Network Scanner

A Python-based **network port scanner** that scans a specified IP address for open ports within a user-defined range. The script features real-time progress tracking and displays detailed scan results in an intuitive format.

## Features

- **IP Address Input**: Users can specify a target IP address or hostname.
- **Port Range Selection**: Define the start and end port to customize the scanning range.
- **Open Port Detection**: Identifies open ports and lists them after the scan.
- **Progress Bar**: Real-time progress bar shows scan progress and percentage completion.
- **Error Handling**: Handles common errors like invalid hostnames and connection timeouts.
- **Graceful Exit**: Supports clean program termination via keyboard interrupts (Ctrl+C).

## Technologies Used

![Python](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)

- **Python 3.8+**: Programming language.
- **Colorama**: For colorful terminal outputs.
- **Socket**: Enables port scanning and connection checks.
- **Datetime**: For timestamping the scan.
- **Sys and Termios**: Manages user inputs and terminal echo settings.

## Prerequisites

Python 3.8 or higher installed.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/network-scanner.git
   cd network-scanner
   ```

2. Run the script:
   ```bash
   python network_scanner.py
   ```

3. Follow the prompts:
   - Enter the target IP address or hostname.
   - Input the start and end port range.

4. View results:
   - Open ports will be displayed after the scan.
   - A real-time progress bar will track scan completion.

## Example

```
Enter the target IP address: 10.0.0.1
Enter the start port: 20
Enter the end port: 100
----------------------------------------
Scan started on target: 10.0.0.1
Time started: 2024-12-12 10:00:00
----------------------------------------
██████████████████████████████          60.00% 48/80 ports scanned
Port 22 is open
Port 80 is open

Scan complete.
```

## Notes

- This scanner is for educational and ethical purposes only. **Do not use it to scan networks without permission.**
- The script uses a timeout of 1 second per port to balance speed and accuracy.
