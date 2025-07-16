class Category:
    """
    Repräsentiert eine Kategorie mit ID, Namen und Beschreibung.
    """

    def __init__(self, category_id, name, description):
        """
        Initialisiert die Kategorie mit ID, Name und Beschreibung.

        :param category_id: Eindeutige Kennung der Kategorie.
        :param name: Name der Kategorie.
        :param description: Beschreibung der Kategorie.

        :type category_id: int
        :type name: str
        :type description: str

        """
        self.category_id = category_id
        self.name = name
        self.description = description

    def __repr__(self):
        """
        Gibt eine String-Repräsentation der Kategorie zurück.

        Diese Darstellung ist hilfreich für Debugging und Logging.

        :return: String-Repräsentation der Kategorie.
        :rtype: str
        """
        return f"Category(id={
            self.category_id}, name='{
            self.name}', description='{
            self.description}')"

    def __str__(self):
        """
        Gibt eine benutzerfreundliche String-Repräsentation der Kategorie zurück.

        Diese Darstellung eignet sich für Benutzeroberflächen oder Logs.
        :return: Benutzerfreundliche String-Repräsentation der Kategorie.
        :rtype: str

        """
        return f"Category ID: {
            self.category_id}, Name: {
            self.name}, Description: {
            self.description}"

    def to_dict(self):
        """
        Wandelt die Kategorie in ein Dictionary um.

        Diese Methode ist nützlich für die Serialisierung oder zur Übergabe an APIs.

        :return: Dictionary-Repräsentation der Kategorie.
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
        Erstellt eine ``Category``-Instanz aus einer Dictionary-Repräsentation.

        Diese Methode ist hilfreich, um Daten aus APIs oder Datenbanken zu deserialisieren.

        :param data: Dictionary mit Kategoriedaten.
        :type data: dict
        :return: Aus dem Dictionary erzeugte ``Category``-Instanz.
        :rtype: Category

        """
        return cls(
            category_id=data.get("category_id"),
            name=data.get("name"),
            description=data.get("description")
        )
