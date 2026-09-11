"""
Module: script_02.py
Description: Demonstrates if-elif-else in python.
"""

price = int(input("Enter Price:"))

if(price < 1000):
    discount = price * 0.05 # 5% Discount
    print("Discount:", discount)
elif(price < 5000):
    discount = price * 0.10 # 10% Discount
    print("Discount:", discount)
else:
    discount = price * 0.15 # 15% Discount
    print("Discount:", discount)

netpay = price - discount
print("Net Payable:", netpay)
