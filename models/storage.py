import json


class Storage:
    """
    Eine einfache Storage-Klasse zum Laden und Speichern von JSON-Dateien.
    """

    def __init__(self, filename):
        """
        Initialisiert die Storage-Klasse mit dem Dateinamen.

        :param filename: Der Name der JSON-Datei, in der die Daten gespeichert werden sollen.
        :type filename: str

       """
        self.filename = filename

    def save(self, data):
        """
        Speichert Daten als JSON-Datei.

        :param data: Die Daten, die gespeichert werden sollen. Sollte ein serialisierbares Python-Objekt sein.
        :type data: dict or list

        """
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self):
        """
        Lädt Daten aus einer JSON-Datei.
        Gibt eine leere Liste zurück, falls Datei nicht existiert.

        :return: Die geladenen Daten als Python-Objekt (dict oder list).
        :rtype: dict or list

        """
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
