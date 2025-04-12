# visual_html.py
def generate_html_report(vulnerabilities, configuration_issues=None):
    with open("vulnerability_report.html", "w") as file:
        file.write("<html><head><style>")
        file.write(".critical { background-color: red; color: white; }")
        file.write(".high { background-color: orange; color: white; }")
        file.write(".medium { background-color: yellow; color: black; }")
        file.write(".low { background-color: green; color: white; }")
        file.write("body { font-family: Arial, sans-serif; line-height: 1.6; }")
        file.write("h1, h2 { color: #333; }")
        file.write("</style></head><body>")
        
        # Title
        file.write("<h1>Vulnerability and Configuration Issues Report</h1>")
        
        # Vulnerabilities Section
        file.write("<h2>Vulnerabilities</h2>")
        if vulnerabilities:
            for software, vuln_list in vulnerabilities.items():
                file.write(f"<h3>{software}</h3>")
                file.write("<ul>")
                for vuln in vuln_list:
                    severity = float(vuln["cvss"]) if vuln["cvss"] != "N/A" else 0
                    if severity >= 9.0:
                        cls = "critical"
                    elif severity >= 7.0:
                        cls = "high"
                    elif severity >= 4.0:
                        cls = "medium"
                    else:
                        cls = "low"
                    file.write(f"<li class='{cls}'>{vuln['id']}: {vuln['summary']} (CVSS: {vuln['cvss']})</li>")
                file.write("</ul>")
        else:
            file.write("<p>No vulnerabilities found.</p>")
        
        # Configuration Issues Section
        file.write("<h2>Weak Configuration Issues</h2>")
        if configuration_issues:
            file.write("<ul>")
            for issue in configuration_issues:
                file.write(f"<li>{issue}</li>")
            file.write("</ul>")
        else:
            file.write("<p>No configuration issues found.</p>")
        
        file.write("</body></html>")
    
    print("HTML report generated as 'vulnerability_report.html'")