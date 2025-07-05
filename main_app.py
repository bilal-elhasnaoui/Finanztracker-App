import streamlit as st
import plotly.graph_objects as go
import hashlib
import csv
import io
from models import (
    User,
    Account,
    Income,
    Expense,
    Category,
    BudgetPlan,
    Storage
)

# -------------------------------
# Storage vorbereiten
# -------------------------------

user_storage = Storage("users.json")

# -------------------------------
# Users laden
# -------------------------------

if "users" not in st.session_state:
    st.session_state.users = []
    users_data = user_storage.load()
    for u in users_data:
        accounts = []
        for acc_data in u["accounts"]:
            categories = [
                Category(c["name"], c["limit"])
                for c in acc_data.get("categories", [])
            ]
            acc = Account(
                acc_data["name"],
                categories,
                acc_data.get("monthly_budget", None)
            )
            for tx in acc_data["transactions"]:
                if tx["type"] == "income":
                    t = Income(
                        tx["amount"],
                        tx["date"],
                        tx["category"],
                        tx["description"],
                        tx["source"],
                        tx["tax_info"]
                    )
                else:
                    t = Expense(
                        tx["amount"],
                        tx["date"],
                        tx["category"],
                        tx["description"],
                        tx["payment_method"],
                        tx["is_recurring"]
                    )
                acc.add_transaction(t)
            accounts.append(acc)
        user = User(
            u["name"],
            u["email"],
            u.get("password_hash", ""),
            accounts
        )
        st.session_state.users.append(user)

# -------------------------------
# User-Login / Registrierung
# -------------------------------

st.title("💸 Finanztracker")

with st.form("user_form"):
    st.subheader("🔐 Einloggen oder Registrieren")

    name = st.text_input("Name")
    email = st.text_input("E-Mail")
    password = st.text_input("Passwort", type="password")
    submit_user = st.form_submit_button("Einloggen / Registrieren")

if submit_user:
    existing_user = None
    for u in st.session_state.users:
        if u.email == email:
            existing_user = u
            break

    if existing_user:
        if existing_user.check_password(password):
            st.session_state.active_user = existing_user
            st.success(f"Willkommen zurück, {existing_user.name}!")
        else:
            st.error("❌ Falsches Passwort!")
    else:
        pw_hash = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(name, email, pw_hash)
        st.session_state.users.append(new_user)
        st.session_state.active_user = new_user
        st.success(f"Benutzer {name} registriert!")

# -------------------------------
# Haupt-App
# -------------------------------

if "active_user" in st.session_state:
    user = st.session_state.active_user

    st.subheader(f"Angemeldet als: {user.name} ({user.email})")

    # -----------------------------------
    # Konto anlegen
    # -----------------------------------

    st.header("1️⃣ Konto anlegen")

    with st.form("account_form"):
        acc_name = st.text_input("Name des Kontos")
        submit_acc = st.form_submit_button("Konto anlegen")

    if submit_acc:
        acc = Account(acc_name)
        user.add_account(acc)
        st.success(f"Konto {acc_name} angelegt!")


    # -----------------------------------
    # Konten verwalten
    # -----------------------------------

    if user.accounts:
        st.subheader("⚙️ Konten verwalten")

        # Konten anzeigen + löschen
        for idx, acc in enumerate(user.accounts):
            col1, col2 = st.columns([5, 1])

            with col1:
                st.write(f"**{acc.name}**")

            with col2:
                if st.button(
                        "🗑️ Konto löschen",
                        key=f"delete_account_{idx}"
                ):
                    user.accounts.pop(idx)
                    st.success(f"Konto **{acc.name}** wurde gelöscht!")


        # Konto auswählen (falls noch eines übrig ist)
        if user.accounts:
            selected_account_name = st.selectbox(
                "Konto auswählen",
                [acc.name for acc in user.accounts]
            )
            selected_account = next(
                (acc for acc in user.accounts if acc.name == selected_account_name),
                None
            )

            if selected_account is not None:

                # -----------------------------------
                # Monatliches Budget festlegen
                # -----------------------------------

                if selected_account.monthly_budget is None:
                    st.header("🔢 Monatliches Budget festlegen")

                    with st.form("budget_form"):
                        budget_value = st.number_input(
                            "Wie viel Geld steht dir monatlich zur Verfügung? (€)",
                            step=50.0,
                            min_value=0.0
                        )
                        submit_budget = st.form_submit_button("Budget speichern")

                    if submit_budget:
                        selected_account.monthly_budget = budget_value
                        st.success(
                            f"Monatliches Budget von {budget_value:.2f} € gespeichert für Konto {selected_account_name}!"
                        )

                else:
                    st.info(
                        f"Monatliches Budget für Konto **{selected_account_name}**: "
                        f"{selected_account.monthly_budget:.2f} €"
                    )

                st.markdown("---")

                # -----------------------------------
                # Kategorien anlegen
                # -----------------------------------

                st.header("2️⃣ Kategorien für Konto anlegen")

                with st.form("category_form"):
                    cat_name = st.text_input("Kategorie-Name")
                    cat_limit = st.number_input("Budget-Limit (€)", step=10.0, min_value=0.0)
                    submit_cat = st.form_submit_button("Kategorie speichern")

                if submit_cat and selected_account:
                    if any(cat.name == cat_name for cat in selected_account.categories):
                        st.warning(f"Kategorie '{cat_name}' existiert bereits!")
                    else:
                        new_category = Category(cat_name, cat_limit)
                        selected_account.add_category(new_category)
                        st.success(
                            f"Kategorie {cat_name} gespeichert für Konto {selected_account_name}!"
                        )


                # Kategorien anzeigen + löschen
                if selected_account.categories:
                    st.subheader(f"Kategorien in Konto {selected_account_name}:")

                    for idx, cat in enumerate(selected_account.categories):
                        col1, col2 = st.columns([5, 1])

                        with col1:
                            st.write(f"**{cat.name}** → Limit: {cat.budget_limit:.2f} €")

                        with col2:
                            if st.button(
                                    "🗑️ Löschen",
                                    key=f"delete_category_{selected_account_name}_{idx}"
                            ):
                                selected_account.categories.pop(idx)
                                st.success(f"Kategorie {cat.name} gelöscht!")

                else:
                    st.info("Noch keine Kategorien in diesem Konto.")

                st.markdown("---")

                # -----------------------------------
                # Transaktionen erfassen
                # -----------------------------------

                st.header("3️⃣ Neue Transaktion hinzufügen")

                if selected_account.categories:
                    t_type = st.selectbox("Typ der Transaktion", ["income", "expense"])

                    with st.form("transaction_form"):
                        amount = st.number_input("Betrag (€)", step=0.01, min_value=0.01)
                        date = st.date_input("Datum")
                        category = st.selectbox(
                            "Kategorie auswählen",
                            [cat.name for cat in selected_account.categories]
                        )
                        description = st.text_input("Beschreibung")

                        if t_type == "income":
                            source = st.text_input("Quelle")
                            tax_info = st.text_input("Steuerinfo")
                        else:
                            payment_method = st.text_input("Zahlungsmethode")
                            is_recurring = st.checkbox("Wiederkehrend?")

                        submit_tx = st.form_submit_button("Transaktion speichern")

                    if submit_tx:
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
                        selected_account.add_transaction(tx)
                        st.success(
                            f"Transaktion gespeichert für Konto {selected_account_name}!"
                        )

                else:
                    st.warning("Bitte zuerst Kategorien für das Konto anlegen!")

                st.markdown("---")

                # -----------------------------------
                # Saldo-Berechnung & Anzeige
                # -----------------------------------

                st.header("4️⃣ Kontostand & Transaktionen")

                balance = selected_account.get_balance()

                if balance is not None:
                    if balance < 0:
                        st.error(
                            f"❌ Dein Budget ist überschritten! Saldo: {balance:.2f} €"
                        )
                    else:
                        st.success(
                            f"✅ Dein verbleibendes Budget: {balance:.2f} €"
                        )
                else:
                    st.info("Noch kein monatliches Budget festgelegt.")

                if selected_account.transactions:
                    st.subheader("Transaktionen:")

                    for idx, t in enumerate(selected_account.transactions):
                        col1, col2 = st.columns([5, 1])

                        with col1:
                            st.write(str(t))

                        with col2:
                            if st.button(
                                    "🗑️ Löschen",
                                    key=f"delete_{selected_account.name}_{idx}"
                            ):
                                selected_account.transactions.pop(idx)
                                st.success("Transaktion gelöscht!")


                    # Export-Button
                    st.markdown("---")
                    st.subheader("⬇️ Transaktionen exportieren")

                    if st.button("CSV-Export starten"):


                        output = io.StringIO()
                        writer = csv.writer(output, delimiter=';')

                        # Budget Info
                        writer.writerow(["Monatliches Budget", selected_account.monthly_budget or 0.0])
                        writer.writerow([])

                        # Kopfzeile
                        writer.writerow([
                            "Datum", "Typ", "Kategorie", "Betrag", "Beschreibung", "Extra Infos"
                        ])

                        for t in selected_account.transactions:
                            if t.type == "income":
                                extra = f"Quelle: {t.source}, Steuerinfo: {t.tax_info}"
                            else:
                                extra = f"Zahlweise: {t.payment_method}, Wiederkehrend: {t.is_recurring}"

                            writer.writerow([
                                t.date,
                                t.type,
                                t.category,
                                f"{t.amount:.2f}",
                                t.description,
                                extra
                            ])

                        st.download_button(
                            label="📥 CSV herunterladen",
                            data=output.getvalue(),
                            file_name=f"transaktionen_{selected_account.name}.csv",
                            mime="text/csv",
                        )
                else:
                    st.info("Keine Transaktionen vorhanden.")

                st.markdown("---")

                # -----------------------------------
                # Budgetprüfung
                # -----------------------------------

                st.header("5️⃣ Budgetprüfung")

                if selected_account.transactions and selected_account.categories:
                    plan = BudgetPlan(
                        selected_account.categories,
                        "2025-06-01",
                        "2025-06-30"
                    )
                    budget_check = plan.check_budget(selected_account.transactions)

                    for cat, over in budget_check.items():
                        if over:
                            st.error(f"⚠️ Budget überschritten in Kategorie: {cat}")
                        else:
                            st.success(f"✅ Budget ok in Kategorie: {cat}")
                else:
                    st.info("Keine Transaktionen oder Kategorien vorhanden für Budgetprüfung.")

                st.markdown("---")

                # -----------------------------------
                # Diagramme
                # -----------------------------------

                st.header("6️⃣ Diagramme")

                summary = selected_account.summary_by_category()

                if summary:
                    categories = list(summary.keys())
                    values = list(summary.values())

                    # Balkendiagramm
                    fig_bar = go.Figure(
                        data=[
                            go.Bar(
                                x=categories,
                                y=values,
                                text=[f"{v:.2f} €" for v in values],
                                textposition='auto'
                            )
                        ]
                    )
                    fig_bar.update_layout(
                        title=f"Beträge nach Kategorie ({selected_account_name})"
                    )
                    st.plotly_chart(fig_bar, use_container_width=True)

                    # Pie Chart nur für Ausgaben
                    expense_categories = []
                    expense_values = []

                    for cat, val in summary.items():
                        if val < 0:
                            expense_categories.append(cat)
                            expense_values.append(abs(val))

                    if expense_categories:
                        fig_pie = go.Figure(
                            data=[
                                go.Pie(
                                    labels=expense_categories,
                                    values=expense_values
                                )
                            ]
                        )
                        fig_pie.update_layout(
                            title=f"Anteile der Ausgaben pro Kategorie ({selected_account_name})"
                        )
                        st.plotly_chart(fig_pie, use_container_width=True)
                    else:
                        st.info("Keine Ausgaben vorhanden für das Kreisdiagramm.")
                else:
                    st.info("Keine Daten für Diagramme vorhanden.")

            else:
                st.info("Kein Konto ausgewählt.")
        else:
            selected_account = None
            st.info("Bitte erst ein Konto anlegen.")
    else:
        selected_account = None
        st.info("Bitte erst ein Konto anlegen.")
