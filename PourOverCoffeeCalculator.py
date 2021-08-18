
def calculate_coffee(water_grams, base_coffee, base_water):
    return (base_coffee * water_grams) / base_water

def calculate_water(coffee_grams, base_coffee, base_water):
    return (base_water * coffee_grams) / base_coffee

def main():
    # Variables
    # Coffee in grams; water in ml
    base_coffee_pour_over: float = 40.0
    base_water_pour_over:float = 600.0
    base_coffee_cold_brew: float = 100.0
    base_water_cold_brew: float = 980.0

    base_coffee: float = 0.0
    base_water: float = 0.0
    userCoffee: float = 0.0          
    userWater:float = 0.0
    brew_method: chr = ''
    userInputOption: chr = ''
    userUpdateBaseOption: chr = ''

    # Prompt for brew method
    while brew_method not in ('p', 'c'):
        brew_method = input("Would you like to calculate for (P)our over or (C)old brew method? ").lower()
    
    if brew_method == 'p':
        base_coffee = base_coffee_pour_over
        base_water = base_water_pour_over
    elif brew_method == 'c':
        base_coffee = base_coffee_cold_brew
        base_water = base_water_cold_brew
    
    print('==================================')
    print(f'Base coffee: {base_coffee} grams')
    print(f'Base water: {base_water} ml')
    print('==================================')

    # Update base amounts, if needed
    if input("Would you like to update the base values? (Y)es/(N)o ").lower() == 'y':
        while userUpdateBaseOption not in ('c', 'w', 'b'):
            userUpdateBaseOption = input("Would you like to update (C)offee, (W)ater, or (B)oth? ").lower()

        if userUpdateBaseOption == 'c':
            base_coffee = int(input('Please enter base coffee amount in grams: '))
        elif userUpdateBaseOption == 'w':
            base_water = int(input('Please enter base water amount in milliliters: '))
        elif userUpdateBaseOption == 'b':
            base_coffee = int(input('Please enter base coffee amount in grams: '))
            base_water = int(input('Please enter base water amount in milliliters: '))            
        
        print(f'Base coffee: {base_coffee} grams')
        print(f'Base water: {base_water} ml')
        print('==================================')

    # Input validation on option to calculate
    while userInputOption not in ('c', 'w'):
        userInputOption = input('Would you like to calculate (C)offee or (W)ater? ').lower()

    # Calculate
    if userInputOption == 'c':
        userWater = int(input('Please enter the amount of water to be used (in milliliters): '))
        userCoffee = calculate_coffee(userWater, base_coffee, base_water)
    elif userInputOption == 'w':
        userCoffee = int(input('Please enter the amount of coffee to be used (in grams): '))
        userWater = calculate_water(userCoffee, base_coffee, base_water)
        
    print('Your ratio:')
    print(f'Coffee: {userCoffee}\tWater: {userWater}')


if __name__ == "__main__":
    main()