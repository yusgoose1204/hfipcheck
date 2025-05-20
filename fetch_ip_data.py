import requests
import json

def update_ip_data():
    # URL to Salesforce's official JSON listing of infrastructure IP ranges
    url = "https://ip-ranges.salesforce.com/ip-ranges.json"

    # Perform an HTTP GET request to fetch the latest IP ranges
    res = requests.get(url)

    # Raise an exception if the response indicates a client or server error (4xx or 5xx)
    # This ensures failures are caught early in automated environments
    res.raise_for_status()

    # Proceed only if the response was successful (status code 200)
    if res.ok:
        # Save the JSON payload locally as 'ip_data.json'
        # This will be used by the Slack bot to match input IPs against Salesforce infrastructure
        with open('ip_data.json', 'w') as f:
            json.dump(res.json(), f, indent=2)

if __name__ == "__main__":
    update_ip_data()