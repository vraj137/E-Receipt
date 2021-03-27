"""
Name: Vraj Bhavsar
Date: October 04, 2020

This program asks the user for eight different items on the shopping list 
(Name of the item, quantity, price and the discount applied. Then prints out a reciept
that includes the subtotal, discount amount, HST (13%) and grand total.  

"""
import time 

greetings = print("Welcome to Bhavsar Supermarket, Valued E-Customer!")

# Waits 3 seconds then runs the code below
time.sleep(3.5)
print(" ") 

items = int(input("Before we begin, how many items do you have today? "))
total_amount = ""
subtotal = 0
tax = 1.13

for i in range(items):
# Asks the user for their input for each item, price, quantity and discount  
    amount_items = input("What is item " + "#" + str(i + 1) + ": ")
    amount_price = float(input("What is the price: " + "$"))
    quantity = int(input("Quantity?: "))
    discount = float(input("What discount percent should be applied on this item?: "))
    
# Makes sure the user doesn't input a discount value lower than 0 or greater than 50 percentpwd
    while int(discount) < 0 or int(discount) > 50:
        print("Invaild, try again")
        discount = float(input("What discount percent should be applied on this item?: "))
        
# Does the calculations after the user inputs the data from above to find the grand total with the -
# discount and tax included
    total = round(amount_price * quantity, 2)
    discount_one = round(total * discount/100, 2)
    cost = round(total - discount_one, 2)
    subtotal = subtotal + cost  
    subtax = (subtotal * 1.13) - subtotal
    grand_total = subtotal + subtax

# Puts the users input together to form a receipt, the \n is used to create a new row for each item
    total_amount += amount_items + "         " + "$" + str(amount_price) + "         " + str(quantity) + "        " \
    + "$" + str(total) + "         " + "$" + str(discount_one) + "         " + "$" + str(cost) + " \n"

# Prints the final receipt with all the calculations completed     
print("")
print("Receipt: ")
print("Item Name     Price      Quantity     Total      Discount        Cost ")
print(total_amount)
print("")
print("Subtotal: " + "$" + str(round(subtotal, 2)))
print("HST: " + "$" + str(round(subtax, 2)))
print("Grand Total: " + "$" + str(round(grand_total,2)))

time.sleep(2)
print("Thank you for Shopping at Bhavsar Supermarket!")

# End of Code