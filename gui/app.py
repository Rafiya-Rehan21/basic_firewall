# import tkinter as tk
# from tkinter import ttk
# from firewall.rules import (
#     add_ip_to_blocklist,
#     remove_ip_from_blocklist,
#     add_port_to_blocklist,
#     remove_port_from_blocklist,
#     apply_firewall_rules,
#     clear_firewall_rules,
#     blocked_ips,
#     blocked_ports
# )

# class FirewallGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Firewall Manager")
#         self.root.geometry("600x400")

#         # Create the layout
#         self.create_navbar()
#         self.create_frames()

#     def create_navbar(self):
#         """Create a navigation bar."""
#         self.navbar = tk.Frame(self.root, bg="#333", width=150)
#         self.navbar.pack(side="left", fill="y")

#         # Navigation Buttons
#         nav_buttons = [
#             ("IP Management", self.show_ip_frame),
#             ("Port Management", self.show_port_frame),
#             ("Apply Rules", self.apply_rules),
#             ("Clear Rules", self.clear_rules),
#         ]
#         for text, command in nav_buttons:
#             btn = tk.Button(
#                 self.navbar,
#                 text=text,
#                 bg="#444",
#                 fg="white",
#                 relief="flat",
#                 command=command,
#                 height=2,
#                 width=20,
#             )
#             btn.pack(pady=5, padx=10, fill="x")

#     def create_frames(self):
#         """Create frames for IP and Port management."""
#         self.ip_frame = self.create_ip_frame()
#         self.port_frame = self.create_port_frame()

#         # Show the default frame (IP management)
#         self.show_ip_frame()

#     def create_ip_frame(self):
#         """Create the frame for managing IPs."""
#         frame = tk.Frame(self.root, bg="#f5f5f5")
#         tk.Label(frame, text="Manage IPs", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

#         form_frame = tk.Frame(frame, bg="#f5f5f5")
#         form_frame.pack(pady=20)

#         tk.Label(form_frame, text="IP Address:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
#         self.ip_entry = tk.Entry(form_frame)
#         self.ip_entry.grid(row=0, column=1, padx=10, pady=5)

#         tk.Button(form_frame, text="Add IP", command=self.add_ip).grid(row=1, column=0, padx=10, pady=10)
#         tk.Button(form_frame, text="Remove IP", command=self.remove_ip).grid(row=1, column=1, padx=10, pady=10)

#         self.ip_listbox = tk.Listbox(frame, height=10)
#         self.ip_listbox.pack(padx=10, pady=10, fill="x")

#         # Message display area
#         self.ip_message_label = tk.Label(frame, text="", fg="red", bg="#f5f5f5")
#         self.ip_message_label.pack()

#         return frame

#     def create_port_frame(self):
#         """Create the frame for managing Ports."""
#         frame = tk.Frame(self.root, bg="#f5f5f5")
#         tk.Label(frame, text="Manage Ports", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

#         form_frame = tk.Frame(frame, bg="#f5f5f5")
#         form_frame.pack(pady=20)

#         tk.Label(form_frame, text="Port:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
#         self.port_entry = tk.Entry(form_frame)
#         self.port_entry.grid(row=0, column=1, padx=10, pady=5)

#         tk.Button(form_frame, text="Add Port", command=self.add_port).grid(row=1, column=0, padx=10, pady=10)
#         tk.Button(form_frame, text="Remove Port", command=self.remove_port).grid(row=1, column=1, padx=10, pady=10)

#         self.port_listbox = tk.Listbox(frame, height=10)
#         self.port_listbox.pack(padx=10, pady=10, fill="x")

#         # Message display area
#         self.port_message_label = tk.Label(frame, text="", fg="red", bg="#f5f5f5")
#         self.port_message_label.pack()

#         return frame

#     def show_ip_frame(self):
#         """Show the IP management frame."""
#         self.port_frame.pack_forget()
#         self.ip_frame.pack(fill="both", expand=True)
#         self.update_ip_listbox()

#     def show_port_frame(self):
#         """Show the Port management frame."""
#         self.ip_frame.pack_forget()
#         self.port_frame.pack(fill="both", expand=True)
#         self.update_port_listbox()

#     def add_ip(self):
#         """Add IP to the blocklist."""
#         ip = self.ip_entry.get()
#         if ip:
#             message = add_ip_to_blocklist(ip)
#             self.ip_message_label.config(text=message, fg="green" if "added" in message else "red")
#             self.update_ip_listbox()

#     def remove_ip(self):
#         """Remove IP from the blocklist."""
#         ip = self.ip_entry.get()
#         if ip:
#             message = remove_ip_from_blocklist(ip)
#             self.ip_message_label.config(text=message, fg="green" if "removed" in message else "red")
#             self.update_ip_listbox()

#     def add_port(self):
#         """Add Port to the blocklist."""
#         port = self.port_entry.get()
#         if port:
#             message = add_port_to_blocklist(port)
#             self.port_message_label.config(text=message, fg="green" if "added" in message else "red")
#             self.update_port_listbox()

#     def remove_port(self):
#         """Remove Port from the blocklist."""
#         port = self.port_entry.get()
#         if port:
#             message = remove_port_from_blocklist(port)
#             self.port_message_label.config(text=message, fg="green" if "removed" in message else "red")
#             self.update_port_listbox()

#     def update_ip_listbox(self):
#         """Update the IP listbox."""
#         self.ip_listbox.delete(0, tk.END)
#         for ip in blocked_ips:
#             self.ip_listbox.insert(tk.END, ip)

#     def update_port_listbox(self):
#         """Update the Port listbox."""
#         self.port_listbox.delete(0, tk.END)
#         for port in blocked_ports:
#             self.port_listbox.insert(tk.END, port)

#     def apply_rules(self):
#         """Apply the firewall rules."""
#         message = apply_firewall_rules()
#         self.ip_message_label.config(text=message, fg="green")

#     def clear_rules(self):
#         """Clear the firewall rules."""
#         message = clear_firewall_rules()
#         self.ip_message_label.config(text=message, fg="green")
        
        
        
        
        
        
        
        
        
        
        
        
        



import tkinter as tk
from tkinter import messagebox
import subprocess
from firewall.rules import (
    add_ip_to_blocklist,
    remove_ip_from_blocklist,
    add_port_to_blocklist,
    remove_port_from_blocklist,
    apply_firewall_rules,
    clear_firewall_rules,
    blocked_ips,
    blocked_ports
)
from simulation import (
    simulate_traffic
)


# Check if IP is blocked
def check_ip_connection(ip):
    """Check the connection to the given IP address."""
    if ip in blocked_ips:
        return "Connection blocked"
    else:
        return "Connection established"

# Check if Port is blocked
def check_port_connection(port):
    """Check the connection to the given port."""
    try:
        # Convert the port to integer and check if it's blocked
        port = int(port)
        print(f"Checking port: {port}")  # Debugging line
        print(f"Blocked Ports: {blocked_ports}")  # Debugging line

        # Check if the port is in the blocked list
        if port in blocked_ports:
            return "Connection blocked"
        else:
            return "Connection established"
    except ValueError:
        return "Invalid port number"
    

# GUI Class
class FirewallGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Firewall Manager")
        self.root.geometry("600x500")

        # Create the layout
        self.create_navbar()
        self.create_frames()

    def create_navbar(self):
        """Create a navigation bar."""
        self.navbar = tk.Frame(self.root, bg="#333", width=150)
        self.navbar.pack(side="left", fill="y")

        # Navigation Buttons
        nav_buttons = [
            ("IP Management", self.show_ip_frame),
            ("Port Management", self.show_port_frame),
            ("Apply Rules", self.apply_rules),
            ("Clear Rules", self.clear_rules),
            ("Simulation", self.show_simulation_frame),  # New button for simulation
        ]
        for text, command in nav_buttons:
            btn = tk.Button(
                self.navbar,
                text=text,
                bg="#444",
                fg="white",
                relief="flat",
                command=command,
                height=2,
                width=20,
            )
            btn.pack(pady=5, padx=10, fill="x")

    def create_frames(self):
        """Create frames for IP and Port management."""
        self.ip_frame = self.create_ip_frame()
        self.port_frame = self.create_port_frame()
        self.simulation_frame = self.create_simulation_frame()  # Simulation frame

        # Show the default frame (IP management)
        self.show_ip_frame()

    def create_ip_frame(self):
        """Create the frame for managing IPs."""
        frame = tk.Frame(self.root, bg="#f5f5f5")
        tk.Label(frame, text="Manage IPs", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

        form_frame = tk.Frame(frame, bg="#f5f5f5")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="IP Address:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
        self.ip_entry = tk.Entry(form_frame)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Add IP", command=self.add_ip).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(form_frame, text="Remove IP", command=self.remove_ip).grid(row=1, column=1, padx=10, pady=10)

        self.ip_listbox = tk.Listbox(frame, height=10)
        self.ip_listbox.pack(padx=10, pady=10, fill="x")

        self.ip_message_label = tk.Label(frame, text="", bg="#f5f5f5", fg="red")
        self.ip_message_label.pack()

        return frame

    def create_port_frame(self):
        """Create the frame for managing Ports."""
        frame = tk.Frame(self.root, bg="#f5f5f5")
        tk.Label(frame, text="Manage Ports", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

        form_frame = tk.Frame(frame, bg="#f5f5f5")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Port:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
        self.port_entry = tk.Entry(form_frame)
        self.port_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Add Port", command=self.add_port).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(form_frame, text="Remove Port", command=self.remove_port).grid(row=1, column=1, padx=10, pady=10)

        self.port_listbox = tk.Listbox(frame, height=10)
        self.port_listbox.pack(padx=10, pady=10, fill="x")

        self.port_message_label = tk.Label(frame, text="", bg="#f5f5f5", fg="red")
        self.port_message_label.pack()

        return frame

    def create_simulation_frame(self):
        """Create the frame for simulation."""
        frame = tk.Frame(self.root, bg="#f5f5f5")
        tk.Label(frame, text="Network Traffic Simulation", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

        form_frame = tk.Frame(frame, bg="#f5f5f5")
        form_frame.pack(pady=20)

        # IP Simulation
        tk.Label(form_frame, text="IP Address (Ping):", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
        self.sim_ip_entry = tk.Entry(form_frame)
        self.sim_ip_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Ping IP", command=self.ping_ip).grid(row=1, column=0, columnspan=2, pady=10)

        # Port Simulation
        tk.Label(form_frame, text="Port Number (Request):", bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5)
        self.sim_port_entry = tk.Entry(form_frame)
        self.sim_port_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Send Request", command=self.simulate_port_request).grid(row=3, column=0, columnspan=2, pady=10)

        return frame

    def show_ip_frame(self):
        """Show the IP management frame."""
        self.port_frame.pack_forget()
        self.simulation_frame.pack_forget()
        self.ip_frame.pack(fill="both", expand=True)
        self.update_ip_listbox()

    def show_port_frame(self):
        """Show the Port management frame."""
        self.ip_frame.pack_forget()
        self.simulation_frame.pack_forget()
        self.port_frame.pack(fill="both", expand=True)
        self.update_port_listbox()

    def show_simulation_frame(self):
        """Show the Simulation frame."""
        self.ip_frame.pack_forget()
        self.port_frame.pack_forget()
        self.simulation_frame.pack(fill="both", expand=True)

    def add_ip(self):
        """Add IP to the blocklist."""
        ip = self.ip_entry.get()
        if ip:
            message = add_ip_to_blocklist(ip)
            self.update_ip_listbox()
            self.ip_message_label.config(text=message, fg="green")

    def remove_ip(self):
        """Remove IP from the blocklist."""
        ip = self.ip_entry.get()
        if ip:
            message = remove_ip_from_blocklist(ip)
            self.update_ip_listbox()
            self.ip_message_label.config(text=message, fg="red")

    def add_port(self):
        """Add Port to the blocklist."""
        port = self.port_entry.get()
        if port:
            message = add_port_to_blocklist(port)
            self.update_port_listbox()
            self.port_message_label.config(text=message, fg="green")

    def remove_port(self):
        """Remove Port from the blocklist."""
        port = self.port_entry.get()
        if port:
            message = remove_port_from_blocklist(port)
            self.update_port_listbox()
            self.port_message_label.config(text=message, fg="red")

    def ping_ip(self):
        """Simulate pinging an IP address."""
        ip = self.sim_ip_entry.get()
        if ip:
            response = check_ip_connection(ip)
            messagebox.showinfo("Simulation Result", response)

    def simulate_port_request(self):
        """Simulate a request to a port and display connection status."""
        port = self.sim_port_entry.get()
        if port:
            response = check_port_connection(port)
            messagebox.showinfo("Simulation Result", response)

    def apply_rules(self):
        """Apply firewall rules."""
        messagebox.showinfo("Simulation Result", "Firewall rules applied successfully!")

    def clear_rules(self):
        """Clear all firewall rules."""
        messagebox.showinfo("Simulation Result", "Firewall rules cleared!")

    def update_ip_listbox(self):
        """Update the IP listbox."""
        self.ip_listbox.delete(0, tk.END)
        for ip in blocked_ips:
            self.ip_listbox.insert(tk.END, ip)

    def update_port_listbox(self):
        """Update the Port listbox."""
        self.port_listbox.delete(0, tk.END)
        for port in blocked_ports:
            self.port_listbox.insert(tk.END, port)