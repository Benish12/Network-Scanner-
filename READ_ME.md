# Network Scanner

## Project Overview

Developed a Python-based Network Scanner using the Scapy packet manipulation framework to perform network discovery and identify active devices on a local network.

This project demonstrates practical knowledge of network security, packet analysis, ARP communication, and cybersecurity automation. Instead of relying on existing network scanning tools, I built a custom scanner to understand how network discovery works at the packet level.

https://github.com/user-attachments/assets/aaa7d409-79c3-4428-b0a9-7a899bd221aa



# Project Objectives

- Understand how network discovery tools operate.
- Learn how the ARP protocol works.
- Create and analyze network packets using Python.
- Automate device discovery within a local network.
- Gain hands-on experience with cybersecurity scripting and network security concepts.

# Features

- Scans local networks to identify active devices.
- Discovers connected hosts using ARP requests.
- Collects and displays:
  - IP addresses
  - MAC addresses
- Creates and sends custom network packets.
- Processes network responses to identify connected devices.
- Supports user-defined target networks through command-line arguments.
- Provides a lightweight network discovery solution.

# How It Works

## ARP Packet Creation & Network Discovery

The scanner uses the Scapy framework to create and manipulate ARP packets.

The program:

1. Creates ARP request packets targeting a specified IP range.
2. Broadcasts packets across the local network.
3. Waits for responses from active devices.
4. Extracts IP and MAC address information from returned packets.
5. Displays discovered network devices.

This process allows the scanner to identify active hosts connected to a local network.

## Command-Line Argument Handling

The project uses Python's `argparse` module to allow users to provide target network information directly through the Linux terminal.

Example:

```bash
python3 network_scanner.py -t 192.168.1.0/24
```

This allows users to scan different network ranges without modifying the source code.

# Tools & Technologies Used

## Python

**How it was used:**

- Developed the complete network scanning application.
- Automated packet creation, transmission, and response processing.
- Implemented scanning logic and command-line functionality.

## Scapy

**How it was used:**

- Created and manipulated ARP packets.
- Sent network requests across the local network.
- Captured and analyzed responses.
- Extracted IP and MAC address information from discovered devices.

Scapy provided hands-on experience with packet-level networking and allowed the project to be built without relying on pre-existing scanning tools.

## Kali Linux

**How it was used:**

- Developed and tested the project in a cybersecurity-focused Linux environment.
- Executed the scanner through the command line.
- Tested network discovery functionality in a controlled environment.

## VirtualBox

**How it was used:**

- Created isolated virtual machines for testing.
- Built a controlled network environment.
- Tested scanning functionality safely without affecting external networks.

## Git & GitHub

**How it was used:**

- Managed source code versions.
- Tracked project development.
- Stored and documented the project for portfolio purposes.

# Installation & Setup

## Requirements

- Python 3
- Kali Linux or another Linux distribution
- Scapy library

Install Scapy:

```bash
pip install scapy
```
# Running the Program

Run the scanner using:

```bash
sudo python3 network_scanner.py -t <target_network>
```

Example:

```bash
sudo python3 network_scanner.py -t 192.168.1.0/24
```

Root privileges may be required because the program creates and sends raw network packets.

# Example Output

Example:

```
IP Address          MAC Address
-----------------------------------------
192.168.1.1         AA:BB:CC:DD:EE:FF
192.168.1.5         11:22:33:44:55:66
```

# Project Outcome

Successfully developed a functional network discovery tool capable of identifying active devices within a local network.

Through this project, I gained practical experience with:

- ARP protocol communication
- Network packet creation and analysis
- IP and MAC address discovery
- Python scripting for cybersecurity automation
- Linux command-line tools
- Network security concepts

This project strengthened my understanding of how network reconnaissance tools operate and provided a foundation for developing more advanced cybersecurity tools such as vulnerability scanners, network monitoring systems, and security assessment utilities.

# Skills Demonstrated

- Python Programming
- Network Security
- Packet Analysis
- Scapy Framework
- ARP Protocol
- Linux Administration
- Cybersecurity Automation
- Git/GitHub
- Command-Line Tools

# Ethical Disclaimer

This project was created for educational purposes and tested only in authorized lab environments using personally controlled virtual machines.

Network scanning should only be performed on systems where proper authorization has been granted. Unauthorized scanning of networks may violate legal and organizational policies.
