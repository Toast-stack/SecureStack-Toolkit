# visual_csv.py
import csv

def generate_csv_report(vulnerabilities, configuration_issues=None):
    with open("vulnerability_report.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(["Type", "Software/Target", "Details", "Severity (if applicable)"])
        
        # Vulnerabilities Section
        if vulnerabilities:
            for software, vuln_list in vulnerabilities.items():
                for vuln in vuln_list:
                    severity = vuln["cvss"] if vuln["cvss"] != "N/A" else "N/A"
                    writer.writerow(["Vulnerability", software, vuln["summary"], severity])
        else:
            writer.writerow(["Vulnerability", "N/A", "No vulnerabilities found", "N/A"])
        
        # Configuration Issues Section
        if configuration_issues:
            for issue in configuration_issues:
                writer.writerow(["Configuration Issue", "N/A", issue, "N/A"])
        else:
            writer.writerow(["Configuration Issue", "N/A", "No configuration issues found", "N/A"])
    
    print("CSV report generated as 'vulnerability_report.csv'")