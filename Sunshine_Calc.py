import tkinter as tk
from tkinter import messagebox

#Sunshine Port Calculator by ULTRA_VAGUE on Github

# Differences from config port for each service
port_differences = {
    "HTTPS": -5,
    "HTTP": 0,
    "Web": +1,
    "RTSP": +21,
    "Video": +9,
    "Control": +10,
    "Audio": +11,
    "Mic (unused)": +13
}

def calculate_ports():
    try:
        # Get the default port from the entry field
        default_port = int(entry.get())
        
        # Calculate actual ports for each service
        actual_ports = {service: default_port + diff for service, diff in port_differences.items()}

        # Sort services by port number
        sorted_services = sorted(actual_ports.items(), key=lambda item: item[1])

        # Clear the text widget
        text.delete('1.0', tk.END)

        # Print actual ports for each service in the text widget
        for service, port in sorted_services:
            if service == "HTTP":
                text.insert(tk.END, f"{service.ljust(15)}: {port} (new default port)\n", 'highlight')
            else:
                text.insert(tk.END, f"{service.ljust(15)}: {port}\n")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter an integer.")

# Create the main window
root = tk.Tk()
root.geometry('800x600')  # Set the size of the window
root.title("Port Calculator")  # Set the title of the window

# Create a label
label = tk.Label(root, text="Enter a new default Port for Sunshine:")
label.pack()

# Create an entry field
entry = tk.Entry(root)
entry.pack()

# Create a button
button = tk.Button(root, text="Calculate Ports", command=calculate_ports)
button.pack()

# Create a text widget for displaying the ports
text = tk.Text(root)
text.pack()

# Define a tag for highlighting text
text.tag_config('highlight', background='yellow')

# Run the event loop
root.mainloop()
