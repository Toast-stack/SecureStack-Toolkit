import subprocess
import requests
from mock_data import mock_vulnerabilities
from concurrent.futures import ThreadPoolExecutor

# Function to list installed software using PowerShell (Real Scan)
def list_installed_software_real():
    """
    Fetch the list of installed software using an optimized PowerShell command.

    Returns:
        dict: A dictionary of software names and their versions.
    """
    installed_software = {}
    try:
        # Optimized PowerShell command using Get-CimInstance and NoProfile mode
        command = ["powershell.exe", "-NoProfile", "-Command", "Get-CimInstance -ClassName Win32_Product | Select-Object Name, Version"]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

        # Split the output into lines
        lines = result.stdout.split("\n")

        # Process each line to extract software name and version
        for line in lines[1:]:  # Skip the header row
            if line.strip():  # Ignore blank lines
                parts = line.strip().split()
                name = " ".join(parts[:-1])  # All parts except the last one
                version = parts[-1]  # Last part is the version
                installed_software[name] = version
    except Exception as e:
        print(f"Error while fetching installed software: {e}")
    return installed_software


# Function to fetch vulnerabilities for mock scan
def fetch_cve_data_mock(software, version):
    return mock_vulnerabilities.get(software, [])

# Function to fetch vulnerabilities for real scan using the CVE API
def fetch_cve_data_real(software, version):
    url = f"https://cve.circl.lu/api/search/{software}/{version}"
    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        if data and isinstance(data, list):  # Ensure data is a list of vulnerabilities
            return [
                {
                    "id": vuln.get("id", "Unknown ID"),
                    "summary": vuln.get("summary", "No description available"),
                    "cvss": vuln.get("cvss", "N/A"),
                }
                for vuln in data
            ]
        else:
            return []
    except requests.RequestException as e:
        print(f"Error fetching vulnerabilities for {software} {version}: {e}")
        return []

# Function to fetch vulnerabilities for all installed software using a thread pool
def fetch_all_vulnerabilities(installed_software, max_threads=25):
    """
    Fetch vulnerabilities for all installed software using controlled multithreading.

    Parameters:
        installed_software (dict): A dictionary of software names and their versions.
        max_threads (int): Maximum number of threads to use concurrently.

    Returns:
        dict: A dictionary containing vulnerabilities for each software.
    """
    vulnerabilities = {}

    def fetch_vulns(software, version):
        """
        Helper function for thread pool to fetch vulnerabilities for a specific software.
        """
        return software, fetch_cve_data_real(software, version)

    print("\nStarting threaded vulnerability scan with controlled concurrency...")

    # Use ThreadPoolExecutor to limit the number of concurrent threads
    with ThreadPoolExecutor(max_threads) as executor:
        # Submit tasks for each software-version pair
        future_to_software = {executor.submit(fetch_vulns, software, version): software for software, version in installed_software.items()}
        for future in concurrent.futures.as_completed(future_to_software):
            software = future_to_software[future]
            try:
                software, vulns = future.result()
                vulnerabilities[software] = vulns
            except Exception as e:
                print(f"Error fetching vulnerabilities for {software}: {e}")

    print("\nThreaded vulnerability scan completed.")
    return vulnerabilities