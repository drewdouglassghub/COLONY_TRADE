from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums


gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

BASE_MARKET_PRICES = {
            YieldTypes.YIELD_ORE: 4,
            YieldTypes.YIELD_TOOLS: 8,
            YieldTypes.YIELD_FUR: 6,
        }


class TradePlayerRegistry:
    TRADE_PLAYERS = {
        "Local": gc.getGame().getLocalPlayer(),
        "Africa": gc.getGame().getAfricaPlayer(),
        "Caribbean": gc.getGame().getCaribbeanPlayer(),
        "LocalTraderA": 44,
        "LocalTraderB": 55,
    }

    PLAYER_YIELD_FILTERS = {
        "Local": ["YIELD_FOOD", "YIELD_LUMBER"],
        "Africa": ["YIELD_ORE", "YIELD_TOOLS"],
        "Caribbean": ["YIELD_FUR", "YIELD_COATS"],
    }

    

    @staticmethod
    def getBuyPrice(playerKey, eYield):
        iPlayer = TradePlayerRegistry.TRADE_PLAYERS[playerKey]
        if playerKey == "LocalTrader":
            
            stored = gc.getPlayer(iPlayer).getYieldStored(eYield)
            modifier = 0.9 if stored > 4 else 1000
            return int(BASE_MARKET_PRICES.get(eYield, 0) * modifier)
        # Otherwise default    
        return gc.getPlayer(iPlayer).getYieldBuyPrice(eYield)

    @staticmethod
    def getSellPrice(playerKey, eYield):
        iPlayer = TradePlayerRegistry.TRADE_PLAYERS[playerKey]
        return gc.getPlayer(iPlayer).getYieldSellPrice(eYield)

    @staticmethod
    def getTradeableYields(playerKey):
        return TradePlayerRegistry.PLAYER_YIELD_FILTERS.get(playerKey, [])