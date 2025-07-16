# 💸 Digitaler Finanztracker

Ein modularer Finanztracker für private Haushalte, Freelancer oder KMU.

## 🚀 Features

✅ **User-Registrierung & Login**
- Passwort-Hashing (SHA-256)
- Sichere Speicherung (keine Klartext-Passwörter)

✅ **Mehrkontenverwaltung**
- Beliebig viele Konten pro User
- Monatliches Budget pro Konto

✅ **Kategorienverwaltung**
- Kategorien anlegen
- Budget-Limits pro Kategorie
- Kategorien löschen

✅ **Transaktionsverwaltung**
- Einnahmen und Ausgaben erfassen
- Kategorien zuweisen
- Transaktionen löschen

✅ **Budget-Check**
- Warnung bei Überschreitung des Budgets

✅ **Visualisierung**
- Balkendiagramm der Kategorien
- Kreisdiagramm der Ausgabenanteile

✅ **Export**
- Download aller Transaktionen als CSV
- Enthält Budget-Infos pro Konto

---

## 🎯 Zielgruppe

- **Privatpersonen**, die ihre Finanzen im Blick behalten wollen
- **Freelancer**, die Budgets planen
- **Kleine und mittlere Unternehmen (KMU)**
    - Überblick über betriebliche Kosten
    - Budgetüberwachung pro Abteilung

---

## 🛠️ Technologien

- **Frontend:** Streamlit
- **Backend:** Python OOP
- **Visualisierung:** Plotly
- **Speicher:** JSON-Dateien (leicht auf DB erweiterbar)

---

## 🗄️ Datenstruktur

- Alle Daten werden im JSON-Format gespeichert:
    - Users (Name, E-Mail, Passwort-Hash)
    - Accounts (Name, Budget)
    - Categories (Name, Limit)
    - Transactions (Betrag, Datum, Kategorie, Beschreibung)

---

## 🔒 Sicherheit

- Passwörter werden niemals im Klartext gespeichert.
- Verwendung von SHA-256 Hashes für Passwörter.

---

## 💻 Installation

### Voraussetzungen

- Python ≥ 3.10
- pip
- Virtuelle Umgebung empfohlen

### Installation

```bash
# Repository klonen
git clone https://github.com/deinusername/finanztracker.git

# Ins Projektverzeichnis wechseln
cd finanztracker

# Virtuelle Umgebung anlegen
python -m venv .venv

# Aktivieren (Windows)
.venv\Scripts\activate

# Aktivieren (Mac/Linux)
source .venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Streamlit starten
streamlit run main_app.py
```
