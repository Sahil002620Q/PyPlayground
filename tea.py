print('Do you want to prepare ? (Y/N) :')
choice = input()
if choice == "Y" or 'y':
    choice2 = input('Do you want to proceed and want to add water on flame ? (Y/N) :\n')
    if choice2 == 'Y'or 'y':
        input('Continue adding sugar and tea powder. (Y/N) :\n')
        print("wait a minute to boil water ")

        import time
        time.sleep(5)

        print('Water have been boiled now')
        choice3 = input('continue adding milk ? (Y/N) :\n')
        if choice3 == 'Y' or 'y':
            print('Milk added successfully')

            time.sleep(1)
            print('Wait for few minutes till the mixture boil\'s')
        
            time.sleep(5)
            print('Mixture boiled successfully')

            time.sleep(3)
            choice4 = input('Countinue filtration of mixtue to cup. (Y/N):\n')
            if choice4 == 'Y'or 'y':
                time.sleep(3)
                print('WOOHOO!, Here is your tea ')
                print('☕')
else :
    print('🥲')
