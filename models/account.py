class Account:
    """Account-Objekt für die Finanz-App."""
    def __init__(self, name, categories=None, monthly_budget=None):
        """
        Initialisiert ein Account-Objekt mit Name, Kategorien und optionalem monatlichen Budget.

        :param name: Name des Kontos
        :param categories: Liste von Kategorien, die diesem Konto zugeordnet sind
        :param monthly_budget: Optionales monatliches Budget für das Konto

        :type name: str
        :type categories: list of Category objects
        :type monthly_budget: float or None


        Initialisiert ein Account-Objekt mit einem Namen, einer Liste von Kategorien und einem optionalen monatlichen Budget.

        """
        self.name = name
        self.categories = categories if categories is not None else []
        self.transactions = []
        self.monthly_budget = monthly_budget

    def add_category(self, category):
        """
        Fügt eine Kategorie zum Account hinzu.

        :param category: Kategorie-Objekt, das hinzugefügt werden soll
        :type category: Category object
        :return: None


        """
        self.categories.append(category)

    def add_transaction(self, transaction):
        """
        Fügt eine Transaktion zum Account hinzu.

        :param transaction: Transaktion-Objekt, das hinzugefügt werden soll
        :type transaction: Transaction object
        :return: None



        """
        self.transactions.append(transaction)

    def get_balance(self):
        """
        Berechnet das verbleibende Budget:
        Budget - Ausgaben + Einnahmen

        Gibt None zurück, falls kein Budget gesetzt ist.

        :return: Verbleibendes Budget oder None, falls kein Budget gesetzt ist
        :rtype: float or None

        """
        if self.monthly_budget is None:
            return None

        total_incomes = sum(
            t.amount for t in self.transactions if t.type == "income"
        )
        total_expenses = sum(
            t.amount for t in self.transactions if t.type == "expense"
        )

        saldo = self.monthly_budget - total_expenses + total_incomes
        return saldo

    def list_transactions(self):
        """
        Gibt eine Liste aller Transaktionen als Strings zurück.
        :return: Liste von Transaktions-Strings
        :rtype: list of str

        """
        return [str(t) for t in self.transactions]

    def summary_by_category(self):
        """
        Erstellt eine Zusammenfassung der Transaktionen nach Kategorien.
        :return: Dictionary mit Kategorien als Schlüsseln und Summen der Beträge
        :rtype: dict

        """
        summary = {}
        for t in self.transactions:
            if t.category in summary:
                summary[t.category] += t.amount if t.type == "income" else -t.amount
            else:
                summary[t.category] = t.amount if t.type == "income" else -t.amount
        return summary
