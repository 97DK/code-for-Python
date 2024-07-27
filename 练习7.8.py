sandwich_orders=['liulian_sandwich','turkey_sandwich','typical_sandwich']
finished_sandwiches=[]
while sandwich_orders:
    print(f"I made your {sandwich_orders[-1]}.")
    a=sandwich_orders.pop()
    finished_sandwiches.append(a)
print(finished_sandwiches)