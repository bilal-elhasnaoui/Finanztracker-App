class Category:
    """
    Represents a budget category with a name and a budget limit.
    This class is used to define budget categories and check if expenses exceed the budget limit.

    Attributes:
        name (str): The name of the budget category.
        budget_limit (float): The maximum budget limit for this category.
    """
    def __init__(self, name, budget_limit):
        """
        Initialize the Category with a name and a budget limit.
        This constructor sets the name and budget limit for the category.

        :param name: The name of the budget category.
        :param budget_limit: The maximum budget limit for this category.

        :type name: str
        :type budget_limit: float


        """
        self.name = name
        self.budget_limit = budget_limit

    def is_over_budget(self, amount):
        """
        Check if the given amount exceeds the budget limit for this category.

        This method compares the provided amount with the budget limit and returns True if the amount exceeds the limit, otherwise False.
        :param amount: The amount to check against the budget limit.

        :type amount: float

        :return: True if the amount exceeds the budget limit, otherwise False.
        :rtype: bool



        """
        return amount > self.budget_limit


class BudgetPlan:
    """
    Represents a budget plan that tracks expenses against defined categories within a specified date range.
    """
    def __init__(self, categories, start_date, end_date):
        """
        Initialize the BudgetPlan with categories and a date range.
        :param categories: List of Category objects defining the budget categories.
        :param start_date: Start date of the budget plan (datetime object).
        :param end_date: End date of the budget plan (datetime object).

        :type categories: list of Category objects
        :type start_date: datetime
        :type end_date: datetime


        """
        self.categories = categories
        self.start_date = start_date
        self.end_date = end_date

    def check_budget(self, transactions):
        """
        Check if the expenses in the given transactions exceed the budget for each category.
        This method iterates through the transactions and calculates the total expenses for each category.
        It returns a dictionary where the keys are category names and the values are booleans indicating whether the budget is exceeded.


        :param transactions: List of Transaction objects to check against the budget.
        :type transactions: list of Transaction objects
        :return: Dictionary with category names as keys and booleans as values indicating if the budget is exceeded.
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
