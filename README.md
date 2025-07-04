# 💰 Spendlore 

Spendlore is a minimal Flask web app to log and visualize your daily expenses. It supports adding entries, viewing analytics, and generating monthly summaries, all with a clean UI and lightweight backend.

![Spendlore](https://img.shields.io/badge/Flask-Web%20App-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)


## 🌟 Features

### 📊 **Daily Expense Tracking**
- **Quick Entry**: Log expenses with purpose and amount
- **Real-time Display**: See today's expenses instantly
- **Delete Functionality**: Remove incorrect entries with one click
- **Daily Totals**: Automatic calculation of daily spending

### 📈 **Monthly Analytics**
- **Visual Charts**: Interactive line charts showing monthly expense trends
- **Detailed Breakdown**: Expandable monthly summaries with daily breakdowns
- **Historical Data**: View all months with recorded expenses
- **Smart Formatting**: Clean date formatting and currency display

### 🎨 **Modern Design**
- **Black & White Theme**: Professional, clean aesthetic
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile
- **Smooth Animations**: Elegant hover effects and transitions
- **Intuitive UI**: User-friendly interface with clear visual hierarchy





## 📁 Project Structure

```
spendlore/
├── app.py                 # Main Flask application
├── database.py           # Database operations and queries
├── expenses.db           # SQLite database (auto-created)
├── static/
│   └── style.css         # Modern CSS styling
├── templates/
│   ├── index.html        # Main dashboard
│   ├── monthly.html      # Monthly summary page
│   ├── base.html         # Base template
│   └── analytics.html    # Analytics page
├── __pycache__/          # Python cache files
└── README.md            # Project documentation
```

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js
- **Styling**: Custom CSS with CSS Variables
- **Icons**: Unicode symbols and custom CSS icons


## 🔮 Future Enhancements

- [ ] **Category Analytics**: Spending breakdown by category
- [ ] **Budget Limits**: Set monthly spending goals
- [ ] **Export Data**: CSV/PDF export functionality
- [ ] **Dark/Light Toggle**: Theme switching option
- [ ] **Search/Filter**: Find specific expenses
- [ ] **Recurring Expenses**: Automatic entry for regular expenses





*Last updated: July 2025*
