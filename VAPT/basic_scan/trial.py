import requests
import json
import urllib3

urllib3.disable_warnings()
# Set up Nessus API credentials and endpoint
NESSUS_URL = 'https://192.168.56.1:8834'
USERNAME = 'av0154'
PASSWORD = 'Foundathon123'

# Authenticate with Nessus
login_data = {'username': USERNAME, 'password': PASSWORD}
response = requests.post(f'https://192.168.56.1:8834/#/', json=login_data, verify=False)

if response.status_code == 200:
    token = response.json()['token']
    headers = {'X-Cookie': f'token={token}'}
    print('Login successful.')
else:
    print('Login failed.')
    exit()

# Define scan configuration
scan_name = 'Basic Scan'
target = input("Enter the IP Address:")  # Example target IP address
policy_id = 1  # Example policy ID (1 represents the default policy)

# Create scan
scan_data = {
    'uuid': '00000000-0000-0000-0000-000000000000',  # You can set a custom UUID or leave it as default
    'settings': {
        'name': scan_name,
        'text_targets': target,
        'policy_id': policy_id,
        'enabled': 'true'
    }
}

response = requests.post(f'{NESSUS_URL}/scans', headers=headers, json=scan_data, verify=False)

if response.status_code == 200:
    scan_id = response.json()['id']
    print(f'Scan "{scan_name}" created successfully with ID: {scan_id}')
else:
    print('Failed to create scan.')
    exit()

# Launch scan
response = requests.post(f'{NESSUS_URL}/scans/{scan_id}/launch', headers=headers, verify=False)

if response.status_code == 200:
    print('Scan launched successfully.')
else:
    print('Failed to launch scan.')

