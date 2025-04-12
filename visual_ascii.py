# visual_ascii.py
def display_ascii_report(vulnerabilities):
    print("\nVulnerability Report (ASCII Symbols):")
    for software, vuln_list in vulnerabilities.items():
        print(f"\n{software} vulnerabilities:")
        for vuln in vuln_list:
            severity = float(vuln["cvss"]) if vuln["cvss"] != "N/A" else 0
            if severity >= 9.0:
                icon = "!!!"
            elif severity >= 7.0:
                icon = "!!"
            elif severity >= 4.0:
                icon = "!"
            else:
                icon = "."
            print(f"{icon} {vuln['id']}: {vuln['summary']} (Severity: {vuln['cvss']})")