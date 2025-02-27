import os

# Rename 'list' to avoid conflict with built-in type
ip_list = ["8.8.8.8", "8.8.4.4"]  # Use strings instead of numbers

for ip in ip_list:
    print(f"Running nslookup for {ip}...")
    os.system(f"nslookup {ip}")  # Run nslookup for each IP
