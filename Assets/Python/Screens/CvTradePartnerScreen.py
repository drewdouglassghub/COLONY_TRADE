from CvPythonExtensions import *
import CvScreenEnums
import CvUtil

gc = CyGlobalContext()

class CvTradePartnerScreen:
    def __init__(self):
        self.SCREEN_NAME = "TradePartnerScreen"

    def interfaceScreen(self):
        CyInterface().addMessage(gc.getGame().getActivePlayer(), True, 10,
                                 "Entered interfaceScreen()", "", 0, "",
                                 gc.getInfoTypeForString("COLOR_GREEN"), 0, 0,
                                 False, False)

        screen = CyGInterfaceScreen(self.SCREEN_NAME, CvScreenEnums.TRADE_PARTNER_SCREEN)
        screen.setDimensions(0, 0, screen.getXResolution(), screen.getYResolution())
        screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)

        screen.setLabel("TestLabel", "Background", u"Trade Partner Screen Loaded",
                        CvUtil.FONT_CENTER_JUSTIFY, screen.getXResolution() // 2, 100, 0,
                        FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
