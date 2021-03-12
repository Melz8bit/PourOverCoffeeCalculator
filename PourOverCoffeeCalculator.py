

def main():
    # Variables
    # Coffee in grams; water in ml
    baseCoffee = 55
    userCoffee = 0    
    baseWater = 1000    
    userWater = 0
    userInputOption = ''
    userUpdateBaseOption = ''

    print('==================================')
    print('Base coffee: %d grams' % baseCoffee)
    print('Base water: %d ml' % baseWater)
    print('==================================')

    if input("Would you like to update the base values? (Y)es/(N)o ").lower() == 'y':
        while userUpdateBaseOption not in ('c', 'w'):
            userUpdateBaseOption = input("Would you like to update (C)offee or (W)ater? ").lower()

        if userUpdateBaseOption == 'c':
            baseCoffee = int(input('Please enter base coffee amount in grams: '))
        elif userUpdateBaseOption == 'w':
            baseWater = int(input('Please enter base water amount in milliliters: '))
        
        print('Base coffee: %d grams' % baseCoffee)
        print('Base water: %d ml' % baseWater)
        print('==================================')

    while userInputOption not in ('c', 'w'):
        userInputOption = input('Would you like to calculate (C)offee or (W)ater? ').lower()

    if userInputOption == 'c':
        userWater = int(input('Please enter the amount of water to be used (in milliliters): '))
        userCoffee = (baseCoffee * userWater) / baseWater
    elif userInputOption == 'w':
        userCoffee = int(input('Please enter the amount of coffee to be used (in grams): '))
        userWater = (baseWater * userCoffee) / baseCoffee

    
    print('Your ratio:')
    print('Coffee: %d\tWater: %d' % (userCoffee, userWater))


if __name__ == "__main__":
    main()