from datetime import datetime


class Transaction:
    """
    Represents a financial transaction, which can be either an income or an expense.

    Attributes:
        amount (float): The amount of the transaction.
        date (datetime): The date of the transaction.
        category (str): The category of the transaction.
        description (str): A description of the transaction.
        type (str): The type of the transaction, either "income" or "expense".
    """

    def __init__(self, amount, date, category, description, t_type):
        """
        Initialize a Transaction instance.

        :param amount: The amount of the transaction.
        :param date: The date of the transaction, can be a datetime object or a string in "YYYY-MM-DD" format.
        :param category: The category of the transaction.
        :param description: A description of the transaction.
        :param t_type: The type of the transaction, either "income" or "expense".

        :type amount: float
        :type date: datetime or str
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
        Return a user-friendly string representation of the transaction.
        This string includes the date, type, amount, category, and description.

        :return: A formatted string representing the transaction.
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
    Represents an income transaction, inheriting from Transaction.
    """
    def __init__(self, amount, date, category, description, source, tax_info):
        """
        Initialize an Income instance.
        This constructor sets the amount, date, category, description, source of income, and tax information.

        :param amount: The amount of the income transaction.
        :param date: The date of the income transaction, can be a datetime object or a string in "YYYY-MM-DD" format.
        :param category: The category of the income transaction.
        :param description: A description of the income transaction.
        :param source: The source of the income (e.g., salary, freelance work).
        :param tax_info: Tax information related to the income (e.g., tax rate, deductions).

        :type amount: float
        :type date: datetime or str
        :type category: str
        :type description: str
        :type source: str
        :type tax_info: dict or str

        """
        super().__init__(amount, date, category, description, "income")
        self.source = source
        self.tax_info = tax_info


class Expense(Transaction):
    """
    Represents an expense transaction, inheriting from Transaction.
    """

    def __init__(self, amount, date, category,
                 description, payment_method, is_recurring):
        """
        Initialize an Expense instance.
        This constructor sets the amount, date, category, description, payment method, and whether the expense is recurring.

        :param amount: The amount of the expense transaction.
        :param date: The date of the expense transaction, can be a datetime object or a string in "YYYY-MM-DD" format.
        :param category: The category of the expense transaction.
        :param description: A description of the expense transaction.
        :param payment_method: The method of payment (e.g., cash, credit card).
        :param is_recurring: A boolean indicating if the expense is recurring (True) or one-time (False).

        :type amount: float
        :type date: datetime or str
        :type category: str
        :type description: str
        :type payment_method: str
        :type is_recurring: bool

        """
        super().__init__(amount, date, category, description, "expense")
        self.payment_method = payment_method
        self.is_recurring = is_recurring
