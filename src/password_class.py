import random
import secrets


class Password:

    def __init__(self, length: int, letters_amount: int, numbers_amount: int, chars_amount: int, use: str):
        self.length = length
        self.letters_amount = letters_amount
        self.numbers_amount = numbers_amount
        self.chars_amount = chars_amount
        self.use = use
        self.password = self.shufflePassword()

    def getLettersAmount(self):
        return self.letters_amount

    def getNumbersAmount(self):
        return self.numbers_amount

    def getCharsAmount(self):
        return self.chars_amount

    def getUse(self):
        return self.use

    def getPassword(self):
        return self.password


    def shufflePassword(self):
        """
        Eine Methode, die die Zeichen eines Passworts zufällig durchmischt.
        :return: zufällig durchmischtes password
        """
        # rufe die generatePassword Methode auf und wandle das so erstellte Generator Objekt in ein Liste um
        generator = self.generatePassword()
        out_list = list(generator)
        # vermische die Lise zufällig und gib sie anschließend aus
        random.shuffle(out_list)
        # konvertiere liste in string
        password_str = "".join(str(x) for x in list(out_list))
        return password_str

    def generatePassword(self):
        """
        Ein Generator, der randomStr Methode nutzt um anhand der Attribute des Objekts Password ein Generator Objekt mit
        vorgegebener Länge und Anzahl der Buchstaben, Zahlen, Zeichen erstellt.
        :return: Generator Objekt, das randon generierte Chars anhand von Länge und Anzahl der Buchstaben,
        Zahlen, Zeichen des Passworts enthält.
        """
        # erstellt jeweils ein generator objekt mit der Anzahl der gewünschten Zahlen, Zeichen und Buchstaben
        # unter der Bedingung, dass die Anzahl der jeweiligen Zahlen, Zeichen oder Buchstaben ungleich 0
        if self.getNumbersAmount() > 0:
            for i in range(self.getNumbersAmount()):
                yield self.rdNumber()
        if self.getCharsAmount() > 0:
            for i in range(self.getCharsAmount()):
                yield self.rdChar()
        if self.getLettersAmount() > 0:
            for i in range(self.getLettersAmount()):
                yield self.rdLetter()

    def rdChar(self):
        """
        Eine Methode, die ein zufällig und kryptographisch sicher generiertes Zeichen nach ASCII Englisch (ohne Leerzeichen)
        erstellt
        :return: ein zufällig und kryptographisch sicher generiertes Zeichen nach ASCII Englisch (ohne Leerzeichen)
        """
        # Liste mit ASCII Werten von 33-47 und 56-64 (Zeichen ohne Leerzeichen)
        ascii_list = [y for y in range(33, 47)] + [x for x in range(56, 64)]
        # zufällig generiertes byte aus dem Betriebssystem (kryptografisch sicher) an der Stelle 0 (Wert von 0 bis 255)
        random_byte = secrets.token_bytes(1)[0]
        # mittels modulo wird ein Wert aus der Liste als random Wert ausgesucht
        random_value = random_byte % len(ascii_list)
        return chr(ascii_list[random_value])

    def rdNumber(self):
        """
        Eine Methode, die eine zufällig und kryptographisch sicher generierte Zahl nach ASCII Englisch (0-9) erstellt
        :return: ein zufällig und kryptographisch sicher generierte Zahl nach ASCII Englisch (0-9)
        """
        # Liste mit ASCII Werten von 48-57 (Zahlen 0-9)
        ascii_list = [y for y in range(48, 57)]
        # zufällig generiertes byte aus dem Betriebssystem (kryptografisch sicher) an der Stelle 0 (Wert von 0 bis 255)
        random_byte = secrets.token_bytes(1)[0]
        # mittels modulo wird ein Wert aus der Liste als random Wert ausgesucht
        random_value = random_byte % len(ascii_list)
        return chr(ascii_list[random_value])

    def rdLetter(self):
        """
        Eine Methode, die einen zufällig und kryptographisch sicher generierten Buchstaben nach ASCII Englisch (A-Z, a-z)
        erstellt
        :return: ein zufällig und kryptographisch sicher generierter Buchstabe nach ASCII Englisch (A-Z, a-z)
        """
        # Liste mit ASCII Werten von 65-91(A-Z) und 97-123 (a-z)
        ascii_list = [y for y in range(65, 91)] + [x for x in range(97, 123)]
        # zufällig generiertes byte aus dem Betriebssystem (kryptografisch sicher) an der Stelle 0 (Wert von 0 bis 255)
        random_byte = secrets.token_bytes(1)[0]
        # mittels modulo wird ein Wert aus der Liste als random Wert ausgesucht
        random_value = random_byte % len(ascii_list)
        return chr(ascii_list[random_value])
