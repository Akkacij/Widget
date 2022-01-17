from datetime import datetime, timedelta
import random

from widget import Widget

from blocks.bl_time import BlockTime
from blocks.bl_time_to import BlockTimeTo
from blocks.ownblocks.bl_text_currency_USD import BlockTextCurrencyUSD
from blocks.bl_graph import BlockGraph
from database.db_currency import DataBaseCurrency


if __name__ == '__main__':
    wi = Widget(pos=3)
    # wi.add_block(BlockTime(wi), True)
    wi.add_block(BlockTextCurrencyUSD(wi), True)
    # wi.add_block(BlockGraph(wi), True)
    wi.add_block(BlockTimeTo(win=wi,
                             name="ЗП",
                             finish_message=[],
                             message=[],
                             cycle=True,
                             autonext=True,
                             d_month=1,
                             day=13,
                             hour=12,
                             minute=0,
                             second=0
                            ), True)
    wi.add_block(BlockTimeTo(win=wi,
                             name="Подъем",
                             finish_message=["ПОДЪЕМ!"],
                             message=[],
                             cycle=True,
                             autonext=True,
                             d_year=0,
                             d_month=0,
                             d_day=1,
                             d_hour=0,
                             d_minute=0,
                             d_second=0,
                             hour=7,
                             minute=30,
                             second=0
                             ), True)
    wi.add_block(BlockTimeTo(win=wi,
                             name="Учеба",
                             finish_message=["Жаль!"],
                             message=[],
                             cycle=True,
                             autonext=True,
                             day=26,
                             hour=0,
                             minute=0,
                             second=0
                             ), True)
    wi.alarm()
    wi.mainloop()

"""
Написать блок статистики и отображания
"""









# ################---------------------------__############################------------------__########################
#
#     # widget_inf['blocks_list'].append(BlockTime(win=window,
#     #                                            x=0+widget_inf['widget_blocks_indent'],
#     #                                            y=0+widget_inf['widget_blocks_indent']))
#     pos = (0 + widget_inf['widget_blocks_indent'], 0 + widget_inf['widget_blocks_indent'])
#     pos2 = (150 + widget_inf['widget_blocks_indent'], 0 + widget_inf['widget_blocks_indent'])
#     pos3 = (0 + widget_inf['widget_blocks_indent'], 70 + widget_inf['widget_blocks_indent'])
#     pos4 = (150 + widget_inf['widget_blocks_indent'], 70 + widget_inf['widget_blocks_indent'])
#     widget_inf['blocks_list'].append(BlockTime(win=window, x=pos[0], y=pos[1]))
#     # widget_inf['blocks_list'].append(BlockTime(win=window, x=pos2[0], y=pos2[1]))
#     widget_inf['blocks_list'].append(BlockTime(win=window, x=pos3[0], y=pos3[1]))
#     widget_inf['blocks_list'].append(BlockTime(win=window, x=pos4[0], y=pos4[1]))

#     # widget_inf['blocks_list'].append(BlockTime(win=window,
#     #                                        x=0 + widget_inf['widget_blocks_indent'],
#     #                                        y=0 + widget_inf['widget_blocks_indent']))
#
#     # img = PhotoImage(file="s.png")
#     # widget_inf['blocks_list'][0].canvas.create_image(42+30, 5.5+15, anchor='nw', image=img)
#
#     #_____________ Блок таймера кол-ва врмени до зап _____________
#     # widget_inf['blocks_list'].append(BlockTimeTo(win=window,
#     #                                              x=150+widget_inf['widget_blocks_indent'],
#     #                                              y=0+widget_inf['widget_blocks_indent'],
#     #                                              finish_message=["УРА!", "РАБОТАЕМ ДАЛЬШЕ!"],
#     #                                              message=["ЗАП"],
#     #                                              cycle=True,
#     #                                              autonext=True,
#     #                                              d_year=0,
#     #                                              d_month=1,
#     #                                              d_day=0,
#     #                                              d_hour=0,
#     #                                              d_minute=0,
#     #                                              d_second=0,
#     #                                              # year=2022,
#     #                                              # month=1,
#     #                                              day=15,
#     #                                              hour=12,
#     #                                              minute=0,
#     #                                              second=0
#     #                                              ))
#     # widget_inf['blocks_list'].append(BlockTimeTo(win=window,
#     #                                              x=0+widget_inf['widget_blocks_indent'],
#     #                                              y=70+widget_inf['widget_blocks_indent'],
#     #                                              finish_message=["ПОДЪЕМ!", "ВРЕМЯ ВСТАВАТЬ!"],
#     #                                              message=["ПОДЪЕМ"],
#     #                                              cycle=True,
#     #                                              autonext=True,
#     #                                              d_year=0,
#     #                                              d_month=0,
#     #                                              d_day=1,
#     #                                              d_hour=0,
#     #                                              d_minute=0,
#     #                                              d_second=0,
#     #                                              # year=2022,
#     #                                              # month=1,
#     #                                              # day=9,
#     #                                              hour=7,
#     #                                              minute=30,
#     #                                              second=0
#     #                                              ))
#     # _____________ Блок таймера кол-ва врмени до экза _____________
#     # widget_inf['blocks_list'].append(BlockTimeTo(win=window,
#     #                                              x=150 + widget_inf['widget_blocks_indent'],
#     #                                              y=70 + widget_inf['widget_blocks_indent'],
#     #                                              finish_message=["ЭКЗ!", ],
#     #                                              message=["ЭКЗАМЕН"],
#     #                                              day=10,
#     #                                              hour=16,
#     #                                              minute=0,
#     #                                              second=0
#     #                                              ))

