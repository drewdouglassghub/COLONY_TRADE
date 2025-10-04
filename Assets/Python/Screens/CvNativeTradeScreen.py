from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

# globals
# Allowed yields for local trade
# ALLOWED_LOCAL_TRADE_YIELDS = [
#     YieldTypes.YIELD_CORN,
#     YieldTypes.YIELD_TOBACCO,
#     YieldTypes.YIELD_SUGAR,
#     YieldTypes.YIELD_FUR
# ]

gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class CvNativeTradeScreen:
	
    def __init__(self):
        self.SCREEN_ID = "NATIVE_TRADE_SCREEN"
        self.WIDGET_ID = "nativeTradeScreen"
        gc.getGame().setScriptData("NATIVE_TRADE_SCREEN")
    def getScreen(self):
        return CyGInterfaceScreen("nativeTradeScreen", CvScreenEnums.NATIVE_TRADE_SCREEN)
  
    def interfaceScreen(self):
        if gc.getPlayer(gc.getGame().getActivePlayer()).getParent() == PlayerTypes.NO_PLAYER:
            return
	
        screen = self.getScreen()
        if screen.isActive():
            return
        
        
        self.XResolution = screen.getXResolution()
        self.YResolution = screen.getYResolution()

        self.Y_EXIT = self.YResolution - 36
        self.X_EXIT = self.XResolution - 30

        self.Y_RATES = int((self.YResolution - 55) * 36 / 40)

        self.IN_PORT_PANE_WIDTH = int(self.XResolution * 9 / 20)
        self.X_IN_PORT = int(self.XResolution * 3 / 10)
        self.PANE_HEIGHT = int((self.YResolution - 55) * 31 / 40)
        self.X_DOCK = int(self.XResolution * 7 / 10)

        self.SHIP_ICON_SIZE = int(self.YResolution / 10)
        self.CARGO_ICON_SIZE = int(self.XResolution / 25)
        self.CARGO_SPACING  = self.CARGO_ICON_SIZE + 2

        self.H_TEXT_MARGIN = int(self.YResolution / 30)
        self.W_TEXT_MARGIN = int(self.XResolution / 30)

        self.X_RECRUIT_PANE = int(self.X_IN_PORT + self.IN_PORT_PANE_WIDTH + (self.W_TEXT_MARGIN / 2))
        self.PANE_WIDTH = int(self.XResolution * 7 / 20)
        self.W_SLIDER = self.PANE_WIDTH - (self.W_TEXT_MARGIN * 2)
        self.H_LOADING_SLIDER = int(self.YResolution * 7 / 10)
        self.Y_UPPER_EDGE = int(self.YResolution / 10)
        self.RECRUIT_PANE_HEIGHT = int(self.YResolution / 7)

        self.Y_RECRUIT_OFFSET = 25
        self.Y_TITLE = 4
        self.Y_BOUND = int(self.Y_UPPER_EDGE + (self.PANE_HEIGHT / 2))
        self.Y_DOCKS_OFFSET = 50
        self.H_DOCK = int((self.PANE_HEIGHT - (self.H_TEXT_MARGIN * 2)) * 35 / 100)

        screen.setRenderInterfaceOnly(True)
        screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)

        # Background panel
        screen.addDDSGFC("EuropeScreenBackground", ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_BACKGROUND").getPath(), 0, 0, self.XResolution, self.YResolution, WidgetTypes.WIDGET_GENERAL, -1, -1 )
        screen.addDDSGFC("BottomPanel", ArtFileMgr.getInterfaceArtInfo("INTERFACE_SCREEN_TAB_OFF").getPath(), 0, self.YResolution - 55, self.XResolution, 55, WidgetTypes.WIDGET_GENERAL, -1, -1 )
       
       # Header...
        screen.setLabel("NativeScreenWidgetHeader", "Background", u"<font=4b>" + localText.getText("Local Trade", ()).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, int(self.XResolution / 2), self.Y_TITLE, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

       
       
    #    # Messages
        # screen.addDDSGFC("EuropeScreenMessageImage_Native", ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_SHADOW_BOX").getPath(), self.X_IN_PORT + self.IN_PORT_PANE_WIDTH - (self.W_TEXT_MARGIN / 2), self.Y_UPPER_EDGE + self.RECRUIT_PANE_HEIGHT + self.H_TEXT_MARGIN + self.H_DOCK + 60, self.PANE_WIDTH, self.H_DOCK, WidgetTypes.WIDGET_GENERAL, -1, -1 )
        # screen.addListBoxGFC("MessageList", "", self.X_IN_PORT + self.IN_PORT_PANE_WIDTH, self.Y_UPPER_EDGE + self.RECRUIT_PANE_HEIGHT + self.H_TEXT_MARGIN + self.H_DOCK + 60, self.PANE_WIDTH - (self.W_TEXT_MARGIN * 3), self.H_DOCK, TableStyles.TABLE_STYLE_STANDARD)
        # screen.enableSelect("MessageList", False)
        # szText = localText.changeTextColor(localText.getText("TXT_KEY_KING_DREW", ()).upper(), gc.getInfoTypeForString("COLOR_FONT_CREAM"))
        # screen.setLabel("EuropeScreenMessageText", "Background", u"<font=4>" + szText + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_DOCK + self.PANE_WIDTH / 2, self.Y_UPPER_EDGE + self.RECRUIT_PANE_HEIGHT + self.H_TEXT_MARGIN + self.H_DOCK + 40, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

    
    def drawContents(self):
        # player = gc.getPlayer(gc.getGame().getActivePlayer())
        # # playerEurope = gc.getPlayer(player.getParent())

        # self.deleteAllWidgets()

        # screen = self.getScreen()
        # # # Trade Messages
        # # screen.clearListBoxGFC("MessageList")
        # # for i in range(player.getNumTradeMessages()):
        # #     screen.prependListBoxString("MessageList", player.getTradeMessage(i), WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY )

        # # Yield Rates
        # YieldList = []
        # for iYield in range(YieldTypes.NUM_YIELD_TYPES):
        #     kYield = gc.getYieldInfo(iYield)
        #     if kYield.isCargo():
        #         YieldList.append(iYield)

        # YieldAreaWidth = (self.XResolution / 20) * len(YieldList)
        # xLocation = (self.XResolution / 2) - (YieldAreaWidth / 2) - 10
        # BoxSize = self.XResolution / (len(YieldList) + 1)
        # for iYield in ALLOWED_LOCAL_TRADE_YIELDS:
        #     self.drawYieldTradeOption(iYield)
        # for iYield in getAllowedYieldsForCiv(self.currentTradeMarket):
        # self.drawYieldTradeOption(iYield)


        # screen.addDDSGFC(self.getNextWidgetName(), ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_BOX_PRICE").getPath(), xLocation - BoxSize, self.Y_RATES, BoxSize, BoxSize, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1 )
        # screen.addDragableButton(self.getNextWidgetName(), gc.getYieldInfo(iYield).getIcon(), "", xLocation - BoxSize + (BoxSize / 8), self.Y_RATES + (BoxSize / 3), BoxSize * 3 / 4, BoxSize * 3 / 4, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1, ButtonStyles.BUTTON_STYLE_IMAGE )
        # if not player.isYieldEuropeTradable(iYield): 
        #    szPrices = u"<font=4>%d/%d</font>" % (iBuyPrice, iSellPrice)
        # screen.setLabel(self.getNextWidgetName(), "Background", szPrices, CvUtil.FONT_CENTER_JUSTIFY, xLocation - (BoxSize / 2), self.Y_RATES, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1)
        # xLocation += BoxSize
        # szWidget = self.getNextWidgetName()
        # screen.addStackedBarGFC(szWidget, self.XResolution * 3 / 8, self.Y_EXIT, self.XResolution / 4, 30, InfoBarTypes.NUM_INFOBAR_TYPES, WidgetTypes.WIDGET_GENERAL, self.HELP_CROSS_RATE, -1)
        # screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_STORED, gc.getInfoTypeForString("COLOR_GREAT_PEOPLE_STORED"))
        # screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_RATE, gc.getInfoTypeForString("COLOR_GREAT_PEOPLE_RATE"))
        # screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_RATE_EXTRA, gc.getInfoTypeForString("COLOR_EMPTY"))
        # screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_EMPTY, gc.getInfoTypeForString("COLOR_EMPTY"))
        # fStoredPercent = float(player.getCrossesStored()) / float(player.immigrationThreshold())
        # screen.setBarPercentage(szWidget, InfoBarTypes.INFOBAR_STORED, fStoredPercent)
        # if (fStoredPercent < 1.0):
        #     fRatePercent = float(player.getYieldRate(YieldTypes.YIELD_CROSSES)) / float(player.immigrationThreshold()) / (1 - fStoredPercent)
        #     screen.setBarPercentage(szWidget, InfoBarTypes.INFOBAR_RATE, fRatePercent)
        # screen.setLabel(self.getNextWidgetName(), "", u"<font=3>" + localText.getText("TXT_KEY_IMMIGRATION_BAR", (player.getCrossesStored(), player.immigrationThreshold(), gc.getYieldInfo(YieldTypes.YIELD_CROSSES).getChar())) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, self.Y_EXIT + 3, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, self.HELP_CROSS_RATE, -1)

        return 0

    def handleInput(self, inputClass):
        'Calls function mapped in EuropeScreenInputMap'

        if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_CLICKED):

            if (inputClass.getButtonType() == WidgetTypes.WIDGET_GENERAL):

                if (inputClass.getData1() == self.BUY_UNIT_BUTTON_ID) :
                    popupInfo = CyPopupInfo()
                    popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PURCHASE_EUROPE_UNIT)
                    CyInterface().addPopup(popupInfo, gc.getGame().getActivePlayer(), true, false)

                elif (inputClass.getData1() == self.SAIL_TO_NEW_WORLD) :
                    activePlayer = gc.getPlayer(gc.getGame().getActivePlayer())
                    transport = activePlayer.getUnit(inputClass.getData2())
                    if (not transport.isNone()) and transport.getUnitTravelState() != UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE:
                        CyMessageControl().sendDoCommand(inputClass.getData2(), CommandTypes.COMMAND_SAIL_TO_EUROPE, UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE, self.EUROPE_EAST, false)

                elif (inputClass.getData1() == self.SAIL_TO_NEW_WORLD_WEST) :
                    activePlayer = gc.getPlayer(gc.getGame().getActivePlayer())
                    transport = activePlayer.getUnit(inputClass.getData2())
                    if (not transport.isNone()) and transport.getUnitTravelState() != UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE:
                        CyMessageControl().sendDoCommand(inputClass.getData2(), CommandTypes.COMMAND_SAIL_TO_EUROPE, UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE, self.EUROPE_WEST, false)

                elif (inputClass.getData1() == self.SELL_ALL) :
                    player = gc.getPlayer(gc.getGame().getActivePlayer())
                    transport = player.getUnit(inputClass.getData2())

                    (unit, iter) = player.firstUnit()
                    while (unit):
                        if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_IN_EUROPE and unit.isCargo() and unit.isGoods()):
                            if (unit.getTransportUnit().getID() == transport.getID()):
                                CyMessageControl().sendPlayerAction(player.getID(), PlayerActionTypes.PLAYER_ACTION_SELL_YIELD_UNIT, 0, unit.getYieldStored(), unit.getID())
                        (unit, iter) = player.nextUnit(iter)

                elif (inputClass.getData1() == self.LOAD_ALL) :
                    player = gc.getPlayer(gc.getGame().getActivePlayer())
                    transport = player.getUnit(inputClass.getData2())
                    for i in range(player.getNumEuropeUnits()):
                        loopUnit = player.getEuropeUnit(i)
                        if (not transport.isNone() and transport.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_IN_EUROPE and not transport.isFull()):
                            CyMessageControl().sendPlayerAction(player.getID(), PlayerActionTypes.PLAYER_ACTION_LOAD_UNIT_FROM_EUROPE, loopUnit.getID(), inputClass.getData2(), -1)

        return 0
    
    def update(self, fDelta):

        if CyInterface().isDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT):
            scriptFlag = gc.getGame().getScriptData()
            
        if (CvScreenEnums.NATIVE_TRADE_SCREEN):
            self.drawContents()  # or your custom refresh logic
            CyInterface().setDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT, False)
            gc.getGame().setScriptData("")  # clear flag

        if (CyInterface().isDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT)):
                CyInterface().setDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT, False)
                self.drawContents()


