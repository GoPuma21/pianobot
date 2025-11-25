import requests
import time
import sys
import subprocess
import tempfile
import os

ASCII_LOGO = r"""
██╗  ██╗██╗   ██╗███╗   ██╗███████╗██╗  ██╗██╗███████╗
██║ ██╔╝╚██╗ ██╔╝████╗  ██║██╔════╝╚██╗██╔╝██║██╔════╝
█████╔╝  ╚████╔╝ ██╔██╗ ██║█████╗   ╚███╔╝ ██║███████╗
██╔═██╗   ╚██╔╝  ██║╚██╗██║██╔══╝   ██╔██╗ ██║╚════██║
██║  ██╗   ██║   ██║ ╚████║███████╗██╔╝ ██╗██║███████║
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝                                                                                                                                                                             
         _____                 _               
        / ___/___  ______   __(_)_______  _____
        \__ \/ _ \/ ___/ | / / / ___/ _ \/ ___/
          / /  __/ /   | |/ / / /__/  __(__  ) 
      /____/\___/_/    |___/_/\___/\___/____/                        
            Kynexis License Checker
"""

SERVER_URL = "https://renderserver-1ujb.onrender.com/validate"  # Replace with your Render URL
EXE_URL = "https://www.dropbox.com/scl/fi/bhz4bug0ra8u7mp9mcb0u/app.exe?rlkey=2i1mv8hodr3d8yfoau4jj11jc&st=cdthhsih&dl=0"

def check_license(key):
    try:
        resp = requests.post(SERVER_URL, json={"key": key}, timeout=5)
        data = resp.json()
        if data.get("valid") and data.get("expires_at") > time.time():
            return True, data.get("expires_at")
    except Exception as e:
        print(f"Error connecting to server: {e}")
    return False, None

def download_and_run_exe():
    print("Downloading Kyneksis app...")
    with requests.get(EXE_URL, stream=True) as r:
        r.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as tmp:
            for chunk in r.iter_content(chunk_size=8192):
                tmp.write(chunk)
            exe_path = tmp.name
    print("Download complete. Launching app...")
    subprocess.Popen([exe_path])
    # Wait a few seconds before deleting
    time.sleep(5)
    try:
        os.remove(exe_path)
    except Exception:
        pass

def main():
    print(ASCII_LOGO)
    license_key = input("Enter your license key: ")
    valid, expires_at = check_license(license_key)
    if valid:
        exp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expires_at))
        print(f"\nLicense valid! Expires at: {exp_str}")
        print("You have 3 seconds to check the expiration date...")
        time.sleep(3)
        download_and_run_exe()
        sys.exit(0)
    else:
        print("\nLicense invalid or expired.")
        sys.exit(1)

if __name__ == "__main__":
    main()
