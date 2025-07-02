class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = []

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

    def filter_by_type(self, t_type):
        return [t for t in self.transactions if t.type == t_type]

    def summary_by_category(self):
        summary = {}
        for t in self.transactions:
            if t.category in summary:
                summary[t.category] += t.amount if t.type == "income" else -t.amount
            else:
                summary[t.category] = t.amount if t.type == "income" else -t.amount
        return summary

