#!/bin/bash

TARGET="172.19.0.3" 
OUTPUT_FILE="nmap_scan_results.txt"

echo "Starte Scan des Ziels $TARGET"
nmap -v -A $TARGET > $OUTPUT_FILE

echo "Scan abgeschlossen. Ergebnisse gespeichert in $OUTPUT_FILE"
