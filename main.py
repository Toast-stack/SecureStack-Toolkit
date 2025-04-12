from data_fetching import list_installed_software_real, fetch_cve_data_mock, fetch_cve_data_real
from visual_ascii import display_ascii_report
from visual_html import generate_html_report
from visual_csv import generate_csv_report
from visual_chart import generate_chart
from network_scanning import scan_open_ports, perform_nmap_scan
from weak_configuration_checks import check_http_headers, check_ssh_credentials, check_ftp_credentials


def main():
    """
    Main function to manage the hybrid menu system.
    """
    all_vulnerabilities = {}
    configuration_issues = []

    while True:
        # Top-level Menu
        print("\nMain Menu:")
        print("1. Vulnerability Scanning")
        print("2. Reporting Options")
        print("3. Network Tools")
        print("4. Exit")

        choice = input("Select an option (1–4): ")

        # Submenu: Vulnerability Scanning
        if choice == "1":
            print("\nVulnerability Scanning Menu:")
            print("1. Run Mock Scan")
            print("2. Run Real Scan")
            print("3. Back to Main Menu")
            scan_choice = input("Select an option (1–3): ")

            if scan_choice == "1":
                print("\nRunning Mock Scan...")
                software_data = {"Log4j": "2.14.1", "Apache Struts": "2.3.34", "WordPress": "4.7.0"}
                all_vulnerabilities = {
                    software: fetch_cve_data_mock(software, version) for software, version in software_data.items()
                }
                print("\nMock scan completed successfully.")
            elif scan_choice == "2":
                print("\nRunning Real Scan...")
                try:
                    software_data = list_installed_software_real()
                    print(f"\nInstalled Software: {software_data}")

                    all_vulnerabilities = {}
                    for software, version in software_data.items():
                        print(f"Fetching vulnerabilities for {software} {version}...")
                        vulnerabilities = fetch_cve_data_real(software, version)
                        if vulnerabilities:
                            print(f"Found {len(vulnerabilities)} vulnerabilities for {software} {version}.")
                        else:
                            print(f"No vulnerabilities found for {software} {version}.")
                        all_vulnerabilities[software] = vulnerabilities

                    print("\nReal scan completed successfully!")
                except Exception as e:
                    print(f"Error during real scan: {e}")

        # Submenu: Reporting Options
        elif choice == "2":
            print("\nReporting Options Menu:")
            print("1. Generate ASCII Symbols Report")
            print("2. Generate HTML Report")
            print("3. Generate CSV Report")
            print("4. Show Chart Visualization")
            print("5. Back to Main Menu")
            report_choice = input("Select an option (1–5): ")

            if report_choice == "1":
                display_ascii_report(all_vulnerabilities)
            elif report_choice == "2":
                generate_html_report(all_vulnerabilities, configuration_issues)
            elif report_choice == "3":
                generate_csv_report(all_vulnerabilities, configuration_issues)
            elif report_choice == "4":
                generate_chart(all_vulnerabilities)

        # Submenu: Network Tools
        elif choice == "3":
            print("\nNetwork Tools Menu:")
            print("1. Basic Port Scan (Socket)")
            print("2. Advanced Nmap Scan")
            print("3. Weak Configuration Checks")
            print("4. Back to Main Menu")
            network_choice = input("Select an option (1–4): ")

            if network_choice == "1":
                target_ip = input("Enter the target IP for port scan: ")
                port_range = input("Enter port range (default: 1-1024): ") or "1-1024"
                start_port, end_port = map(int, port_range.split('-'))
                scan_open_ports(target_ip, port_range=(start_port, end_port))
            elif network_choice == "2":
                target_ip = input("Enter the target IP for Nmap scan: ")
                perform_nmap_scan(target_ip)
            elif network_choice == "3":
                print("\nWeak Configuration Check Menu:")
                print("1. Check HTTP Headers")
                print("2. Check SSH Credentials")
                print("3. Check FTP Credentials")
                config_choice = input("Select an option (1–3): ")

                if config_choice == "1":
                    target_url = input("Enter the target URL (e.g., http://example.com): ")
                    check_http_headers(target_url)
                elif config_choice == "2":
                    target_ip = input("Enter the target IP for SSH check: ")
                    username = input("Enter username (default: root): ") or "root"
                    password = input("Enter password (default: password): ") or "password"
                    check_ssh_credentials(target_ip, username, password)
                elif config_choice == "3":
                    target_ip = input("Enter the target IP for FTP check: ")
                    username = input("Enter username (default: anonymous): ") or "anonymous"
                    password = input("Enter password (default: anonymous): ") or "anonymous"
                    check_ftp_credentials(target_ip, username, password)

        elif choice == "4":
            print("Exiting Vulnerability Scanner. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()