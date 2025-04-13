# **SecureStack Toolkit Documentation**

## **Overview**
The SecureStack Toolkit is a modular cybersecurity program designed to simplify tasks such as vulnerability scanning, network analysis, reporting, and weak configuration checks. Featuring a user-friendly hybrid menu and threaded processes, it offers a powerful and intuitive solution for securing systems.

## **Table of Contents**
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Program Structure](#program-structure)
- [Usage Instructions](#usage-instructions)
- [Example Workflows](#example-workflows)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## **Features**
### **1. Vulnerability Scanning**
- **Mock Scan**: Simulate vulnerabilities using predefined test data.
- **Real Scan**: Fetch real vulnerabilities via the CVE API with multi-threading for speed.

### **2. Reporting Options**
- **ASCII Report**: Present vulnerabilities in a concise, readable text format.
- **HTML Report**: Create a styled, detailed HTML Summary of vulnerabilities.
- **CSV Report**: Export data to CSV for external analysis.
- **Chart Visualization**: Visualize vulnerabilities in easy-to-understand charts.

### **3. Network Tools**
- **Basic Port Scan**: Detect open ports for a specified IP and port range.
- **Advanced Nmap Scan**: Perform in-depth network analysis using Nmap.
- **Weak Configuration Checks**:
  - **HTTP Headers Check**: Analyze HTTP headers for missing or insecure configurations.
  - **SSH Credentials Check**: Verify default or weak SSH credentials.
  - **FTP Credentials Check**: Assess FTP configurations for vulnerabilities.
- **DNS Analysis**:
    - Perform DNS-related tasks to analyze domains and IP addresses:
      - **DNS Lookup**: Retrieve the IP address of a domain.
      - **Reverse DNS Lookup**: Get the domain name associated with an IP address.
      - **Query Specific DNS Records**: Retrieve DNS records like `A`, `MX`, and `CNAME`.

## **Dependencies**
The SecureStack Toolkit requires the following libraries and tools to operate:
### **Python Libraries**
Ensure these libraries are installed via `pip`:
- `concurrent.futures`: Manages thread pooling for concurrent operations.
- `csv`: Exports vulnerabilities and configurations to CSV files.
- `dnspython`: Provides advanced DNS querying capabilities.
- `matplotlib`: Generates charts and visual representations of vulnerabilities.
- `nmap`: Python wrapper for Nmap, enabling advanced network analysis.
- `requests`: Handles HTTP requests for the CVE API.
- `socket`: Powers basic port scanning functionality and DNS queries.
- `subprocess`: Used to run PowerShell commands and interact with the operating system.
- `threading`: Supports multi-threaded tasks for efficiency.

### **External Tools**
Ensure these tools are installed on your system:
- **Nmap**: Necessary for performing advanced network scans. Install it from [Nmap.org](https://nmap.org/download.html).
- **PowerShell**: Required for retrieving installed software on Windows systems.


## **Installation**
To install the required Python packages, run:
```bash
pip install -r requirements.txt
```

## **Program Structure**
The toolkit is organized into modular files:
- **`data_fetching.py`**: Retrieves software data and vulnerabilities (mock and real).
- **`dns_analysis.py`**: Handles DNS lookups, reverse lookups, and DNS record queries.
- **`main.py`**: Facilitates the hybrid menu system and integrates all features.
- **`network_scanning.py`**: Conducts socket-based port scans and Nmap network analysis.
- **`visual_ascii.py`**: Creates terminal-friendly ASCII reports.
- **`visual_chart.py`**: Produces graphical charts of vulnerability trends.
- **`visual_csv.py`**: Exports structured vulnerability data to CSV files.
- **`visual_html.py`**: Generates HTML summaries of vulnerabilities.
- **`weak_configuration_checks.py`**: Performs HTTP, SSH, and FTP configuration checks.

## **Usage Instructions**
to start the toolkit, run the following command:
```bash
python main.py
```

### **Menu Options**
- **Vulnerability Scanning**
  - Mock Scan: Simulate vulnerabilities with test data.
  - Real Scan: Fetch real vulnerabilities using the CVE API.
- **Reporting Options**
  - Generate ASCII, HTML, or CSV reports.
  - Visualize vulnerabilities with charts.
- **Network Tools**
  - Perform port scans and advanced network analysis.
  - Analyze system configurations for weak points.
  - Allows users to perform DNS lookups, reverse DNS lookups, and query specific DNS records (e.g., A, MX, CNAME).
- **Exit**
  - Close the toolkit.


## **Example Workflows**
### **1. Vulnerability Scan**
- Run a **Mock Scan** for predefined vulnerabilities.
- Perform a **Real Scan** to fetch vulnerabilities via the CVE API.

### **2. Network Analysis**
- Run a **Basic Port Scan** to detect open ports.
- Perform an **Advanced Nmap Scan** for in-depth analysis.
- Perform **DNS Analysis** to retrieve IP addresses, resolve domains for IPs, and query specific DNS records for deeper insights.

### **3. Reporting**
- Generate an **HTML Report** to review vulnerabilities in detail.
- Export data to **CSV** for external processing.

## **License**
This project is licensed under the MIT License. This means:
- You are free to use, modify, and distribute the code.
- Proper attribution is required.
See the [LICENSE](LICENSE) file for more details.

## **Contributing**

I welcome contributions to SecureStack Toolkit! Here's how you can help:
1. **Fork** the repository and create a new branch.
2. Make your changes and commit them with clear messages.
3. Submit a **Pull Request**, describing what you've changed or added.

## **Acknowledgments**

- **API Providers**: Special thanks to the CVE API for providing vulnerability data.
- **Tools and Libraries**: This project relies on open-source tools like Nmap and Python libraries.
- **Community Support**: Shoutout to the cybersecurity community for their knowledge and inspiration.
