def generate_monthly_report(incomes, expenses):
    """
    Calculates total income, expenses, and net balance, then returns a summary.
    Includes input validation.
    """
    # --- New: Input Validation ---
    if not isinstance(incomes, list) or not isinstance(expenses, list):
        return "Error: Input data must be in a list."
    
    if not all(isinstance(i, (int, float)) for i in incomes):
        return "Error: All income values must be numbers."
        
    if not all(isinstance(e, (int, float)) for e in expenses):
        return "Error: All expense values must be numbers."
    # --- End of New Code ---

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