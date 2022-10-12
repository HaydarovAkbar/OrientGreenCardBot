import time

from telegram.ext import CallbackContext
from telegram import Update
from telegram import ParseMode
from datetime import datetime
from battons import *
from static import *
import random


# text reklama ?


def get_link_batton(update: Update, context: CallbackContext):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[3]
    text = update.message.text
    if text == 'Y':
        batton_lists = []
    else:
        batton_lists = []
        batton_list = [item for item in text.split(' - ')]
        for item in batton_list:
            if '\n' in item:
                for i in item.split('\n'):
                    batton_lists.append(i)
            else:
                batton_lists.append(item)
    context.chat_data['battons'] = batton_lists
    update.message.reply_html(text=reklama_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 5000


def reklama(update, context):
    user = update.effective_user
    user_lang = database_db.get_user_if_id(user.id)[3]
    update.message.reply_html(text=reklama_get_inline_batton_txt.get(user_lang), reply_markup=back_batton(user_lang))
    return 4999


def get_rek_photo(update: Update, context: CallbackContext):
    user_ = update.effective_user
    user_lang = database_db.get_user_if_id(user_.id)[3]
    photo, caption = update.message.photo[-1].file_id, update.message.caption
    c = 0
    a = context.bot.send_message(chat_id=user_.id, text=reklama_time_of_dispatch_txt.get(user_lang),parse_mode='HTML')
    if context.chat_data['battons']:
        for user in database_db.get_user_allID():
            try:
                update.message.bot.send_photo(chat_id=user[0],
                                              photo=photo,
                                              caption=caption,
                                              disable_notification=False,
                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_allID():
            try:
                context.bot.send_photo(chat_id=user[0],
                                       photo=photo,
                                       caption=caption)
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    context.bot.delete_message(chat_id=user_.id, message_id=a, timeout=1)
    context.bot.send_message(chat_id=758934089, text=f"XABAR {c}-ta foydalanuvchiga bordi")
    return 1000


def get_rek_video(update: Update, context: CallbackContext):
    user_ = update.effective_user
    user_lang = database_db.get_user_if_id(user_.id)[3]
    video, caption = update.message.video.file_id, update.message.caption
    c = 0
    a = context.bot.send_message(chat_id=user_.id, text=reklama_time_of_dispatch_txt.get(user_lang),parse_mode='HTML')
    if context.chat_data['battons']:
        for user in database_db.get_user_allID():
            try:
                update.message.bot.send_video(chat_id=user[0],
                                              video=video,
                                              caption=caption,
                                              disable_notification=False,
                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_allID():
            try:
                context.bot.send_video(chat_id=user[0],
                                       video=video,
                                       caption=caption)
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    context.bot.delete_message(chat_id=user_.id, message_id=a, timeout=1)
    context.bot.send_message(chat_id=758934089, text=f"XABAR {c}-ta foydalanuvchiga bordi")
    return 1000


def get_rek_voice(update: Update, context: CallbackContext):
    user_ = update.effective_user
    user_lang = database_db.get_user_if_id(user_.id)[3]
    voice, caption = update.message.voice.file_id, update.message.caption
    c = 0
    a = context.bot.send_message(chat_id=user_.id, text=reklama_time_of_dispatch_txt.get(user_lang),parse_mode='HTML')
    if context.chat_data['battons']:
        for user in database_db.get_user_allID():
            try:
                update.message.bot.send_voice(chat_id=user[0],
                                              voice=voice,
                                              caption=caption,
                                              disable_notification=False,
                                              reply_markup=link_batton(context.chat_data['battons']))
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_allID():
            try:
                context.bot.send_voice(chat_id=user[0],
                                       voice=voice,
                                       caption=caption)
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    context.bot.delete_message(chat_id=user_.id, message_id=a, timeout=1)
    context.bot.send_message(chat_id=758934089, text=f"XABAR {c}-ta foydalanuvchiga bordi")
    return 1000
    # update.message.bot.forward_message(chat_id=update.message.chat.id, from_chat_id='@' + channel_username, message_id=message_id)


def get_rek_text(update: Update, context: CallbackContext):
    text = update.message.text
    user_ = update.effective_user
    user_lang = database_db.get_user_if_id(user_.id)[3]
    c = 0
    a = context.bot.send_message(chat_id=user_.id, text=reklama_time_of_dispatch_txt.get(user_lang),parse_mode='HTML')
    if context.chat_data['battons']:
        for user in database_db.get_user_allID():
            try:
                update.message.bot.send_message(chat_id=user[0], text=text,
                                                reply_markup=link_batton(context.chat_data['battons']))
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    else:
        for user in database_db.get_user_allID():
            try:
                context.bot.send_message(chat_id=user[0], text=text)
                c += 1
                time.sleep(1)
            except Exception as e:
                print(e)
    context.bot.delete_message(chat_id=user_.id, message_id=a, timeout=1)
    context.bot.send_message(chat_id=758934089, text=f"XABAR {c}-ta foydalanuvchiga bordi")
    return 1000


def get_user_count(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_db = database_db.get_user_if_id(chat_id)
    lang = user_db[3] if user_db else context.user_data['language']
    user_count = database_db.get_all_userCOUNT()[0]
    admin_text = {
        "uz": f"<b>Botdan ro'yxatdan o'tganlar soni: {user_count}</b>",
        "ru": f"<b>Количество регистраций ботов: {user_count}</b>",
    }
    update.message.reply_html(text=admin_text.get(lang, '<b>xatolik</b>'), reply_markup=back_batton(lang))
    return 1000