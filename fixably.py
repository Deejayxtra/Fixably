import time
from fixably_utility import *
import json


print("Obtaining Token...")
token = getFixablyToken(34962787)
time.sleep(2)
print("Done!\n")


print("Obtaining Orders...")
orders = getFixablyOrders(token)
print("Done!\n")

while True:
    choice = int(input('''\nWhat action would you like to perform:
    1. Print token
    2. Get statistics of orders
    3. Print iPhones assigned to a technician
    Press any other key to terminate the program: '''))

    if choice == 1:
        print(token)
    elif choice == 2:
        order_stats = getFixablyOrderStats(token, orders)
        print(f"\nOut of {len(orders)} orders: ")
        for stat in order_stats:
            print(f"{stat[1]} orders are {stat[0]}")
    elif choice == 3:
        iPhoneAndAssigned = getIPhoneAndAssigned(orders)
        print(json.dumps(iPhoneAndAssigned, sort_keys=False, indent=4))
    else:
        break