class Account:
    def __init__(self, name, categories=None, monthly_budget=None):
        self.name = name
        self.categories = categories if categories is not None else []
        self.transactions = []
        self.monthly_budget = monthly_budget

    def add_category(self, category):
        self.categories.append(category)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        total = 0
        for t in self.transactions:
            if t.type == "income":
                total += t.amount
            elif t.type == "expense":
                total -= t.amount
        return total

    def list_transactions(self):
        return [str(t) for t in self.transactions]

    def summary_by_category(self):
        summary = {}
        for t in self.transactions:
            if t.category in summary:
                summary[t.category] += t.amount if t.type == "income" else -t.amount
            else:
                summary[t.category] = t.amount if t.type == "income" else -t.amount
        return summary

