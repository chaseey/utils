#coding=utf-8
__author__ = 'kidd'

import six
import wx
from base import MyFrame1
import threading


class MainWindow(MyFrame1):
    # MARKET_CHOICES_YUEGUI = [u"粤贵银", u"粤贵钯", u'粤贵铂']
    # MARKET_CHOICES_GUANDONG = [u'冠东油', u'冠东油B']

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


    def func_append(self, event):
        market = self.choice_market.GetString(self.choice_market.GetSelection())
        client_name = self.text_client_name.GetValue()
        choice_direction = self.choice_direction.GetString(self.choice_direction.GetSelection()) # 0 揸， 1 沽
        choice_action = self.choice_action.GetString(self.choice_action.GetSelection())  # 0建仓 1 平仓
        goods = self.choice_goods.GetString(self.choice_goods.GetSelection())
        num = self.text_number.GetValue()
        price_in = self.text_price_in.GetValue()
        price_out = self.text_price_out.GetValue()



        num_unit = 'KG' if market == u'粤贵' else u'手'
        msg = u'{market} {client_name} {choice_action}{num}{num_unit} {goods} {choice_direction}单,'\
              u'建仓价{price_in}'.format(
            market=market,
            client_name=client_name,
            choice_action=choice_action,
            goods=goods,
            num=num,
            num_unit=num_unit,
            choice_direction=choice_direction,
            price_in=price_in,
        )
        if choice_action == u'平仓':
            msg = u'{} 平仓价{}'.format(
                msg, price_out
            )
        output = u"{}\n{}\n".format(
            self.text_output.GetValue().strip(),
            msg)


        self.text_output.SetValue(output.lstrip())

    def event_choice_market(self, event):
        market = self.choice_market.GetString(self.choice_market.GetSelection())



    def func_clean(self, event):
        self.text_output.SetValue("")


    def func_radio_type_in(self, event):
        choice_action = self.choice_action.GetString(self.choice_action.GetSelection())  # 0建仓 1 平仓
        if choice_action == u'建仓':
            self.static_text_price_out.Hide()
            self.text_price_out.Hide()
        else:
            self.static_text_price_out.Show()
            self.text_price_out.Show()





if __name__ == '__main__':
    app = wx.App()
    main_win = MainWindow(None)
    main_win.Show()
    app.MainLoop()





