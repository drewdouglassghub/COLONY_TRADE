from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums
import TradeYieldRegistry

# globals
# Allowed yields for local trade


gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class CvNativeTradeScreen:
	
    def __init__(self):
        self.SCREEN_ID = "NATIVE_TRADE_SCREEN"
        self.WIDGET_ID = "nativeTradeScreen"
        
        self.nWidgetCount = 0
        self.UNIT_BUTTON_ID = 1
        self.UNIT_CARGO_BUTTON_ID = 2
        self.BUY_YIELD_BUTTON_ID = 3
        self.YIELD_CARGO_BUTTON_ID = 4
        self.BUY_UNIT_BUTTON_ID = 5
        self.DOCK_BUTTON_ID = 6
        self.SAIL_TO_NEW_WORLD = 7
        self.SAIL_TO_NEW_WORLD_WEST = 12
        self.SELL_ALL = 8
        self.LOAD_ALL = 9
        self.HELP_CROSS_RATE = 10
        self.TREASURY_ID = 11

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

        self.Y_RATES = (self.YResolution - 170) * 36 / 40

        self.IN_PORT_PANE_WIDTH = self.XResolution * 9 / 20
        self.X_IN_PORT = self.XResolution * 3 / 10
        self.PANE_HEIGHT = (self.YResolution - 55) * 31 / 40
        self.X_DOCK = self.XResolution * 7 / 10

        self.SHIP_ICON_SIZE = self.YResolution / 10
        self.CARGO_ICON_SIZE = self.XResolution / 25
        self.CARGO_SPACING  = self.CARGO_ICON_SIZE + 2

        self.H_TEXT_MARGIN = self.YResolution / 30
        self.W_TEXT_MARGIN = self.XResolution / 30

        self.X_RECRUIT_PANE = self.X_IN_PORT + self.IN_PORT_PANE_WIDTH + (self.W_TEXT_MARGIN / 2)
        self.PANE_WIDTH = self.XResolution * 7 / 20
        self.W_SLIDER = self.PANE_WIDTH - (self.W_TEXT_MARGIN * 2)
        self.H_LOADING_SLIDER = self.YResolution * 7 / 10
        self.Y_UPPER_EDGE = self.YResolution / 10
        self.RECRUIT_PANE_HEIGHT = self.YResolution / 7

        self.Y_RECRUIT_OFFSET = 25
        self.Y_TITLE = 4
        self.Y_BOUND = self.Y_UPPER_EDGE + (self.PANE_HEIGHT / 2)
        self.Y_DOCKS_OFFSET = 50
        self.H_DOCK = (self.PANE_HEIGHT - (self.H_TEXT_MARGIN * 2)) * 35 / 100
  
        screen.setRenderInterfaceOnly(True)
        screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)

        # Background panel
        screen.addDDSGFC("EuropeScreenBackground", ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_BACKGROUND").getPath(), 0, 0, self.XResolution, self.YResolution, WidgetTypes.WIDGET_GENERAL, -1, -1 )
        screen.addDDSGFC("BottomPanel", ArtFileMgr.getInterfaceArtInfo("INTERFACE_SCREEN_TAB_OFF").getPath(), 0, self.YResolution - 55, self.XResolution, 55, WidgetTypes.WIDGET_GENERAL, -1, -1 )
       
       
       # Header...
        screen.setLabel("NativeScreenWidgetHeader", "Background", u"<font=4b>" + localText.getText("Local Trade", ()).upper() + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, int(self.XResolution / 2), self.Y_TITLE, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

        self.drawContents()
       
    #    # Messages
        # screen.addDDSGFC("EuropeScreenMessageImage_Native", ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_SHADOW_BOX").getPath(), self.X_IN_PORT + self.IN_PORT_PANE_WIDTH - (self.W_TEXT_MARGIN / 2), self.Y_UPPER_EDGE + self.RECRUIT_PANE_HEIGHT + self.H_TEXT_MARGIN + self.H_DOCK + 60, self.PANE_WIDTH, self.H_DOCK, WidgetTypes.WIDGET_GENERAL, -1, -1 )
        # screen.addListBoxGFC("MessageList", "", self.X_IN_PORT + self.IN_PORT_PANE_WIDTH, self.Y_UPPER_EDGE + self.RECRUIT_PANE_HEIGHT + self.H_TEXT_MARGIN + self.H_DOCK + 60, self.PANE_WIDTH - (self.W_TEXT_MARGIN * 3), self.H_DOCK, TableStyles.TABLE_STYLE_STANDARD)
        # screen.enableSelect("MessageList", False)
        # szText = localText.changeTextColor(localText.getText("TXT_KEY_KING_DREW", ()).upper(), gc.getInfoTypeForString("COLOR_FONT_CREAM"))
        # screen.setLabel("EuropeScreenMessageText", "Background", u"<font=4>" + szText + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.X_DOCK + self.PANE_WIDTH / 2, self.Y_UPPER_EDGE + self.RECRUIT_PANE_HEIGHT + self.H_TEXT_MARGIN + self.H_DOCK + 40, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

    
    def drawContents(self):
        player = gc.getPlayer(gc.getGame().getActivePlayer())
        playerEurope = gc.getPlayer(player.getParent())
        
        self.deleteAllWidgets()

        screen = self.getScreen()
        
        YieldAreaWidth = (self.XResolution / 20) * len(TradeYieldRegistry.ALL_TRADE_YIELDS)
        xLocation = (self.XResolution / 2) - (YieldAreaWidth / 2) - 10
        BoxSize = self.YResolution / (len(TradeYieldRegistry.SCREEN_YIELD_FILTERS["LocalScreen"]) + 3)
         # Available Yields
        # screen.addDDSGFC(self.getNextWidgetName(), ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_BOX_PRICE").getPath(), xLocation - BoxSize, self.Y_RATES, BoxSize, BoxSize, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1 )
        # screen.addDragableButton(self.getNextWidgetName(), gc.getYieldInfo(iYield).getIcon(), "", xLocation - BoxSize + (BoxSize / 8), self.Y_RATES + (BoxSize / 3), BoxSize * 3 / 4, BoxSize * 3 / 4, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1, ButtonStyles.BUTTON_STYLE_IMAGE )
               
        #     self.drawYieldTradeOption(iYield)
        # for iYield in SCREEN_YIELD_FILTERS["LocalScreen"]:
        #     self.drawYieldTradeOption(iYield)

                 
        for iYield in TradeYieldRegistry.SCREEN_YIELD_FILTERS["LocalScreen"]:
            kYield = gc.getYieldInfo(iYield)
            iSellPrice = playerEurope.getYieldSellPrice(iYield)
            iBuyPrice = playerEurope.getYieldBuyPrice(iYield)
            screen.addDDSGFC(self.getNextWidgetName(), ArtFileMgr.getInterfaceArtInfo("INTERFACE_EUROPE_BOX_PRICE").getPath(), xLocation - BoxSize, self.Y_RATES - 15, BoxSize, BoxSize, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1 )
            screen.addDragableButton(self.getNextWidgetName(), gc.getYieldInfo(iYield).getIcon(), "", xLocation - BoxSize + (BoxSize / 8), self.Y_RATES + (BoxSize / 3), BoxSize * 3 / 4, BoxSize * 3 / 4, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1, ButtonStyles.BUTTON_STYLE_IMAGE )
            szPrices = u"<font=4>%d/%d</font>" % (iBuyPrice, iSellPrice)
            screen.setLabel(self.getNextWidgetName(), "Background", szPrices, CvUtil.FONT_CENTER_JUSTIFY, xLocation - (BoxSize / 2), self.Y_RATES, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_MOVE_CARGO_TO_TRANSPORT, iYield, -1)
        
            xLocation += BoxSize
            
        szWidget = self.getNextWidgetName()       
        # if not player.isYieldEuropeTradable(iYield): 
        screen.addStackedBarGFC(szWidget, self.XResolution * 3 / 8, self.Y_EXIT, self.XResolution / 4, 30, InfoBarTypes.NUM_INFOBAR_TYPES, WidgetTypes.WIDGET_GENERAL, self.HELP_CROSS_RATE, -1)
        screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_STORED, gc.getInfoTypeForString("COLOR_GREAT_PEOPLE_STORED"))
        screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_RATE, gc.getInfoTypeForString("COLOR_GREAT_PEOPLE_RATE"))
        screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_RATE_EXTRA, gc.getInfoTypeForString("COLOR_EMPTY"))
        screen.setStackedBarColors(szWidget, InfoBarTypes.INFOBAR_EMPTY, gc.getInfoTypeForString("COLOR_EMPTY"))
        fStoredPercent = float(player.getCrossesStored()) / float(player.immigrationThreshold())
        screen.setBarPercentage(szWidget, InfoBarTypes.INFOBAR_STORED, fStoredPercent)
        if (fStoredPercent < 1.0):
            fRatePercent = float(player.getYieldRate(YieldTypes.YIELD_CROSSES)) / float(player.immigrationThreshold()) / (1 - fStoredPercent)
            screen.setBarPercentage(szWidget, InfoBarTypes.INFOBAR_RATE, fRatePercent)
        screen.setLabel(self.getNextWidgetName(), "", u"<font=3>" + localText.getText("TXT_KEY_IMMIGRATION_BAR", (player.getCrossesStored(), player.immigrationThreshold(), gc.getYieldInfo(YieldTypes.YIELD_CROSSES).getChar())) + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, self.Y_EXIT + 3, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, self.HELP_CROSS_RATE, -1)

        return 0

    def handleInput(self, inputClass):
        'Calls function mapped in EuropeScreenInputMap'

        # if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_CLICKED):

        #     if (inputClass.getButtonType() == WidgetTypes.WIDGET_GENERAL):

        #         if (inputClass.getData1() == self.BUY_UNIT_BUTTON_ID) :
        #             popupInfo = CyPopupInfo()
        #             popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PURCHASE_EUROPE_UNIT)
        #             CyInterface().addPopup(popupInfo, gc.getGame().getActivePlayer(), true, false)

        #         elif (inputClass.getData1() == self.SAIL_TO_NEW_WORLD) :
        #             activePlayer = gc.getPlayer(gc.getGame().getActivePlayer())
        #             transport = activePlayer.getUnit(inputClass.getData2())
        #             if (not transport.isNone()) and transport.getUnitTravelState() != UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE:
        #                 CyMessageControl().sendDoCommand(inputClass.getData2(), CommandTypes.COMMAND_SAIL_TO_EUROPE, UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE, self.EUROPE_EAST, false)

        #         elif (inputClass.getData1() == self.SAIL_TO_NEW_WORLD_WEST) :
        #             activePlayer = gc.getPlayer(gc.getGame().getActivePlayer())
        #             transport = activePlayer.getUnit(inputClass.getData2())
        #             if (not transport.isNone()) and transport.getUnitTravelState() != UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE:
        #                 CyMessageControl().sendDoCommand(inputClass.getData2(), CommandTypes.COMMAND_SAIL_TO_EUROPE, UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE, self.EUROPE_WEST, false)

        #         elif (inputClass.getData1() == self.SELL_ALL) :
        #             player = gc.getPlayer(gc.getGame().getActivePlayer())
        #             transport = player.getUnit(inputClass.getData2())

        #             (unit, iter) = player.firstUnit()
        #             while (unit):
        #                 if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_IN_EUROPE and unit.isCargo() and unit.isGoods()):
        #                     if (unit.getTransportUnit().getID() == transport.getID()):
        #                         CyMessageControl().sendPlayerAction(player.getID(), PlayerActionTypes.PLAYER_ACTION_SELL_YIELD_UNIT, 0, unit.getYieldStored(), unit.getID())
        #                 (unit, iter) = player.nextUnit(iter)

        #         elif (inputClass.getData1() == self.LOAD_ALL) :
        #             player = gc.getPlayer(gc.getGame().getActivePlayer())
        #             transport = player.getUnit(inputClass.getData2())
        #             for i in range(player.getNumEuropeUnits()):
        #                 loopUnit = player.getEuropeUnit(i)
        #                 if (not transport.isNone() and transport.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_IN_EUROPE and not transport.isFull()):
        #                     CyMessageControl().sendPlayerAction(player.getID(), PlayerActionTypes.PLAYER_ACTION_LOAD_UNIT_FROM_EUROPE, loopUnit.getID(), inputClass.getData2(), -1)

        return 0
    
    def getNextWidgetName(self):
        szName = self.WIDGET_ID + str(self.nWidgetCount)
        self.nWidgetCount += 1
        return szName

    def deleteAllWidgets(self):
        screen = self.getScreen()
        i = self.nWidgetCount - 1
        while (i >= 0):
            self.nWidgetCount = i
            screen.deleteWidget(self.getNextWidgetName())
            i -= 1

        self.nWidgetCount = 0
    
    def update(self, fDelta):
        if CyInterface().isDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT):
            scriptFlag = gc.getGame().getScriptData()
            
        if scriptFlag == "NATIVE_TRADE_SCREEN":
            self.drawContents()  # or your custom refresh logic
            CyInterface().setDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT, False)
            gc.getGame().setScriptData("")  # clear flag
                   
    # def drawYieldTradeOption(self, iYieldType, iX, iY, szCallback=None, bEnabled=True):
    #     screen = self.getScreen()
    #     szName = "YieldTradeOption_%s" % iYieldType


    #     # Get yield icon path
    #     szIcon = gc.getYieldInfo(iYieldType).getButton()

    #     # Draw the yield button
    #     screen.addDDSGFC(szName, szIcon, iX, iY, 32, 32, WidgetTypes.WIDGET_GENERAL, -1, -1)
    #     screen.enable(szName, bEnabled)

    #     # Add tooltip
    #     szYieldName = gc.getYieldInfo(iYieldType).getDescription()
    #     szTooltip = "Trade %s with Europe" % szYieldName
    #     screen.setToolTip(szName, szTooltip)

    #     # Optional callback
    #     if szCallback:
    #         screen.setButtonCallback(szName, szCallback)

