class Transaction:
    """
    A class to represent a financial transaction.
    """
    def __init__(self, transaction_id, amount, date, description):
        """
        Initialize the transaction with an ID, amount, date, and description.
        :param transaction_id: Unique identifier for the transaction.
        :param amount: The amount of the transaction.
        :param date: The date of the transaction.
        :param description: A brief description of the transaction.


        :type transaction_id: str
        :type amount: float
        :type date: str
        :type description: str

        """
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description

    def __repr__(self):
        return f"Transaction(id={
            self.transaction_id}, amount={
            self.amount}, date={
            self.date}, description='{
                self.description}')"

    def __str__(self):
        return f"Transaction ID: {
            self.transaction_id}, Amount: {
            self.amount}, Date: {
            self.date}, Description: {
                self.description}"


class Expense(Transaction):
    """
    A class to represent an expense transaction, inheriting from Transaction.
    """
    def __init__(self, transaction_id, amount, date, description, category):
        """
        Initialize the expense with an ID, amount, date, description, and category.
        """
        super().__init__(transaction_id, amount, date, description)
        self.category = category

    def __repr__(self):
        """
        Return a string representation of the expense.
        """
        return f"Expense(id={
            self.transaction_id}, amount={
            self.amount}, date={
            self.date}, description='{
                self.description}', category='{
                    self.category}')"

    def __str__(self):
        """
        Return a user-friendly string representation of the expense.
        """
        return f"Expense ID: {
            self.transaction_id}, Amount: {
            self.amount}, Date: {
            self.date}, Description: {
                self.description}, Category: {
                    self.category}"


class Income(Transaction):
    """
    A class to represent an income transaction, inheriting from Transaction.
    """
    def __init__(self, transaction_id, amount, date, description, source):
        super().__init__(transaction_id, amount, date, description)
        self.source = source

    def __repr__(self):
        """
        Return a string representation of the income.
        """
        return f"Income(id={
            self.transaction_id}, amount={
            self.amount}, date={
            self.date}, description='{
                self.description}', source='{
                    self.source}')"

    def __str__(self):
        """
        Return a user-friendly string representation of the income.
        """
        return f"Income ID: {
            self.transaction_id}, Amount: {
            self.amount}, Date: {
            self.date}, Description: {
                self.description}, Source: {
                    self.source}"
