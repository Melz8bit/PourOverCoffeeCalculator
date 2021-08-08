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
my_anchor = tk.W # Used for text align of all the widgets
user_calc_var = tk.StringVar(window, 'empty') # Saves the radio button values
button_text = 'Calculate'

def calculate_amount(event):
    global button_text
    user_entry_amount = int(text_entry.get())
    
    print(button_text)
    if button_text == 'Calculate':
        if user_entry_amount > 0:
            if user_input_option == 'coffee':
                measurement = 'g'
                amount_needed = calculate_coffee(user_entry_amount, BASE_COFFEE, BASE_WATER)
            elif user_input_option == 'water':
                measurement = 'ml'
                amount_needed = calculate_water(user_entry_amount, BASE_COFFEE, BASE_WATER)

            # Updates and displays the calculated amount label
            calculated_total.configure(
                text='You will need %.2f %s of %s.' % (amount_needed, measurement, user_input_option))
            calculated_total.place(x=5, y=defaultValuesLabel.winfo_height() + 160, anchor=my_anchor)

            # Update button for reset
            button_text = 'Reset'
            calculate_coffee_button.configure(text=button_text)

    # Resets form            
    elif button_text == 'Reset':
        button_text = 'Calculate'
        calculate_coffee_button.configure(text=button_text)
        reset_window()

def calculate_coffee(water_grams, BASE_COFFEE, BASE_WATER):
    return (BASE_COFFEE * water_grams) / BASE_WATER

def calculate_water(coffee_grams, BASE_COFFEE, BASE_WATER):
    return (BASE_WATER * coffee_grams) / BASE_COFFEE    

# Clear the items from the window
def reset_window():
    global user_calc_var
    enter_coffee_label.place_forget()
    text_entry.place_forget()
    calculate_coffee_button.place_forget()
    calculated_total.place_forget()
    user_calc_var.set('empty')    

def clear_text():
    text_entry.delete(0, 'end') # Clear entry box
    text_entry.insert(-1, 0) # Default value to 0

# Sets values for calculating the coffee or water depending on radio button selection
def set_calc_selection():
    global user_input_option

    clear_text()

    if user_calc_var.get() == 'coffee':
        calc_item = 'water' # What is being calculated
        measurement = 'ml'
        user_input_option = 'coffee'

    elif user_calc_var.get() == 'water':
        calc_item = 'coffee' # What is being calculated
        measurement = 'grams'    
        user_input_option = 'water'
    
    # Update and place the label prompting user to enter amount of coffee/water they have
    enter_coffee_label.configure(text='Please enter the amount of %s to be used (in %s):' % (calc_item, measurement))
    enter_coffee_label.place(x=5, y=defaultValuesLabel.winfo_height() + 95, anchor=my_anchor)
    enter_coffee_label.update()

    # Places the text box and button on screen
    text_entry.place(x=enter_coffee_label.winfo_width() + 10, y=defaultValuesLabel.winfo_height() + 95, anchor=my_anchor)
    calculate_coffee_button.place(x=15, y=defaultValuesLabel.winfo_height() + 125, anchor=my_anchor)
    
# Label with default values
defaultValuesLabel = tk.Label(
    text="Coffee: %d grams\nWater: %d ml" % (BASE_COFFEE, BASE_WATER),
    justify=tk.LEFT,
    padx=0,
    pady=5
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
coffee_calc_select.place(x=15, y=defaultValuesLabel.winfo_height() + 45, anchor=my_anchor)

water_calc_select = tk.Radiobutton(window, 
    text='Water',
    value='water',
    variable=user_calc_var,
    command=set_calc_selection
)
water_calc_select.place(x=15, y=defaultValuesLabel.winfo_height() + 65, anchor=my_anchor)

# Label on screen prompting user for entry 
enter_coffee_label = tk.Label(
    text='',
    justify=tk.LEFT
)

# Create textbox for amount
text_entry = tk.Entry(width=5)

# Create Calculate/Reset button
calculate_coffee_button = tk.Button(
    text=button_text,
    width=10,
    height=1
)

# Button click functionality
calculate_coffee_button.bind("<Button-1>", calculate_amount)

# Create label for calculated amount
calculated_total = tk.Label()

# Displays window
tk.mainloop()