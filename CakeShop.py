import itertools
import sys
from tabulate import tabulate as table
from collections import Counter
from CakeMenu import menu1, menu2, menu3, Cake, Pricing
from CakeMenu import menu_flavor, menu_frosting, menu_topping, OrderCake


class CakeDelivery(Pricing):
    total_cost = 2.50

    def __init__(self):
        super().__init__()
        print(self.__str__())
        self.cake_stack = OrderCake()
        self.cake_stack.add_item("Cake Board")
        self.cake_prices = {"Cake Board": 2.5}
        self.cake_layer = []
        self.entry = []
        self.user_prompts()

    def __str__(self):
        return '''
===============
 The Cake Shop
=============== 

Welcome to The Cake Shop! We bake handmade cakes for any special occasion.
Please select an item number listed on the menu. Type "Yes" to confirm your order or "Cancel" to try again. 
You can type "Clear" on the screen to start over.

A cake board is placed on the bottom. What can I get for you today?'''

    def user_prompts(self):
        try:
            num_stacks = int(input("How many layers should the cake have? (1-3) "))
            if num_stacks <= 3:
                for _ in itertools.repeat(None, num_stacks):
                    self.show_layers()
                    self.flavor()
                    self.show_icing()
                    self.frosting()
                self.show_toppers()
                self.topping()
                self.order_summary()
            else:
                print("The cake can only have three layers at most.")
        except ValueError:
            print("Error: Input must be an integer.")
            self.user_prompts()

    @staticmethod
    def check_order(confirm):
        while confirm not in Cake.check_again:
            print("Your input was not valid. Try again.\n")
            confirm = input("Confirm your order? [Yes] [Cancel] [Clear] ").title()
            continue
        return confirm

    @staticmethod
    def confirm_order(selection):
        while selection not in Cake.input_values:
            print("Error: This option is not on the menu.")
            selection = input("\nPlease select another item. ").title()
            continue
        return selection

    def __add__(self, value):
        CakeDelivery.total_cost += value

    def __sub__(self, value):
        CakeDelivery.total_cost -= value

    def flavor(self):
        # Add cake layer
        cake_type = input("Add a new layer to the cake. (1-7) ").title()
        number = self.confirm_order(cake_type)
        user_choice = menu1.search_ll(menu_flavor[int(number)-1])
        self.cake_stack.add_item(user_choice)
        self.cake_stack.display_order()
        finalize = input("Confirm your order? [Yes] [Cancel] [Clear] ").title()
        answer = self.check_order(finalize)
        unit_price = self.get_layer(user_choice)
        self.__add__(unit_price)
        if answer == "Yes":
            self.cake_prices.update({user_choice: unit_price})
            print(f"You have created a {menu_flavor[int(number)-1]} cake.")
            print(f"Your total is ${CakeDelivery.total_cost:.2f}.")
        elif answer == "Cancel":
            print("You have removed the last item.\n")
            self.cake_stack.remove_item()
            self.__sub__(unit_price)
            self.flavor()
        else:
            self.clear_all(finalize)

    def frosting(self):
        # Add frosting
        cake_type = input("What kind of icing do you want? (1-7) ").title()
        number = self.confirm_order(cake_type)
        user_choice = menu2.search_ll(menu_frosting[int(number)-1])
        self.cake_stack.add_item(user_choice)
        self.cake_stack.display_order()
        finalize = input("Confirm your order? [Yes] [Cancel] [Clear] ").title()
        answer = self.check_order(finalize)
        unit_price = self.get_icing(user_choice)
        self.__add__(unit_price)
        if answer == "Yes":
            self.cake_prices.update({user_choice: unit_price})
            print(f"The cake is now covered in {menu_frosting[int(number)-1]}.")
            print(f"Your total is ${CakeDelivery.total_cost:.2f}.")
        elif answer == "Cancel":
            print("You have removed the last item.\n")
            self.cake_stack.remove_item()
            self.__sub__(unit_price)
            self.frosting()
        else:
            self.clear_all(finalize)

    def topping(self):
        # Add topping
        cake_type = input("Would you like to include a topper? (1-7) ").title()
        number = self.confirm_order(cake_type)
        user_choice = menu3.search_ll(menu_topping[int(number)-1])
        self.cake_stack.add_item(user_choice)
        self.cake_stack.display_order()
        finalize = input("Confirm your order? [Yes] [Cancel] [Clear] ").title()
        answer = self.check_order(finalize)
        unit_price = self.get_topper(user_choice)
        self.__add__(unit_price)
        if answer == "Yes":
            self.cake_prices.update({user_choice: unit_price})
            print(f"You have added a {menu_topping[int(number)-1]} topper.")
            print(f"Your total is ${CakeDelivery.total_cost:.2f}.")
        elif answer == "Cancel":
            print("You have removed the last item.\n")
            self.cake_stack.remove_item()
            self.__sub__(unit_price)
            self.topping()
        else:
            self.clear_all(finalize)
            
    def order_summary(self):
        # Create a Table
        while not self.cake_stack.has_no_items():
            popped = self.cake_stack.remove_item()
            self.cake_layer.append(popped)
        for layer, qty in Counter(self.cake_layer).items():
            cost = self.cake_prices.get(layer)
            self.entry.append([layer, qty, f"${cost:.2f}"])
        self.receipt()

    def receipt(self):
        title = ["Layer", "Qty", "Price"]
        data = [["Total Cost:", f"${CakeDelivery.total_cost:.2f}"]]
        ask_user = input("\nWould you like a receipt? (Yes/No) ").title()
        if ask_user == "Yes":
            print("\n" + table(self.entry, headers=title, tablefmt="fancy_grid"))
            print(table(data, tablefmt="fancy_grid"))
            print("\nThanks for stopping by. Try one of our other options!")
        elif ask_user == "No":
            print("Thanks for your purchase. Come back anytime!")
            print("\n==============")
            sys.exit()
        else:
            print("Invalid Input: Cannot print the receipt.")
            self.receipt()

    def clear_all(self, user_input):
        if user_input == "Clear":
            print("Your order has been cleared.")
            self.cake_stack.cancel_order()
            CakeDelivery.total_cost = 2.50
            print("\n==============")
            sys.exit()


CakeDelivery()
