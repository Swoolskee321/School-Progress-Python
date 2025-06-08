#shopping cart lists and options 
shopping_cart_items = []
shopping_cart_prices = []
menu = ["Add item", "View Cart", "Remove Item", "Total Cost", "Clear Cart", "Quit"]


#Shopping cart specs
shopping_cart_item = ""
shopping_cart_price = ""

#menu system loop
while True:
    print ("Which menu options would you like to select from the list below?")
    for i in range(len(menu)):
        print (f"{i+1}. {menu[i]}")

    user_choice = input("Please enter an action:  ")

    #add item option
    if user_choice == "1":
        shopping_cart_item = input ("Add new Shopping Cart Item:  ")
        shopping_cart_price = float(input("What is the price for this item?" ))

        shopping_cart_items.append(shopping_cart_item)
        shopping_cart_prices.append(shopping_cart_price)
        print(f"{shopping_cart_item} Has been added to the cart.")

    #view cart option
    elif user_choice == "2":
        print("Here is your list of current items:")
        if len(shopping_cart_items) == 0:
            print("Your Shopping cart is empty.")
        else:
             for i in range(len(shopping_cart_items)):
                  print(f"{i+1}. {shopping_cart_items[i]} - ${shopping_cart_prices[i]:.2f}")
                
    #Remove item option
    elif user_choice == "3":
        print("Here is your list of current items:")
        if len(shopping_cart_items) == 0:
             print("Your shopping cart is empty.")
        else:
             for i in range(len(shopping_cart_items)):
                  print(f"{i+1}. {shopping_cart_items[i]} - ${shopping_cart_prices[i]:.2f}")

             remove_input = input("Which item number would you like to remove? ")
             if remove_input.isdigit():
                  remove_index = int(remove_input) - 1

             if 0 <= remove_index < len(shopping_cart_items):
                       removed_item = shopping_cart_items.pop(remove_index)
                       shopping_cart_prices.pop(remove_index)
                       print(f"{removed_item} has been removed from the cart.")
             else:
                    print("Sorry, that item number is invalid.")
        
    #calculate the total in the cart

    elif user_choice == "4":
        total = sum(shopping_cart_prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    #clear cart option
    elif user_choice == "5":
        shopping_cart_items.clear()
        shopping_cart_prices.clear()
        print("The shopping cart has been cleared.")

    #Quit
    elif user_choice == "6":
        print("Thank you. Have a nice day!")
    else:
        print("Option not selected. Please try again")
    