import streamlit as st
from models import Account, Income, Expense, Category, BudgetPlan

# Session State initialisieren
if "account" not in st.session_state:
    st.session_state.account = Account("Bilals Konto")

st.title("💸 Finanztracker")

# Eingabemaske
st.subheader("Neue Transaktion hinzufügen")

amount = st.number_input("Betrag (€)", step=0.01)
date = st.date_input("Datum")
category = st.text_input("Kategorie")
description = st.text_input("Beschreibung")
t_type = st.selectbox("Typ", ["income", "expense"])

if t_type == "income":
    source = st.text_input("Quelle")
    tax_info = st.text_input("Steuerinfo")
else:
    payment_method = st.text_input("Zahlungsmethode")
    is_recurring = st.checkbox("Wiederkehrend?")

if st.button("Hinzufügen"):
    if t_type == "income":
        tx = Income(
            amount,
            date.strftime("%Y-%m-%d"),
            category,
            description,
            source,
            tax_info
        )
    else:
        tx = Expense(
            amount,
            date.strftime("%Y-%m-%d"),
            category,
            description,
            payment_method,
            is_recurring
        )

    st.session_state.account.add_transaction(tx)
    st.success("Transaktion hinzugefügt!")

# Saldo anzeigen
st.subheader("Kontostand")
balance = st.session_state.account.get_balance()
st.write(f"**Aktueller Saldo:** {balance:.2f} €")

# Transaktionen anzeigen
st.subheader("Alle Transaktionen")
for t in st.session_state.account.list_transactions():
    st.write(t)

# Kategorie-Übersicht
st.subheader("Übersicht nach Kategorien")
summary = st.session_state.account.summary_by_category()
for cat, total in summary.items():
    st.write(f"{cat}: {total:.2f} €")

# Budgetprüfung (optional)
categories = [
    Category("Essen", 200),
    Category("Miete", 800),
    Category("Freizeit", 150)
]
budget_plan = BudgetPlan(categories, "2025-06-01", "2025-06-30")
budget_check = budget_plan.check_budget(st.session_state.account.transactions)

st.subheader("Budgetprüfung")
for cat, over in budget_check.items():
    if over:
        st.error(f"Budget überschritten in Kategorie {cat}")
    else:
        st.success(f"Budget ok in Kategorie {cat}")
