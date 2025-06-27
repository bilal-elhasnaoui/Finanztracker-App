import streamlit as st
from models.transaction import Income, Expense
from models.account import Account

st.set_page_config(page_title="Finanztracker")

st.title("💸 Finanztracker")
# Initialisiere das Konto mit einem Startguthaben
account = Account("Mein Konto", 1000.00)

st.subheader("Neue Transaktion hinzufügen")

amount = st.number_input("Betrag", step=0.01)
date = st.date_input("Datum")
category = st.text_input("Kategorie")
description = st.text_input("Beschreibung")
t_type = st.selectbox("Typ", ["income", "expense"])

if st.button("Hinzufügen"):
    if t_type == "income":
        tx = Income(
            amount,
            date.strftime("%Y-%m-%d"),
            category,
            description,
            source="Unbekannt",
            tax_info="netto")
    else:
        tx = Expense(
            amount,
            date.strftime("%Y-%m-%d"),
            category,
            description,
            payment_method="Karte",
            is_recurring=False)

    account.add_transaction(tx)
    st.success("Transaktion hinzugefügt!")

st.subheader("Aktueller Kontostand")
st.write(f"{account.get_balance():.2f} €")

st.subheader("Transaktionen")
for t in account.transactions:
    st.write(str(t))
