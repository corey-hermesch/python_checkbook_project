#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Checkbook Project
# Simple checkbook program that will 
# 1. View Current Balance
# 2. Make a withdrawal (debit)
# 3. Add a deposit (credit)
# 4. Exit
#
# Upon exit, the new balance should be available the next
# time the program is run. (i.e. write it to a file)
#
# For more details, see https://ds.codeup.com/python/project/

import os
import subprocess

# global variable definitions
# name of file to store the current balance
balance_file_name = 'balance.txt'


# In[2]:


def menu_input():
    '''
    menu_input take no input. It prints a menu for the user with 4 options
    It then requests an input from the user. The function loops until the 
    user inputs a valid input 1-4, and returns the valid user input.
    '''
    choice = '0'
    while True:
        print("\nWhat would you like to do? \n")
        print("1) view current balance")
        print("2) record a debit (withdraw)")
        print("3) record a credit (deposit)")
        print("4) exit\n")
        choice = input("Your choice? ")
        choice = choice.strip()
        if choice in ['1','2','3','4']:
            return choice
        else:
            print("That choice is invalid. Please make a valid selection 1-4\n")


# In[3]:


def write_balance(new_bal_str):
    '''
    write_balance takes a string as an input and writes that string to the 
    balance file (balance_file_name). The function assumes the input is a 
    string that is a valid dollar amount in the form d.dd, dd.dd, etc.
    write_balance returns nothing
    '''
    with open(balance_file_name, 'w') as bf:
        bf.write(new_bal_str)
        return
        


# In[4]:


def read_balance():
    '''
    read_balance takes no input. It reads the balance file 
    (balance_file_name) and returns that string
    '''    
    with open(balance_file_name) as bf:
        cur_bal_str = bf.read()
    return cur_bal_str


# In[6]:


def get_valid_money(amount_str):
    '''
    get_valid_money takes a string as an input, checks to see if the string is a positive amount of money,
    and returns a string which is a money amount in the form d.dd or dd.dd or ddd.dd etc.
    If the input is not valid, it will prompt the user for a new input and loop until input is valid
    
    Valid inputs:
    125.00 returns 125.00
    $125   returns 125.00
      $125 returns 125.00
    .5     returns 0.50
    5.     returns 5.00
    .62    returns 0.62

    Invalid inputs:
    xyz
    .
    1/2
    5..
    .623
    .62w
    '''    
    while True:
        # use try because if float(amount_str) fails, I can use except to ask the user again
        # for a valid input
        try:
            # strip leading and trailing white space and '$'
            amount_str = amount_str.strip('$ ')                  
            # attempt to make a float out of amount_str (failure goes to the except)
            float_amount = float(amount_str)
            # check for negative input (not allowed)
            if float_amount < 0:
                amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")
                continue
            # after the decimal point, I want exactly two characters. 
            # If there are more than two -> invalid input; if only one, I add a '0' 
            amount_str = str(float_amount)
            if amount_str.index('.') < len(amount_str) - 3:
                amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")
                continue
            elif amount_str.index('.') == len(amount_str) - 2:
                amount_str += '0'
            break
        except ValueError:
            # the try failed because float(amount_str) errored out so it asks again
            amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")
    return amount_str

x = '75.69'
print(x)
print (get_valid_money(x))


# In[7]:


def debit():
    '''
    debit() takes no input. It asks the user for a valid dollar amount
    in the form d.dd or dd.dd etc. It then reads the current balance.
    If the debit_amount entered is greater than the current balance, it
    asks informs the user they do not have enough funds and asks for
    a new withrdrawal amount. Upon receiving an amount < the current 
    balance, the function subtracts the user input from the current 
    balance, writes the new balance to the balance file, informs the 
    user of their new balance, and returns
    '''
    while True:
        debit_amount_str = input("How much would you like to withdraw? ")
        debit_amount = get_valid_money(debit_amount_str)
        cur_balance = read_balance()
        if float(debit_amount) > float(cur_balance):
            print(f"Your current balance of {cur_balance} does not allow that withdrawal amount.")
            continue
        else:
            break
    new_balance = str(round(float(cur_balance) - float(debit_amount), 2))
    new_balance = get_valid_money(new_balance)
    write_balance(new_balance)
    print(f"Your new balance is ${new_balance}.")
    return


# In[8]:


def credit():
    '''
    credit() takes no input. It asks the user for a valid dollar amount
    in the form d.dd or dd.dd etc. It then reads the current balance,
    adds the user input from the current balance, writes the new
    balance to the balance file, informs the user of their new balance,
    and returns
    '''
    debit_amount_str = input("How much would you like to deposit? ")
    debit_amount = get_valid_money(debit_amount_str)
    cur_balance = read_balance()
    new_balance = str(round(float(cur_balance) + float(debit_amount), 2))
    new_balance = get_valid_money(new_balance)
    write_balance(new_balance)
    print(f"Your new balance is ${new_balance}.")
    return


# In[9]:


## main program block

print("~~~ Welcome to your terminal checkbook! ~~~")
if not os.path.exists(balance_file_name):
    print("As our way of saying thank you for opening a checking account with us,")
    print("we are starting you with a balance of $100.00!\n")
    write_balance('100.00')
menu_choice = '0'
while True:
    menu_choice = menu_input()
    if menu_choice == '1':
        print(f"Your current balance is {read_balance()}")
    elif menu_choice == '2':
        debit()
    elif menu_choice == '3':
        credit()
    elif menu_choice == '4': 
        print("Thanks, have a great day!")
        break


# In[ ]:


# functions below were rejected or still in test


# In[ ]:


# def get_valid_money_1(amount_str):
#     # first attempt at checking for a valid dollar amount. 
#     # it works, but there was an easier way (above)
    
#     while True:
#         # first strip leading and trailing whitespace and '$'
#         amount_str = amount_str.strip('$ ')

#         # if user accidentally hit enter by mistake, there's no input -> invalid
#         if len(amount_str) == 0:
#             amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")            
#             continue

#         # if there is more than one period, the input is invalid
#         period_count = amount_str.count('.')
#         if period_count > 1:
#             amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")            
#             continue
        
#         # if there are characters in the string that are not a digit or a '.', the input is invalid
#         not_digit = False
#         for c in amount_str:
#             if c.isdigit() or c == '.':
#                 pass
#             else:
#                 amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")  
#                 not_digit = True
#                 break
#         if not_digit: continue
        
#         # if the input does not have a '.', it is still valid since we've already checked for
#         # all digits and the edge case empty string ('') above.
#         if period_count == 0:
#             return (amount_str + ".00")

#         # if there is only one period, there are still some weird cases to account for
#         # like '.', '1.','.1' and '2.001'
#         if period_count == 1:
#             if len(amount_str) == 1: 
#                 amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")
#             dec_index = amount_str.index('.')
#             if dec_index == 0:
#                 if len(amount_str) == 2:
#                     return ("0" + amount_str + "0")
#                 elif len(amount_str) == 3:
#                     return ("0" + amount_str)
#                 else:
#                     amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")
#                     continue
#             if dec_index == (len(amount_str) - 1):
#                 return (amount_str + "00")
#             elif dec_index == (len(amount_str) - 2):
#                 return (amount_str + "0")
#             elif dec_index == (len(amount_str) - 3):
#                 return (amount_str)
#             else: 
#                 amount_str = input("Invalid entry. Please enter a valid dollar amount (dd.dd):")  
#                 continue


# In[ ]:


# def get_valid_money3(amount_str):
#     # a work in progress
#     # utilizing a post from stack overflow
#     # https://stackoverflow.com/questions/66361824/python-verifying-a-string-represents-a-valid-us-currency-value
#     while True:
#         re.match("\$?(-?(\d+[,.])*\d+)", amount_str)  # match
#         amount_str = re.match("\$?(-?(\d+[,.])*\d+)", amount_str).group(1)  # extract matched value
#         amount_str = re.sub('[,$]', '', amount_str)                  # remove comma and dollar sign
#         try:
#             amount_float = float(re.sub('[,$]', '', amount_str))           # convert to float if the result doesn't contain any special character such as comma
#             break
#         except ValueError:
#             amount_str = input("invalid, try again: ")
#     return amount_str


# In[ ]:




