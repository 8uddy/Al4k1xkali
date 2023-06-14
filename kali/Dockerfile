# Verwenden Sie das neueste Kali Linux-Image als Basis
FROM kalilinux/kali-rolling:latest

# Aktualisieren Sie die Paketliste und führen Sie ein Upgrade durch
RUN apt-get update && apt-get upgrade -y

# Installieren Sie nmap und metasploit-framework
RUN apt-get install -y net-tools nano iputils-ping nmap metasploit-framework hydra

# Festlegen des Arbeitsverzeichnisses
WORKDIR /root

# Setzen Sie die Standardinteraktion auf Bash
CMD ["/bin/bash"]
