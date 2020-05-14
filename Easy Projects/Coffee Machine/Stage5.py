money = 550
water = 400
milk = 540
coffee = 120
cups = 9

def buy():
    global money,water,milk,coffee,cups
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    choice = input()
    if choice == 'back':
        return
    choice = int(choice)
    if cups < 1:
        print("Not enough Cups")
        return
    
    if choice == 1:
        if coffee < 16:
            print("Not enough Coffee")
            return
        if water <250:
            print("Not Enough Water")
            return
        money+= 4
        water-=250
        coffee-= 16

    elif choice == 2:
        if coffee < 20:
            print("Not Enough Coffee")
            return
        if water < 350:    
            print("Not Enough Water")
            return
        if milk < 75:
            print("Not Enough Milk")
            return
        coffee-= 20
        milk-= 75
        water-=350
        money+= 7
    else:
        if coffee < 12:
            print("Not Enough Coffee")
            return
        if water < 200:    
            print("Not Enough Water")
            return
        if milk < 100:
            print("Not Enough Milk")
            return
        money+= 6
        milk-= 100
        water-=200
        coffee-= 12
    cups-=1
    print('I have enough resources, making you a coffee!')


def fill():
    global money,water,milk,coffee,cups
    print('Write how many ml of water do you want to add:')
    water+= int(input())
    print('Write how many ml of milk do you want to add:')
    milk+= int(input())
    print('Write how many grams of coffee beans do you want to add:')
    coffee+= int(input())
    print('Write how many disposable cups of coffee do you want to add:')    
    cups+= int(input())
def take():
    global money
    print('I gave you ' + str(money))
    money = 0
def printer():
    global money,water,milk,coffee,cups
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print("$"+str(money) + " of money")
choice = 'x'
while(choice != 'exit'):
    print('Write action (buy, fill, take, remaining, exit):')
    choice = input()
    if choice == 'buy':
        buy()
    elif choice == 'fill':
        fill()
    elif choice == 'remaining':
        printer()
    elif choice == 'take':
        take()
    