# report_generator.py

def generate_monthly_report(incomes, expenses):
    """
    Calculates total income, expenses, and net balance, then returns a summary.
    """
    # Calculate totals
    total_income = sum(incomes)
    total_expenses = sum(expenses)
    net_balance = total_income - total_expenses

    # Create the summary string
    summary = (
        f"--- Monthly Financial Summary ---\n"
        f"Total Income:   ${total_income:,.2f}\n"
        f"Total Expenses: ${total_expenses:,.2f}\n"
        f"---------------------------------\n"
        f"Net Balance:    ${net_balance:,.2f}\n"
        f"---------------------------------"
    )
    
    return summary

# --- Main part of the script ---
if __name__ == "__main__":
    # Sample data for the month
    sample_incomes = [2500, 300.50, 50.25]  # Salary, freelance, sale
    sample_expenses = [800, 150.75, 45.50, 200, 75] # Rent, groceries, gas, utilities, entertainment

    # Generate and print the report
    report = generate_monthly_report(sample_incomes, sample_expenses)
    print(report)