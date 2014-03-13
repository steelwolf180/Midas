try:
	
	#Import python module
	from tkinter import *

	# Set up dictionaries to hold any windows, along with their widgets.
	# Keeps things organised, in my opinion.
	windows = {}
	widgets = {}

	#Declare Salary
	salary = 0
	
	# Calculate expected outcome for the month.
	expected_savings = float(salary*0.1);
	expected_spending = float(salary*0.1);
	expected_donation = float(salary*0.1);
	expected_learning = float(salary*0.05);


	class MainWindow():
		def __init__(self, windows):
			# Assign the main window to self.parent, since it will serve as the parent of all the widgets in this class.
			self.windows = windows
			self.parent = windows["main"]
		
			# Dictionaries to hold each widget, one for each type.
			self.labels = {}
			self.entries = {}
			self.buttons = {}
			self.canvases = {}
		
			self.init_ui()
	
			# Initialise the window with all the required properties and widgets.
			def init_ui(self):
				# Set the window's title and size.
				self.parent.title("Midas")
				self.parent.geometry("400x520+200+25")
		
				# Labels
				# Header:
				self.labels["standing"] = Label(self.parent, bg = "blue", text = "Standing Orders")
				self.labels["standing"].place(bordermode = "outside", x = 5, y = 5, width = 390, height = 25)
		
			# Savings:
			self.labels["savings"] = Label(self.parent, bg = "red", text = "Savings:")
			self.labels["savings"].place(bordermode = "outside", x = 5, y = 35, width = 70, height = 25)
		
			# Spending:
			self.labels["spending"] = Label(self.parent, bg = "green", text = "Spending:")
			self.labels["spending"].place(bordermode = "outside", x = 205, y = 35, width = 70, height = 25)
		
			# Donation:
			self.labels["donation"] = Label(self.parent, bg = "yellow", text = "Donation:")
			self.labels["donation"].place(bordermode = "outside", x = 5, y = 65, width = 70, height = 25)
		
			# Loans:
			self.labels["loan"] = Label(self.parent, bg = "pink", text = "Loan:")
			self.labels["loan"].place(bordermode = "outside", x = 205, y = 65, width = 70, height = 25)
		
			# Entry boxes
			# Savings:
			self.entries["savings"] = Entry(self.parent, bg = "red", justify = "center")
			self.entries["savings"].place(bordermode = "outside", x = 80, y = 35, width = 115, height = 25)
		
			# Spending:
			self.entries["spending"] = Entry(self.parent, bg = "green", justify = "center")
			self.entries["spending"].place(bordermode = "outside", x = 280, y = 35, width = 115, height = 25)
		
			# Donation:
			self.entries["donation"] = Entry(self.parent, bg = "yellow", justify = "center")
			self.entries["donation"].place(bordermode = "outside", x = 80, y = 65, width = 115, height = 25)
		
			# Loans:
			self.entries["loan"] = Entry(self.parent, bg = "pink", justify = "center")
			self.entries["loan"].place(bordermode = "outside", x = 280, y = 65, width = 115, height = 25)
		
			# Buttons
			# Triggers code to calculate the user's financial plan.
			self.buttons["calculate"] = Button(self.parent, bg = "red", text = "Calculate")
			self.buttons["calculate"].place(bordermode = "outside", x = 5, y = 95, width = 190, height = 25)
		
			# Exports the result to a CSV file.
			self.buttons["export"] = Button(self.parent, bg = "red", text = "Export")
			self.buttons["export"].place(bordermode = "outside", x = 205, y = 95, width = 190, height = 25)
		
			# Canvas
			# Shows the calculated output to the user directly.
			self.canvases["output"] = Canvas(self.parent, bg = "black")
			self.canvases["output"].place(bordermode = "outside", x = 5, y = 125, width = 390, height = 390)

			# Creates the main window and an object to handle its widgets, then executes the event loop for that window.
			def main():
				windows["main"] = Tk()
				widgets["main"] = MainWindow(windows)
				windows["main"].mainloop()

	if __name__ == "__main__":
		main()
# Catching the common exceptions in the program
except ImportError:
	print("No module found")
except ValueError:
    print("Could not convert data to integer.")
except KeyboardInterrupt:
    print("You cancelled the operation")
except EOFError:
    print("Why you end of file on me")
except Exception as err:
    print("Error: ", err)