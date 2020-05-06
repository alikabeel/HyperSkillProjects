money = 550
water = 400
milk = 540
coffee = 120
cups = 9

def buy():
    global money,water,milk,coffee,cups
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    choice = int(input())
    if choice == 1:
      money+= 4
      coffee-= 16
      water-=250
    elif choice == 2:
        money+= 7
        coffee-= 20
        water-=350
        milk-= 75
    else:
        money+= 6
        coffee-= 12
        water-= 200
        milk-= 100
    cups-=1

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
    print(str(money) + " of money")
    
print('Write action (buy, fill, take):')
printer()
choice =  input()
if choice == 'buy':
    buy()
elif choice == 'fill':
    fill()
else:
    take()
printer()