from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardRemove
from telegram import ParseMode
from datetime import datetime
from battons import *
from static import *


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    get_user_from_db = database_db.get_user_if_id(chat_id)
    if get_user_from_db:
        update.message.reply_html(back_user_txt.get(get_user_from_db[3]),
                                  reply_markup=basic_batton(get_user_from_db[3]))
        return 15
    update.message.reply_html(when_the_user_first_logs_in_txt.get('uz'), reply_markup=language_batton())
    return 1


def get_language(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    lang = query.data
    query.delete_message(timeout=0.5)
    # context.user_data['language'] = lang
    database_db.insert_user(user.id, lang, user.username)
    context.bot.send_message(chat_id=user.id,
                             text=back_user_txt.get(lang),
                             parse_mode="HTML",
                             reply_markup=basic_batton(lang))
    return 15


def update_language_error_txt(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    update.message.reply_text(update_lang_txt_error.get(user_db[3]), parse_mode=ParseMode.HTML)
    return 1


def user_first_start_lang_error(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3] if user_db else 'ru'
    update.message.reply_html(update_lang_txt_error.get(lang), reply_markup=language_batton())
    return 1


def back_user(update, context):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    update.message.reply_html(back_user_txt.get(user_db[3]), reply_markup=basic_batton(user_db[3]))
    return 15


def user_txt_bug(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3] if user_db else 'ru'
    update.message.reply_text(user_txt_error.get(lang), parse_mode=ParseMode.HTML)
    return 15


def about_company(update: Update, context: CallbackContext):
    user = update.effective_user
    user_db = database_db.get_user_if_id(user.id)
    lang = user_db[3]
    bot_stats_text = {
        'uz': f"""
🛫 "Amerika orzusi" yohud nega butun dunyodan odamlar AQSHga intiladi? 

🎊 Xar yili millionlab odamlar Grin kard o‘ynaydi. Odamlar qalbida "Amerika orzusi" degan o‘y, tushuncha yashaydi. Qo‘shma Shtatlarda xayot tarzi qanday? Nega odamlar bu yurtga talpinadi?

💸 Xo‘sh, AQSHda taxminan maoshlar qancha? Yig‘lamang, so‘kinmang, asabiylashmasdan o‘qing:

🍽 Idish yuvuvchi va uy tozalovchi - 2300$;
🚗 Haydovchi - 2700$;
🪚 Qurilishdagi ishchilar - 2800$;
📞 Kotiba - 3100$;
📦 Yuk tashuvchi - 3200$;
👩‍⚕️ Hamshira - 3500$;
👩‍🍳 Oshpaz - 4000$;
👩‍🚒 O‘t o‘chiruvchi - 4000$;
💡 Elektrik - 4300$;
👮‍♂️ Militsiya - 4900$;
👨‍💼 O‘qituvchi - 6200$;
🚛 Yuk mashinasi haydovchisi - 7000$.
👨‍💻 Dasturchi - 9200$;
🩺 Terapevt - 9500$;
🏠 Injiner - 10200$;
🧑🏼‍⚖️ Advokat - 10500$;
🦷 Stomatolog - 13000$;
👨‍⚕️ Shifokor - 15700$;
<b>
"Qayerdagi ofisga borishimiz kerak"
"Ofisda to'ldirmasak ishonchsiz bo'lib qolmaydimi?"

1) Hechqanday ofisga borishingiz shart emas. Chunki bu onlayn lotereya, hammasi onlayn bajariladi

2) Ofisdagilar ham hamma bitta saytdan ro'yxatdan o'tkazishadi. Chunki green card sayti yagona va bitta.

Green Card saytini yuqorida keltirib o'tdim. Bu sayt orqali anketani bemalol o'zingiz ham to'ldirsangiz bo'ladi. Faqat ingliz tilini bilmasangiz va bunday ishlarga yaxshi tushunmasangiz bu ishni bizga topshiring😊
❗️Eslatma: Biz orqali ro'yxatdan o'tsangiz, Green Card Confirmation kodingizni darhol beramiz

☝️Chunki Green Card o'yinidagi kichik bir xato ham sizni Amerikaga keta olmasligingizga sabab bo'ladi

Link: https://t.me/GreenCardAdmins
</b>
""",
        'ru': f"""
🛫 «Американская мечта» или почему люди со всего мира стремятся в США?

🎊 Ежегодно миллионы людей играют в Green Card. Идея и концепция «американской мечты» живет в сердцах людей. Какова жизнь в Соединенных Штатах? Почему люди едут в эту страну?

💸 Итак, какие примерные зарплаты в США? Не плачь, не ругайся, читай не нервничая:

🍽 Посудомоечная машина и уборщица - 2300$;
🚗 Водитель - 2700$;
🪚 Строители - 2800 долларов;
📞 Секретарь - 3100$;
📦 Грузовик - 3200$;
👩‍⚕️ Медсестра - 3500$;
👩‍🍳 Шеф-повар - 4000$;
👩‍🚒 Пожарный - 4000 долларов;
💡Электричество - 4300$;
👮‍♂️ Полиция - 4900$;
👨‍💼 Учитель - 6200$;
🚛 Водитель грузовика - 7000 долларов.
👨‍💻 Разработчик - 9200$;
🩺 Терапевт - 9500$;
🏠 Инженер - 10 200 долларов;
🧑🏼‍⚖️ Юрист - 10 500 долларов США;
🦷 Стоматолог - $13 000;
👨‍⚕️ Доктор - 15700$;
<b>
«В какой кабинет нам пойти»
"Разве это не будет ненадежно, если мы не заполним офис?"

1) Вам не нужно идти в любой офис. Поскольку это онлайн-лотерея, все делается онлайн.

2) Все в офисе тоже регистрируются с одного сайта. Потому что сайт грин-карты единственный и неповторимый.

Я упомянул сайт Green Card выше. Вы можете легко заполнить анкету самостоятельно через этот сайт. Только если вы не знаете английского и плохо разбираетесь в таких вещах, доверьте эту работу нам
❗️Примечание. Если вы зарегистрируетесь через нас, мы сразу же предоставим вам код подтверждения грин-карты.

☝️Потому что даже небольшая ошибка в игре на грин-карту приведет к тому, что вы не сможете поехать в Америку

Ссылка: https://t.me/GreenCardAdmins
</b>
"""
    }
    update.message.reply_html(text=bot_stats_text.get(lang), reply_markup=basic_batton(lang))
    return 15


def settings(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    lang = database_db.get_user_if_id(chat_id)[3]
    admin = database_db.get_if_id_admin(chat_id)
    if admin:
        update.message.reply_html(text=settings_txt.get(lang, '<b>xatolik</b>'), reply_markup=admin_batton(lang))
        return 1000
    else:
        update.message.reply_html(text=settings_txt.get(lang, '<b>xatolik</b>'), reply_markup=settings_batton(lang))
    return 17
