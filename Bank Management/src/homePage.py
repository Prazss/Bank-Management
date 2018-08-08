'''
Created on 22-Jul-2018

@authors:   Prajnesh, Priya, Vikhyath, Nishant
'''

from menus import *

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print('\t\t\t\t\t\t\t\t\tLEO NATIONAL BANK')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
print('\t\t\t\t\t\t     The most reliable bank for every citizen of our country.')
print('\t\t\t\t  Established since 1997 and have been providing the most reliable services across the nation.')
print('\t\t\t\t\t\t\t\t  Your happiness is our priority.\n\n') 
 

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        sign_up_menu()
    elif choice == 2:
        sign_in_menu()
    elif choice == 3:
        admin_menu_display()
    elif choice == 4:
        loop = 0
        print("Thank You for stopping by the bank")
    else:
        print('Wrong Choice......Try again!!!')