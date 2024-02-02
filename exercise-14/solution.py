# Instantiating a menu dictionary
# keys correspond to items
# values correspont to prices

menu = dict(latte = 6, drip = 3, chocolatine = 4, poutine = 7)

# the very standard way of typically solving this problem

def restaurant():

    order_total: int = 0

    # using walrus for assignment + boolean eval
    while choice := input("What would you like to order today?"):

        if choice in menu:

            order_total += menu[choice]

            print(f"The {choice} costs ${menu[choice]}. Your total is {order_total:.2f}")

        else:

            print("I couldn't find that in our menu. Please try again.")
        
    print(f"Your order total is ${order_total}")

restaurant()

