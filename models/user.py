import hashlib


class User:
    """
    User-Objekt für die Finanz-App.
    """
    def __init__(self, name, email, password_hash, accounts=None):
        """
        Initialisiert ein User-Objekt mit Name, E-Mail, Passwort-Hash und optionalen Accounts.

        :param name: Name des Users
        :param email: E-Mail-Adresse
        :param password_hash: Passwort-Hash (SHA-256)
        :param accounts: Liste der Accounts des Users

        :type accounts: list of Account objects
        :type name: str
        :type email: str
        :type password_hash: str


        """
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.accounts = accounts if accounts is not None else []

    def add_account(self, account):
        """
        Fügt dem User ein neues Konto hinzu.

        :param account: Account-Objekt, das hinzugefügt werden soll
        :type account: Account object
        :return: None

        """
        self.accounts.append(account)

    def total_balance(self):
        """
        Berechnet die Summe der Salden aller Accounts des Users.

        :return: Gesamtsumme der Salden aller Accounts
        :rtype: float
        """
        return sum(acc.get_balance() for acc in self.accounts)

    def check_password(self, password):
        """
        Prüft, ob das eingegebene Passwort korrekt ist.

        :param password: Eingegebenes Passwort (Plaintext)
        :return: True, wenn Passwort korrekt, sonst False
        :rtype: bool

        """
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed == self.password_hash
