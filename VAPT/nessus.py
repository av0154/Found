import requests
import json

# Define your Nessus server URL and credentials
NESSUS_URL = 'https://your-nessus-server-address'
USERNAME = 'your-username'
PASSWORD = 'your-password'

# Define the endpoint for initiating a scan
SCAN_URL = f'{NESSUS_URL}/scans'

# Define the name of the scan and target to scan
SCAN_NAME = 'Example Scan'
TARGET = '192.168.1.1'

# Define the template UUID for the scan (you can get it from Nessus UI or API)
SCAN_TEMPLATE_UUID = '11111111-1111-1111-1111-111111111111'

# Define headers with content-type and authorization
headers = {'Content-Type': 'application/json'}
auth = (USERNAME, PASSWORD)

# Define the payload for starting a new scan
payload = {
    "uuid": SCAN_TEMPLATE_UUID,
    "settings": {
        "name": SCAN_NAME,
        "text_targets": TARGET
    }
}

# Make a POST request to start the scan
response = requests.post(SCAN_URL, headers=headers, auth=auth, data=json.dumps(payload))

# Check the response status
if response.status_code == 200:
    # If the request is successful, print the response JSON
    print(response.json())
else:
    # If there's an error, print the status code and reason
    print(f'Error: {response.status_code} - {response.reason}')
