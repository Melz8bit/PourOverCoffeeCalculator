import tkinter as tk

# Variables
# Coffee in grams; water in ml
baseCoffee = 40
userCoffee = 0    
baseWater = 600    
userWater = 0
userInputOption = ''
userUpdateBaseOption = ''


def buttonClick(event):
    userWater = int(textEntry.get())
    userCoffee = (baseCoffee * userWater) / baseWater
    print(userCoffee)

window = tk.Tk() # Creates window
window.title("Pour Over Coffee Calculator") # Sets window title
window.resizable(0,0) # Disables maximize computer
window.geometry("500x200") # Sets window size (w x h)

defaultValuesLabel = tk.Label(
    text="Coffee: %d grams\n Water: %d ml" % (baseCoffee, baseWater),
    padx=20,
    pady=20
)

# Label on screen
enterCoffeeLabel = tk.Label(
    text="Please enter the amount of coffee to be used (in grams):",
    padx=10,
    pady=10
)

# Create button
calculateCoffeeButton = tk.Button(
    text="Calculate Coffee",
    height=2,
    width=14
)

# Create textbox
textEntry = tk.Entry(width=10)

# Puts widgets on screen
defaultValuesLabel.pack()
enterCoffeeLabel.pack(side=tk.LEFT)
textEntry.pack(side=tk.LEFT)
calculateCoffeeButton.pack(side=tk.BOTTOM)

calculateCoffeeButton.bind("<Button-1>", buttonClick)

# Displays window
tk.mainloop()