from CvPythonExtensions import *
import CvUtil


gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class YieldTypes:
    YIELD_CLOTH = 0
    YIELD_TOBACCO = 1
    YIELD_SUGAR = 2
    YIELD_FUR = 3
    YIELD_SILVER = 4
    YIELD_FOOD = 5
    YIELD_LUMBER = 6
    YIELD_COTTON = 7
    YIELD_RUM = 8
    YIELD_CIGARS = 9
    YIELD_COATS = 10
    YIELD_GOODS = 11
    YIELD_HAMMERS = 12
    YIELD_BELLS = 13
    YIELD_CROSSES = 14
    YIELD_EDUCATION = 15
    YIELD_HEALTH = 16
    YIELD_HAPPINESS = 17
    YIELD_GOLD = 18
    YIELD_ORE = 19
    YIELD_TOOLS = 20
    YIELD_MUSKETS = 21
    YIELD_HORSES = 22
    YIELD_TREASURE = 23
    # Add more as needed

ALL_TRADE_YIELDS = [
    # RAW GOODS
    YieldTypes.YIELD_FOOD,
    YieldTypes.YIELD_LUMBER,
    YieldTypes.YIELD_COTTON,
    YieldTypes.YIELD_TOBACCO,
    YieldTypes.YIELD_SUGAR,
    YieldTypes.YIELD_FUR,
    YieldTypes.YIELD_ORE,
    # PROCESSED GOODS
    YieldTypes.YIELD_CLOTH,
    YieldTypes.YIELD_COATS,
    YieldTypes.YIELD_RUM,
    YieldTypes.YIELD_CIGARS,
    # SPECIAL YIELDS
    YieldTypes.YIELD_SILVER,
    YieldTypes.YIELD_TOOLS,
    YieldTypes.YIELD_MUSKETS,
    YieldTypes.YIELD_HORSES
]

ALL_YIELD_TYPES = [
    YieldTypes.YIELD_FOOD,
    YieldTypes.YIELD_LUMBER,
    YieldTypes.YIELD_COTTON,
    YieldTypes.YIELD_FUR,
    YieldTypes.YIELD_SILVER,
    YieldTypes.YIELD_TOBACCO,
    YieldTypes.YIELD_SUGAR,
    YieldTypes.YIELD_CLOTH,
    YieldTypes.YIELD_RUM,
    YieldTypes.YIELD_CIGARS,
    YieldTypes.YIELD_COATS,
    YieldTypes.YIELD_GOODS,
    YieldTypes.YIELD_HAMMERS,
    YieldTypes.YIELD_BELLS,
    YieldTypes.YIELD_CROSSES,
    YieldTypes.YIELD_EDUCATION,
    YieldTypes.YIELD_HEALTH,
    YieldTypes.YIELD_HAPPINESS,
    YieldTypes.YIELD_GOLD,
    YieldTypes.YIELD_TREASURE,
    YieldTypes.YIELD_TOOLS,
    YieldTypes.YIELD_MUSKETS,
    YieldTypes.YIELD_HORSES
]

SCREEN_YIELD_FILTERS = {
    "LocalScreen": [ YieldTypes.YIELD_FOOD,YieldTypes.YIELD_LUMBER,YieldTypes.YIELD_COATS,YieldTypes.YIELD_RUM, YieldTypes.YIELD_CIGARS],
    "AfricaScreen": [YieldTypes.YIELD_FOOD, YieldTypes.YIELD_FUR],
    "CaribbeanScreen": [YieldTypes.YIELD_SUGAR, YieldTypes.YIELD_FOOD]
}
