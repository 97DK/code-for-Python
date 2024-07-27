sandwich_orders=['liulian_sandwich','pastrami','pastrami','pastrami','turkey_sandwich','typical_sandwich','pastrami']
print('pastrami was sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)