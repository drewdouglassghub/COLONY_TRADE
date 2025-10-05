from CvPythonExtensions import *
gc = CyGlobalContext()


class RefreshRouter:
    def __init__(self):
        self.DIRTY_BIT = InterfaceDirtyBits.EuropeScreen_DIRTY_BIT  # ✅ moved here
        self.routes = {
            "REFRESH_TRADE_SCREEN": self.refreshTradeScreen,
            "REFRESH_NATIVE_SCREEN": self.refreshNativeScreen,
            # Add more routes here
        }

    def checkAndRoute(self):
        flag = gc.getGame().getScriptData()
        if flag == "REFRESH_TRADE_SCREEN":
            CvNativeTradeScreen.CvNativeTradeScreen().interfaceScreen()
            gc.getGame().setScriptData("")
            CyInterface().setDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT, False)
            flag = gc.getGame().getScriptData()
            if flag in self.routes:
                self.routes[flag]()  # Call the appropriate refresh function
                CyInterface().setDirty(self.DIRTY_BIT, False)
                gc.getGame().setScriptData("")  # Clear flag

    def refreshTradeScreen(self):
        import CvNativeTradeScreen
        CvNativeTradeScreen.CvNativeTradeScreen().interfaceScreen()

    def refreshNativeScreen(self):
        import CvNativeAdvisorScreen
        CvNativeAdvisorScreen.CvNativeAdvisorScreen().interfaceScreen()