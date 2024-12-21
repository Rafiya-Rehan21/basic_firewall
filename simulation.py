import platform
import subprocess
from firewall.rules import blocked_ips, blocked_ports

def ping_ip(ip):
    """Ping the given IP address and return detailed results with statistics."""
    
    if ip in blocked_ips:
        return "Connection blocked. The IP is in the blocklist."
    
    try:
        # Use the correct ping command for the OS
        command = ['ping', '-n', '1', ip] if platform.system().lower() == 'windows' else ['ping', '-c', '1', ip]
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout = response.stdout.decode()
        returncode = response.returncode

        if returncode == 0:
            # Combine full output with success message
            result = f"{stdout.strip()}\n\nPing successful!"
        else:
            # Combine full output with failure message
            result = f"{stdout.strip()}\n\nPing failed!"
        
        return result
    except Exception as e:
        return f"Error occurred: {e}"
    
def check_blocked_port(port):
    """Simulate checking if a port is blocked."""
    if port in blocked_ports:
        return f"Port {port} is blocked."
    else:
        # For ports not in the blocked list, always consider the port as open
        return f"Port {port} is open."