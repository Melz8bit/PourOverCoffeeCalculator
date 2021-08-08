import tkinter as tk

# Variables
# Coffee in grams; water in ml
base_coffee = 40
user_coffee = 0    
base_water = 600    
user_water = 0
user_input_option = ''
user_update_base_option = ''


def buttonClick(event):
    user_water = int(textEntry.get())
    user_coffee = (base_coffee * user_water) / base_water
    # print(user_coffee)

def set_calc_selection():
    pass
    #user_input_option = user_calc_options.get()
    #print(user_input_option)

window = tk.Tk() # Creates window
window.title("Pour Over Coffee Calculator") # Sets window title
window.resizable(0,0) # Disables maximize computer
window.geometry("500x200") # Sets window size (w x h)

# tk Variables
my_anchor = tk.W
user_calc_var = tk.StringVar(window, 'melz')

defaultValuesLabel = tk.Label(
    text="Coffee: %d grams\nWater: %d ml" % (base_coffee, base_water),
    justify=tk.LEFT,
    padx=5,
    pady=5,
    borderwidth=1,
    relief='solid'
)
defaultValuesLabel.place(x=5, y=5)
defaultValuesLabel.update()

# Create radio buttons for calculation selection
tk.Label(text='Choose which to calculate:').place(x=5, y=defaultValuesLabel.winfo_height() + 15)
coffee_calc_select = tk.Radiobutton(window, 
    text='Coffee',
    value='coffee',
    variable=user_calc_var
)

water_calc_select = tk.Radiobutton(window, 
    text='Water',
    value='water',
    variable=user_calc_var
)
coffee_calc_select.place(x=5, y=defaultValuesLabel.winfo_height() + 45, anchor=my_anchor)
water_calc_select.place(x=5, y=defaultValuesLabel.winfo_height() + 65, anchor=my_anchor)

test = user_calc_var.get()
print(test)

# Label on screen
enterCoffeeLabel = tk.Label(
    text='Please enter the amount of %s to be used (in grams):' % user_input_option,
    justify=tk.LEFT
)
#enterCoffeeLabel.place(x=5, y=defaultValuesLabel.winfo_height() + 20, anchor=my_anchor)
enterCoffeeLabel.update()
""" print(enterCoffeeLabel.winfo_width())
print(enterCoffeeLabel.winfo_height())
print(enterCoffeeLabel.winfo_y()) """

# Create textbox
textEntry = tk.Entry(width=10)
#textEntry.place(x=enterCoffeeLabel.winfo_width() + 10, y=defaultValuesLabel.winfo_height() + 20, anchor=my_anchor)

# Create button
calculateCoffeeButton = tk.Button(
    text="Calculate Coffee",
    height=2,
    width=14
)
# calculateCoffeeButton.pack(side=tk.BOTTOM)

""" # Puts widgets on screen
defaultValuesLabel.pack()
enterCoffeeLabel.pack(side=tk.LEFT)
textEntry.pack(side=tk.LEFT)
calculateCoffeeButton.pack(side=tk.BOTTOM) """

calculateCoffeeButton.bind("<Button-1>", buttonClick)

# Displays window
tk.mainloop()