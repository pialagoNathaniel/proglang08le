# Pialago, Nathaniel Christian M.  BSCS601

def add_to_stock(stock_list):
    inventory.append(75)
    print("Inside function (stock): ", inventory)

inventory = [100, 200, 150]
add_to_stock(inventory)

print("Outside function (stock): ", inventory)

def update_price(price):
    new_price = price + (price * 0.10)
    print("Inside function (price): ", new_price)

base_price = 250.0
update_price(base_price)

print("Outside function (price): ", base_price)
