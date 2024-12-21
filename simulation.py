# simulation.py
from firewall.rules import blocked_ips, blocked_ports  # Importing blocked IPs and Ports

def simulate_traffic(ip, port):
    """Simulates network traffic and checks it against firewall rules."""
    
    # Check if the packet is from a blocked IP or has a blocked port
    if ip in blocked_ips:
        return f"Connection attempt from IP {ip} blocked!"
    elif str(port) in blocked_ports:
        return f"Connection attempt to Port {port} blocked!"
    else:
        return f"Connection to IP {ip}, Port {port} established successfully."
