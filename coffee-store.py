'''

Author: Daniel N Anorue

Program Title: Coffee Store

File Description:

A program which uses functions to help the user place orders on what cofee they'd like and show
Statistics on The total amount of coffee bought per type, total coffee sold in gallons and total
profit made. 

'''

def purchase_coffee():

        print('What Size are you purchasing today?')
        print('1. Small (9 fl oz): $1.75')
        print('2. Medium (12 fl oz): $1.90')
        print('3. Large (15 fl oz): $2.00')
        userChoice = int(input('Enter your choice: '))
        while userChoice not in (1,2,3):
            userChoice = int(input('Incorrect Choice. Enter Again: '))
        if (userChoice == 1):
            size = 9
            price = 1.75
        elif (userChoice == 2):
            size = 12
            price = 1.90
        else:
            size = 15
            price = 2
        return size,price


def show_stats(smallCups, mediumCups, bigCups, profit):
        gallons = ((smallCups * 9) + (mediumCups * 12) + (bigCups * 15))/128


        print('\nCups sold so far:')
        print(f'9 fl oz: {smallCups}')
        print(f'12 fl oz: {mediumCups}')
        print(f'15 fl oz: {bigCups}')
        print(f"Gallons Sold: {gallons}")
        print(f"Total Sale Profits: ${profit:.2f}")

def show_menu():

    print('Main Menu:')
    print('\t1. Purchase A Cup of Coffee')
    print('\t2. Show Store Statistics')
    print('\t3. Exit Program')
    userChoice = int(input('Enter your Choice: '))

    while userChoice not in (1,2,3):
     userChoice = int(input('Incorrect Choice. Enter Again: '))

    return userChoice

    


def main():
    

    size_9 = 0
    size_12 = 0
    size_15 = 0
    profit = 0
    total_sales = 0

    userChoice = 0

    while userChoice != 3:
     userChoice = show_menu()

     if (userChoice == 1):
           size, price = purchase_coffee()
           if (size == 9):
                    size_9 += 1
                    profit += price
                    total_sales += 1
           elif (size == 12):
                    size_12 += 1
                    profit += price
                    total_sales += 1
           elif (size == 15):
                    size_15 += 1
                    profit += price
                    total_sales += 1

     elif (userChoice == 2):
            show_stats (size_9, size_12, size_15, profit)

     else:
          return

    





main()