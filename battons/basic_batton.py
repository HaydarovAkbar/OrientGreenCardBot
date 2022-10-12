from database import Database
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from static import *

database_db = Database()


def phone_batton(lang='uz'):
    phone = KeyboardButton(contact_batton_txt[lang], request_contact=True)
    contact_key = ReplyKeyboardMarkup([[phone]], resize_keyboard=True)
    return contact_key


def language_batton():
    result = InlineKeyboardMarkup([[InlineKeyboardButton("🇺🇿 O'zbek tili 🇺🇿", callback_data='uz')],
                                   [InlineKeyboardButton("🇷🇺 Русский 🇷🇺", callback_data='ru')]
                                   ])
    return result


def basic_batton(lang='uz'):
    key = basic_batton_txt[lang]
    batton = ReplyKeyboardMarkup([
        [key[0], key[1]],
        [key[2]]
    ], resize_keyboard=True)
    return batton


def back_batton(lang='uz'):
    batton = ReplyKeyboardMarkup([
        [back_txt[lang]],
    ], resize_keyboard=True)
    return batton


def get_user_data_confirm_batton(til='uz'):
    key = batton_user_data_txt.get(til)
    batton = ReplyKeyboardMarkup([
        [key[0], key[1]]
    ], resize_keyboard=True)
    return batton


def settings_batton(lang='uz'):
    batton = ReplyKeyboardMarkup([
        [settings_basic_txt[lang][0], settings_basic_txt[lang][1]]
    ], resize_keyboard=True)
    return batton
