import re
import subprocess
import sys
from scapy.all import ARP, Ether, srp
from ipaddress import ip_network, IPv4Network


def check_dependencies():
    # Check if WinPcap or Npcap is installed
    # try:
    #     subprocess.run(["dumpcap", "-D"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # except (subprocess.CalledProcessError, FileNotFoundError):
    #     raise RuntimeError("WinPcap or Npcap is not installed. Please install it and retry.")
    # Check if scapy and ipaddress libraries are installed

    # TO DO

    # https://npcap.com/#download
    # https://nmap.org/npsl/

    try:
        import scapy
        import ipaddress
    except ImportError:
        raise ImportError("Required Python libraries (scapy, ipaddress) are not installed. Please install them and retry.")


def get_local_ip_windows():
    result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)
    ipv4_pattern = re.compile(r"IPv4 Address.*: (?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)")
    match = ipv4_pattern.search(result.stdout)
    if match:
        return match.group("ip")
    else:
        return None


def calculate_network_address(ip_address):
    network = IPv4Network(f"{ip_address}/24", strict=False)
    return str(network.network_address)


def scan(ip):
    arp = ARP(pdst=str(ip_network(ip, False)))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients


def automated_scan(network=None):
    if network is None:
        local_ip = get_local_ip_windows()
        if local_ip:
            network = f"{calculate_network_address(local_ip)}/24"
        else:
            return []
    return scan(network)


def main():
    try:
        check_dependencies()
        user_input = input("Enter the network address (e.g., '192.168.1.0/24') or press Enter to scan the current network: ")
        if user_input:
            network = user_input.strip()
        else:
            network = None
        devices = automated_scan(network)
        print("Available devices in the network:")
        print("IP" + " " * 18 + "MAC")
        for device in devices:
            print("{:16}    {}".format(device['ip'], device['mac']))

    except Exception as e:
        print(f"Error: {e}")
        input("Press any key to close.")
        sys.exit()


if __name__ == "__main__":
    main()
