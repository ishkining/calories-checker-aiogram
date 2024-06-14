from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lang import KEYBOARD_INFO

BASE_LANG = 'EN'


def intro_menu_keyboard():
    builder = InlineKeyboardBuilder()

    insert_data_btn = InlineKeyboardButton(text=KEYBOARD_INFO[BASE_LANG]['insert_data_btn'], callback_data='insert_data_menu')
    info_btn = InlineKeyboardButton(text=KEYBOARD_INFO[BASE_LANG]['info_btn'], callback_data='info_data_menu')

    [builder.row(btn) for btn in [insert_data_btn, info_btn]]

    return builder.as_markup()


def insert_data_keyboard():
    builder = InlineKeyboardBuilder()

    for_today_btn = InlineKeyboardButton(text=KEYBOARD_INFO[BASE_LANG]['for_today_btn'], callback_data='1')
    specific_date_btn = InlineKeyboardButton(text=KEYBOARD_INFO[BASE_LANG]['specific_date_btn'], callback_data='1')
    back_btn = InlineKeyboardButton(text=KEYBOARD_INFO[BASE_LANG]['back_btn'], callback_data='to_intro_menu')

    [builder.row(btn) for btn in [for_today_btn, specific_date_btn, back_btn]]

    return builder.as_markup()
