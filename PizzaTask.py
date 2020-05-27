def highestPrice():
    orders = DeluxePizza.order_details
    if any(orders):
        max_cost = max([order['cost'] for order in orders])
        for order in orders:
            sizes = {'s':'Small', 'm':'Medium', 'l':'Large'}
            if order['cost'] == max_cost:
                oid = order['order_ID']
                size = sizes[order['size']]
                cheese = order['cheese']
                pep = order['pepper']
                mush = order['mushroom']
                cost = order['cost']
                yn = 'Yes' if order['stuffedcheese'] else 'No'
                veg = order['veg']

                string = f'''Order ID# : {oid}
Pizza size: {size}
Cheese filled dough: {yn}
Number of cheese toppings: {cheese}
Number of pepperoni toppings: {pep}
Number of mushroom toppings: {mush}
Number of vegetable toppings: {veg}

Price: $ {cost}\n'''
                print(string)
                print('----------------')
        
    else:
        print('Oops! no orders so far')


def lowestPrice():
    orders = DeluxePizza.order_details
    if any(orders):
        min_cost = min([order['cost'] for order in orders])
        for order in orders:
            sizes = {'s':'Small', 'm':'Medium', 'l':'Large'}
            if order['cost'] == min_cost:
                oid = order['order_ID']
                size = sizes[order['size']]
                cheese = order['cheese']
                pep = order['pepper']
                mush = order['mushroom']
                cost = order['cost']
                yn = 'Yes' if order['stuffedcheese'] else 'No'
                veg = order['veg']

                string = f'''Order ID# : {oid}
Pizza size: {size}
Cheese filled dough: {yn}
Number of cheese toppings: {cheese}
Number of pepperoni toppings: {pep}
Number of mushroom toppings: {mush}
Number of vegetable toppings: {veg}

Price: $ {cost}\n\n'''
                print(string)
                print('----------------')
        
    else:
        print('Oops! no orders so far')

def cheaperThan(price):
    orders = DeluxePizza.order_details

    if any(orders):
        min_costs = [order['cost'] for order in orders if order['cost'] < price]
        if any(min_costs):
            print(f'List of pizzas sold today below the price ${price}')
            for order in orders:
                sizes = {'s':'Small', 'm':'Medium', 'l':'Large'}
                if order['cost'] in min_costs:
                    oid = order['order_ID']
                    size = sizes[order['size']]
                    cheese = order['cheese']
                    pep = order['pepper']
                    mush = order['mushroom']
                    cost = order['cost']
                    yn = 'Yes' if order['stuffedcheese'] else 'No'
                    veg = order['veg']

                    string = f'''Order ID# : {oid}
    Pizza size: {size}
    Cheese filled dough: {yn}
    Number of cheese toppings: {cheese}
    Number of pepperoni toppings: {pep}
    Number of mushroom toppings: {mush}
    Number of vegetable toppings: {veg}\n'''
                    print(string)
                    print('----------------')
                else:
                    pass
        else:
            print(f'No orders been places lessthan ${price}')
        
    else:
        print('Oops! no orders so far')

def pizzasOfSize(size):
    orders = DeluxePizza.order_details
    count = 0
    sizes = {'s': 'Small', 'm': 'Medium', 'l': 'Large'}
    for order in orders:
        
        if order['size'] == size:
            print('List of {size} size pizzas sold today:\n'.format(size=sizes[size]))
            count += 1
            yn = 'Yes' if order['stuffedcheese'] else 'No'
            {'order_ID': 1, 'size': 's', 'cheese': '5', 'pepper': '4', 'mushroom': '3', 'stuffedcheese': False, 'veg': '3'}
            string = '''Order ID# : {oid} 
Pizza size: {size}
Cheese filled dough: {yn}
Number of cheese toppings: {cheese}
Number of pepperoni toppings: {pep}
Number of mushroom toppings: {mush}
Number of vegetable toppings: {veg}\n'''.format(oid = order['order_ID'], size=sizes[size], yn=yn, cheese=order['cheese'],
                                              pep=order['pepper'], mush=order['mushroom'], veg=order['veg'])
            print(string)

        else:
            pass
    print('\nOur Chef, made {count} "{size}" sized pizzas today!'.format(count=count, size=sizes[size]))


class Pizza:
    def __init__(self):
        size = 's'
        self.size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
        self.cheese = input('Enter the number of cheese toppings: ')
        self.pepper = input('Enter the number of pepperoni toppings: ')
        self.mushroom = input('Enter the number of mushroom toppings: ')

    def get(self, access):
        sizes = {'s': 'Small', 'm': 'Medium', 'l': 'Large'}
        if access == 'size':
            return sizes.get(self.size, 'unknown')

        if access in self.__dict__.keys():
            return getattr(self, access)

        else:
            print('Oops your access in unknown')
            return 'your access should be among %s' % ','.join(self.__dict__.keys())

    def modify(self):
        access = input('S) Size\nC) Cheese\nP) Pepper \nM) Mushroom\nPlease select: ')
        if access.upper() == 'S':
            size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
            setattr(self, 'size', size)
            return 'changes been noted'

        elif access.lower() in 'cpm':
            di = {'c': 'cheese', 'p': 'pepper', 'm': 'mushroom'}
            tops = int(input('Enter number of {acc} toppings: '.format(acc=di[access])))
            setattr(self, di[access.lower()], tops)
            return 'changes been noted'

        else:
            print('Invalid selection')

    def calcCost(self):
        price = {'S': 10, 'M': 12, 'L': 14}
        size = self.size.upper()
        amt = price[size]
        print(self.cheese, self.pepper, self.mushroom)
        ctop = int(self.cheese) * 2 if self.cheese.isdigit() else 0
        print(f'Cheese toppings : ${ctop}')
        ptop = int(self.pepper) * 2 if self.pepper.isdigit() else 0
        print(f'Pepperoni toppings : ${ptop}')
        mtop = int(self.mushroom) * 2 if self.mushroom.isdigit() else 0
        print(f'Mushroom toppings : ${mtop}')

        totalcost = amt + ctop + mtop + ptop
        return 'total cost : ${tc}'.format(tc=totalcost)



class DeluxePizza:
    total_pizza = 0
    order_details = []
    orderId = 1
    def __init__(self):
        curOrder = {}
        size = 's'
        self.size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
        self.cheese = input('Enter the number of cheese toppings: ')
        self.pepper = input('Enter the number of pepperoni toppings: ')
        self.mushroom = input('Enter the number of mushroom toppings: ')
        swc = input('Would you like to have stuffed with cheese (Y/N): ').upper()
        self.stuffed_cheese = True if swc == 'Y' else False
        self.veg = input('Enter the number of veggie toppings: ')
        DeluxePizza.total_pizza += 1

        curOrder['order_ID'] = DeluxePizza.orderId
        curOrder['size'] = self.size
        curOrder['cheese'] = self.cheese
        curOrder['pepper'] = self.pepper
        curOrder['mushroom'] = self.mushroom
        curOrder['stuffedcheese'] = self.stuffed_cheese
        curOrder['veg'] = self.veg

        cost = self.calc_cost()
        curOrder['cost'] = cost

        DeluxePizza.order_details.append(curOrder) 
        DeluxePizza.orderId += 1

        

    @classmethod
    def numberOfPizzas(cls):
        count = DeluxePizza.total_pizza
        print(f'The total number of pizzas: {count}')
        

    def get(self, access):
        sizes = {'s': 'Small', 'm': 'Medium', 'l': 'Large'}
        if access == 'size':
            return sizes.get(self.size, 'unknown')

        if access in self.__dict__.keys():
            return getattr(self, access)

        else:
            print('Oops your access in unknown')
            return 'your access should be among %s' % ','.join(self.__dict__.keys())

    def modify(self):
        access = input('''S) Size\nC) Cheese\nP) Pepper \nM) Mushroom\nX) Stuffed with Cheese \nV) Veggie Toppings\n 
Please select: ''')
        if access.upper() == 'S':
            size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
            setattr(self, 'size', size)
            return 'changes been noted'

        elif access.lower() in 'cpmxv':
            di = {'c': 'cheese', 'p': 'pepper', 'm': 'mushroom', 'x': 'Stuffed with Cheese', 'v': 'Veggie Toppings'}
            tops = int(input('Enter number of {acc} toppings: '.format(acc=di[access])))
            setattr(self, di[access.lower()], tops)
            return 'changes been noted'

        else:
            print('Invalid selection')

    def calc_cost(self):
        price = { 'S': 2, 'M': 4, 'L': 6}
        size = self.size.upper()
        amt = price[size]

        vtop = int(self.veg) * 3 if self.veg.isdigit() else 0
        #print(f'Veg toppings : ${vtop}')
        ctop = int(self.cheese) * 2 if self.cheese.isdigit() else 0
        #print(f'Cheese toppings : ${ctop}')
        ptop = int(self.pepper) * 2 if self.pepper.isdigit() else 0
        #print(f'Pepperoni toppings : ${ptop}')
        mtop = int(self.mushroom) * 2 if self.mushroom.isdigit() else 0
        #print(f'Mushroom toppings : ${mtop}')

        totalcost = amt + ctop + vtop + ptop + mtop
        #print('total cost : ${tc}'.format(tc=totalcost))

        return totalcost

    def __str__(self):
        yn = 'Yes' if self.stuffed_cheese else 'No'
        string = '''Pizza size: {size}
Cheese filled dough: {yn}
Number of cheese toppings: {cheese}
Number of pepperoni toppings: {pep}
Number of mushroom toppings: {mush}
Number of vegetable toppings: {veg}'''.format(size=self.size, yn=yn, cheese=self.cheese,
                                              pep=self.pepper, mush=self.mushroom, veg=self.veg) 

        return string
        



flag = True
password = 'deluxepizza'
orderId = 1
while flag:
    print('--------- Main Menu ---------') 
    print('''Papa John, what do you want to do?
1.    Enter a new pizza order (password required)
2.    Change information of a specific order (password required)
3.    Display details for all pizzas of a specific size (s/m/l)
4.    Statistics on today’s pizzas
5.    Quit
''')
    choice = int(input('Please enter your choice > '))
    if choice == 1:
        atmpt = 0
        while atmpt <3:
            pas = input('password: ')
            if pas == password:
                atmpt =4
                obj = DeluxePizza()
                
            else:
                print('Incorrect password')
                atmpt +=1
        else:
            pass
    
    elif choice == 2:
        atmpt = 0
        while atmpt <3:
            pas = input('password: ')
            if pas == password:
                orders = DeluxePizza.order_details
                if any(orders):
                    atmpt = 4
                    pznum = int(input('Enter Pizza number to update: '))
                    pznums = [order['order_ID'] for order in orders]

                    if pznum in pznums:
                        for order in orders:
                            if order['order_ID'] == pznum:
                                sizes = {'s':'Small', 'm':'Medium', 'l':'Large'}            
                                oid = order['order_ID']
                                size = sizes[order['size']]
                                cheese = order['cheese']
                                pep = order['pepper']
                                mush = order['mushroom']
                                cost = order['cost']
                                yn = 'Yes' if order['stuffedcheese'] else 'No'
                                veg = order['veg']

                                string = f'''Order ID# : {oid}              
    Pizza size: {size}
    Cheese filled dough: {yn}
    Number of cheese toppings: {cheese}
    Number of pepperoni toppings: {pep}
    Number of mushroom toppings: {mush}
    Number of vegetable toppings: {veg}

    Price: $ {cost}\n\n'''
                                print(string)
                                print('----------------')

                                intflag = True

                                while intflag:
                                    print('''Papa John, what would you like to change?
1.	Size
2.	Cheese filled or not
3.	Number of cheese toppings
4.	Number of pepperoni toppings
5.	Number of mushroom toppings
6.	Number of vegetable toppings
7.      Quit''')
                                    cho = int(input('Enter choice > '))

                                    if cho == 1:
                                        nsiz = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
                                        order['size'] = nsiz

                                    elif cho == 2:
                                        fche = input('Cheese filled or not(Y/N): ')
                                        if fche.lower() in ['y','n']:
                                            
                                            order['stuffedcheese'] = fche
                                        else:
                                            print('wrong choice')
                                    elif cho == 3:
                                        nche = int(input('number of cheese toppings: '))
                                        order['cheese'] =nche
                                    elif cho == 4:
                                        npep = int(input('number of pepperoni toppings: '))
                                        order['pepper'] = npep
                                    elif cho == 5:
                                        nmush = int(input('number of mushrooms: '))
                                        order['mushroom'] = nmush

                                    elif cho == 6:
                                        nveg = int(input('number of vegetable toppings: '))
                                        order['veg'] = nveg
                                    elif cho == 7:
                                        con = input('Are you sure to exit(Y/N): ')
                                        if con.lower() == 'y':
                                            intflag = False
                                        else:
                                            pass
                                    else:
                                        print('wrong choice')


                        else:
                            pass
                        
                    else:
                        print(f'No Deluxe pizza found with the order ID {pznum}')
                        
                else:
                    print('Oops! no order places so far')
            
            else:
                print('Incorrect password')
                atmpt +=1
        else:
            pass
        
    elif choice == 3:
        size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
        if size.lower() in 'sml':        
            pizzasOfSize(size.lower())
        else:
            print('invalid choice')

    elif choice == 4:
        flag4 = True
        while flag4:
            print('''Papa John, what information would you like?
    1.    Cost and details of cheapest pizza
    2.    Cost and details of most costly pizza
    3.    Number of pizzas sold today
    4.    Number of pizzas of a specific size
    5.    Average cost of pizzas
    6.    Quit''')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                lowestPrice()
                
            elif choice == 2:
                highestPrice()
                
            elif choice == 3:
                pizzas = DeluxePizza.total_pizza
                print(f'Our chef made total {pizzas} pizzas today') 
                
            elif choice == 4:
                size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
                if size.lower() in 'sml':        
                    pizzasOfSize(size.lower())
                else:
                    print('invalid choice')
                
            elif choice == 5:
                orders = DeluxePizza.order_details
                if any(orders):
                    avg_cost = round(sum([order['cost'] for order in orders]) / len(orders), 3)
                    print('The average cost of Pizza is: ${avgcost}'.format(avgcost=avg_cost)) 
                else:
                    print('No orders so far')
            elif choice == 6:
                con = input('Are you sure to quit (Y/N) : ')
                if con.upper() == 'Y':
                    flag4 = False
                else:
                    pass
            else:
                print('invalid choice')
                
    elif choice == 5:
        con = input('Are you sure to quit(Y/N): ')
        if con.upper() == 'Y':
            print('Thanks for visiting')
            flag = False
        else:
            pass
    else:
        print('Invalid option')



