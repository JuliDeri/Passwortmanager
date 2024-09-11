import json
import os

from cryptography.fernet import Fernet

import password_class


class JsonWrite:

    def __init__(self, password: password_class.Password):
        self._file_name = "passwordManager.json"
        self._file_name_encrypted = "encryptedPasswordManager.json"
        self.password = password

    def getFileName(self):
        return self._file_name

    def getEncryptedFileName(self):
        return self._file_name_encrypted

    def getPassword(self):
        return self.password

    def write(self):
        """
        Funktion, die ein dict des Passworts als JSON abspeichert
        :return:
        """
        json_dict = {"Verwendung des Passworts": self.getPassword().getUse(),
                     "Passwort": self.getPassword().getPassword()}
        text_file = open(self.getFileName(), "w")
        json.dump(json_dict, text_file, indent=4, sort_keys=True)

    def encrypt(self):
        """
        Methode verschlüsselt das übergebene Passwort und speichert es in json datei ab
        :return: key
        """
        # generiere key
        key = Fernet.generate_key()
        # öffne json und lese Daten in "data"
        with open(self.getFileName(), "rb") as f:
            data = f.read()
        # verschlüssle die Daten aus der JSON und speicher in "encrypted
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        string_data = encrypted.decode("utf-8")

        # schreibe die verschlüsselten Daten in ein neues JSON
        text_file = open(self.getEncryptedFileName(), "w")
        json_dict = {"Verwendung des Passworts": self.getPassword().getUse(),
                     "Verschluesseltes Passwort": string_data}
        json.dump(json_dict, text_file, indent=4, sort_keys=True)
        return key

    def decrypt(self, key):
        """
        Methode entschlüsselt das verschlüsselte Passwort und gibt dieses wieder als json datei aus
        :param key: Key, der erstellt wurde bei der Verschlüsselung
        :return:
        """
        # generiere Fernet objekt
        decipher = Fernet(key)
        # lese und entschlüssel data aus file
        with open(self.getEncryptedFileName(), "rb") as json_file:
            # lese json ein, return ist dict
            encrypted_data = json.load(json_file)
            # frage werte des dicts ab
            encrypted_password = encrypted_data["Verschluesseltes Passwort"]
            password_use = encrypted_data["Verwendung des Passworts"]
            # entschlüssel das verschlüsselte passwort
            decrypted_password = decipher.decrypt(encrypted_password)
            # wandle byte in string um und wende strip() an
            string_data = decrypted_password.decode("utf-8").strip()
        # wende die formatier Methode an für filtern nach passwort
        formatted_decrypted_string_password = self.formatString(string_data)
        # schreibe werte in json und speichere in json file
        new_data_dict = {"Verwendung des Passworts": password_use,
                         "Passwort": formatted_decrypted_string_password}
        with open(self.getFileName(), "w") as text_file:
            json.dump(new_data_dict, text_file, indent=None)

    def formatString(self, input_string):
        """
        Methode filternt einen String nach dem enthaltenen Passwort
        :param input_string:
        :return:
        """
        # Finde den Index des ersten Vorkommens von ":"
        colon_index = input_string.find(":")
        # Finde den Index des ersten Vorkommens von ","
        comma_index = input_string.find(",", colon_index)
        # Extrahiere den Wert zwischen ":" und ","
        password_value = input_string[colon_index + 3:comma_index - 1]
        return password_value

    def deletePasswordManager(self):
        """
        Löscht die unverschlüsselte Datei in dem das Passwort enthalten ist
        :return:
        """
        os.remove(self.getFileName())
