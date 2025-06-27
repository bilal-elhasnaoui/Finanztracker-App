class Category:
    """
    Represents a category with an ID, name, and description.
    """
    def __init__(self, category_id, name, description):
        """
        Initialize the category with an ID, name, and description.
        """
        self.category_id = category_id
        self.name = name
        self.description = description

    def __repr__(self):
        """
        Return a string representation of the category.
        """
        return f"Category(id={
            self.category_id}, name='{
            self.name}', description='{
            self.description}')"

    def __str__(self):
        """
        Return a user-friendly string representation of the category.
        """
        return f"Category ID: {
            self.category_id}, Name: {
            self.name}, Description: {
            self.description}"

    def to_dict(self):
        """
        Convert the category to a dictionary representation.
        """
        return {
            "category_id": self.category_id,
            "name": self.name,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Category instance from a dictionary representation.
        """
        return cls(
            category_id=data.get("category_id"),
            name=data.get("name"),
            description=data.get("description")
        )
