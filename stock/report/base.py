# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"建仓平仓报价", pos=wx.DefaultPosition, size=wx.Size(323, 556),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"哪个盘", wx.Point(-1, -1), wx.Size(-1, -1), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        choice_marketChoices = [u"粤贵", u"冠东"]
        self.choice_market = wx.RadioBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         choice_marketChoices, 1, wx.RA_SPECIFY_ROWS)
        self.choice_market.SetSelection(0)
        fgSizer2.Add(self.choice_market, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"客户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText31.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText31.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText31, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.text_client_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.text_client_name, 0, wx.ALL, 5)

        self.m_staticText312 = wx.StaticText(self, wx.ID_ANY, u"商品", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText312.Wrap(-1)
        self.m_staticText312.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText312.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText312.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText312, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        choice_goodsChoices = [u"粤贵银", u"粤贵钯", u"粤贵铂", u"粤东油", u"粤东油B"]
        self.choice_goods = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_goodsChoices, 0)
        self.choice_goods.SetSelection(0)
        fgSizer2.Add(self.choice_goods, 0, wx.ALL, 5)

        self.m_staticText3111 = wx.StaticText(self, wx.ID_ANY, u"操作类型", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3111.Wrap(-1)
        self.m_staticText3111.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText3111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText3111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        choice_actionChoices = [u"建仓", u"平仓"]
        self.choice_action = wx.RadioBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         choice_actionChoices, 1, wx.RA_SPECIFY_ROWS)
        self.choice_action.SetSelection(1)
        fgSizer2.Add(self.choice_action, 0, wx.ALL, 5)

        self.m_staticText311 = wx.StaticText(self, wx.ID_ANY, u"建仓方向", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText311.Wrap(-1)
        self.m_staticText311.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText311.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText311.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText311, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        choice_directionChoices = [u"揸", u"沽"]
        self.choice_direction = wx.RadioBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            choice_directionChoices, 1, wx.RA_SPECIFY_ROWS)
        self.choice_direction.SetSelection(0)
        fgSizer2.Add(self.choice_direction, 0, wx.ALL, 5)

        self.m_staticText31111 = wx.StaticText(self, wx.ID_ANY, u"数量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31111.Wrap(-1)
        self.m_staticText31111.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText31111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText31111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText31111, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.text_number = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.text_number, 0, wx.ALL, 5)

        self.m_staticText311111 = wx.StaticText(self, wx.ID_ANY, u"建仓价", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText311111.Wrap(-1)
        self.m_staticText311111.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText311111.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText311111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.m_staticText311111, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.text_price_in = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.text_price_in, 0, wx.ALL, 5)

        self.static_text_price_out = wx.StaticText(self, wx.ID_ANY, u"平仓价", wx.DefaultPosition, wx.DefaultSize, 0)
        self.static_text_price_out.Wrap(-1)
        self.static_text_price_out.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.static_text_price_out.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.static_text_price_out.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        fgSizer2.Add(self.static_text_price_out, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.text_price_out = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.text_price_out, 0, wx.ALL, 5)

        self.button_ok = wx.Button(self, wx.ID_ANY, u"追加", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.button_ok, 0, wx.ALL, 5)

        self.button_clean = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.button_clean, 0, wx.ALL, 5)

        fgSizer2.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        fgSizer2.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer6.Add(fgSizer2, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.text_output = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, 120),
                                       wx.TE_MULTILINE)
        bSizer6.Add(self.text_output, 0, wx.ALL, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.choice_market.Bind(wx.EVT_RADIOBOX, self.event_choice_market)
        self.choice_action.Bind(wx.EVT_RADIOBOX, self.func_radio_type_in)
        self.choice_direction.Bind(wx.EVT_RADIOBOX, self.func_radio_type_in)
        self.button_ok.Bind(wx.EVT_BUTTON, self.func_append)
        self.button_clean.Bind(wx.EVT_BUTTON, self.func_clean)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def event_choice_market(self, event):
        event.Skip()

    def func_radio_type_in(self, event):
        event.Skip()

    def func_append(self, event):
        event.Skip()

    def func_clean(self, event):
        event.Skip()


