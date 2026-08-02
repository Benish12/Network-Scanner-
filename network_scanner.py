#!/usr/bin/env python

#I am adding this comment to test the git commit and push functionality
import scapy.all as scapy
import argparse
import csv
import json
from datetime import datetime


# Allows user console input
def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Target IP / IP range"
    )

    options = parser.parse_args()
    return options


# ARP Network Scanner
def scan(ip):

    # Creates ARP request
    arp_request = scapy.ARP(pdst=ip)

    # Creates Ethernet broadcast frame
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combines Ethernet + ARP request
    arp_request_broadcast = broadcast / arp_request

    # Sends packet and receives responses
    answered_list = scapy.srp(
        arp_request_broadcast,
        timeout=1,
        verbose=False
    )[0]


    clients_list = []

    for element in answered_list:

        client_dict = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }

        clients_list.append(client_dict)


    return clients_list



# Prints scan results
def printer(results):

    print("\nIP Address\t\tMAC Address")
    print("---------------------------------------------")

    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])



# Save results as CSV
def save_csv(results):

    filename = "network_scan.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "IP Address",
                "MAC Address"
            ]
        )


        for client in results:

            writer.writerow(
                [
                    client["ip"],
                    client["mac"]
                ]
            )


    print(f"\n[+] CSV report saved: {filename}")



# Save results as JSON
def save_json(results):

    filename = "network_scan.json"


    report = {

        "scan_time": str(datetime.now()),

        "devices": results

    }


    with open(filename, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print(f"[+] JSON report saved: {filename}")



# Main program

options = get_args()

scan_results = scan(options.target)

printer(scan_results)

save_csv(scan_results)

save_json(scan_results)