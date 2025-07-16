from datetime import datetime


class Transaction:
    """
    Repräsentiert eine Finanztransaktion, die entweder eine Einnahme oder eine Ausgabe sein kann.

    Attribute:
        amount (float): Der Betrag der Transaktion.
        date (datetime): Das Datum der Transaktion.
        category (str): Die Kategorie der Transaktion.
        description (str): Eine Beschreibung der Transaktion.
        type (str): Der Typ der Transaktion, entweder ``"income"`` oder ``"expense"``.
    """

    def __init__(self, amount, date, category, description, t_type):
        """
        Initialisiert eine ``Transaction``-Instanz.

        :param amount: Der Betrag der Transaktion.
        :param date: Das Datum der Transaktion, entweder als ``datetime``-Objekt oder als String im Format ``"YYYY-MM-DD"``.
        :param category: Die Kategorie der Transaktion.
        :param description: Eine Beschreibung der Transaktion.
        :param t_type: Der Typ der Transaktion, entweder ``"income"`` oder ``"expense"``.

        :type amount: float
        :type date: datetime | str
        :type category: str
        :type description: str
        :type t_type: str

        """
        self.amount = amount
        self.date = datetime.strptime(
            date, "%Y-%m-%d") if isinstance(date, str) else date
        self.category = category
        self.description = description
        self.type = t_type  # "income" oder "expense"

    def __str__(self):
        """
        Gibt eine benutzerfreundliche String-Repräsentation der Transaktion zurück.
        Dieser String enthält Datum, Typ, Betrag, Kategorie und Beschreibung.

        :return: Formatierter String, der die Transaktion repräsentiert.
        :rtype: str

        """
        return f"{
            self.date.date()} | {
            self.type.upper()} | {
            self.amount:.2f} € | {
                self.category} | {
                    self.description}"


class Income(Transaction):
    """
    Repräsentiert eine Einnahmetransaktion und erbt von ``Transaction``.
    """

    def __init__(self, amount, date, category, description, source, tax_info):
        """
        Initialisiert eine ``Income``-Instanz.
        Dieser Konstruktor setzt Betrag, Datum, Kategorie, Beschreibung, Herkunft der Einnahme sowie Steuerinformationen.

        :param amount: Der Betrag der Einnahme.
        :param date: Das Datum der Einnahme, entweder als ``datetime``-Objekt oder als String im Format ``"YYYY-MM-DD"``.
        :param category: Die Kategorie der Einnahme.
        :param description: Eine Beschreibung der Einnahme.
        :param source: Die Quelle der Einnahme (z. B. Gehalt, freiberufliche Arbeit).
        :param tax_info: Steuerinformationen zu dieser Einnahme (z. B. Steuersatz, Abzüge).

        :type amount: float
        :type date: datetime | str
        :type category: str
        :type description: str
        :type source: str
        :type tax_info: dict | str

        """
        super().__init__(amount, date, category, description, "income")
        self.source = source
        self.tax_info = tax_info


class Expense(Transaction):
    """
    Repräsentiert eine Ausgabetransaktion und erbt von ``Transaction``.
    """

    def __init__(self, amount, date, category,
                 description, payment_method, is_recurring):
        """
        Initialisiert eine ``Expense``-Instanz.
        Dieser Konstruktor setzt Betrag, Datum, Kategorie, Beschreibung, Zahlungsmethode sowie die Information, ob es sich um eine wiederkehrende Ausgabe handelt.

        :param amount: Der Betrag der Ausgabe.
        :param date: Das Datum der Ausgabe, entweder als ``datetime``-Objekt oder als String im Format ``"YYYY-MM-DD"``.
        :param category: Die Kategorie der Ausgabe.
        :param description: Eine Beschreibung der Ausgabe.
        :param payment_method: Die Zahlungsmethode (z. B. Bargeld, Kreditkarte).
        :param is_recurring: ``True`` bei wiederkehrender Ausgabe, sonst ``False``.

        :type amount: float
        :type date: datetime | str
        :type category: str
        :type description: str
        :type payment_method: str
        :type is_recurring: bool

        """
        super().__init__(amount, date, category, description, "expense")
        self.payment_method = payment_method
        self.is_recurring = is_recurring
