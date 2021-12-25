from random import sample, uniform, randint
import datetime
from blackMarketItems import *


def isMagic(item):
    """
    Used only for Weapons and Armor, to determine if it is a magic item
    3% chance for +2 magical item, 15% for +1
    """

    if isinstance(item, weapon) or isinstance(item, armor):
        magicChance = randint(1,100)
        
        if magicChance <= 3:

            if isinstance(item, armor):
                return 1 #Armor should never return +2, so there is a 3% chance
                        #of +1 armor
            else:
                return 2

        elif magicChance <= 15:
            return 1
        
        else:
            return False

    else:
        return False


def getQuantity(item, magicMod):
    #For magic weapons and armor, the quantity should only ever be 1,
    #So this will check for that, otherwise randomize based on attributes

    if magicMod:
        return 1

    else:
        return randint(item.minQuantity, item.maxQuantity)


def getPrice(item, magicMod):
    """
The randomized 'blackMarketMod' is to simulate randomized black
market prices. This can easily be changed if the price ranges ever
feel too high or too low.

For now, standard items, standard weapons and standard armor use
the same random black market modifier formula, but these are
seperate so that these numbers can be adjusted individually if
needed.

The price attribute from the item class will be used for most
calculations.
    """


#Standard items
    if isinstance(item, standardItem):
        blackMarketMod = uniform(.4,1.10)
        return str(round(item.price * blackMarketMod, 2)).split(".")


#Armor
    if isinstance(item, armor):

        #Price for magic armor. Magic armor should only ever be +1 in
        #the Chultan market, so the magicMod number doesn't actually
        #apply to amor. There is no static price, either, so this price
        #is much more randomized.
        if magicMod == 2:
            magicItemPrice = uniform(3.8, 6.0)
            blackMarketMod = uniform(.7,1.10)

            return str(round((item.price * magicItemPrice)
            * blackMarketMod, 2)).split(".")
        
        #For non-magical armor. For now, modifier matches standard items.
        else:
            blackMarketMod = uniform(.4,1.10)
            return str(round(item.price * blackMarketMod, 2)).split(".")


#Weapons
    if isinstance(item, weapon):

        if magicMod == 2:
            itemPrice = 4000 #In this instance, replaces item.price
            blackMarketMod = uniform(.7,1.50)

            return str(round(itemPrice * blackMarketMod, 2)).split(".")

        
        elif magicMod == 1:
            itemPrice = 1000 #In this instance, replaces item.price
            blackMarketMod = uniform(.7,1.50)

            return str(round(itemPrice * blackMarketMod, 2)).split(".")


        else:
            blackMarketMod = uniform(.4,1.10)
            return str(round(item.price * blackMarketMod, 2)).split(".")


#Potions
    if isinstance(item, potion):
        blackMarketMod = uniform(.5,1.05)
        return str(round(item.price * blackMarketMod, 2)).split(".")

#Magic Items
    if isinstance(item, magicItem):
        blackMarketMod = uniform(.6,1.20)
        return str(round(item.price * blackMarketMod, 2)).split(".")


def getDisplayName(item, magicMod):
    """To determin the display name. Magic items and potions may
    have their display name hidden, based on the mystery chance
    attribute. Magic weapons and armor will also have their magic
    modifier added to the name."""

    if isinstance(item, standardItem):
        return item.name

    if isinstance(item, weapon) or isinstance(item, armor):
    #Appends +1 or +2 modifier to weapon or armor name
        if magicMod:
            return f"+{magicMod} {item.name}"
        
        else:
            return item.name

    if isinstance(item, potion) or isinstance(item, magicItem):
    #Hides the item name if the random number is less than
    #the myster chance attribute
        if randint(1,100) <= item.mysteryChance:
            return item.itemNumber

        else:
            return item.name




def printString(quantity, itemPrice, displayName):
    """Will generate the string for printing. Must determine
    amount of gold, silver, and copper, based on random price."""

    gold = int(itemPrice[0])
    silver = int(itemPrice[1][0])

    #This is primarily to prevent an an error when setting the copper
    #amount, in case the returned price doesn't have enough decimal places
    if len(itemPrice[1]) > 1: 
        copper = int(itemPrice[1][1])
    else:
        copper = 0


    if silver > 0 and copper > 0:
        return f"{displayName}, {quantity} available at {gold} gold, {silver} silver and {copper} copper each"

    elif silver > 0 and copper == 0:
        return f"{displayName}, {quantity} available at {gold} gold, and {silver} silver each"

    elif silver == 0 and copper > 0:
        return f"{displayName}, {quantity} available at {gold} gold, and {copper} copper each"

    else:
        return f"{displayName}, {quantity} available at {gold} gold each"
    

def randomItems(listOfItems):
    """
    To randomly generate the list of available items.
    The number of available items and items available will
    change with each visit to the black market.
    Standard items, weapons and armor use the same fomulas,
    but are seperated in case individual numbers need to be adjusted.
    """
    availableItems = [] #Needed for items with rarity: magic items and potions
    totalItems = len(listOfItems) #Set here to make the formulas look cleaner

#Standard Items
    if isinstance(listOfItems[0], standardItem):

        listMin = round(totalItems * .10)
        listMax = round(totalItems * .40)
        
        return sample(listOfItems, randint(listMin,listMax))

#Weapons
    if isinstance(listOfItems[0], weapon):

        listMin = round(totalItems * .10)
        listMax = round(totalItems * .40)
        
        return sample(listOfItems, randint(listMin,listMax))

#Armor
    if isinstance(listOfItems[0], armor):

        listMin = round(totalItems * .10)
        listMax = round(totalItems * .40)
        
        return sample(listOfItems, randint(listMin,listMax))

#Potions and Magic items
#First creates list of available items, since both types have rarity
    if isinstance(listOfItems[0], potion) or \
        isinstance(listOfItems[0], magicItem):
                
        for eachItem in listOfItems:
            if randint(1,100) <= eachItem.rarity:
                availableItems.append(eachItem)


#Potions
        if isinstance(listOfItems[0], potion):
        #Check to make sure sure no more than 7 potions are
        #available at any time. Also helps prevent errors,
        #in case a randomized number was higher than the number
        #of available p0tions.

            listMin = 4

            if len(availableItems) < 7:
                listMax = len(availableItems)

            else:
                listMax = 7

            return sample(availableItems, randint(listMin,listMax))

#Magic Items
        if isinstance(listOfItems[0], magicItem):
            #Magic items should never have a large quantity of available items,
            #but totals can be adjusted here.
            listMin = 1
            listMax = 2
            return sample(availableItems, randint(listMin,listMax))


def getWriteString(item):
#This puts everything together to generate the output for each available
#item.

    magicMod = isMagic(item)
    quantity = getQuantity(item, magicMod)
    price = getPrice(item, magicMod)
    displayName = getDisplayName(item,magicMod)

    return printString(quantity, price, displayName)


def sortedItemList(listOfItems):
    #Turning sorting items in to a function
    return sorted(randomItems(listOfItems), key = lambda eachItem: eachItem.name)

sortedStandardItems = sortedItemList(standardItems)
sortedWeapons = sortedItemList(weapons)
sortedArmors = sortedItemList(armors)
sortedPotions = sortedItemList(potions)
sortedMagicItems = sortedItemList(magicItems)

filename = f"BlackMarket-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"

with open(filename, 'w') as output:

    output.write(f"Generated On: {datetime.datetime.now().strftime('%d')} {datetime.datetime.now().strftime('%m')}, {datetime.datetime.now().strftime('%Y')}\n\n")
    
    output.write("Standard Items\n_______\n")
    for eachItem in sortedStandardItems:
        output.write(f"{getWriteString(eachItem)} \n")

    output.write("\nWeapons\n_______\n")
    for eachItem in sortedWeapons:
        output.write(f"{getWriteString(eachItem)} \n")

    output.write("\nArmors\n_______\n")
    for eachItem in sortedArmors:
        output.write(f"{getWriteString(eachItem)} \n")

    output.write("\nPotions and Poisons\n_______\n")
    for eachItem in sortedPotions:
        output.write(f"{getWriteString(eachItem)} \n")

    output.write("\nMagic Items\n_______\n")
    for eachItem in sortedMagicItems:
        output.write(f"{getWriteString(eachItem)} \n")