from modelle.order import Order

dish1 = {'pui':13, 'porc':18}
drink1 = {'cola':7, 'sprite':8}

order = Order('order1', 'daius', dish1, drink1)

order.calculate_prices()
print(order.total_price)

print(order.print_receipt())
