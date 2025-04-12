import requests
import paramiko
import ftplib

# Check for missing or insecure HTTP headers
def check_http_headers(target_url):
    try:
        response = requests.get(target_url)
        headers = response.headers

        print(f"Checking HTTP headers for {target_url}...")
        missing_headers = []
        if "X-Frame-Options" not in headers:
            missing_headers.append("X-Frame-Options")
        if "Content-Security-Policy" not in headers:
            missing_headers.append("Content-Security-Policy")
        if "Strict-Transport-Security" not in headers:
            missing_headers.append("Strict-Transport-Security")

        if missing_headers:
            print(f"Insecure headers found: {missing_headers}")
        else:
            print(f"All security headers are present for {target_url}.")
    except Exception as e:
        print(f"Error checking HTTP headers: {e}")

# Check for default SSH credentials
def check_ssh_credentials(target_ip, username="root", password="password"):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(f"Checking SSH credentials for {target_ip}...")
        ssh.connect(target_ip, username=username, password=password)
        print(f"Default credentials found for SSH on {target_ip}!")
        ssh.close()
    except paramiko.AuthenticationException:
        print(f"Default credentials not found for SSH on {target_ip}.")
    except Exception as e:
        print(f"Error checking SSH credentials: {e}")

# Check for default FTP credentials
def check_ftp_credentials(target_ip, username="anonymous", password="anonymous"):
    try:
        print(f"Checking FTP credentials for {target_ip}...")
        ftp = ftplib.FTP(target_ip)
        ftp.login(username, password)
        print(f"Default credentials found for FTP on {target_ip}!")
        ftp.quit()
    except ftplib.error_perm:
        print(f"Default credentials not found for FTP on {target_ip}.")
    except Exception as e:
        print(f"Error checking FTP credentials: {e}")