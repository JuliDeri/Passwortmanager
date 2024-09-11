import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import json_write
import password_class

# root window
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title('Password Generator')

# speicher Verwendung, Länge, Anzahl der Buchstaben, Zahlen und Sonderzeichen
use_query = tk.StringVar()
length_query = tk.StringVar()
letters_query = tk.StringVar()
numbers_query = tk.StringVar()
chars_query = tk.StringVar()


def functionWrapper():
    """
    Functionwrapper, der beim klicken des generiere Passwort Buttons aufgerufen wird. Initialisiert Passwort und
    json_write Objekte
    :return:
    """
    i = 0
    if not checkEntries() and i < 3:
        checkEntries()
        i = + 1

    # parse Eingaben in int und string
    letters_amount = intParse(letters_query)
    length = intParse(length_query)
    numbers_amount = intParse(numbers_query)
    chars_amount = intParse(chars_query)
    use = strParse(use_query)
    # initialisiere password Objekt mit Eingaben
    password = password_class.Password(length, letters_amount, numbers_amount, chars_amount, use)
    # initialisiere json_write Objekt abhängig von password
    write_object = json_write.JsonWrite(password)
    # schreibe in .json Datei das Passwort
    write_object.write()
    # verschlüssel das Passwort und speicher es in einem .json ab
    write_object.encrypt()
    # lösche die .json datei, in der das entschlüsselte passwort zwischengespeichert wurde
    write_object.deletePasswordManager()
    msg = (
        f"Du hast erfolgreich dein Passwort: \"{password.getPassword()}\" für \"{password.getUse()}\" erstellt. "
        f"\nEs ist verschlüsselt in der Datei "
        f"{write_object.getEncryptedFileName()}.\nDu kannst dieses Fenster nun schließen.")
    showinfo(title="Falsche Eingabe", message=msg)
    # schließe Dialogfenster
    root.destroy()


def checkEntries():
    """
    Prüft die eingegebenen Parameter auf Typsicherheit und Values.
    :return: True falls Parameter in Ordnung sind. False falls es Fehler gibt
    """

    try:
        letters_amount = intParse(letters_query)
        length = intParse(length_query)
        numbers_amount = intParse(numbers_query)
        chars_amount = intParse(chars_query)
        use = strParse(use_query)
        checkSum(length, letters_amount, numbers_amount, chars_amount)
        checkSmallerZero(length, letters_amount, numbers_amount)
        return True
    except ValueError:
        msg2 = (
            "Die Eingabe der Passwortlänge, Anzahl der Zahlen, Buchstaben oder Sonderzeichen sind kein Integer.")
        showinfo(title="Falsche Eingabe", message=msg2)
        return False


def checkSum(length, letters_amount, numbers_amount, chars_amount):
    """
    Prüft, ob eingegebene Passwortlänge gleich summe der eingegebenen Zeichentypen ist.
    :param length: Passwortlänge
    :param letters_amount:  Anzahl Buchstaben
    :param numbers_amount: Anzahl Zahlen
    :param chars_amount: Anzahl Sonderzeichen
    """
    try:
        if length != (letters_amount + numbers_amount + chars_amount):
            raise ValueError(f"Die eingegebene Passwortlänge und die Summe der Zahlen, Buchstaben und Sonderzeichen"
                             f"stimmen nicht überein.\n"
                             f"Eingegebene Passwortlänge: {length}.\n"
                             f"Summe der Zahlen, Buchstaben und Sonderzeichen: {letters_amount + numbers_amount + chars_amount}")
        return True
    except ValueError as e:
        showinfo(title="Falsche Eingabe", message=str(e))
        return False


def checkSmallerZero(letters_amount, numbers_amount, chars_amount):
    """
    Prüft, ob Eingabeparameter größer 0 sind.
    :param letters_amount:  Anzahl Buchstaben
    :param numbers_amount: Anzahl Zahlen
    :param chars_amount: Anzahl Sonderzeichen
    """
    try:
        if (letters_amount < 0) or (letters_amount < 0) or (numbers_amount < 0) or (chars_amount < 0):
            raise ValueError("Einer oder mehrere Werte der Passwortlänge, Anzahl der Zahlen, Buchstaben oder "
                             "Sonderzeichen sind kleiner 0 ")
        correct_entries = True
        return True
    except ValueError as e:
        showinfo(title="Falsche Eingabe", message=str(e))
        return False


def intParse(string_var):
    """
     Parsed stringVar in Integer.
    :param string_var: zu parsender stringVar
    :return: Integer
     """
    # Wert aus dem StringVar abrufen und in einen Integer umwandeln
    value = int(string_var.get())
    return value


def strParse(string_var):
    """
    Parsed stringVar in String.
    :param string_var: zu parsender stringVar
    :return: String
    """
    # Wert aus dem StringVar abrufen und in einen Str umwandeln
    value = str(string_var.get())
    return value


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# Verwendung
email_label = ttk.Label(signin, text="Verwendung des Passworts:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=use_query)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# Laenge
password_label = ttk.Label(signin, text="Länge des Passworts:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=length_query)
password_entry.pack(fill='x', expand=True)

# Anzahl Zahlen
password_label = ttk.Label(signin, text="Anzahl der Zahlen (0-9):")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=numbers_query)
password_entry.pack(fill='x', expand=True)

# Anzahl Buchstaben
password_label = ttk.Label(signin, text="Anzahl der Buchstaben (a-z, A-Z) ohne Umlaute:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=letters_query)
password_entry.pack(fill='x', expand=True)

# Anzahl Sonderzeichen
password_label = ttk.Label(signin, text="Anzahl der Sonderzeichen ohne Leerzeichen:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=chars_query)
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Generate", command=functionWrapper)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
