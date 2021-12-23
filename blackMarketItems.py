class standardItem:
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

class potion(magicItem):
    pass

###List from "Other Adventuring Gear", no 1cp items, no potions
item001 = standardItem("Abacus", 2, 5, 10)
item002 = standardItem("Acid(Vial)", 25, 1, 5)
item003 = standardItem("Alchemist's Fire (flask)", 50, 1, 2)
item004 = standardItem("Antitoxin (vial)", 50, 1, 5)
item005 = standardItem("Backpack", 2, 6, 10)
item006 = standardItem("Ball bearings (bag of 1,000)", 1, 2, 8)
item007 = standardItem("Barrel", 2, 1, 3)
item008 = standardItem("Basket", .4, 4, 20)
item009 = standardItem("Bedroll", 1, 1, 4)
item010 = standardItem("Bell", 1, 2, 10)
item011 = standardItem("Blanket", .5, 1, 5)
item012 = standardItem("Block and Tackle", 1, 2, 10)
item013 = standardItem("Bottle, glass", 2, 2, 5)
item014 = standardItem("Bucket", .05, 5, 10)
item015 = standardItem("Caltrops (bag of 20)", 1, 2, 5)
item016 = standardItem("Case, crossbow bolt", 1, 1, 5)
item017 = standardItem("Case, map or scroll", 1, 1, 5)
item018 = standardItem("Chain (10 feet)", 5, 1, 5)
item019 = standardItem("Chest", 5, 1, 4)
item020 = standardItem("Climber's Kit", 25, 1, 2)
item020 = standardItem("Clothes, common", .5, 8, 20)
item022 = standardItem("Clothes, costume", 5, 1, 5)
item023 = standardItem("Clothes, fine", 15, 1, 5)
item024 = standardItem("Clothes, traveler's", 2, 4, 10)
item025 = standardItem("Component Pouch", 25, 1, 4)
item026 = standardItem("Crowbar", 2, 1, 4)
item027 = standardItem("Fishing tackle", 1, 2, 20)
item028 = standardItem("Flask or tankard", .02, 5, 20)
item029 = standardItem("Grappling hook", 2, 1, 2)
item030 = standardItem("Hammer", 1, 4, 15)
item031 = standardItem("Hammer, sledge", 2, 1, 3)
item032 = standardItem("Healer's kit", 5, 3, 10)
item033 = standardItem("Holy water (flask)", 25, 1, 10)
item034 = standardItem("Hourglass", 25, 1, 5)
item035 = standardItem("Hunting trap", 5, 1, 5)
item036 = standardItem("Ink (1 ounce bottle)", 10, 1, 5)
item037 = standardItem("Jug or pitcher", .02, 5, 20)
item038 = standardItem("Ladder (10 foot)", .1, 1, 5)
item039 = standardItem("Lamp", .5, 1, 10)
item040 = standardItem("Lantern, bullseye", 10, 1, 3)
item040 = standardItem("Lantern, hooded", 5, 1, 5)
item042 = standardItem("Lock", 10, 4, 10)
item043 = standardItem("Magnifying Glass", 100, 1, 2)
item044 = standardItem("Manacles", 2, 1, 4)
item045 = standardItem("Mess kit", .2, 1, 5)
item046 = standardItem("Mirror, steel", 5, 1, 5)
item047 = standardItem("Oil (flask)", .1, 5, 20)
item048 = standardItem("Paper (one sheet)", .2, 10, 50)
item049 = standardItem("Parchment (one sheet)", .1, 10, 50)
item050 = standardItem("Perfume (vial)", 5, 1, 7)
item051 = standardItem("Pick, miner's", 2, 1, 4)
item052 = standardItem("Piton", .05, 10, 100)
item053 = standardItem("Poison, basic (vial)", 100, 1, 5)
item054 = standardItem("Pole (10-foot)", .05, 1, 6)
item055 = standardItem("Pot, iron", 2, 4, 10)
item056 = standardItem("Pouch", .5, 5, 20)
item057 = standardItem("Quiver", 1, 1, 4)
item058 = standardItem("Ram, portable", 4, 1, 3)
item059 = standardItem("Rations (1 day)", .5, 3, 30)
item060 = standardItem("Robes", 1, 1, 3)
item061 = standardItem("Rope, hempen (50 feet)", 1, 1, 10)
item062 = standardItem("Rope, silk (50 feet)", 10, 1, 4)
item063 = standardItem("Scale, merchant's", 5, 1, 10)
item064 = standardItem("Sealing wax", .5, 1, 10)
item065 = standardItem("Shovel", 2, 1, 8)
item066 = standardItem("Signal Whistle", .05, 1, 6)
item067 = standardItem("Soap", .02, 5, 25)
item068 = standardItem("Spikes, iron (10)", 1, 7, 40)
item069 = standardItem("Spyglass", 1000, 1, 1)
item070 = standardItem("Tent, two-person", 2, 1, 4)
item071 = standardItem("Tinderbox", .5, 2, 6)
item072 = standardItem("Vial", 1, 5, 20)
item073 = standardItem("Waterskin", .2, 1, 4)

#Potions
item074 = potion("Potion of Climbing", "Item074", 80, 1, 5, 100, 1)
item075 = potion("Potion of Comprehension", "Item075", 80, 1, 5, 100, 1)
item076 = potion("Potion of Healing", "Item076", 80, 1, 5, 100, 1)
item077 = potion("Potion of Watchful Rest", "Item077", 80, 1, 5, 100, 1)
item078 = potion("Potion of Greater Healing", "Item078", 300, 1, 3, 90, 3)
item079 = potion("Bottled Breath", "Item079", 300, 1, 3, 90, 3)
item080 = potion("Philter of Love", "Item080", 300, 1, 3, 90, 3)
item081 = potion("Potion of Animal Friendship", "Item081", 300, 1, 3, 90, 3)
item082 = potion("Potion of Fire Breath", "Item082", 300, 1, 3, 90, 3)
item083 = potion("Potion of Hill Giant Strength", "Item083", 300, 1, 3, 90, 3)
item084 = potion("Potion of Growth", "Item084", 300, 1, 3, 90, 3)
item085 = potion("Potion of Resistance", "Item085", 300, 1, 3, 90, 3)
item086 = potion("Potion of Water Breathing", "Item086", 300, 1, 3, 90, 3)
item087 = potion("Potion of Advantage", "Item087", 300, 1, 3, 80, 6)
item088 = potion("Oil of Slipperiness", "Item088", 300, 1, 3, 80, 6)
item089 = potion("Elixer of Health", "Item089", 700, 1, 2, 50, 10)
item090 = potion("Potion of Clairvoyance", "Item090", 600, 1, 2, 50, 10)
item091 = potion("Potion of Frost Giant Strength", "Item091", 900, 1, 1, 50, 20)
item092 = potion("Potion of Stone Giant Strength", "Item092", 900, 1, 1, 50, 20)
item093 = potion("Potion of Fire Giant Strength", "Item093", 1000, 1, 1, 40, 30)
item094 = potion("Potion of Heroism", "Item094", 900, 1, 1, 50, 20)
item095 = potion("Potion of Invulnerability", "Item095", 900, 1, 1, 50, 20)
item096 = potion("Potion of Maximum Power", "Item096", 1000, 1, 1, 40, 30)
item097 = potion("Potion of Mind Reading", "Item097", 800, 1, 1, 50, 20)
item098 = potion("Potion of Superior Healing", "Item098", 700, 1, 2, 50, 10)
item099 = potion("Potion of Maximum Power", "Item099", 1000, 1, 1, 40, 30)
item100 = potion("Oil of Sharpness", "Item100", 3200, 1, 1, 30, 30)
item101 = potion("Potion of Flying", "Item101", 1350, 1, 1, 30, 30)
item102 = potion("Potion of Cloud Giant Strength", "Item102", 5000, 1, 1, 20, 40)
item103 = potion("Potion of Supreme Healing", "Item103", 1350, 1, 1, 30, 30)
item104 = potion("Potion of Invisibility", "Item104", 1350, 1, 1, 30, 30)
item105 = potion("Potion of Speed", "Item105", 1350, 1, 1, 30, 30)
item106 = potion("Potion of Vitality", "Item106", 1350, 1, 1, 30, 30)
item107 = potion("Potion of Flying", "Item101", 1350, 1, 1, 30, 30)
item108 = potion("Potion of Dragon's Majesty", "Item108", 15000, 1, 1, 1, 50)
item109 = potion("Potion of Giant Size", "Item109", 15000, 1, 1, 1, 50)
item110 = potion("Potion of Storm Giant Strength", "Item110", 150000, 1, 1, 1, 50)

#Weapons
item111 = standardItem("Battleaxe", 10, 1, 3)
item112 = standardItem("Blowgun", 10, 1, 3)
item113 = standardItem("Boomerang", .1, 1, 3)
item114 = standardItem("Club", .1, 1, 3)
item115 = standardItem("Crossbow, Hand", 75, 1, 1)
item116 = standardItem("Crossbow, Heavy", 50, 1, 1)
item117 = standardItem("Crossbow, Light", 25, 1, 3)
item118 = standardItem("Dagger", 2, 1, 10)
item119 = standardItem("Dart", .05, 10, 30)
item120 = standardItem("Double-Bladed Scimitar", 100, 1, 1)
item121 = standardItem("Flail", 10, 1, 3)
item122 = standardItem("Glaive", 20, 1, 2)
item123 = standardItem("Greataxe", 30, 1, 2)
item124 = standardItem("Greatclub", .2, 1, 3)
item125 = standardItem("Greatsword", 50, 1, 2)
item126 = standardItem("Halberd", 20, 1, 3)
item127 = standardItem("Handaxe", 5, 1, 2)
item128 = standardItem("Javelin", .5, 3, 10)
item129 = standardItem("Lance", 10, 1, 3)
item130 = standardItem("Light Hammer", 2, 1, 3)
item131 = standardItem("Longbow", 50, 1, 3)
item132 = standardItem("Longsword", 15, 1, 10)
item133 = standardItem("Mace", 10, 1, 3)
item134 = standardItem("Morningstar", 15, 1, 3)
item135 = standardItem("Net", 1, 1, 3)
item136 = standardItem("Pike", 5, 1, 3)
item137 = standardItem("Quarterstaff", .2, 1, 3)
item138 = standardItem("Rapier", 25, 1, 3)
item139 = standardItem("Scimitar", 25, 1, 3)
item140 = standardItem("Shortbow", 25, 1, 3)
item141 = standardItem("Shortsword", 10, 1, 3)
item142 = standardItem("Sickle", 1, 1, 3)
item143 = standardItem("Sling", .1, 1, 3)
item144 = standardItem("Spear", 1, 1, 3)
item145 = standardItem("Trident", 5, 1, 3)
item146 = standardItem("War Pick", 5, 1, 3)
item147 = standardItem("Warhammer", 15, 1, 3)
item148 = standardItem("Whip", 2, 1, 3)
item149 = standardItem("Yklwa", 1, 1, 10)

#Armor
item150 = standardItem("Padded", 5, 1, 3)
item151 = standardItem("Leather", 10, 1, 3)
item152 = standardItem("Studded Leather", 45, 1, 3)
item153 = standardItem("Hide", 10, 1, 3)
item154 = standardItem("Chain Shirt", 50, 1, 2)
item155 = standardItem("Scale Mail", 50, 1, 2)
item156 = standardItem("Breastplate", 400, 1, 2)
item157 = standardItem("Half Plate", 750, 1, 2)
item158 = standardItem("Ring Mail", 90, 1, 1)
item159 = standardItem("Chian Mail", 225, 1, 1)
item160 = standardItem("Splint", 600, 1, 1)
item161 = standardItem("Plate", 4500, 1, 1)
item162 = standardItem("Shield, wooden", 10, 1, 3)

#Poisons, which will be listed with Potions
item163 = potion("Assassin's blood", "Item163", 150, 1, 2, 60, 10)
item164 = potion("Burnt othur fumes", "Item164", 500, 1, 1, 50, 10)
item165 = potion("Carrion crawler mucus", "Item165", 200, 1, 2, 60, 10)
item166 = potion("Drow Poison", "Item166", 200, 1, 2, 60, 10)
item167 = potion("Essence of ether", "Item167", 300, 1, 2, 60, 10)
item168 = potion("Malice", "Item168", 250, 1, 2, 60, 10)
item169 = potion("Midnight tears", "Item169", 1500, 1, 1, 40, 20)
item170 = potion("Oil of taggit", "Item170", 400, 1, 1, 50, 10)
item171 = potion("Pale tincture", "Item171", 250, 1, 1, 60, 10)
item172 = potion("Purple worm poison", "Item172", 2000, 1, 1, 30, 20)
item173 = potion("Serpent venom", "Item173", 200, 1, 1, 60, 10)
item174 = potion("Torpor", "Item174", 600, 1, 1, 50, 10)
item175 = potion("Truth serum", "Item175", 150, 1, 1, 60, 10)
item176 = potion("Wyvern poison", "Item176", 1200, 1, 1, 40, 20)

#Magic Items
item177 = magicItem("Bead of Nourishment", "Item177", 15, 3, 10, 100, 0)
item178 = magicItem("Bead of Refreshment", "Item178", 15, 3, 10, 100, 0)
item179 = magicItem("Boots of False Tracks", "Item179", 60, 1, 2, 100, 0)
item180 = magicItem("Bead of Refreshment", "Item180", 15, 3, 10, 100, 0)
item181 = magicItem("Bottle of Boundless Coffee", "Item181", 100, 1, 1, 100, 0)
item182 = magicItem("Candle of the Deep", "Item182", 50, 1, 2, 100, 0)
item183 = magicItem("Charlatan's Die", "Item183", 75, 1, 1, 100, 0)
item184 = magicItem("Cloak of Billowing", "Item184", 60, 1, 3, 100, 0)
item185 = magicItem("Clockwork Amulet", "Item185", 80, 1, 1, 100, 0)
item186 = magicItem("Ear Horn of Hearing", "Item186", 50, 1, 1, 100, 0)
item187 = magicItem("Lock of Trickery", "Item187", 75, 1, 5, 100, 0)
item188 = magicItem("Mystery Key", "Item188", 100, 1, 5, 100, 0)
item189 = magicItem("Orb of Direction", "Item189", 75, 1, 1, 100, 0)
item190 = magicItem("Orb of Time", "Item190", 75, 1, 1, 100, 0)
item191 = magicItem("Perfume of Bewitching", "Item191", 75, 1, 1, 100, 0)
item192 = magicItem("Pot of Awakening", "Item192", 90, 1, 1, 100, 0)
item193 = magicItem("Pressure Capsule", "Item193", 60, 1, 1, 100, 0)
item194 = magicItem("Rope of Mending", "Item194", 75, 1, 1, 100, 0)
item195 = magicItem("Shield of Expression", "Item195", 75, 1, 1, 100, 0)
item196 = magicItem("Walloping Ammunition (x5)", "Item196", 60, 2, 7, 100, 0)
item197 = magicItem("Wand of Scowls", "Item197", 75, 1, 1, 100, 0)
item198 = magicItem("Wand of Smiles", "Item198", 75, 1, 1, 100, 0)
item199 = magicItem("Boots of Elven Kind", "Item199", 2500, 1, 1, 60, 30)
item200 = magicItem("Boots of Striding and Springing", "Item200", 5000, 1, 1, 60, 30)
item201 = magicItem("Boots of the Winterlands", "Item201", 1000, 1, 1, 50, 30)
item202 = magicItem("Bracers of Archery", "Item202", 1500, 1, 1, 50, 20)
item203 = magicItem("Brooch of Shielding", "Item203", 7500, 1, 1, 50, 20)
item204 = magicItem("Cap of Water Breathing", "Item204", 1000, 1, 1, 60, 20)
item205 = magicItem("Circlet of Blasting", "Item205", 1500, 1, 1, 50, 20)
item206 = magicItem("Cloak of Elven Kind", "Item206", 5000, 1, 1, 50, 20)
item207 = magicItem("Cloak of Protection", "Item207", 3500, 1, 1, 40, 50)
item208 = magicItem("Cracked Driftglobe", "Item208", 400, 1, 1, 70, 0)
item209 = magicItem("Driftglobe", "Item209", 750, 1, 1, 50, 20)
item210 = magicItem("Quiver of Ehlonna", "Item210", 1000, 1, 1, 50, 20)
item211 = magicItem("Eyes of the Eagle", "Item211", 2500, 1, 1, 50, 20)
item212 = magicItem("Finder's Goggles", "Item212", 2500, 1, 1, 50, 20)
item213 = magicItem("Gloves of Missile Snaring", "Item213", 3000, 1, 1, 50, 20)
item214 = magicItem("Gloves of Swimming and Climbing", "Item214", 2000, 1, 1, 50, 20)
item215 = magicItem("Gloves of Thievery", "Item215", 5000, 1, 1, 50, 20)
item216 = magicItem("Goggles of Night", "Item216", 1500, 1, 1, 50, 20)
item217 = magicItem("Goggles of Object Reading", "Item217", 5000, 1, 1, 50, 20)
item218 = magicItem("Hat of Disguise", "Item218", 5000, 1, 1, 50, 20)
item219 = magicItem("Helm of Comprehend Languages", "Item219", 1000, 1, 1, 50, 20)
item220 = magicItem("Amulet of Proof Against Detection and Location", "Item220", 20000, 1, 1, 30, 50)
item221 = magicItem("Medallion of Thoughts", "Item221", 3000, 1, 1, 50, 20)
item222 = magicItem("Nature's Mantle", "Item221", 5000, 1, 1, 50, 20)
item223 = magicItem("Necklace of Adaptation", "Item222", 1500, 1, 1, 50, 20)
item224 = magicItem("Pearl of Power", "Item224", 6000, 1, 1, 40, 20)
item225 = magicItem("Periapt of Health", "Item225", 5000, 1, 1, 50, 20)
item226 = magicItem("Ring of Warmth", "Item226", 1000, 1, 1, 50, 20)
item227 = magicItem("Sentinel Shield", "Item227", 20000, 1, 1, 30, 50)
item228 = magicItem("Slippers of Spider Climbing", "Item228", 5000, 1, 1, 50, 20)
item229 = magicItem("Trident of Fish Command", "Item229", 800, 1, 1, 50, 20)
item230 = magicItem("Wand of Web", "Item230", 8000, 1, 1, 50, 20)
item231 = magicItem("Hew", "Item231", 1000, 1, 1, 50, 20)
item232 = magicItem("Immovable Rod", "Item232", 5000, 1, 1, 50, 20)
item233 = magicItem("Wand of Web", "Item230", 1500, 1, 1, 50, 20)


#Item lists
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
item020,
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
item040,
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
item073
]

potions = [
item074,
item075,
item076,
item077,
item078,
item079,
item080,
item081,
item082,
item083,
item084,
item085,
item086,
item087,
item088,
item089,
item090,
item091,
item092,
item093,
item094,
item095,
item096,
item097,
item098,
item099,
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
#poisons start here
item163,
item164,
item165,
item166,
item167,
item168,
item169,
item170,
item171,
item172,
item173,
item174,
item175,
item176,
]

weapons = [
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
item149
]

armors = [
item150,
item151,
item152,
item153,
item154,
item155,
item156,
item157,
item158,
item159,
item160,
item161,
item162,
]

magicItems = [
item177,
item178,
item179,
item180,
item181,
item182,
item183,
item184,
item185,
item186,
item187,
item188,
item189,
item190,
item191,
item192,
item193,
item194,
item195,
item196,
item197,
item198,
item199,
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
item233
]
