class Check():
    def __init__(self, tax, total_tax):
        self.tax = tax
        self.total_tax = total_tax
        self.check = {}

    def add_item(self, product, quantity):
        tax_position = round((product.price * quantity) * (self.tax / 100), 2)
        self.check[product] = [product.price, quantity, tax_position]

    def count(self):
        sum_p = 0
        sum_tax = 0
        max_tax = 0
        max_tax_item = None
        for item in self.check:
            if max_tax < self.check[item][2]:
                max_tax_item = item
                max_tax = self.check[item][2]
            sum_p += self.check[item][0] * self.check[item][1]
            sum_tax += self.check[item][2]
        delta = self.total_tax - sum_tax
        print('position for delta: ',max_tax_item.name, self.check[max_tax_item])
        self.check[max_tax_item][2] += delta
        print('Total sum: %0.2f, sum tax: %0.2f, delta %0.2f' % (sum_p, sum_tax, delta))

    def print_check(self):
        print('name price quantity tax')
        for item in self.check:
            res = item.name + '   ' + str(self.check[item])
            print(res)


class Items():
    def __init__(self, name, price):
        self.name = name
        self.price = price

# add items
item1 = Items('1', 397.01)
item2 = Items('2', 435.00)
item3 = Items('3', 435.00)
item4 = Items('4', 443.33)
item5 = Items('5', 443.33)
item6 = Items('6', 370.00)
item7 = Items('7', 630.00)
item8 = Items('8', 630.00)
item9 = Items('9', 630.00)

sum_tax = 1434.07
#create check
check1 = Check(20, sum_tax) # tax 20%

#add items in check
check1.add_item(item1, 1)
check1.add_item(item2, 2)
check1.add_item(item3, 2)
check1.add_item(item4, 2)
check1.add_item(item5, 2)
check1.add_item(item6, 2)
check1.add_item(item7, 1)
check1.add_item(item8, 1)
check1.add_item(item9, 2)

check1.count()

check1.print_check()