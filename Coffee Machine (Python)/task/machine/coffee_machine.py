class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing action"

    def process_input(self, user_input):
        if self.state == "choosing action":
            self.choose_action(user_input)
        elif self.state == "choosing coffee type":
            self.choose_coffee_type(user_input)
        elif self.state == "filling water":
            self.water += int(user_input)
            self.state = "filling milk"
        elif self.state == "filling milk":
            self.milk += int(user_input)
            self.state = "filling beans"
        elif self.state == "filling beans":
            self.beans += int(user_input)
            self.state = "filling cups"
        elif self.state == "filling cups":
            self.cups += int(user_input)
            self.state = "choosing action"

    def choose_action(self, action):
        if action == "buy":
            self.state = "choosing coffee type"
        elif action == "fill":
            self.state = "filling water"
        elif action == "take":
            print(f"I gave you ${self.money}")
            self.money = 0
        elif action == "remaining":
            self.display_remaining()
        elif action == "exit":
            self.state = "exit"

    def choose_coffee_type(self, coffee_type):
        if coffee_type == "1":  # espresso
            self.make_coffee(250, 0, 16, 4)
        elif coffee_type == "2":  # latte
            self.make_coffee(350, 75, 20, 7)
        elif coffee_type == "3":  # cappuccino
            self.make_coffee(200, 100, 12, 6)
        elif coffee_type == "back":
            self.state = "choosing action"

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.beans < beans_needed:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost
        self.state = "choosing action"

    def display_remaining(self):
        print(f"The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} g of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money")

# Simulating interaction
coffee_machine = CoffeeMachine()
while coffee_machine.state != "exit":
    if coffee_machine.state == "choosing action":
        user_input = input("Write action (buy, fill, take, remaining, exit): ")
    elif coffee_machine.state == "choosing coffee type":
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    elif coffee_machine.state == "filling water":
        user_input = input("Write how many ml of water you want to add: ")
    elif coffee_machine.state == "filling milk":
        user_input = input("Write how many ml of milk you want to add: ")
    elif coffee_machine.state == "filling beans":
        user_input = input("Write how many grams of coffee beans you want to add: ")
    elif coffee_machine.state == "filling cups":
        user_input = input("Write how many disposable cups you want to add: ")
    coffee_machine.process_input(user_input)