import json


class Storage:
    """
    Eine einfache Storage-Klasse zum Laden und Speichern von JSON-Dateien.
    """

    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        """
        Speichert Daten als JSON-Datei.
        """
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self):
        """
        Lädt Daten aus einer JSON-Datei.
        Gibt eine leere Liste zurück, falls Datei nicht existiert.
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
