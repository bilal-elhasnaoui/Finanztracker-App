class Category:
    def __init__(self, name, budget_limit):
        self.name = name
        self.budget_limit = budget_limit

    def is_over_budget(self, amount):
        return amount > self.budget_limit

class BudgetPlan:
    def __init__(self, categories, start_date, end_date):
        self.categories = categories
        self.start_date = start_date
        self.end_date = end_date

    def check_budget(self, transactions):
        result = {}
        for category in self.categories:
            total = sum(
                t.amount for t in transactions
                if t.category == category.name and t.type == "expense"
            )
            result[category.name] = category.is_over_budget(total)
        return result
