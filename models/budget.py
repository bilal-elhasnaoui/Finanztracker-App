class Category:
    """
    Repräsentiert eine Budgetkategorie mit einem Namen und einem Budgetlimit.
    Diese Klasse dient dazu, Budgetkategorien zu definieren und zu prüfen, ob Ausgaben das Budgetlimit überschreiten.

    Attribute:
        name (str): Der Name der Budgetkategorie.
        budget_limit (float): Das maximale Budgetlimit für diese Kategorie.
    """
    def __init__(self, name, budget_limit):
        """
        Initialisiert die Kategorie mit einem Namen und einem Budgetlimit.
        Dieser Konstruktor setzt den Namen und das Budgetlimit der Kategorie.

        :param name: Der Name der Budgetkategorie.
        :param budget_limit: Das maximale Budgetlimit für diese Kategorie.

        :type name: str
        :type budget_limit: float

        """
        self.name = name
        self.budget_limit = budget_limit

    def is_over_budget(self, amount):
        """
        Prüft, ob der angegebene Betrag das Budgetlimit dieser Kategorie überschreitet.

        Diese Methode vergleicht den bereitgestellten Betrag mit dem Budgetlimit und gibt ``True`` zurück, wenn der Betrag das Limit übersteigt, andernfalls ``False``.
        :param amount: Der zu überprüfende Betrag.

        :type amount: float

        :return: ``True`` bei Überschreitung des Budgetlimits, sonst ``False``.
        :rtype: bool

        """
        return amount > self.budget_limit


class BudgetPlan:
    """
    Repräsentiert einen Budgetplan, der Ausgaben anhand definierter Kategorien in einem bestimmten Zeitraum nachverfolgt.
    """
    def __init__(self, categories, start_date, end_date):
        """
        Initialisiert den Budgetplan mit Kategorien und einem Datumsbereich.
        :param categories: Liste von ``Category``-Objekten, die die Budgetkategorien definieren.
        :param start_date: Startdatum des Budgetplans (``datetime``-Objekt).
        :param end_date: Enddatum des Budgetplans (``datetime``-Objekt).

        :type categories: list[Category]
        :type start_date: datetime
        :type end_date: datetime

        """
        self.categories = categories
        self.start_date = start_date
        self.end_date = end_date

    def check_budget(self, transactions):
        """
        Prüft, ob die Ausgaben in den gegebenen Transaktionen das Budget jeder Kategorie überschreiten.
        Diese Methode durchläuft die Transaktionen und berechnet die Gesamtausgaben pro Kategorie.
        Sie gibt ein Dictionary zurück, dessen Schlüssel die Kategorienamen und dessen Werte Booleans sind, die angeben, ob das Budget überschritten wurde.

        :param transactions: Liste von ``Transaction``-Objekten, die überprüft werden sollen.
        :type transactions: list[Transaction]
        :return: Dictionary mit Kategorienamen als Schlüsseln und ``True``/``False`` als Wert, je nachdem, ob das Budget überschritten wurde.
        :rtype: dict

        """
        result = {}
        for category in self.categories:
            total = sum(
                t.amount for t in transactions
                if t.category == category.name and t.type == "expense"
            )
            result[category.name] = category.is_over_budget(total)
        return result
