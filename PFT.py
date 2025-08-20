import csv
from datetime import datetime

class Transaction:
    def __init__(self, date, ttype, category, amount, note):
        self.date = date
        self.type = ttype
        self.category = category
        self.amount = amount
        self.note = note

TX = []
goal = {"name": None, "target": 0}

def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()

def add_transaction():
    date_str = input("Enter date (YYYY-MM-DD): ")
    ttype = input("Type (I=Income, E=Expense): ").upper()
    category = input("Category: ")
    amount = float(input("Amount: "))
    note = input("Note: ")
    TX.append(Transaction(parse_date(date_str), ttype, category, amount, note))
    print("Transaction added.")

def list_transactions():
    if not TX:
        print("No transactions yet.")
        return
    TX_sorted = sorted(TX, key=lambda t: t.date)
    income, expense = 0, 0
    print("Date        Type     Category       Amount     Note")
    print("-" * 60)
    for t in TX_sorted:
        print(f"{t.date}   {t.type}       {t.category:12} ${t.amount:<10.2f} {t.note}")
        if t.type == 'I':
            income += t.amount
        else:
            expense += t.amount
    print("-" * 60)
    print(f"Total Income: ${income:.2f} | Total Expense: ${expense:.2f} | Net: ${income - expense:.2f}")

def filter_expenses_over(threshold):
    print(f"Expenses over ${threshold}:")
    for t in TX:
        if t.type == 'E' and t.amount > threshold:
            print(f"{t.date} {t.category} ${t.amount:.2f} {t.note}")

def search_by_text(query):
    results = [t for t in TX if query.lower() in t.category.lower() or query.lower() in t.note.lower()]
    if not results:
        print("No matches.")
        return
    for t in results:
        print(f"{t.date} {t.type} {t.category} ${t.amount:.2f} {t.note}")

def save_to_file(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        if goal["name"]:
            writer.writerow(["#GOAL", goal["name"], goal["target"]])
        for t in TX:
            writer.writerow([t.date, t.type, t.category, t.amount, t.note])
    print("Data saved.")

def load_from_file(path):
    global TX, goal
    TX = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if row[0] == "#GOAL":
                goal["name"] = row[1]
                goal["target"] = float(row[2])
                continue
            TX.append(Transaction(parse_date(row[0]), row[1], row[2], float(row[3]), row[4]))
    print("Data loaded.")

def set_goal():
    goal["name"] = input("Goal name: ")
    goal["target"] = float(input("Target amount: "))
    print("Goal set.")

def view_goal():
    if not goal["name"]:
        print("No goal set.")
        return
    income = sum(t.amount for t in TX if t.type == 'I')
    expense = sum(t.amount for t in TX if t.type == 'E')
    net = income - expense
    pct = (net / goal["target"] * 100) if goal["target"] > 0 else 0
    print(f"Goal: {goal['name']} | Target: ${goal['target']:.2f} | Net: ${net:.2f} ({pct:.1f}%)")
    print("[" + "#" * int(pct/4) + "-" * (25 - int(pct/4)) + "]")

def monthly_spending_chart():
    year = int(input("Enter year (YYYY): "))
    months = [0] * 12
    for t in TX:
        if t.type == 'E' and t.date.year == year:
            months[t.date.month - 1] += t.amount
    max_val = max(months)
    if max_val == 0:
        print("No expenses found for this year.")
        return
    print(f"\nMonthly Spending {year}")
    for i, val in enumerate(months, 1):
        bar = "#" * int((val / max_val) * 40)
        print(f"{i:2} | {bar} ${val:.2f}")

def menu():
    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1) Add transaction")
        print("2) List transactions")
        print("3) Filter expenses over amount")
        print("4) Search by text")
        print("5) Set savings goal")
        print("6) View savings goal")
        print("7) Monthly spending chart")
        print("8) Save to file")
        print("9) Load from file")
        print("0) Exit")
        choice = input("Choose: ")
        if choice == '1': add_transaction()
        elif choice == '2': list_transactions()
        elif choice == '3':
            thr = float(input("Threshold: "))
            filter_expenses_over(thr)
        elif choice == '4':
            q = input("Query: ")
            search_by_text(q)
        elif choice == '5': set_goal()
        elif choice == '6': view_goal()
        elif choice == '7': monthly_spending_chart()
        elif choice == '8':
            p = input("File path (default finance.csv): ") or "finance.csv"
            save_to_file(p)
        elif choice == '9':
            p = input("File path (default finance.csv): ") or "finance.csv"
            load_from_file(p)
        elif choice == '0': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    menu()
