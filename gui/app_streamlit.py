import streamlit as st
import plotly.graph_objects as go
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
from simulation import ping_ip, check_blocked_port

# Helper function to display messages
def display_message(message, success=True):
    if success:
        st.success(message)
    else:
        st.error(message)

class FirewallApp:
    def __init__(self):
        st.set_page_config(page_title="Firewall Manager", layout="wide")
        self.create_navbar()
        self.create_frames()

    def create_navbar(self):
        """Create a sidebar navigation menu."""
        st.sidebar.title("Navigation")
        options = [
            "Home",
            "IP Management",
            "Port Management",
            "Apply Rules",
            "Clear Rules",
            "IP Simulation",
            "Port Simulation",
            "Firewall Statistics",  
        ]
        self.selected_option = st.sidebar.radio("Select an option", options)

    def create_frames(self):
        """Display the selected option frame."""
        if self.selected_option == "Home":
            self.home_page()
        elif self.selected_option == "IP Management":
            self.ip_management_frame()
        elif self.selected_option == "Port Management":
            self.port_management_frame()
        elif self.selected_option == "Apply Rules":
            self.apply_rules()
        elif self.selected_option == "Clear Rules":
            self.clear_rules()
        elif self.selected_option == "IP Simulation":
            self.ip_simulation_frame()
        elif self.selected_option == "Port Simulation":
            self.port_simulation_frame()
        elif self.selected_option == "Firewall Statistics":
            self.firewall_statistics_page()  
            
    def home_page(self):
        """Display the home page."""
        st.title("Firewall Management")
        st.write("Here you can manage IPs, Ports, and apply firewall rules to enhance your network security.")
        st.write("Use the navigation menu on the left to select options.")

    def ip_management_frame(self):
        """Manage blocked IPs."""
        st.header("IP Management")
        col1, col2 = st.columns([3, 1])
        with col1:
            ip = st.text_input("IP Address to Block/Unblock", "")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Block IP"):
                if ip:
                    message = add_ip_to_blocklist(ip)
                    display_message(message, success="blocked" in message)
        with col2:
            if st.button("Unblock IP"):
                if ip:
                    message = remove_ip_from_blocklist(ip)
                    display_message(message, success="unblocked" in message)
        st.subheader("Blocked IPs")
        for blocked_ip in blocked_ips:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(blocked_ip)
            with col2:
                if st.button(f"Remove {blocked_ip}"):
                    message = remove_ip_from_blocklist(blocked_ip)
                    display_message(message, success="removed" in message)

    def port_management_frame(self):
        """Manage blocked ports."""
        st.header("Port Management")
        col1, col2 = st.columns([3, 1])
        with col1:
            port = st.text_input("Port to Block/Unblock", "")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Block Port"):
                if port:
                    message = add_port_to_blocklist(port)
                    display_message(message, success="blocked" in message)
        with col2:
            if st.button("Unblock Port"):
                if port:
                    message = remove_port_from_blocklist(port)
                    display_message(message, success="unblocked" in message)
        st.subheader("Blocked Ports")
        for blocked_port in blocked_ports:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(blocked_port)
            with col2:
                if st.button(f"Remove {blocked_port}"):
                    message = remove_port_from_blocklist(blocked_port)
                    display_message(message, success="removed" in message)

    def apply_rules(self):
        """Apply firewall rules."""
        message = apply_firewall_rules()
        st.info(message)

    def clear_rules(self):
        """Clear all firewall rules."""
        message = clear_firewall_rules()
        st.warning(message)

    def ip_simulation_frame(self):
        """Simulate IP ping."""
        st.header("IP Simulation")
        ip_to_ping = st.text_input("IP Address to Ping:", "")
        if st.button("Ping IP"):
            if ip_to_ping:
                result = ping_ip(ip_to_ping)
                display_message(result, success="success" in result)

    def port_simulation_frame(self):
        """Simulate port check."""
        st.header("Port Simulation")
        port_to_check = st.text_input("Port to Check:", "")
        if st.button("Check Port"):
            if port_to_check:
                result = check_blocked_port(port_to_check)
                display_message(result, success="open" in result)

    def firewall_statistics_page(self):
        """Display Firewall Statistics (Donut Chart)."""
        st.header("Firewall Statistics")

        # Data for the Donut chart
        labels = ["Blocked IPs", "Blocked Ports"]
        values = [len(blocked_ips), len(blocked_ports)]

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.4,  
            textinfo="percent+label",
            marker=dict(colors=['#87CEEB', '#A9A9A9'])  
        )])

        st.plotly_chart(fig)