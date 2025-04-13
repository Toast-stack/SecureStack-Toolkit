import socket
from dns import resolver, reversename, exception

def dns_lookup(domain):
    """
    Perform a DNS lookup to retrieve the IP address of a domain.
    """
    try:
        ip = socket.gethostbyname(domain)
        return f"DNS Lookup: {domain} -> {ip}"
    except socket.gaierror:
        return f"Error: Unable to resolve domain {domain}."

def reverse_dns_lookup(ip_address):
    """
    Perform a reverse DNS lookup to retrieve the domain name of an IP address.
    """
    try:
        reversed_dns = socket.gethostbyaddr(ip_address)
        return f"Reverse DNS Lookup: {ip_address} -> {reversed_dns[0]}"
    except socket.herror:
        return f"Error: Unable to resolve IP address {ip_address}"

def query_dns_record(domain, record_type):
    """
    Query specific DNS records (e.g., A, MX, CNAME) for a domain.
    """
    try:
        answers = resolver.resolve(domain, record_type)
        records = [str(rdata) for rdata in answers]
        return f"{record_type} Records for {domain}: {records}"
    except (resolver.NoAnswer, resolver.NXDOMAIN):
        return f"Error: No {record_type} records found for {domain}."
    except resolver.Timeout:
        return f"Err0r: Query timed out for {domain}."
    except exception.DNSException as e:
        return f"Error: DNS query failed for {domain}. Reason {e}"

