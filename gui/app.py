import tkinter as tk
from tkinter import messagebox

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

from simulation import ping_ip, check_blocked_port  # Import the port simulation function

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
            ("IP Simulation", self.show_ip_simulation_frame),  # Existing option for IP simulation
            ("Port Simulation", self.show_port_simulation_frame),  # New option for Port simulation
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
        self.ip_simulation_frame = self.create_ip_simulation_frame()  # Frame for IP simulation
        self.port_simulation_frame = self.create_port_simulation_frame()  # Frame for Port simulation

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

        # Message display area
        self.ip_message_label = tk.Label(frame, text="", fg="red", bg="#f5f5f5")
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

        # Message display area
        self.port_message_label = tk.Label(frame, text="", fg="red", bg="#f5f5f5")
        self.port_message_label.pack()

        return frame

    def create_ip_simulation_frame(self):
        """Create the frame for IP simulation."""
        frame = tk.Frame(self.root, bg="#f5f5f5")
        tk.Label(frame, text="IP Simulation", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

        form_frame = tk.Frame(frame, bg="#f5f5f5")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="IP Address to Ping:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
        self.sim_ip_entry = tk.Entry(form_frame)
        self.sim_ip_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Ping IP", command=self.ping_ip).grid(row=1, column=0, columnspan=2, pady=10)

        # Message display area for simulation
        self.sim_message_label = tk.Label(frame, text="", fg="red", bg="#f5f5f5")
        self.sim_message_label.pack()

        return frame

    def create_port_simulation_frame(self):
        """Create the frame for Port simulation."""
        frame = tk.Frame(self.root, bg="#f5f5f5")
        tk.Label(frame, text="Port Simulation", font=("Arial", 16), bg="#f5f5f5").pack(pady=10)

        form_frame = tk.Frame(frame, bg="#f5f5f5")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Port to Check:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
        self.sim_port_entry = tk.Entry(form_frame)
        self.sim_port_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Check Port", command=self.check_port).grid(row=1, column=0, columnspan=2, pady=10)

        # Message display area for port simulation
        self.sim_port_message_label = tk.Label(frame, text="", fg="red", bg="#f5f5f5")
        self.sim_port_message_label.pack()

        return frame

    def show_ip_frame(self):
        """Show the IP management frame."""
        self.port_frame.pack_forget()
        self.port_simulation_frame.pack_forget()  # Hide the port simulation frame
        self.ip_simulation_frame.pack_forget()  # Hide the IP simulation frame
        self.ip_frame.pack(fill="both", expand=True)
        self.update_ip_listbox()

    def show_port_frame(self):
        """Show the Port management frame."""
        self.ip_frame.pack_forget()
        self.port_simulation_frame.pack_forget()  # Hide the port simulation frame
        self.ip_simulation_frame.pack_forget()  # Hide the IP simulation frame
        self.port_frame.pack(fill="both", expand=True)
        self.update_port_listbox()

    def show_ip_simulation_frame(self):
        """Show the IP simulation frame."""
        self.ip_frame.pack_forget()
        self.port_frame.pack_forget()
        self.port_simulation_frame.pack_forget()  # Hide the port management frame
        self.ip_simulation_frame.pack(fill="both", expand=True)

    def show_port_simulation_frame(self):
        """Show the Port simulation frame."""
        self.ip_frame.pack_forget()
        self.port_frame.pack_forget()
        self.ip_simulation_frame.pack_forget()  # Hide the IP simulation frame
        self.port_simulation_frame.pack(fill="both", expand=True)

    def add_ip(self):
        """Add IP to the blocklist."""
        ip = self.ip_entry.get()
        if ip:
            message = add_ip_to_blocklist(ip)
            self.ip_message_label.config(text=message, fg="green" if "added" in message else "red")
            self.update_ip_listbox()

    def remove_ip(self):
        """Remove IP from the blocklist."""
        ip = self.ip_entry.get()
        if ip:
            message = remove_ip_from_blocklist(ip)
            self.ip_message_label.config(text=message, fg="green" if "removed" in message else "red")
            self.update_ip_listbox()

    def add_port(self):
        """Add port to the blocklist."""
        port = self.port_entry.get()
        if port:
            message = add_port_to_blocklist(port)
            self.port_message_label.config(text=message, fg="green" if "added" in message else "red")
            self.update_port_listbox()

    def remove_port(self):
        """Remove port from the blocklist."""
        port = self.port_entry.get()
        if port:
            message = remove_port_from_blocklist(port)
            self.port_message_label.config(text=message, fg="green" if "removed" in message else "red")
            self.update_port_listbox()

    def apply_rules(self):
        """Apply the firewall rules."""
        message = apply_firewall_rules()
        messagebox.showinfo("Success", message)

    def clear_rules(self):
        """Clear all firewall rules."""
        message = clear_firewall_rules()
        messagebox.showinfo("Cleared", message)

    def ping_ip(self):
        """Simulate IP ping."""
        ip = self.sim_ip_entry.get()
        if ip:
            result = ping_ip(ip)
            self.sim_message_label.config(text=result, fg="green" if "success" in result else "red")

    def check_port(self):
        """Simulate port check."""
        port = self.sim_port_entry.get()
        if port:
            result = check_blocked_port(port)
            self.sim_port_message_label.config(text=result, fg="green" if "open" in result else "red")

    def update_ip_listbox(self):
        """Update the listbox with blocked IPs."""
        self.ip_listbox.delete(0, tk.END)
        for ip in blocked_ips:
            self.ip_listbox.insert(tk.END, ip)

    def update_port_listbox(self):
        """Update the listbox with blocked ports."""
        self.port_listbox.delete(0, tk.END)
        for port in blocked_ports:
            self.port_listbox.insert(tk.END, port)