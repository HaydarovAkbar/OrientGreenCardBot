from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove
from telegram import ParseMode
from datetime import datetime
from battons import *
from static import *

photo_group_id = -1001529246003


def start_registration(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    update.message.reply_html(text=enter_the_user_phone_number_txt.get(user_db[3]),
                              reply_markup=phone_batton(user_db[3]))
    return 20


def get_contact(update: Update, context: CallbackContext):
    contact = update.message.contact.phone_number
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    context.user_data['contact'] = contact
    update.message.reply_html(text=input_first_name_txt.get(lang, '<b>xatolik</b>'), reply_markup=ReplyKeyboardRemove())
    return 21


def phone_number_bag_(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_db = database_db.get_user_if_id(chat_id)
    lang = user_db[3]
    update.message.reply_html(text=phone_number_bag_text.get(lang, '<b>xatolik</b>'), reply_markup=phone_batton(lang))
    return 20


def get_user_firstname(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    text = update.message.text
    context.user_data['firstname'] = text
    update.message.reply_text(input_last_name_txt.get(lang), parse_mode=ParseMode.HTML, reply_markup=back_batton(lang))
    return 22


def get_user_lastname(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    text = update.message.text
    context.user_data['lastname'] = text
    context.bot.send_message(chat_id=update.effective_user.id, text=get_user_date_of_birthday_text.get(lang),
                             parse_mode=ParseMode.HTML, reply_markup=back_batton(lang))
    return 23


def get_birtday_date(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    birthday_date = update.message.text
    context.user_data['birthday'] = birthday_date
    update.message.reply_html(text=get_user_information_text.get(lang), reply_markup=back_batton(lang))
    return 24


def get_information(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    text = update.message.text
    if 'maktab' in text.lower() or 'kollej' in text.lower() or 'institut' in text.lower() or 'школа' in text.lower() or 'коллеж' in text.lower() or 'институт' in text.lower() or 'мактаб' in text.lower() or 'коллеж' in text.lower() or 'институт' in text.lower():
        birthday_date = update.message.text

        context.user_data['information'] = birthday_date
        context.bot.send_photo(chat_id=user.id, photo=open('passport.jpg', 'rb'))
        context.bot.send_message(chat_id=user.id, text=get_user_passport_text.get(lang), parse_mode='HTML',
                                 reply_markup=back_batton(lang))
        return 25
    else:
        update.message.reply_html(text=get_user_information_text.get(lang), reply_markup=back_batton(lang))
        return 24


def get_passport_image(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    photo = update.message.photo[-1]
    context.user_data['passport'] = photo
    context.bot.send_photo(chat_id=user.id, photo=open('user_photo.jpg', 'rb'))
    context.bot.send_message(chat_id=user.id, text=get_user_photo_text.get(lang), parse_mode='HTML',
                             reply_markup=back_batton(lang))
    return 26


def get_user_photo(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    photo = update.message.photo[-1]
    context.user_data['user_photo'] = photo

    chatid, username, phone_number, first_name, last_name = user.id, user.username, context.user_data[
        'contact'], context.user_data['firstname'], context.user_data['lastname']
    birthday_date, information = context.user_data['birthday'], context.user_data['information']
    bot_confirm_user_data_txt = {
        "uz": f"""
     <b>Ma'lmotlaringiz qabul qilindi! Ma'lumotlaringiz to‘g‘ri kiritilganligini tekshirib oling. 

Sizning malumotlaringiz:</b>\n

🔹 <b>Ismingiz: {first_name}
🔹 Familiyangiz: {last_name}
🔹 Username: @{username}
🔹 Tug'ulgan kuningiz: {birthday_date}
🔹 Malumotingiz: {information}
🔹 Telefon raqam: {phone_number}</b>

<code>Ma'lumotlaringizni tasdiqlaysizmi?</code>
     """,
        "ru": f"""
<b>Ваша информация принято!
Пожалуйста, проверьте правильность вашей данный.

Ваша данный:</b>\n

🔹 <b>Ваше имя: {first_name}
🔹 Твоя фамилия: {last_name}
🔹 Username: @{username}
🔹 Ваш день рождения: {birthday_date}
🔹 Ваша информация: {information}
🔹 Номер телефона: {phone_number}</b>

<code>Подтвердить информацию?</code>
     """,
    }

    context.bot.send_message(chat_id=user.id, text=bot_confirm_user_data_txt.get(lang, '<b>xatolik</b>'),
                             parse_mode=ParseMode.HTML,
                             reply_markup=get_user_data_confirm_batton(lang))
    return 27


def confirm_user_data(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    chatid, username, phone_number, first_name, last_name = user.id, user.username, context.user_data[
        'contact'], context.user_data['firstname'], context.user_data['lastname']
    birthday_date, information = context.user_data['birthday'], context.user_data['information']
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    group_photo_msg = context.bot.send_photo(chat_id=photo_group_id, photo=context.user_data['user_photo'],
                                             caption=f"#{user.id}\n{now}")
    group_photo_msg_url = f"https://t.me/orient_group_photos/{group_photo_msg['message_id']}"
    group_passport_msg = context.bot.send_photo(chat_id=photo_group_id, photo=context.user_data['passport'],
                                                caption=f"#{user.id}\n{now}")
    group_passport_msg_url = f"https://t.me/orient_group_photos/{group_passport_msg['message_id']}"
    user_db = database_db.get_user_if_id(user.id)
    username = user.username
    if not user_db:
        a = database_db.insert_registration(first_name, last_name, birthday_date, information, group_passport_msg_url,
                                            group_photo_msg_url,
                                            phone_number)
    bot_confirm_user_data_txt = {
        "uz": f"""
<b>Ma'lumotlaringiz qabul qilindi! Ma'lumotlaringiz to‘g‘ri kiritilganligini tekshirib oling. 

Sizning malumotlaringiz:\n

🔹 Ismingiz: {first_name}
🔹 Familiyangiz: {last_name}
🔹 Username: @{username}
🔹 Tug'ulgan kuningiz: {birthday_date}
🔹 Malumotingiz: {information}
🔹 Telefon raqam: {phone_number}
🔹 Passport: {group_passport_msg_url}
🔹 Rasm: {group_photo_msg_url}
</b>
    
<code>Ma'lumotlaringizni tasdiqlaysizmi?</code>
         """,
        "ru": f"""
<b>Ваша информация принято!
Пожалуйста, проверьте правильность вашей данный.

Ваша данный:\n

🔹 Ваше имя: {first_name}
🔹 Ваша фамилия: {last_name}
🔹 Имя пользователя: @{username}
🔹 Ваш день рождения: {birthday_date}
🔹 Ваша информация: {information}
🔹 Номер телефона: {phone_number}
🔹 Паспорт: {group_passport_msg_url}
🔹 Фото: {group_photo_msg_url}</b>

<code>Подтвердить информацию?</code>
         """,
    }
    context.bot.send_message(chat_id=photo_group_id, text=bot_confirm_user_data_txt.get(lang), parse_mode="HTML")
    update.message.reply_html(bot_menu_txt.get(lang), reply_markup=basic_batton(lang))
    return 15


def user_data_not_confirm_user(update, context):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    update.message.reply_html(delete_user_data_txt.get(lang), reply_markup=ReplyKeyboardRemove())
    update.message.reply_html(when_the_user_first_logs_in_txt.get(lang), reply_markup=basic_batton())
    return 15


def set_language(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    lang = database_db.get_user_if_id(chat_id)[3]
    update.message.reply_html(text=set_language_txt.get(lang, '<b>xatolik</b>'), reply_markup=language_batton())
    return 18


def update_language(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    query = update.callback_query
    database_db.update_lang(query.data, chat_id)
    new_lang = query.data
    query.message.delete(timeout=1)
    context.bot.send_message(chat_id=chat_id, text=update_bot_lang_txt.get(new_lang, '<b>xatolik</b>'),
                             parse_mode="HTML",
                             reply_markup=basic_batton(new_lang))
    return 15
