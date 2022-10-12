from telegram import ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup
from static import *


def admin_batton(lang='uz'):
    bt_txt = admin_basic_batton_txts[lang]
    batton = ReplyKeyboardMarkup([
        [bt_txt[0], bt_txt[1], bt_txt[2]],
        [bt_txt[3], bt_txt[4], bt_txt[5]],
        [bt_txt[6], bt_txt[7], bt_txt[8]],
        [bt_txt[9], bt_txt[10], bt_txt[11]]
    ], resize_keyboard=True)
    return batton


def help_massiv(massiv):
    len_ = len(massiv)
    name, link = [], []
    for item in range(0, len_):  # 0,1,2,3
        if item % 2 == 0:
            name.append(massiv[item])
        else:
            link.append(massiv[item])
    return [name, link]


def link_batton(data=None):
    massiv = help_massiv(data)
    massiv_len, batton, inline, k = len(massiv[0]), [], [], 1
    if massiv_len > 5:
        k = 2
    elif massiv_len > 2:
        k = 1
    else:
        k = 0
    for item in range(massiv_len):
        if len(inline) >= k:
            if k == 0 and not inline:
                inline.append(InlineKeyboardButton(text=massiv[0][item], url=f'{massiv[1][item]}'))
                continue
            inline.append(InlineKeyboardButton(text=massiv[0][item], url=f'{massiv[1][item]}'))
            batton.append(inline)
            inline = []
        else:
            inline.append(InlineKeyboardButton(text=massiv[0][item], url=f'{massiv[1][item]}'))
    batton.append(inline)
    reply_markup = InlineKeyboardMarkup(batton)
    return reply_markup