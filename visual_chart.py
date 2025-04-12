# visual_chart.py
import matplotlib.pyplot as plt

def generate_chart(vulnerabilities):
    severity_counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    
    for vuln_list in vulnerabilities.values():
        for vuln in vuln_list:
            severity = float(vuln["cvss"]) if vuln["cvss"] != "N/A" else 0
            if severity >= 9.0:
                severity_counts["Critical"] += 1
            elif severity >= 7.0:
                severity_counts["High"] += 1
            elif severity >= 4.0:
                severity_counts["Medium"] += 1
            else:
                severity_counts["Low"] += 1
    
    plt.bar(severity_counts.keys(), severity_counts.values(), color=["red", "orange", "yellow", "green"])
    plt.title("Vulnerability Severity Distribution")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.show()