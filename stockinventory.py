stock = {'oranges':5, 'pineapples':2, 'pears':0}
alreadyAte = ['Nabeel']

def menu():
    print("Press 1: To add stock. ")
    print("Press 2: To check stock. ")
    print("Press 3: To enter purchase. ")
    print("Press Q: To quit the program. ")
    return input("What would you like to do? ")

run = menu()

while True:
    if run == '1':
        addStock = input('Food to be added to stock? ')
        amount = int(input('Quantity of food to be added to stock?'))
        stock[addStock] = amount
        run = menu()

    elif run == '2':
        for key, value in stock.items():
            print("{}: {}". format(key,value))
        run = menu()

    elif run == '3':
        food = input('What food was eaten?')
        person = input('Who ate the food?')
        if food in stock:
            if person in alreadyAte:
                print('{} was sent to the brig'. format(person))
                run = menu()
            else:
                if stock[food] > 0:
                    stock[food] -= 1
                    alreadyAte.append(person)
                    print("{} ate {}".format(person,food))
                    run = menu()
                else:
                    print('{} did not eat because we are out of {}'.format(person,food))
                    run = menu()
        else:
            print('{} are out of stock'.format(food))
            run = menu()

    elif run == 'q':
        break

print("The program has ended")