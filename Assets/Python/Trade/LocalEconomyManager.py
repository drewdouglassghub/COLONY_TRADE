from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class LocalEconomyManager:
    iPlayer = TradePlayerRegistry.TRADE_PLAYERS["Local"]
    GoldOnHand = 1000
    
    