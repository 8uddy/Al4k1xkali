from cryptography.fernet import Fernet
import os

def generate_key():
    # Schlüssel generieren
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Lädt den Schlüssel aus der Datei secret.key
    return open("secret.key", "rb").read()

def encrypt(filename, key):
    # Verwendet den Schlüssel um die angegebene Datei zu verschlüsseln
    f = Fernet(key)

    with open(filename, "rb") as file:
        # Datei lesen
        file_data = file.read()

    # Daten verschlüsseln
    encrypted_data = f.encrypt(file_data)

    # Verschlüsselte Daten schreiben
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    # Verwendet den Schlüssel um die angegebene Datei zu entschlüsseln
    f = Fernet(key)

    with open(filename, "rb") as file:
        # Datei lesen
        encrypted_data = file.read()

    # Daten entschlüsseln
    decrypted_data = f.decrypt(encrypted_data)

    # Entschlüsselte Daten schreiben
    with open(filename, "wb") as file:
        file.write(decrypted_data)



#generate_key()
key = load_key()
encrypt("test.txt", key)  # Ersetzen Sie "test.txt" durch den Dateinamen, den Sie verschlüsseln möchten

#key = load_key()
#decrypt("test.txt", key)  # Ersetzen Sie "test.txt" durch den Dateinamen, den Sie entschlüsseln möchten
