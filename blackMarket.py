from random import sample
from random import uniform
from random import randint
import datetime
from blackMarketItems import *


def randomStandardItems(itemList):

    availableItems = sample(itemList, randint(23,51))

    #print(f"Total Available items: {len(availableItems)} of {len(testList)}")
    return availableItems


def itemPriceQty(item):

    itemPrice = str(round(item.price * uniform(.63,1.05), 2)).split(".")

    gold = itemPrice[0]
    silver = itemPrice[1][0]

    if len(itemPrice[1]) > 1:
        copper = itemPrice[1][1]
    else:
        copper = 0

    quantity = randint(item.minQuantity, item.maxQuantity)

    if int(silver) > 0 and int(copper) > 0:
        #return print(f"{item.name}, {quantity} available at {gold} gold, {silver} silver and {copper} copper each")
        return f"{item.name}, {quantity} available at {gold} gold, {silver} silver and {copper} copper each"

    elif int(silver) > 0 and copper == 0:
        #return print(f"{item.name}, {quantity} available at {gold} gold, and {silver} silver each")
        return f"{item.name}, {quantity} available at {gold} gold, and {silver} silver each"

    elif int(silver) == 0 and int(copper) > 0:
        #return print(f"{item.name}, {quantity} available at {gold} gold, and {copper} copper each")
        return f"{item.name}, {quantity} available at {gold} gold, and {copper} copper each"

    else:
        #return print(f"{item.name}, {quantity} available at {gold} gold each")
        return f"{item.name}, {quantity} available at {gold} gold each"


x = sorted(randomStandardItems(testList), key = lambda i: i.name)

filename = f"BlackMarket-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"

with open(filename, 'w') as output:
    output.write(f"Total Available items: {len(x)} of {len(testList)} \n \n")

    for y in x:
        output.write(f"{itemPriceQty(y)} \n")