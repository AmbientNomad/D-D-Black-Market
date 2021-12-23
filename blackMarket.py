from random import sample
from random import uniform
from random import randint
import datetime
from blackMarketItems import *

"""missed items:

toa items
+1 ammunition
spell scrolls"""

def randomItems(listOfitems):
    availableItems = []

    
    if isinstance(listOfitems[0], standardItem):
        listMin = round(len(listOfitems)*.33)
        listMax = round(len(listOfitems)*.66)
        return sample(listOfitems, randint(listMin,listMax))

    elif isinstance(listOfitems[0], potion):
        
        for eachItem in listOfitems:
            if randint(1,100) <= eachItem.rarity:
                availableItems.append(eachItem)

        listMin = 4
        if len(availableItems) < 10:
            listMax = len(availableItems)
        else:
            listMax = 10

        return sample(availableItems, randint(listMin,listMax))

    elif isinstance(listOfitems[0], magicItem):
        return sample(listOfitems, randint(1,2))


def itemPriceQty(item, type):
    isMagic = randint(1,100)
    magicMod = False

    if type == "armors" and isMagic <=3:
        magicMod = 1

        itemPrice = str(round((item.price * 2) * uniform(.7,1.10), 2)).split(".")
        displayName = f"+{magicMod} {item.name}"

    elif type == "weapons" and isMagic <= 15:
        if isMagic <= 3:
            magicMod = 2

            itemPrice = str(round(4000 * uniform(.7,1.50), 2)).split(".")
            displayName = f"+{magicMod} {item.name}"
        
        elif isMagic <= 15:
            magicMod = 1

            if item.name in modulePriced.keys():
                itemPrice = str(round(modulePriced.get(item.name) * uniform(.7,1.50), 2)).split(".")
            else:
                itemPrice = str(round(1000 * uniform(.6,1.20), 2)).split(".")

            displayName = f"+{magicMod} {item.name}"

    elif isinstance(item, standardItem):
        itemPrice = str(round(item.price * uniform(.4,1.10), 2)).split(".")
        displayName = item.name

    elif isinstance(item, potion):
        itemPrice = str(round(item.price * uniform(.5,1.05), 2)).split(".")
        displayName = item.name

        if randint(1,100) <= item.mysteryChance:
            displayName = item.itemNumber
    
    elif isinstance(item, magicItem):
        itemPrice = str(round(item.price * uniform(.6,1.20), 2)).split(".")
        if randint(1,100) <= item.mysteryChance:
            displayName = item.itemNumber
        else:
            displayName = item.name

    gold = itemPrice[0]
    silver = itemPrice[1][0]

    if len(itemPrice[1]) > 1:
        copper = itemPrice[1][1]
    else:
        copper = 0

    if magicMod:
        quantity = 1
    else:
        quantity = randint(item.minQuantity, item.maxQuantity)

    if int(silver) > 0 and int(copper) > 0:
        return f"{displayName}, {quantity} available at {gold} gold, {silver} silver and {copper} copper each"

    elif int(silver) > 0 and copper == 0:
        return f"{displayName}, {quantity} available at {gold} gold, and {silver} silver each"

    elif int(silver) == 0 and int(copper) > 0:
        return f"{displayName}, {quantity} available at {gold} gold, and {copper} copper each"

    else:
        return f"{item.name}, {quantity} available at {gold} gold each"


modulePriced = {"Ammunition":50,
                "Shield, wooden":450,
                "Dagger":500,
                "Yklwa":500
                }


sortedStandardItems = sorted(randomItems(standardItems), key = lambda eachItem: eachItem.name)

sortedPotions = sorted(randomItems(potions), key = lambda eachItem: eachItem.name)

sortedWeapons = sorted(randomItems(weapons), key = lambda eachItem: eachItem.name)

sortedArmors = sorted(randomItems(armors), key = lambda eachItem: eachItem.name)

sortedMagicItems = sorted(randomItems(magicItems), key = lambda eachItem: eachItem.name)

filename = f"BlackMarket-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"

with open(filename, 'w') as output:

    output.write("Standard Items\n_______\n")
    for eachItem in sortedStandardItems:
        output.write(f"{itemPriceQty(eachItem, 'standard')} \n")

    output.write("\nWeapons\n_______\n")
    for eachItem in sortedWeapons:
        output.write(f"{itemPriceQty(eachItem, 'weapons')} \n")

    output.write("\nArmors\n_______\n")
    for eachItem in sortedArmors:
        output.write(f"{itemPriceQty(eachItem, 'armors')} \n")

    output.write("\nPotions and Poisons\n_______\n")
    for eachItem in sortedPotions:
        output.write(f"{itemPriceQty(eachItem, 'potions')} \n")

    output.write("\nMagic Items\n_______\n")
    for eachItem in sortedMagicItems:
        output.write(f"{itemPriceQty(eachItem, 'magic')} \n")
