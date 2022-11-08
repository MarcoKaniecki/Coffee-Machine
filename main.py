class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550
        self.action = None
        self.coffee_type = None
        self.am_available = []
        self.min_index = None
        self.inventory_status = None

    def actions(self):
        while True:
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")

            if self.action == 'buy':
                self.buy_coffee()
            elif self.action == 'fill':
                self.fill_machine()
            elif self.action == 'take':
                self.take_machine_money()
            elif self.action == 'remaining':
                self.display_amount()
            elif self.action == 'exit':
                exit()
            else:
                return

    def display_amount(self):
        print("\nThe coffee machine has:")
        print("{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money\n".format(self.water,
                                                                                                          self.milk,
                                                                                                          self.beans,
                                                                                                          self.cups,
                                                                                                          self.cash))

    def buy_coffee(self):
        self.coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to "
                                 "main menu:\n")

        if self.coffee_type == "back":
            print()
            return

        self.inventory_status = None  # reset
        self.check_inventory()  # checks if there are enough resources to make it

        if self.inventory_status != "refill needed":
            print("I have enough resources, making you a coffee!\n")
            self.cups -= 1

            if self.coffee_type == '1':  # espresso
                self.water -= 250
                self.beans -= 16
                self.cash += 4
            elif self.coffee_type == '2':  # latte
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cash += 7
            elif self.coffee_type == '3':  # cappuccino
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cash += 6

    def check_inventory(self):
        self.am_available = []
        # computes how often the required resources for a coffee type fit into the requirements for it
        if self.coffee_type == '1':
            self.am_available = [self.water // 250, 999999, self.beans // 16, self.cups // 1]
        elif self.coffee_type == '2':
            self.am_available = [self.water // 350, self.milk // 75, self.beans // 20, self.cups // 1]
        elif self.coffee_type == '3':
            self.am_available = [self.water // 200, self.milk // 100, self.beans // 12, self.cups // 1]

        # if there is any 0 in amount available then there is not enough to make coffee
        if min(self.am_available) == 0:
            self.locate_lacking_resource()

    def locate_lacking_resource(self):
        self.inventory_status = "refill needed"
        self.min_index = self.am_available.index(min(self.am_available))

        print("Sorry, not enough ", end="")
        if self.min_index == 0:
            print("water!")
        elif self.min_index == 1:
            print("milk!")
        elif self.min_index == 2:
            print("coffee beans!")
        elif self.min_index == 3:
            print("disposable cups!")
        print()

    def fill_machine(self):
        self.water += int(input("\nWrite how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:\n"))
        print()

    def take_machine_money(self):
        print(f"\nI gave you ${self.cash}\n")
        self.cash = 0


if __name__ == "__main__":
    user = CoffeeMachine()
    user.actions()
