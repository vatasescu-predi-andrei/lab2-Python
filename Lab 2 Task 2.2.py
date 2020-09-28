#TASK 2.2
price=float(input("price of the item: £"))
vat= 0.2
vat_price=float(price*vat)
print("Vat that will be added to your price is", vat_price)
total_price = float(price+vat_price)
print("Item price inc VAT:", total_price)
