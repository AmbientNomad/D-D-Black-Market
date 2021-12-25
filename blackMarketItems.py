class standardItem:
    def __init__(self, name, price, minQuantity, maxQuantity):
        self.name = name
        self.price = price
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity

class weapon:
    def __init__(self, name, price, minQuantity, maxQuantity):
        self.name = name
        self.price = price
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity

class armor:
    def __init__(self, name, price, minQuantity, maxQuantity):
        self.name = name
        self.price = price
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity

class magicItem:
    def __init__(self, name, itemNumber, price, minQuantity, maxQuantity, rarity, mysteryChance):
        self.name = name
        self.itemNumber = itemNumber
        self.price = price
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity
        self.rarity = rarity
        self.mysteryChance = mysteryChance

class potion:
    def __init__(self, name, itemNumber, price, minQuantity, maxQuantity, rarity, mysteryChance):
        self.name = name
        self.itemNumber = itemNumber
        self.price = price
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity
        self.rarity = rarity
        self.mysteryChance = mysteryChance

###List from "Other Adventuring Gear", no 1cp items, no potions
item000 = standardItem("Abacus", 2, 5, 10)
item001 = standardItem("Acid(Vial)", 25, 1, 5)
item002 = standardItem("Alchemist's Fire (flask)", 50, 1, 2)
item003 = standardItem("Antitoxin (vial)", 50, 1, 5)
item004 = standardItem("Backpack", 2, 6, 10)
item005 = standardItem("Ball bearings (bag of 1,000)", 1, 2, 8)
item006 = standardItem("Barrel", 2, 1, 3)
item007 = standardItem("Basket", .4, 4, 20)
item008 = standardItem("Bedroll", 1, 1, 4)
item009 = standardItem("Bell", 1, 2, 10)
item010 = standardItem("Blanket", .5, 1, 5)
item011 = standardItem("Block and Tackle", 1, 2, 10)
item012 = standardItem("Bottle, glass", 2, 2, 5)
item013 = standardItem("Bucket", .05, 5, 10)
item014 = standardItem("Caltrops (bag of 20)", 1, 2, 5)
item015 = standardItem("Case, crossbow bolt", 1, 1, 5)
item016 = standardItem("Case, map or scroll", 1, 1, 5)
item017 = standardItem("Chain (10 feet)", 5, 1, 5)
item018 = standardItem("Chest", 5, 1, 4)
item019 = standardItem("Climber's Kit", 25, 1, 2)
item020 = standardItem("Clothes, common", .5, 8, 20)
item021 = standardItem("Clothes, costume", 5, 1, 5)
item022 = standardItem("Clothes, fine", 15, 1, 5)
item023 = standardItem("Clothes, traveler's", 2, 4, 10)
item024 = standardItem("Component Pouch", 25, 1, 4)
item025 = standardItem("Crowbar", 2, 1, 4)
item026 = standardItem("Fishing tackle", 1, 2, 20)
item027 = standardItem("Flask or tankard", .02, 5, 20)
item028 = standardItem("Grappling hook", 2, 1, 2)
item029 = standardItem("Hammer", 1, 4, 15)
item030 = standardItem("Hammer, sledge", 2, 1, 3)
item031 = standardItem("Healer's kit", 5, 3, 10)
item032 = standardItem("Holy water (flask)", 25, 1, 10)
item033 = standardItem("Hourglass", 25, 1, 5)
item034 = standardItem("Hunting trap", 5, 1, 5)
item035 = standardItem("Ink (1 ounce bottle)", 10, 1, 5)
item036 = standardItem("Jug or pitcher", .02, 5, 20)
item037 = standardItem("Ladder (10 foot)", .1, 1, 5)
item038 = standardItem("Lamp", .5, 1, 10)
item039 = standardItem("Lantern, bullseye", 10, 1, 3)
item040 = standardItem("Lantern, hooded", 5, 1, 5)
item041 = standardItem("Lock", 10, 4, 10)
item042 = standardItem("Magnifying Glass", 100, 1, 2)
item043 = standardItem("Manacles", 2, 1, 4)
item044 = standardItem("Mess kit", .2, 1, 5)
item045 = standardItem("Mirror, steel", 5, 1, 5)
item046 = standardItem("Oil (flask)", .1, 5, 20)
item047 = standardItem("Paper (one sheet)", .2, 10, 50)
item048 = standardItem("Parchment (one sheet)", .1, 10, 50)
item049 = standardItem("Perfume (vial)", 5, 1, 7)
item050 = standardItem("Pick, miner's", 2, 1, 4)
item051 = standardItem("Piton", .05, 10, 100)
item052 = standardItem("Poison, basic (vial)", 100, 1, 5)
item053 = standardItem("Pole (10-foot)", .05, 1, 6)
item054 = standardItem("Pot, iron", 2, 4, 10)
item055 = standardItem("Pouch", .5, 5, 20)
item056 = standardItem("Quiver", 1, 1, 4)
item057 = standardItem("Ram, portable", 4, 1, 3)
item058 = standardItem("Rations (1 day)", .5, 3, 30)
item059 = standardItem("Robes", 1, 1, 3)
item060 = standardItem("Rope, hempen (50 feet)", 1, 1, 10)
item061 = standardItem("Rope, silk (50 feet)", 10, 1, 4)
item062 = standardItem("Scale, merchant's", 5, 1, 10)
item063 = standardItem("Sealing wax", .5, 1, 10)
item064 = standardItem("Shovel", 2, 1, 8)
item065 = standardItem("Signal Whistle", .05, 1, 6)
item066 = standardItem("Soap", .02, 5, 25)
item067 = standardItem("Spikes, iron (10)", 1, 7, 40)
item068 = standardItem("Spyglass", 1000, 1, 1)
item069 = standardItem("Tent, two-person", 2, 1, 4)
item070 = standardItem("Tinderbox", .5, 2, 6)
item071 = standardItem("Vial", 1, 5, 20)
item072 = standardItem("Waterskin", .2, 1, 4)
item073 = standardItem("Canoe", 50, 1, 3)
item074 = standardItem("Rain Catcher", 1, 1, 6)
item075 = standardItem("Tej", .04, 2, 20)
item076 = standardItem("Insect Repellent: Block of Incense", .1, 1, 6)
item077 = standardItem("Insect Repellent: Vial of Salve", 1, 1, 3)

#Potions and Poisons
item100 = potion("Assassin's blood", "Item100", 150, 1, 2, 60, 10)
item101 = potion("Burnt othur fumes", "Item101", 500, 1, 1, 50, 10)
item102 = potion("Carrion crawler mucus", "Item102", 200, 1, 2, 60, 10)
item103 = potion("Drow Poison", "Item103", 200, 1, 2, 60, 10)
item104 = potion("Essence of ether", "Item104", 300, 1, 2, 60, 10)
item105 = potion("Malice", "Item105", 250, 1, 2, 60, 10)
item106 = potion("Midnight tears", "Item106", 1500, 1, 1, 40, 20)
item107 = potion("Oil of taggit", "Item107", 400, 1, 1, 50, 10)
item108 = potion("Pale tincture", "Item108", 250, 1, 1, 60, 10)
item109 = potion("Purple worm poison", "Item109", 2000, 1, 1, 30, 20)
item110 = potion("Serpent venom", "Item110", 200, 1, 1, 60, 10)
item111 = potion("Torpor", "Item111", 600, 1, 1, 50, 10)
item112 = potion("Truth serum", "Item112", 150, 1, 1, 60, 10)
item113 = potion("Wyvern poison", "Item113", 1200, 1, 1, 40, 20)
item114 = potion("Potion of Climbing", "Item114", 80, 1, 5, 100, 1)
item115 = potion("Potion of Comprehension", "Item115", 80, 1, 5, 100, 1)
item116 = potion("Potion of Healing", "Item116", 80, 1, 5, 100, 1)
item117 = potion("Potion of Watchful Rest", "Item117", 80, 1, 5, 100, 1)
item118 = potion("Potion of Greater Healing", "Item118", 300, 1, 3, 90, 3)
item119 = potion("Bottled Breath", "Item119", 300, 1, 3, 90, 3)
item120 = potion("Philter of Love", "Item120", 300, 1, 3, 90, 3)
item121 = potion("Potion of Animal Friendship", "Item121", 300, 1, 3, 90, 3)
item122 = potion("Potion of Fire Breath", "Item122", 300, 1, 3, 90, 3)
item123 = potion("Potion of Hill Giant Strength", "Item123", 300, 1, 3, 90, 3)
item124 = potion("Potion of Growth", "Item124", 300, 1, 3, 90, 3)
item125 = potion("Potion of Resistance", "Item125", 300, 1, 3, 90, 3)
item126 = potion("Potion of Water Breathing", "Item126", 300, 1, 3, 90, 3)
item127 = potion("Potion of Advantage", "Item127", 300, 1, 3, 80, 6)
item128 = potion("Oil of Slipperiness", "Item128", 300, 1, 3, 80, 6)
item129 = potion("Elixer of Health", "Item129", 700, 1, 2, 50, 10)
item130 = potion("Potion of Clairvoyance", "Item130", 600, 1, 2, 50, 10)
item131 = potion("Potion of Frost Giant Strength", "Item131", 900, 1, 1, 50, 20)
item132 = potion("Potion of Stone Giant Strength", "Item132", 900, 1, 1, 50, 20)
item133 = potion("Potion of Fire Giant Strength", "Item133", 1000, 1, 1, 40, 30)
item134 = potion("Potion of Heroism", "Item134", 900, 1, 1, 50, 20)
item135 = potion("Potion of Invulnerability", "Item135", 900, 1, 1, 50, 20)
item136 = potion("Potion of Maximum Power", "Item136", 1000, 1, 1, 40, 30)
item137 = potion("Potion of Mind Reading", "Item137", 800, 1, 1, 50, 20)
item138 = potion("Potion of Superior Healing", "Item138", 700, 1, 2, 50, 10)
item139 = potion("Potion of Maximum Power", "Item139", 1000, 1, 1, 40, 30)
item140 = potion("Oil of Sharpness", "Item140", 3200, 1, 1, 30, 30)
item141 = potion("Potion of Flying", "Item141", 1350, 1, 1, 30, 30)
item142 = potion("Potion of Cloud Giant Strength", "Item142", 5000, 1, 1, 20, 40)
item143 = potion("Potion of Supreme Healing", "Item143", 1350, 1, 1, 30, 30)
item144 = potion("Potion of Invisibility", "Item144", 1350, 1, 1, 30, 30)
item145 = potion("Potion of Speed", "Item145", 1350, 1, 1, 30, 30)
item146 = potion("Potion of Vitality", "Item146", 1350, 1, 1, 30, 30)
item147 = potion("Potion of Flying", "Item147", 1350, 1, 1, 30, 30)
item148 = potion("Potion of Dragon's Majesty", "Item148", 15000, 1, 1, 1, 50)
item149 = potion("Potion of Giant Size", "Item149", 15000, 1, 1, 1, 50)
item150 = potion("Potion of Storm Giant Strength", "Item150", 150000, 1, 1, 1, 50)

#Weapons
item200 = weapon("Battleaxe", 10, 1, 3)
item201 = weapon("Blowgun", 10, 1, 3)
item202 = weapon("Boomerang", .1, 1, 3)
item203 = weapon("Club", .1, 1, 3)
item204 = weapon("Crossbow, Hand", 75, 1, 1)
item205 = weapon("Crossbow, Heavy", 50, 1, 1)
item206 = weapon("Crossbow, Light", 25, 1, 3)
item207 = weapon("Dagger", 2, 1, 10)
item208 = weapon("Dart", .05, 10, 30)
item209 = weapon("Double-Bladed Scimitar", 100, 1, 1)
item210 = weapon("Flail", 10, 1, 3)
item211 = weapon("Glaive", 20, 1, 2)
item212 = weapon("Greataxe", 30, 1, 2)
item213 = weapon("Greatclub", .2, 1, 3)
item214 = weapon("Greatsword", 50, 1, 2)
item215 = weapon("Halberd", 20, 1, 3)
item216 = weapon("Handaxe", 5, 1, 2)
item217 = weapon("Javelin", .5, 3, 10)
item218 = weapon("Lance", 10, 1, 3)
item219 = weapon("Light Hammer", 2, 1, 3)
item220 = weapon("Longbow", 50, 1, 3)
item221 = weapon("Longsword", 15, 1, 10)
item222 = weapon("Mace", 10, 1, 3)
item223 = weapon("Morningstar", 15, 1, 3)
item224 = weapon("Net", 1, 1, 3)
item225 = weapon("Pike", 5, 1, 3)
item226 = weapon("Quarterstaff", .2, 1, 3)
item227 = weapon("Rapier", 25, 1, 3)
item228 = weapon("Scimitar", 25, 1, 3)
item229 = weapon("Shortbow", 25, 1, 3)
item230 = weapon("Shortsword", 10, 1, 3)
item231 = weapon("Sickle", 1, 1, 3)
item232 = weapon("Sling", .1, 1, 3)
item233 = weapon("Spear", 1, 1, 3)
item234 = weapon("Trident", 5, 1, 3)
item235 = weapon("War Pick", 5, 1, 3)
item236 = weapon("Warhammer", 15, 1, 3)
item237 = weapon("Whip", 2, 1, 3)
item238 = weapon("Yklwa", 1, 1, 10)

#Armor
item300 = armor("Padded", 5, 1, 3)
item301 = armor("Leather", 10, 1, 3)
item302 = armor("Studded Leather", 45, 1, 3)
item303 = armor("Hide", 10, 1, 3)
item304 = armor("Chain Shirt", 50, 1, 2)
item305 = armor("Scale Mail", 50, 1, 2)
item306 = armor("Breastplate", 400, 1, 2)
item307 = armor("Half Plate", 750, 1, 2)
item308 = armor("Ring Mail", 90, 1, 1)
item309 = armor("Chian Mail", 225, 1, 1)
item310 = armor("Splint", 600, 1, 1)
item311 = armor("Plate", 4500, 1, 1)
item312 = armor("Shield, wooden", 10, 1, 3)

#Magic Items
item400 = magicItem("Bead of Nourishment", "Item400", 15, 3, 10, 100, 0)
item401 = magicItem("Bead of Refreshment", "Item401", 15, 3, 10, 100, 0)
item402 = magicItem("Boots of False Tracks", "Item402", 60, 1, 2, 100, 0)
item403 = magicItem("Bead of Refreshment", "Item403", 15, 3, 10, 100, 0)
item404 = magicItem("Bottle of Boundless Coffee", "Item404", 100, 1, 1, 100, 0)
item405 = magicItem("Candle of the Deep", "Item405", 50, 1, 2, 100, 0)
item406 = magicItem("Charlatan's Die", "Item406", 75, 1, 1, 100, 0)
item407 = magicItem("Cloak of Billowing", "Item407", 60, 1, 3, 100, 0)
item408 = magicItem("Clockwork Amulet", "Item408", 80, 1, 1, 100, 0)
item409 = magicItem("Ear Horn of Hearing", "Item409", 50, 1, 1, 100, 0)
item410 = magicItem("Lock of Trickery", "Item410", 75, 1, 5, 100, 0)
item411 = magicItem("Mystery Key", "Item411", 100, 1, 5, 100, 0)
item412 = magicItem("Orb of Direction", "Item412", 75, 1, 1, 100, 0)
item413 = magicItem("Orb of Time", "Item413", 75, 1, 1, 100, 0)
item414 = magicItem("Perfume of Bewitching", "Item414", 75, 1, 1, 100, 0)
item415 = magicItem("Pot of Awakening", "Item415", 90, 1, 1, 100, 0)
item416 = magicItem("Pressure Capsule", "Item416", 60, 1, 1, 100, 0)
item417 = magicItem("Rope of Mending", "Item417", 75, 1, 1, 100, 0)
item418 = magicItem("Shield of Expression", "Item418", 75, 1, 1, 100, 0)
item419 = magicItem("Walloping Ammunition (x5)", "Item419", 60, 2, 7, 100, 0)
item420 = magicItem("Wand of Scowls", "Item420", 75, 1, 1, 100, 0)
item421 = magicItem("Wand of Smiles", "Item421", 75, 1, 1, 100, 0)
item422 = magicItem("Boots of Elven Kind", "Item422", 2500, 1, 1, 60, 30)
item423 = magicItem("Boots of Striding and Springing", "Item423", 5000, 1, 1, 60, 30)
item424 = magicItem("Boots of the Winterlands", "Item424", 1000, 1, 1, 50, 30)
item425 = magicItem("Brooch of Shielding", "Item425", 7500, 1, 1, 50, 20)
item426 = magicItem("Cap of Water Breathing", "Item426", 1000, 1, 1, 60, 20)
item427 = magicItem("Cloak of Elven Kind", "Item427", 5000, 1, 1, 50, 20)
item428 = magicItem("Cloak of Protection", "Item428", 3500, 1, 1, 40, 50)
item429 = magicItem("Cracked Driftglobe", "Item429", 400, 1, 1, 70, 0)
item430 = magicItem("Driftglobe", "Item430", 750, 1, 1, 50, 20)
item431 = magicItem("Quiver of Ehlonna", "Item431", 1000, 1, 1, 50, 20)
item432 = magicItem("Eyes of the Eagle", "Item432", 2500, 1, 1, 50, 20)
item433 = magicItem("Finder's Goggles", "Item433", 2500, 1, 1, 50, 20)
item434 = magicItem("Gloves of Missile Snaring", "Item434", 3000, 1, 1, 50, 20)
item435 = magicItem("Gloves of Swimming and Climbing", "Item435", 2000, 1, 1, 50, 20)
item436 = magicItem("Gloves of Thievery", "Item436", 5000, 1, 1, 50, 20)
item437 = magicItem("Goggles of Night", "Item437", 1500, 1, 1, 50, 20)
item438 = magicItem("Goggles of Object Reading", "Item438", 5000, 1, 1, 50, 20)
item439 = magicItem("Hat of Disguise", "Item439", 5000, 1, 1, 50, 20)
item440 = magicItem("Helm of Comprehend Languages", "Item440", 1000, 1, 1, 50, 20)
item441 = magicItem("Amulet of Proof Against Detection and Location", "Item441", 20000, 1, 1, 30, 50)
item442 = magicItem("Medallion of Thoughts", "Item442", 3000, 1, 1, 50, 20)
item443 = magicItem("Nature's Mantle", "Item443", 5000, 1, 1, 50, 20)
item444 = magicItem("Necklace of Adaptation", "Item444", 1500, 1, 1, 50, 20)
item445 = magicItem("Pearl of Power", "Item445", 6000, 1, 1, 40, 20)
item446 = magicItem("Periapt of Health", "Item446", 5000, 1, 1, 50, 20)
item447 = magicItem("Ring of Warmth", "Item447", 1000, 1, 1, 50, 20)
item448 = magicItem("Sentinel Shield", "Item448", 20000, 1, 1, 30, 50)
item449 = magicItem("Slippers of Spider Climbing", "Item449", 5000, 1, 1, 50, 20)
item450 = magicItem("Trident of Fish Command", "Item450", 800, 1, 1, 50, 20)
item451 = magicItem("Wand of Web", "Item451", 8000, 1, 1, 50, 20)
item452 = magicItem("Hew", "Item452", 1000, 1, 1, 50, 20)
item453 = magicItem("Wand of Web", "Item453", 1500, 1, 1, 50, 20)
item454 = magicItem("Dagger of Blindsight", "Item454", 6000, 1, 1, 5, 90)
item455 = magicItem("Dagger of Venom", "Item455", 2500, 1, 1, 5, 80)
item456 = magicItem("Periapt of Proof against Poison", "Item456", 5000, 1, 1, 5, 90)
item457 = magicItem("Elven Chain", "Item457", 4000, 1, 1, 5, 80)
item458 = magicItem("Mantle of Spell Resistance", "Item458", 30000, 1, 1, 5, 90)
item459 = magicItem("Ring of Evasion", "Item459", 5000, 1, 1, 5, 90)
item460 = magicItem("Ring of Free Action", "Item460", 20000, 1, 1, 5, 90)
item461 = magicItem("Ring of Resistance", "Item461", 6000, 1, 1, 5, 80)
item462 = magicItem("Ring of Spell Storing", "Item462", 24000, 1, 1, 5, 90)
item463 = magicItem("Ring of the Ram", "Item463", 5000, 1, 1, 5, 80)
item464 = magicItem("+1 Wand of the War Mage", "Item464", 1200, 1, 1, 90, 70)
item465 = magicItem("+2 Wand of the War Mage", "Item465", 4800, 1, 1, 5, 90)
item466 = magicItem("+3 Wand of the War Mage", "Item466", 19200, 1, 1, .01, 100)
item467 = magicItem("Armor of Resistance", "Item467", 6000, 1, 1, 5, 80)
item468 = magicItem("Armor of Vulnerability", "Item468", 1000, 1, 1, 5, 100)
item469 = magicItem("Arrow Catching Shield", "Item469", 6000, 1, 1, 5, 80)
item470 = magicItem("Battering Shield", "Item470", 1600, 1, 1, 5, 80)
item471 = magicItem("Belt of Dwarven Kind", "Item471", 6000, 1, 1, 5, 90)
item472 = magicItem("Shield of Missile Attraction", "Item472", 6000, 1, 1, 1, 100)
item473 = magicItem("Boots of Levitation", "Item473", 4000, 1, 1, 5, 90)
item474 = magicItem("Boots of Speed", "Item474", 4000, 1, 1, 5, 90)
item475 = magicItem("Javelin of Backbiting", "Item475", 6000, 1, 1, 1, 100)
item476 = magicItem("Spear of Backbiting", "Item476", 6000, 1, 1, 1, 100)
item477 = magicItem("Stone of Ill Luck", "Item477", 4200, 1, 1, 1, 100)
item478 = magicItem("Sword of Vengeance", "Item478", 400, 1, 1, 20, 100)
item479 = magicItem("Demon Armor", "Item479", 400, 1, 1, 20, 100)

standardItems = [
item001,
item002,
item003,
item004,
item005,
item006,
item007,
item008,
item009,
item010,
item011,
item012,
item013,
item014,
item015,
item016,
item017,
item018,
item019,
item020,
item021,
item022,
item023,
item024,
item025,
item026,
item027,
item028,
item029,
item030,
item031,
item032,
item033,
item034,
item035,
item036,
item037,
item038,
item039,
item040,
item041,
item042,
item043,
item044,
item045,
item046,
item047,
item048,
item049,
item050,
item051,
item052,
item053,
item054,
item055,
item056,
item057,
item058,
item059,
item060,
item061,
item062,
item063,
item064,
item065,
item066,
item067,
item068,
item069,
item070,
item071,
item072,
item073,
item074,
item075,
item076,
item077
]

potions = [
item100,
item101,
item102,
item103,
item104,
item105,
item106,
item107,
item108,
item109,
item110,
item111,
item112,
item113,
item114,
item115,
item116,
item117,
item118,
item119,
item120,
item121,
item122,
item123,
item124,
item125,
item126,
item127,
item128,
item129,
item130,
item131,
item132,
item133,
item134,
item135,
item136,
item137,
item138,
item139,
item140,
item141,
item142,
item143,
item144,
item145,
item146,
item147,
item148,
item149,
item150
]

weapons = [
item200,
item201,
item202,
item203,
item204,
item205,
item206,
item207,
item208,
item209,
item210,
item211,
item212,
item213,
item214,
item215,
item216,
item217,
item218,
item219,
item220,
item221,
item222,
item223,
item224,
item225,
item226,
item227,
item228,
item229,
item230,
item231,
item232,
item233,
item234,
item235,
item236,
item237,
item238
]

armors = [
item300,
item301,
item302,
item303,
item304,
item305,
item306,
item307,
item308,
item309,
item310,
item311,
item312
]

magicItems = [
item400,
item401,
item402,
item403,
item404,
item405,
item406,
item407,
item408,
item409,
item410,
item411,
item412,
item413,
item414,
item415,
item416,
item417,
item418,
item419,
item420,
item421,
item422,
item423,
item424,
item425,
item426,
item427,
item428,
item429,
item430,
item431,
item432,
item433,
item434,
item435,
item436,
item437,
item438,
item439,
item440,
item441,
item442,
item443,
item444,
item445,
item446,
item447,
item448,
item449,
item450,
item451,
item452,
item453,
item454,
item455,
item456,
item457,
item458,
item459,
item460,
item461,
item462,
item463,
item464,
item465,
item466,
item467,
item468,
item469,
item470,
item471,
item472,
item473,
item474,
item475,
item476,
item477,
item478,
item479
]