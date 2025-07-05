from datetime import datetime


class Transaction:

    def __init__(self, amount, date, category, description, t_type):
        self.amount = amount
        self.date = datetime.strptime(
            date, "%Y-%m-%d") if isinstance(date, str) else date
        self.category = category
        self.description = description
        self.type = t_type  # "income" oder "expense"

    def __str__(self):
        return f"{
            self.date.date()} | {
            self.type.upper()} | {
            self.amount:.2f} € | {
                self.category} | {
                    self.description}"


class Income(Transaction):
    def __init__(self, amount, date, category, description, source, tax_info):
        super().__init__(amount, date, category, description, "income")
        self.source = source
        self.tax_info = tax_info


class Expense(Transaction):
    def __init__(
            self,
            amount,
            date,
            category,
            description,
            payment_method,
            is_recurring):
        super().__init__(amount, date, category, description, "expense")
        self.payment_method = payment_method
        self.is_recurring = is_recurring
