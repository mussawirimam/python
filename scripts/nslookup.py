import os

# Rename 'list' to avoid conflict with built-in type
ip_list = ["8.8.8.8", "8.8.4.4"]  # Use strings instead of numbers

for ip in ip_list:
    print(f"Running nslookup for {ip}...")
    os.system(f"nslookup {ip}")  # Run nslookup for each IP

#---------------------
# this is sepearte snippet from above but modified on top of it to parameterize the ip_list 
import os

# Define the function to accept command and ip_list as parameters and turned in the function
def run_command(command, ip_list=None):
    # Default ip_list if not provided
    if ip_list is None:
        ip_list = ["8.8.8.8", "8.8.4.4"]
    
    for ip in ip_list:
        print(f"Running {command} for {ip}...")
        os.system(f"{command} {ip}")  # Run the command (nslookup, ping, etc.) for each IP

# Call the function with 'nslookup' and the default ip_list
run_command("nslookup")

# You can also pass a custom list of IPs
custom_ip_list = ["1.1.1.1", "1.0.0.1"]
run_command("ping", custom_ip_list)
