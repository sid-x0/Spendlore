from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import init_db, insert_expense, get_expenses_for_today, delete_expense, get_monthly_summary, get_monthly_chart_data
from datetime import datetime


app = Flask(__name__)

# Custom template filters
@app.template_filter('month_name')
def month_name(value):
    """Convert YYYY-MM to Month YYYY format"""
    try:
        month_obj = datetime.strptime(value, '%Y-%m')
        return month_obj.strftime('%B %Y')
    except:
        return value

@app.template_filter('format_date')
def format_date(value):
    """Convert YYYY-MM-DD to Day, Month DD format"""
    try:
        date_obj = datetime.strptime(value, '%Y-%m-%d')
        return date_obj.strftime('%A, %B %d')
    except:
        return value

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
    
    # Get chart data for monthly expenses
    chart_data = get_monthly_chart_data()

    return render_template('index.html', submitted=True, expenses=today_expenses, total=total, chart_data=chart_data)

@app.route('/monthly')
def monthly():
    summary = get_monthly_summary()
    return render_template('monthly.html', summary=summary)


if __name__ == '__main__':
    init_db()  
    app.run(debug=True)

