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


# k = Pizza()
# print(k.get("size"))

# print(k.get("cheese"))
# print(k.get("vikash"))


class DeluxePizza:
    total_pizza = 0

    def __init__(self):
        size = 's'
        self.size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
        self.cheese = input('Enter the number of cheese toppings: ')
        self.pepper = input('Enter the number of pepperoni toppings: ')
        self.mushroom = input('Enter the number of mushroom toppings: ')
        swc = input('Would you like to have stuffed with cheese (Y/N): ').upper()
        self.stuffed_cheese = True if swc == 'Y' else False
        self.veg = input('Enter the number of veggie toppings: ')
        DeluxePizza.total_pizza += 1

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
        # print(self.cheese, self.pepper, self.mushroom)
        vtop = int(self.veg) * 3 if self.veg.isdigit() else 0
        print(f'Veg toppings : ${vtop}')
        ctop = int(self.cheese) * 2 if self.cheese.isdigit() else 0
        print(f'Cheese toppings : ${ctop}')
        ptop = int(self.pepper) * 2 if self.pepper.isdigit() else 0
        print(f'Pepperoni toppings : ${ptop}')
        mtop = int(self.mushroom) * 2 if self.mushroom.isdigit() else 0
        print(f'Mushroom toppings : ${mtop}')

        totalcost = amt + vtop
        return 'total cost : ${tc}'.format(tc=totalcost)

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
        


l = DeluxePizza()


# class Demo:
#     pass

# testing

flag = True
password = 'deluxepizza'
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
                print('success')
            
            else:
                print('Incorrect password')
                atmpt +=1
        else:
            pass
    
    elif choice == 3:
        atmpt = 0
        while atmpt <3:
            pas = input('password: ')
            if pas == password:
                atmpt =4
                print('success')
            
            else:
                print('Incorrect password')
                atmpt +=1
        else:
            pass
    elif choice == 3:
        #dispaly the details of all pizzas
        pass
    elif choice == 4:
        flag4 = True
        while flag:
            print('''Papa John, what information would you like?
    1.    Cost and details of cheapest pizza
    2.    Cost and details of most costly pizza
    3.    Number of pizzas sold today
    4.    Number of pizzas of a specific size
    5.    Average cost of pizzas
    6.    Quit''')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                print('Cost and details of cheapest pizza')
                
            elif choice == 2:
                print('cost and details of most costly pizza')
                
            elif choice == 3:
                print('number of pizza sold today')
                
            elif choice == 4:
                print('number of pizzas of a specific size')
                
            elif choice == 5:
                print('average cost of pizzas')
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



