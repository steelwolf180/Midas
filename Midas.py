try:
    salary = float(input("Monthly Income :$"))

    # Calculate expected outcome for the month.
    expected_savings = float(salary*0.2)
    expected_spending = float(salary*0.1)
    expected_donation = float(salary*0.1)
    expected_learning = float(salary*0.05)

    # Request input for any standing orders already in effect.
    print("\n=========Standing Order============\n")
    standing_savings = float(input("Monthly Savings :$"))
    standing_spending = float(input("Monthly Spending :$"))
    standing_donation = float(input("Monthly Donation :$"))
    standing_loan = float(input("Monthly Loan :$"))

    # Calculate shortfall (any outcome that remains to be spent)
    shortfall_savings = expected_savings - standing_savings
    shortfall_spending = expected_spending - standing_spending
    shortfall_donation = expected_donation - standing_donation
    expenses =(salary - expected_savings -  expected_spending -  expected_donation - expected_learning - standing_loan)

    # Display outcome so far.
    print("\n====Income Distributed To Account=====\n");
    print("Calculated Savings:$" + "%.2f" % round(expected_savings, 2))
    print("Calculated Spending:$" + "%.2f" % round(expected_spending, 2))
    print("Calculated Donation:$" + "%.2f" % round(expected_donation, 2))
    print("Calculated Learning:$" + "%.2f" % round(expected_learning, 2))
    print("Monthly Loan Repayment:$" + "%.2f" % round(standing_loan, 2))

    # Display remaining shortfall.
    print("\n=============Shortfall==============\n");
    print("Savings:$" + "%.2f" % round(shortfall_savings, 2))
    print("Spending:$" + "%.2f" % round(shortfall_spending, 2))
    print("Donation:$" + "%.2f" % round(shortfall_donation, 2))
    print("Learning:$" + "%.2f" % round(expected_learning, 2))

    # Display remaining money left.
    print("\n======Salary Left For Expenses======\n");
    print("Personal Expenses:$" + "%.2f" % round(expenses, 2))
    print("Monthly Salary:$" + "%.2f" % round(salary, 2) + "\n")

    # Prompting the user to press enter to exit the program.
    question = input("Please press enter to exit the program")

# Catching the common exceptions in the program
except ValueError:
    print("Could not convert data to integer.")
except KeyboardInterrupt:
    print("You cancelled the operation")
except EOFError:
    print("Why you end of file on me")
except Exception as err:
    print("Error: ", err)