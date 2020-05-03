print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
coffee = int(input())
print('Write how many cups of coffee you will need:')
cups = int(input())
N = int(min(water // 200,milk // 50,coffee // 15))
if N == cups:
    print('Yes, I can make that amount of coffee')
elif N > cups:
    print('Yes, I can make that amount of coffee (and even ' + str((N-cups)) + 'more than that)')
else:
    print('No, I can make only ' + str(N) + 'cups of coffee')