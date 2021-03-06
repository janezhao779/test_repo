# Import pathlib
from pathlib import Path
import csv

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():

    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    new_output_path = Path("data/loan_rate.csv")
    header = ["Lender", "Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    with open(output_path,'w',newline='') as csvfile:
           csvwriter = csv.writer(csvfile)
           csvwriter.writerow(header)
           csvwriter.writerows(qualifying_loans)
    return new_output_path

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
    new_out_path = Path('./data/loan_rate.csv')
    header =["Lender", "Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    with open(new_out_path,'r',newline= '') as csvfile:
           csvreader = csv.reader(csvfile)
           csvreader.readrow(header)
           csvreader.readrow(qualifying_loans)
    return new_out_path
    
