# Import various fiancial plans modules

# Prompts the user to choose a financial plan
print("-------Welcome to Midas-------")
print("Below are 3 financial plans that you could take to help control your finances");
print("Option 1 : This option is for people who wants to take a small step towards taking control of your financial future");
print("Option 2 : This option is for people who has some knowledge of personal finance");
print("Option 3 : This option is the most challenging system in place that will help you grow yourself to manage your personal finances")
option = int(input("Option (1-3):"));
if(option == 1):
    print("You had chosen option 1");
    # Calls the option 1 module
    # Option 1 consist of
    # Expenses - 80%
    # Savings - 10%
    # Spending - 10%
elif(option == 2):
    print("You had chosen option 2");
    # Calls the option 2 module
    # Option 1 consist of
    # Expenses - 60%
    # Savings - 20%
    # Spending - 10%
    # Charity - 10%
elif(option == 3):
    print("You had chosen option 3");
    # Calls the option 3 module
    # Option 1 consist of
    # Expenses - 55%
    # Savings - 20%
    # Spending - 10%
    # Charity - 10%
    # Learning - 5%
