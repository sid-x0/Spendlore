import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            category TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_expense(amount, category, date):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)',
              (amount, category, date))
    conn.commit()
    conn.close()

def get_expenses_for_today(date):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('SELECT id, category, amount FROM expenses WHERE date = ?', (date,))
    data = c.fetchall()
    conn.close()
    return data

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()

def get_monthly_summary():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        SELECT date, SUM(amount)
        FROM expenses
        WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        GROUP BY date
        ORDER BY date
    ''')
    data = c.fetchall()
    conn.close()
    return data

