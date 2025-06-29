from flask import Flask, render_template, request
from parser import parse_expenses

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        raw_input = request.form['expense_input']
        parsed_expenses = parse_expenses(raw_input)
        return render_template('index.html', submitted=True, expenses=parsed_expenses)

    return render_template('index.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
