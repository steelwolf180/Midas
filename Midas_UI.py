from tkinter import *

windows = {}
widgets = {}

class MainWindow():
	def __init__(self, windows):
		self.windows = windows
		self.parent = windows["main"]
		
		self.labels = {}
		self.entries = {}
		self.buttons = {}
		self.canvases = {}
		
		self.init_ui()
		
	def init_ui(self):
		self.parent.title("Midas")
		self.parent.geometry("400x520+200+25")
		
		# Labels
		self.labels["standing"] = Label(self.parent, bg = "blue", text = "Standing Orders")
		self.labels["standing"].place(bordermode = "outside", x = 5, y = 5, width = 390, height = 25)
		
		self.labels["savings"] = Label(self.parent, bg = "red", text = "Savings:")
		self.labels["savings"].place(bordermode = "outside", x = 5, y = 35, width = 70, height = 25)
		
		self.labels["spending"] = Label(self.parent, bg = "green", text = "Spending:")
		self.labels["spending"].place(bordermode = "outside", x = 205, y = 35, width = 70, height = 25)
		
		self.labels["donation"] = Label(self.parent, bg = "yellow", text = "Donation:")
		self.labels["donation"].place(bordermode = "outside", x = 5, y = 65, width = 70, height = 25)
		
		self.labels["loan"] = Label(self.parent, bg = "pink", text = "Loan:")
		self.labels["loan"].place(bordermode = "outside", x = 205, y = 65, width = 70, height = 25)
		
		
		# Entry boxes
		self.entries["savings"] = Entry(self.parent, bg = "red", justify = "center")
		self.entries["savings"].place(bordermode = "outside", x = 80, y = 35, width = 115, height = 25)

		self.entries["spending"] = Entry(self.parent, bg = "green", justify = "center")
		self.entries["spending"].place(bordermode = "outside", x = 280, y = 35, width = 115, height = 25)
		
		self.entries["donation"] = Entry(self.parent, bg = "red", justify = "center")
		self.entries["donation"].place(bordermode = "outside", x = 80, y = 65, width = 115, height = 25)
		
		self.entries["donation"] = Entry(self.parent, bg = "pink", justify = "center")
		self.entries["donation"].place(bordermode = "outside", x = 280, y = 65, width = 115, height = 25)
		
		# Buttons
		self.buttons["calculate"] = Button(self.parent, bg = "red", text = "Calculate")
		self.buttons["calculate"].place(bordermode = "outside", x = 5, y = 95, width = 190, height = 25)

		self.buttons["export"] = Button(self.parent, bg = "red", text = "Export")
		self.buttons["export"].place(bordermode = "outside", x = 205, y = 95, width = 190, height = 25)
		
		# Canvas
		self.canvases["output"] = Canvas(self.parent, bg = "black")
		self.canvases["output"].place(bordermode = "outside", x = 5, y = 125, width = 390, height = 390)

def main():
	windows["main"] = Tk()
	widgets["main"] = MainWindow(windows)
	windows["main"].mainloop()

if __name__ == "__main__":
	main()
