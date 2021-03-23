class Machine:
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.working = True

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def espresso(self):
        if self.water - 250 >= 0 and self.beans - 16 >= 0 and self.cups - 1 >= 0:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.cups -= 1
        elif self.water - 250 < 0:
            print('Sorry, not enough water!')

    def latte(self):
        if self.water - 350 >= 0 and self.beans - 20 >= 0 and self.cups - 1 >= 0 and self.milk - 75 >= 0:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.cups -= 1
        elif self.water - 350 < 0:
            print('Sorry, not enough water!')

    def cappuccino(self):
        if self.water - 200 >= 0 and self.beans - 12 >= 0 and self.cups - 1 >= 0 and self.milk - 100 >= 0:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.cups -= 1
        elif self.water - 200 < 0:
            print('Sorry, not enough water!')

    def action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        solution = input()
        if solution == 'buy':
            Machine.buy(self)
        elif solution == 'fill':
            Machine.fill(self)
        elif solution == 'remaining':
            Machine.remaining(self)
        elif solution == 'exit':
            Machine.working = False
        else:
            Machine.take(self)

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choice = input()
        if choice == '1':
            Machine.espresso(self)
        elif choice == '2':
            Machine.latte(self)
        elif choice == 'back':
            Machine.action(self)
        else:
            Machine.cappuccino(self)

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


coffee_inst = Machine()

while coffee_inst.working:
    coffee_inst.action()
