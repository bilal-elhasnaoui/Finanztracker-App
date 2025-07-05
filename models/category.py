class Category:
    """
    Represents a category with an ID, name, and description.
    """

    def __init__(self, category_id, name, description):
        """
        Initialize the category with an ID, name, and description.

        :param category_id: Unique identifier for the category.
        :param name: Name of the category.
        :param description: Description of the category.

        :type category_id: int
        :type name: str
        :type description: str

        """
        self.category_id = category_id
        self.name = name
        self.description = description

    def __repr__(self):
        """
        Return a string representation of the category.

        This representation is useful for debugging and logging.

        :return: String representation of the category.
        :rtype: str
        """
        return f"Category(id={
            self.category_id}, name='{
            self.name}', description='{
            self.description}')"

    def __str__(self):
        """
        Return a user-friendly string representation of the category.

        This string is suitable for display in user interfaces or logs.
        :return: User-friendly string representation of the category.
        :rtype: str

        """
        return f"Category ID: {
            self.category_id}, Name: {
            self.name}, Description: {
            self.description}"

    def to_dict(self):
        """
        Convert the category to a dictionary representation.

        This method is useful for serialization or when passing data to APIs.

        :return: Dictionary representation of the category.
        :rtype: dict
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

        This method is useful for deserializing data from APIs or databases.

        :param data: Dictionary containing category data.
        :type data: dict
        :return: Category instance created from the dictionary.
        :rtype: Category

        """
        return cls(
            category_id=data.get("category_id"),
            name=data.get("name"),
            description=data.get("description")
        )
