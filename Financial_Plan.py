Salary = float(input("Monthly Income :$"));

Current_Savings = float(Salary*0.1);
Current_Spending = float(Salary*0.1);
Current_Donation = float(Salary*0.1);
Current_Learning = float(Salary*0.05);

print("\n=========Standing Order============\n");
Input_Savings = float(input("Monthly Savings :$"));
Input_Spending = float(input("Monthly Spending :$"));
Input_Donation = float(input("Monthly Dondation :$"));

Savings = Input_Savings - Current_Savings;
Spending = Input_Spending - Current_Spending;
Donation = Input_Donation - Current_Donation;
Expanses =(Salary - Input_Savings -  Input_Spending -  Input_Donation - Current_Learning);

print("\n====Income Distributed To Account=====\n");
print("Calculated Savings:$"+str(round(Input_Savings, 2)));
print("Calculated Spending:$"+str(round(Input_Spending, 2)));
print("Calculated Donation:$"+str(round(Input_Donation, 2)));
print("Calculated Learning:$"+str(round(Current_Learning, 2)));
print("\n=============Shortfall==============\n");
print("Savings:$"+str(round(Savings, 2)));
print("Spending:$"+str(round(Spending, 2)));
print("Donation:$"+str(round(Donation, 2)));
print("Learning:$"+str(round(Current_Learning, 2)));
print("\n======Salary Left For Expanses======\n");
print("Personal Expanses:$"+str(round(Expanses, 2)));
print("Monthly Salary:$"+str(round(Salary, 2))+"\n");
