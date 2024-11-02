import requests
import os
import time

# Define the base URL and phone number prefix
base_url = "https://anticybercrimeact.xyz/api/BIO/teletalk.php?phone="
prefix = "015"

# Initialize a counter for successful responses
success_count = 0

# Loop through all possible Teletalk numbers (example range for 6.46 million users)
for i in range(12345678, 12345678 + 6460000):
    phone_number = prefix + str(i)
    url = f"{base_url}{phone_number}"
    
    # Send the request and get the response
    try:
        response = requests.get(url)
        if response.status_code == 200:  # Check for successful response
            success_count += 1
            print(f"Success {success_count}")
        
    except Exception as e:
        print(f"Error querying {phone_number}: {e}")
    
    # Optional: Delay to prevent server overload
    time.sleep(0.00001)  # Adjust as needed

# Define the storage path
storage_path = "/storage/emulated/0/teletalk_data.txt"  # Ensure the path is correct

# Attempt to save the success count to the specified storage path
try:
    with open(storage_path, "w") as file:
        file.write(f"Total successful queries: {success_count}\n")
    print(f"All data saved to {storage_path}")
except Exception as e:
    print(f"Failed to save data: {e}")
