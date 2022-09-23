menu_flavor = ("Vanilla", "Chocolate", "Strawberry", "Lemon Citron", "Red Velvet", "Ice Cream", "Cheese")
menu_frosting = ("Fondant", "Buttercream", "Ganache", "Cream Cheese", "Matcha", "Coffee", "Whipped Cream")
menu_topping = ("Happy B-Day", "Candles", "Coconut Flakes", "Red Roses", "Cherries", "Sprinkles", "Mixed Fruits")


class Pricing:
    all_layers = {}

    def __init__(self):
        self.flavor_price = {"Vanilla": 3.20, "Chocolate": 3.45, "Strawberry": 3.75, "Lemon Citron": 3.90,
                             "Red Velvet": 4.10, "Ice Cream": 4.30, "Cheese": 4.00}
        self.frosting_price = {"Fondant": 0.95, "Buttercream": 1.00, "Ganache": 0.85, "Cream Cheese": 0.80,
                               "Matcha": 0.75, "Coffee": 0.90, "Whipped Cream": 0.70}
        self.topping_price = {"Happy B-Day": 1.90, "Candles": 1.75, "Coconut Flakes": 1.80, "Red Roses": 2.00,
                              "Cherries": 1.70, "Sprinkles": 1.65, "Mixed Fruits": 2.00}

    def get_layer(self, selection):
        return self.flavor_price[selection]

    def get_icing(self, selection):
        return self.frosting_price[selection]

    def get_topper(self, selection):
        return self.topping_price[selection]

    @classmethod
    def show_layers(cls):
        print('''
1. Vanilla          $3.20
2. Chocolate        $3.45
3. Strawberry       $3.75
4. Lemon Citron     $3.90
5. Red Velvet       $4.10
6. Ice Cream        $4.30
7. Cheese           $4.00
                ''')

    @classmethod
    def show_icing(cls):
        print('''
1. Fondant          $0.95
2. Buttercream      $1.00
3. Ganache          $0.85
4. Cream Cheese     $0.80
5. Matcha           $0.75
6. Coffee           $0.90
7. Whipped Cream    $0.70
                ''')

    @classmethod
    def show_toppers(cls):
        print('''
1. Happy B-Day      $1.90
2. Candles          $1.75
3. Coconut Flakes   $1.80
4. Red Roses        $2.00
5. Cherries         $1.70
6. Sprinkles        $1.65
7. Mixed Fruits     $2.00
                ''')


class Cake:
    input_values = ["1", "2", "3", "4", "5", "6", "7"]
    check_again = ["Yes", "Cancel", "Clear"]

    def __init__(self, value):
        self.value = value
        self.next = None


class OrderCake:
    def __init__(self):
        self.cake = []
        self.top_layer = None
        self.items = 0

    def __str__(self):
        self.cake.reverse()
        layers = [str(item) for item in self.cake]
        return "\n".join(layers)

    def has_no_items(self):
        if not self.cake:
            return True
        else:
            return False

    def display_order(self):
        current_item = self.top_layer
        while current_item:
            print(current_item.value)
            current_item = current_item.next

    def add_item(self, layer):
        if self.cake.__len__() > 7:
            print("The cake will fall over if another layer is added!")
            return
        self.cake.append(layer)
        new_item = Cake(layer)
        if self.items == 0:
            self.top_layer = new_item
        else:
            new_item.next = self.top_layer
            self.top_layer = new_item
        self.items += 1

    def remove_item(self):
        if self.has_no_items():
            print("There are no items on the cake board.")
            return None
        current = self.top_layer
        self.top_layer = self.top_layer.next
        current.next = None
        self.items -= 1
        self.cake.pop()
        return current.value

    def cancel_order(self):
        self.cake.clear()
        self.items = 0


class BakeryLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cake_node = self.head
        while cake_node:
            yield cake_node
            cake_node = cake_node.next

    def menu_append(self, item):
        cake_node = Cake(item)
        if self.head is None:
            self.head = cake_node
            self.tail = cake_node
        else:
            self.tail.next = cake_node
            self.tail = cake_node
            return True

    # For Testing Only
    def traverse_ll(self):
        if self.head is None:
            print("The menu is currently empty.")
        else:
            cake_node = self.head
            while cake_node:
                print(cake_node.value)
                cake_node = cake_node.next

    def search_ll(self, selection):
        if self.head is None:
            return "The menu is currently empty."
        else:
            cake_node = self.head
            while cake_node is not None:
                if cake_node.value in selection:
                    return cake_node.value
                cake_node = cake_node.next
            return "The item you selected does not exist."


def custom_cake(options, menu_list):
    for item in menu_list:
        options.menu_append(item)


menu1 = BakeryLL()
custom_cake(menu1, menu_flavor)
menu2 = BakeryLL()
custom_cake(menu2, menu_frosting)
menu3 = BakeryLL()
custom_cake(menu3, menu_topping)
