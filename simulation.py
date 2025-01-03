import platform
import subprocess
from firewall.rules import blocked_ips, blocked_ports, is_valid_ip, is_valid_port

def ping_ip(ip):
    """Ping the given IP address and return detailed results with statistics."""
    
    if not is_valid_ip(ip):
        return "Invalid IP address."
    
    if ip in blocked_ips:
        return "Connection blocked. The IP is in the blocklist."
    
    try:
        command = ['ping', '-n', '1', ip] if platform.system().lower() == 'windows' else ['ping', '-c', '1', ip]
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout = response.stdout.decode()
        returncode = response.returncode

        if returncode == 0:
            result = f"{stdout.strip()}\n\nPing successful!"
        else:
            result = f"{stdout.strip()}\n\nPing failed!"
        
        return result
    except Exception as e:
        return f"Error occurred: {e}"
    
def check_blocked_port(port):
    """Simulate checking if a port is blocked."""
    
    if not is_valid_port(port):
        return "Invalid port number."
    
    if port in blocked_ports:
        return f"Port {port} is blocked."
    else:
        return f"Port {port} is open."