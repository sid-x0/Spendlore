from flask import Flask, render_template, request, redirect, url_for
from database import init_db, insert_expense, get_expenses_for_today, delete_expense
from datetime import datetime
from database import delete_expense



app = Flask(__name__)

@app.route('/delete/<int:expense_id>')
def delete(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        category = request.form['category']
        amount = int(request.form['amount'])
        date = datetime.today().strftime('%Y-%m-%d')
        insert_expense(amount, category, date)
        return redirect(url_for('home'))  

    today = datetime.today().strftime('%Y-%m-%d')
    today_expenses = get_expenses_for_today(today)
    total = sum(int(e[2]) for e in today_expenses)

    return render_template('index.html', submitted=True, expenses=today_expenses, total=total)





if __name__ == '__main__':
    init_db()  
    app.run(debug=True)

