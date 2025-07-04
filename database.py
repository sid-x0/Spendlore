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
    
    # Get all months with expenses
    c.execute('''
        SELECT DISTINCT strftime('%Y-%m', date) as month
        FROM expenses
        ORDER BY month DESC
    ''')
    months = c.fetchall()
    
    summary = {}
    
    for month_tuple in months:
        month = month_tuple[0]
        
        # Get daily expenses for this month
        c.execute('''
            SELECT date, SUM(amount)
            FROM expenses
            WHERE strftime('%Y-%m', date) = ?
            GROUP BY date
            ORDER BY date
        ''', (month,))
        
        daily_data = c.fetchall()
        month_total = sum(day[1] for day in daily_data)
        
        summary[month] = {
            'daily_expenses': daily_data,
            'total': month_total
        }
    
    conn.close()
    return summary

def get_monthly_chart_data():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    
    # Get monthly totals for chart
    c.execute('''
        SELECT strftime('%Y-%m', date) as month, SUM(amount) as total
        FROM expenses
        GROUP BY strftime('%Y-%m', date)
        ORDER BY month
    ''')
    
    data = c.fetchall()
    conn.close()
    
    # Format for Chart.js
    months = []
    amounts = []
    
    for month, amount in data:
        # Convert 'YYYY-MM' to 'Mon YYYY' format
        from datetime import datetime
        month_obj = datetime.strptime(month, '%Y-%m')
        formatted_month = month_obj.strftime('%b %Y')
        months.append(formatted_month)
        amounts.append(amount)
    
    return {'months': months, 'amounts': amounts}

