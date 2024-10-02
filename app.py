from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)

# Updated HTML template with responsive styling
html_form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SME Data Form</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: auto; /* Allow scrolling if needed */
        }
        .form-container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            max-width: 90%;
            width: 500px; /* Fixed width for better visibility */
            margin: 20px; /* Add margin for responsiveness */
        }
        h2 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            color: #555;
            font-size: 16px;
        }
        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
            box-sizing: border-box;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus, input[type="number"]:focus {
            border-color: #007bff;
            outline: none;
        }
        input[type="submit"] {
            background-color: #007bff;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 6px;
            font-size: 18px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Enter SME Details</h2>
        <form action="/submit" method="POST">
            <div class="form-group">
                <label for="sme_scale">SME Scale:</label>
                <input type="text" id="sme_scale" name="sme_scale" placeholder="Enter SME scale" required>
            </div>
            <div class="form-group">
                <label for="annual_revenue">Annual Revenue:</label>
                <input type="number" id="annual_revenue" name="annual_revenue" placeholder="Enter annual revenue" required>
            </div>
            <div class="form-group">
                <label for="industry">Industry:</label>
                <input type="text" id="industry" name="industry" placeholder="Enter industry type" required>
            </div>
            <div class="form-group">
                <label for="asset_value">Asset Value:</label>
                <input type="number" id="asset_value" name="asset_value" placeholder="Enter asset value" required>
            </div>
            <div class="form-group">
                <label for="expenses">Expenses:</label>
                <input type="number" id="expenses" name="expenses" placeholder="Enter expenses" required>
            </div>
            <div class="form-group">
                <label for="profitability">Profitability:</label>
                <input type="number" id="profitability" name="profitability" placeholder="Enter profitability" required>
            </div>
            <div class="form-group">
                <label for="cash_flow">Cash Flow:</label>
                <input type="number" id="cash_flow" name="cash_flow" placeholder="Enter cash flow" required>
            </div>
            <div class="form-group">
                <label for="current_loan">Current Loan:</label>
                <input type="number" id="current_loan" name="current_loan" placeholder="Enter current loan" required>
            </div>
            <div class="form-group">
                <label for="credit_score">Credit Score:</label>
                <input type="number" id="credit_score" name="credit_score" placeholder="Enter credit score" required>
            </div>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_form)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'SME Scale': request.form['sme_scale'],
        'Annual Revenue': request.form['annual_revenue'],
        'Industry': request.form['industry'],
        'Asset Value': request.form['asset_value'],
        'Expenses': request.form['expenses'],
        'Profitability': request.form['profitability'],
        'Cash Flow': request.form['cash_flow'],
        'Current Loan': request.form['current_loan'],
        'Credit Score': request.form['credit_score']
    }

    # Save data to CSV file
    with open('saved_sme_data.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:  # Write header if the file is empty
            writer.writeheader()
        writer.writerow(data)

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
