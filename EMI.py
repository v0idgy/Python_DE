def calculate_emi(principal, annual_interest_rate, loan_period):    
    # Convert annual interest rate to monthly and decimal
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # Convert loan period from years to months
    loan_period_months = loan_period * 12
    # Calculate EMI
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_period_months) / ((1 + monthly_interest_rate) ** loan_period_months - 1)
    return emi
principal = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
loan_period = int(input("Enter the loan period in years: "))

emi = calculate_emi(principal, annual_interest_rate, loan_period)

print(f"The EMI for the loan is: {emi}")
