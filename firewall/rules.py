import json
import os
import subprocess
import re

# File to store the firewall rules persistently
RULES_FILE = "firewall_rules.json"

# Load the firewall rules (IPs and Ports) from a JSON file
def load_rules():
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, "r") as file:
            data = json.load(file)
            return data.get("blocked_ips", []), data.get("blocked_ports", [])
    else:
        return [], []  

# Save the firewall rules (IPs and Ports) to a JSON file
def save_rules(blocked_ips, blocked_ports):
    data = {
        "blocked_ips": blocked_ips,
        "blocked_ports": blocked_ports
    }
    with open(RULES_FILE, "w") as file:
        json.dump(data, file, indent=4)

blocked_ips, blocked_ports = load_rules()

def add_ip_to_blocklist(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address format. Please provide a valid IP address."
    
    if ip not in blocked_ips:
        blocked_ips.append(ip)
        save_rules(blocked_ips, blocked_ports)
        block_ip_firewall(ip)
        return f"IP {ip} added to blocklist and firewall."
    return f"IP {ip} is already in the blocklist."

def remove_ip_from_blocklist(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        save_rules(blocked_ips, blocked_ports)
        unblock_ip_firewall(ip)
        return f"IP {ip} removed from blocklist and firewall."
    return f"IP {ip} not found in blocklist."

def add_port_to_blocklist(port):
    if not is_valid_port(port):
        return "Invalid port number. Please provide a valid port between 1 and 65535."
    
    if port not in blocked_ports:
        blocked_ports.append(port)
        save_rules(blocked_ips, blocked_ports)
        block_port_firewall(port)
        
        print(f"Port {port} added to blocklist.")
        
        return f"Port {port} added to blocklist and firewall."
    
    print(f"Port {port} is already in blocklist.")
    
    return f"Port {port} is already in the blocklist."

def remove_port_from_blocklist(port):
    if port in blocked_ports:
        blocked_ports.remove(port)
        save_rules(blocked_ips, blocked_ports)
        unblock_port_firewall(port)
        return f"Port {port} removed from blocklist and firewall."
    return f"Port {port} not found in blocklist."

def block_ip_firewall(ip):
    command = f"netsh advfirewall firewall add rule name=\"Block IP {ip}\" dir=in action=block remoteip={ip}"
    subprocess.run(command, shell=True)

def unblock_ip_firewall(ip):
    command = f"netsh advfirewall firewall delete rule name=\"Block IP {ip}\""
    subprocess.run(command, shell=True)

def block_port_firewall(port):
    command = f"netsh advfirewall firewall add rule name=\"Block Port {port}\" dir=in action=block protocol=TCP localport={port}"
    subprocess.run(command, shell=True)

def unblock_port_firewall(port):
    command = f"netsh advfirewall firewall delete rule name=\"Block Port {port}\""
    subprocess.run(command, shell=True)

def apply_firewall_rules():
    for ip in blocked_ips:
        block_ip_firewall(ip)
    for port in blocked_ports:
        block_port_firewall(port)
    return "Firewall rules applied successfully."

def clear_firewall_rules():
    for ip in blocked_ips:
        unblock_ip_firewall(ip)
    for port in blocked_ports:
        unblock_port_firewall(port)
    return "All firewall rules cleared."

def is_valid_ip(ip):
    ip_pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    
    return bool(ip_pattern.match(ip))

def is_valid_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False