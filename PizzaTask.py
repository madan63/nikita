class Pizza:
    def __init__(self):
        size = 's'
        cheese = 0
        pepper = 0
        mushroom = 0
        self.size = input('S) Small\nM) Medium\nL) Large\nChoose Pizza size: ')
        self.cheese = input('Enter the number of cheese toppings: ')
        self.pepper = input('Enter the number of pepperoni toppings: ') 
        self.mushroom = input('Enter the number of mushroom toppings: ')

    def get(self, access):
        sizes = {'s':'Small', 'm':'Medium', 'l':'Large'} 
        if access == 'size':
            return getattr(self, sizes.get(access, 'Unknown'))

        if access in self.__dict__.keys():
            return getattr(self, access)

        else:
            print('Oops your access in unknown')
            return 'your access should be among %s'% ','.join(self.__dict__.keys())

    def modify(self):
        access = input('S) Size\nC) Cheese\nP) Pepper \nM) Mushroom')
        if access == 'S':
            self.size

k = Pizza()

print(k.get('cheese'))

print(k.get('madan'))
