# Verwenden Sie das neueste Ubuntu-Image als Basis
FROM ubuntu:latest

# Aktualisieren Sie die Paketliste und führen Sie ein Upgrade durch
RUN apt-get update && apt-get upgrade -y

# Installieren Sie einige grundlegende Werkzeuge
RUN apt-get install -y net-tools nano iputils-ping

# Optional: Installieren Sie einen SSH-Server, um eine Remote-Verbindung zu ermöglichen
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# Setzen Sie das Root-Passwort für den SSH-Zugang
RUN echo 'root:YOUR_SECURE_PASSWORD' | chpasswd

# Erlauben Sie den Root-Zugang über SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Festlegen des Arbeitsverzeichnisses
WORKDIR /root

# Setzen Sie die Standardinteraktion auf Bash
CMD ["/bin/bash"]

# Expose SSH port
EXPOSE 22

# Starten Sie den SSH-Dienst
CMD ["/usr/sbin/sshd", "-D"]
