import nmap3


# Ziel-IP-Adresse
target_ip = "172.20.0.2"

nmap = nmap3.Nmap()
results = nmap.scan_top_ports("your-host.com")
# And you would get your results in json
print(results)


# Initialisiere den Portscanner

# Speichere die Ergebnisse in einer Datei
#with open("scan_results.txt") as f:
#    print(f.read())
