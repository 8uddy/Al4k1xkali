import paramiko

def ssh_login(host, username, password=None, key_filename=None):
    # SSH-Verbindung herstellen
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        if key_filename:
            client.connect(hostname=host, username=username, key_filename=key_filename)
        elif password:
            client.connect(hostname=host, username=username, password=password)
        else:
            raise ValueError("Es muss entweder ein Passwort oder ein Key-Dateiname angegeben werden.")

        # Befehle auf dem Server ausführen
        stdin, stdout, stderr = client.exec_command('sudo apt update && sudo apt upgrade -y')

        # Ausgabe der Befehle abrufen
        output = stdout.read().decode('utf-8')

        # Ausgabe anzeigen
        print(output)

    finally:
        # SSH-Verbindung beenden
        client.close()

# Benutzerinteraktion für die Authentifizierungsmethode

#TODO create .env file and create function
auth_method = input("Wähle eine Authentifizierungsmethode (1 für Benutzername/Passwort, 2 für Key): ")

if auth_method == '1':
    # Benutzername/Passwort-Authentifizierung
    host = input("Host: ")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    ssh_login(username, password=password)
elif auth_method == '2':
    # Key-Authentifizierung
    username = input("Benutzername: ")
    key_filename = input("Pfad zur SSH-Key-Datei: ")
    ssh_login(username, key_filename=key_filename)
else:
    print("Ungültige Auswahl.")
