from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class YieldTypes:
    YIELD_CORN = 0
    YIELD_TOBACCO = 1
    YIELD_SUGAR = 2
    YIELD_FUR = 3
    YIELD_SILVER = 4
    # Add more as needed

ALL_TRADE_YIELDS = [
    YieldTypes.YIELD_CORN,
    YieldTypes.YIELD_TOBACCO,
    YieldTypes.YIELD_SUGAR,
    YieldTypes.YIELD_FUR,
    YieldTypes.YIELD_SILVER
]

ALL_YIELD_TYPES = [
    YieldTypes.YIELD_FOOD,
    YieldTypes.YIELD_LUMBER,
    YieldTypes.YIELD_COTTON,
    YieldTypes.YIELD_FUR,
    YieldTypes.YIELD_SILVER,
    YieldTypes.YIELD_TOBACCO,
    YieldTypes.YIELD_SUGAR,
    YieldTypes.YIELD_CORN,
    YieldTypes.YIELD_COCOA,
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
    YieldTypes.YIELD_GOLD
]

SCREEN_YIELD_FILTERS = {
    "LocalScreen": [YieldTypes.YIELD_SILVER, YieldTypes.YIELD_TOBACCO],
    "AfricaScreen": [YieldTypes.YIELD_CORN, YieldTypes.YIELD_FUR],
    "CaribbeanScreen": [YieldTypes.YIELD_SUGAR, YieldTypes.YIELD_CORN]
}
