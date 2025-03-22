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

#-----------------------
### another way to do nslookup using subprocess module parameterizing the ip_list
import subprocess

def run_command(command, ip_list=None):
    try:
        # If ip_list is provided, loop through the list and run the command for each IP
        if ip_list:
            for ip in ip_list:
                full_command = f"{command} {ip}"
                result = subprocess.run(
                    full_command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(f"Output for {ip}: {result.stdout}")
                
                with open('demofile.txt', 'a') as f:
                    f.write(f"Output for {ip}: {result.stdout}\n")
        else:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            print("Output:", result.stdout)
            
            with open('demofile.txt', 'a') as f:
                f.write(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print("Command failed with error:", e.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}")

# Call the function with "ls -l" and "echo"
run_command("ls -l")
run_command("echo 'Hello World!'")

# Call the function with "nslookup" and an ip_list
ip_list = ["8.8.8.8", "8.8.4.4"]
run_command("nslookup", ip_list)

