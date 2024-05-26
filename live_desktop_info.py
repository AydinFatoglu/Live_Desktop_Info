import tkinter as tk
import ctypes
import socket

# Function to get hostname and IP address
def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

# Function to set window to desktop level
def set_to_desktop(window):
    hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, 0x80)
    ctypes.windll.user32.SetWindowPos(hwnd, 1, 0, 0, 0, 0, 0x0001 | 0x0002)

# Create the main window
root = tk.Tk()
root.title("Desktop Level Window")
root.overrideredirect(True)

# Modern look: custom font, color
font_style = ("Arial", 10, "bold")
bg_color = "#333333"
fg_color = "#FFFFFF"
root.configure(bg=bg_color)

# Get network info
hostname, ip_address = get_network_info()

# Display network info
hostname_label = tk.Label(root, text=f"V-Dektop Hostname: {hostname}", font=font_style, bg=bg_color, fg=fg_color)
hostname_label.pack(pady=(10,0))

ip_label = tk.Label(root, text=f"V-Dektop IP: {ip_address}", font=font_style, bg=bg_color, fg=fg_color)
ip_label.pack(pady=(5,10))

# Screen dimensions and window positioning
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 100
x = screen_width - window_width -10
y = screen_height - window_height - 62
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set to desktop level
root.after(0, lambda: set_to_desktop(root))

# Run the application
root.mainloop()
