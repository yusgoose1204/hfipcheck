import ipaddress
import json


def load_ip_data():
    """Load the locally cached IP data from Salesforce."""
    with open("ip_data.json") as f:
        return json.load(f)


def check_ip(ip):
    """
    Check whether the provided IP belongs to any Salesforce Hyperforce CIDR range.

    Args:
        ip (str): An IPv4 or IPv6 address

    Returns:
        str: A message with region and provider info, or a not-found notice.
    """
    try:
        ip_addr = ipaddress.ip_address(ip)
    except ValueError:
        return "❌ Invalid IP format."

    data = load_ip_data()
    prefixes = data.get("prefixes", [])

    for entry in prefixes:
        cidr_list = entry.get("ip_prefix", [])
        for cidr in cidr_list:
            try:
                if ip_addr in ipaddress.ip_network(cidr):
                    region = entry.get("region", "Unknown")
                    provider = entry.get("provider", "Unknown")
                    return (
                        f"✅ IP belongs to Salesforce Hyperforce\n"
                        f"• Region: {region}\n"
                        f"• Provider: {provider}\n"
                        f"• CIDR: {cidr}"
                    )
            except ValueError:
                continue  # Skip malformed CIDRs

    return "❌ IP not found in Salesforce Hyperforce ranges."
