import tkinter as tk

# Variables
# Coffee in grams; water in ml
BASE_COFFEE = 40
BASE_WATER = 600  
user_coffee = 0      
user_water = 0
user_input_option = ''
user_update_base_option = ''

# tk Variables
WINDOW_WIDTH = '500'
WINDOW_HEIGHT = '250'
window = tk.Tk() # Creates window
window.title("Pour Over Coffee Calculator") # Sets window title
window.resizable(0,0) # Disables maximize computer
window.geometry(WINDOW_WIDTH + 'x' + WINDOW_HEIGHT) # Sets window size (w x h)
my_anchor = tk.W
user_calc_var = tk.StringVar(window, 'empty')

def calculate_amount(event):
    user_entry_amount = int(text_entry.get())
    if user_input_option == 'coffee':
        measurement = 'g'
        amount_needed = calculate_coffee(user_entry_amount, BASE_COFFEE, BASE_WATER)
    elif user_input_option == 'water':
        measurement = 'ml'
        amount_needed = calculate_water(user_entry_amount, BASE_COFFEE, BASE_WATER)

    tk.Label(
        text='You will need %.2f %s of %s.' % (amount_needed, measurement, user_input_option)
    ).place(x=5, y=defaultValuesLabel.winfo_height() + 180, anchor=my_anchor)

def calculate_coffee(water_grams, BASE_COFFEE, BASE_WATER):
    return (BASE_COFFEE * water_grams) / BASE_WATER

def calculate_water(coffee_grams, BASE_COFFEE, BASE_WATER):
    return (BASE_WATER * coffee_grams) / BASE_COFFEE    

def set_calc_selection():
    global user_input_option

    if user_calc_var.get() == 'coffee':
        enter_coffee_label.configure(text='Please enter the amount of water to be used (in mL):')
        user_input_option = 'coffee'
    elif user_calc_var.get() == 'water':
        enter_coffee_label.configure(text='Please enter the amount of coffee to be used (in grams):')
        user_input_option = 'water'
    
    enter_coffee_label.update()
    text_entry.place(x=enter_coffee_label.winfo_width() + 10, y=defaultValuesLabel.winfo_height() + 95, anchor=my_anchor)
    calculate_coffee_button.place(x=5, y=defaultValuesLabel.winfo_height() + 140, anchor=my_anchor)

defaultValuesLabel = tk.Label(
    text="Coffee: %d grams\nWater: %d ml" % (BASE_COFFEE, BASE_WATER),
    justify=tk.LEFT,
    padx=0,
    pady=5
    #borderwidth=1,
    #relief='solid'
)
defaultValuesLabel.place(x=5, y=5)
defaultValuesLabel.update()

# Create radio buttons for calculation selection
tk.Label(text='Choose which to calculate:').place(x=5, y=defaultValuesLabel.winfo_height() + 15)
coffee_calc_select = tk.Radiobutton(window, 
    text='Coffee',
    value='coffee',
    variable=user_calc_var,
    command=set_calc_selection
)

water_calc_select = tk.Radiobutton(window, 
    text='Water',
    value='water',
    variable=user_calc_var,
    command=set_calc_selection
)
coffee_calc_select.place(x=15, y=defaultValuesLabel.winfo_height() + 45, anchor=my_anchor)
water_calc_select.place(x=15, y=defaultValuesLabel.winfo_height() + 65, anchor=my_anchor)

# Label on screen  
enter_coffee_label = tk.Label(
    text='',
    justify=tk.LEFT
)
enter_coffee_label.place(x=5, y=defaultValuesLabel.winfo_height() + 95, anchor=my_anchor)
enter_coffee_label.update()

# Create textbox
text_entry = tk.Entry(width=10)

# Create button
calculate_coffee_button = tk.Button(
    text="Calculate Coffee",
    height=2,
    width=14
)

calculate_coffee_button.bind("<Button-1>", calculate_amount)

""" # Puts widgets on screen
defaultValuesLabel.pack()
enterCoffeeLabel.pack(side=tk.LEFT)
textEntry.pack(side=tk.LEFT)
calculateCoffeeButton.pack(side=tk.BOTTOM) """



# Displays window
tk.mainloop()