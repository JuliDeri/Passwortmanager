# Passwortmanager

## Abschlussprojekt
Dieses Projekt ist Teil eines Abschlussprojekts einer Fortbildung in der Programmierung mit Python. Es wurde mit der Note "Sehr Gut" (100/100 Punkten) bewertet. 

Dieses Projekt ist ein Passwortmanager, der in Python entwickelt wurde. Das System besteht aus drei Hauptkomponenten:

1. **`password_class.py`** - Beinhaltet die Logik zur Erstellung von Passwörtern, einschließlich der Generierung und Mischung der Zeichen.
2. **`json_write.py`** - Verwalten des Speicherns, Verschlüsselns und Entschlüsselns der Passwörter in JSON-Dateien.
3. **`gui.py`** - Stellt eine Benutzeroberfläche bereit, die es ermöglicht, Passwörter zu erstellen und zu speichern.

## Funktionen

- Generierung von Passwörtern mit benutzerdefinierten Anforderungen: Länge, Anzahl von Buchstaben, Zahlen und Sonderzeichen.
- Speicherung des generierten Passworts in einer JSON-Datei.
- Verschlüsselung des Passworts mit dem Fernet-Modul von `cryptography` und Speicherung der verschlüsselten Version in einer separaten JSON-Datei.
- Möglichkeit, das verschlüsselte Passwort zu entschlüsseln und wiederherzustellen.

## Installation

1. **Klonen Sie das Repository:**

   ```bash
   git clone https://github.com/DEIN_USERNAME/DEIN_REPOSITORY.git
   cd DEIN_REPOSITORY

2. **Installieren Sie die benötigten Pakete:**

Stellen Sie sicher, dass Sie Python 3.x und pip installiert haben. Installieren Sie die notwendigen Abhängigkeiten mit:

pip install cryptography

## Verwendung
1. **Führen Sie das GUI-Programm aus:**

python gui.py

2. **Geben Sie die gewünschten Parameter für das Passwort ein (Verwendung, Länge, Anzahl von Buchstaben, Zahlen und Sonderzeichen).**

3. **Klicken Sie auf "Generate", um das Passwort zu erstellen.**

- Das Passwort wird in der Datei passwordManager.json im Klartext gespeichert.
- Eine verschlüsselte Version des Passworts wird in encryptedPasswordManager.json gespeichert.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die LICENSE Datei für Details.
