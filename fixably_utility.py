
import requests
import sys


def getFixablyToken(code):
    try:
        response = requests.post('https://careers-api.fixably.com/token', data={"Code" : f"{code}"}) 
        token = response.json()['token']
    except:
        print("Unable to obtain token. \nTerminating Program...")
        sys.exit()
    return token


def getFixablyOrders(token):
    pageNumber = 1
    orders = []
    while True:
        try:
            response = requests.get(
                f"http://careers-api.fixably.com/orders?page={pageNumber}",
                headers = {'X-Fixably-Token':token, 'Content-Type':'multipart/form-data'}, 
                )
            print(f"Currently on page {pageNumber}", end="\r")
            pageNumber += 1
            orders += response.json()['results']
        except KeyError:
            break
        except:
            print("\nSomething went wrong when attempting to access the endpoint.")
            print(f"Only {len(orders)} orders were obtained.\n")
            break
    return orders


def getFixablyOrderStats(token, orders):
    """Takes a list of orders and returns a
    list of tuples, with each tuple containing
    the status description in index 0 and the number of 
    orders with the status description in index 1"""
    order_stats = {}
    for order in orders:
        try:
            order_stats[order['status']] += 1
        except KeyError:
            order_stats[order['status']] = 1
    order_stats['Open'] = order_stats[1]
    del order_stats[1]
    order_stats['Closed'] = order_stats[2]
    del order_stats[2]
    order_stats['Assigned'] = order_stats[3]
    del order_stats[3]
    order_stats['Unpaid'] = order_stats[4]
    del order_stats[4]
    order_stats = sorted(order_stats.items(), key=lambda x:x[1], reverse=True)
    print(order_stats)
    return order_stats


def getIPhoneAndAssigned(orders):
    iPhoneAndAssigned = []
    for order in orders:
        if order['deviceBrand'].startswith('iPhone') and order['status'] == 3:
            iPhoneAndAssigned.append(order)
    return iPhoneAndAssigned



