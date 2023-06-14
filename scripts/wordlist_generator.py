import random
import string

# Ihr Passwort
your_password = "YOUR_SECURE_PASSWORD"

# Die Gesamtzahl der Passwörter in der Wortliste
total_passwords = 100

# Funktion zum Generieren eines zufälligen Passworts
def generate_random_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

# Erzeugen der Wortliste
wordlist = [generate_random_password() for _ in range(9)]
wordlist.append(your_password)
wordlist.extend(generate_random_password() for _ in range(total_passwords - 10))

# Speichern der Wortliste in einer Datei
with open('kali/kali-files/wordlist.txt', 'w') as f:
    for password in wordlist:
        f.write(password + "\n")
