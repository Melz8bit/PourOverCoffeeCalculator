
def calculate_coffee(water_grams, base_coffee, base_water):
    return (base_coffee * water_grams) / base_water

def calculate_water(coffee_grams, base_coffee, base_water):
    return (base_water * coffee_grams) / base_coffee

def main():
    # Variables
    # Coffee in grams; water in ml
    BASE_COFFEE_POUR_OVER = 40
    BASE_WATER_POUR_OVER = 600

    BASE_COFFEE_COLD_BREW = 106
    BASE_WATER_COLD_BREW = 980

    base_coffee = 0
    base_water = 0
    userCoffee = 0            
    userWater = 0
    brew_method = ''
    userInputOption = ''
    userUpdateBaseOption = ''

    # Prompt for brew method
    while brew_method not in ('p', 'c'):
        brew_method = input("Would you like to calculate for (P)our over or (C)old brew method? ").lower()
    
    if brew_method == 'p':
        base_coffee = BASE_COFFEE_POUR_OVER
        base_water = BASE_WATER_POUR_OVER
    elif brew_method == 'c':
        base_coffee = BASE_COFFEE_COLD_BREW
        base_water = BASE_WATER_COLD_BREW
    
    print('==================================')
    print('Base coffee: %d grams' % base_coffee)
    print('Base water: %d ml' % base_water)
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
        
        print('Base coffee: %d grams' % base_coffee)
        print('Base water: %d ml' % base_water)
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
    print('Coffee: %d\tWater: %d' % (userCoffee, userWater))


if __name__ == "__main__":
    main()