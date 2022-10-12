from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.ext import Dispatcher, ConversationHandler
# code  files
from settings import TOKEN
from function import *
from admin import *

update = Updater(token=TOKEN, use_context=True, workers=20000)

dispatcher: Dispatcher = update.dispatcher

hand_command = ConversationHandler(
    entry_points=[CommandHandler('start', start), ],
    states={
        1: [CommandHandler('start', start),
            CallbackQueryHandler(get_language),
            MessageHandler(Filters.text, user_first_start_lang_error)
            ],
        15: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + basic_batton_txt['uz'][0] + ')$'), start_registration),
             MessageHandler(Filters.regex('^(' + basic_batton_txt['uz'][1] + ')$'), about_company),
             MessageHandler(Filters.regex('^(' + basic_batton_txt['uz'][2] + ')$'), settings),

             MessageHandler(Filters.regex('^(' + basic_batton_txt['ru'][0] + ')$'), start_registration),
             MessageHandler(Filters.regex('^(' + basic_batton_txt['ru'][1] + ')$'), about_company),
             MessageHandler(Filters.regex('^(' + basic_batton_txt['ru'][2] + ')$'), settings),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.text, user_txt_bug)
             ],

        17: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + settings_basic_txt['uz'][0] + ')$'), set_language),
             MessageHandler(Filters.regex('^(' + settings_basic_txt['ru'][0] + ')$'), set_language),

             MessageHandler(Filters.regex('^(' + settings_basic_txt['uz'][1] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + settings_basic_txt['ru'][1] + ')$'), back_user),
             MessageHandler(Filters.text, user_txt_bug)
             ],
        18: [CommandHandler('start', start),
             CallbackQueryHandler(update_language),
             MessageHandler(Filters.text, user_txt_bug)
             ],
        20: [CommandHandler('start', start),
             MessageHandler(Filters.text, phone_number_bag_),
             MessageHandler(Filters.contact & Filters.forwarded, phone_number_bag_),
             MessageHandler(Filters.contact, get_contact)
             ],
        21: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.text, get_user_firstname),
             ],
        22: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.text, get_user_lastname),
             ],
        23: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.text, get_birtday_date),
             ],
        24: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.text, get_information),
             ],
        25: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.photo, get_passport_image),
             ],
        26: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),
             MessageHandler(Filters.photo, get_user_photo),
             ],
        27: [CommandHandler('start', start),
             MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
             MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),

             MessageHandler(Filters.regex('^(' + batton_user_data_txt['uz'][0] + ')$'), confirm_user_data),
             MessageHandler(Filters.regex('^(' + batton_user_data_txt['uz'][1] + ')$'), user_data_not_confirm_user),

             MessageHandler(Filters.regex('^(' + batton_user_data_txt['ru'][0] + ')$'), confirm_user_data),
             MessageHandler(Filters.regex('^(' + batton_user_data_txt['ru'][1] + ')$'), user_data_not_confirm_user),

             ],
        # admins
        1000: [CommandHandler('start', start),

               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['uz'][2] + ')$'), back_user),
               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['ru'][2] + ')$'), back_user),

               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['uz'][3] + ')$'), reklama),
               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['ru'][3] + ')$'), reklama),

               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['uz'][5] + ')$'), get_user_count),
               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['ru'][5] + ')$'), get_user_count),

               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['uz'][11] + ')$'), back_user),
               MessageHandler(Filters.regex('^(' + admin_basic_batton_txts['ru'][11] + ')$'), back_user),

               MessageHandler(Filters.text, user_txt_bug)
               ],

        4999: [
            CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),

            MessageHandler(Filters.text, get_link_batton),
        ],
        5000: [
            CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + back_txt['uz'] + ')$'), back_user),
            MessageHandler(Filters.regex('^(' + back_txt['ru'] + ')$'), back_user),

            MessageHandler(Filters.photo & Filters.forwarded, get_rek_photo),
            MessageHandler(Filters.video & Filters.forwarded, get_rek_video),
            MessageHandler(Filters.text & Filters.forwarded, get_rek_text),
            MessageHandler(Filters.voice & Filters.forwarded, get_rek_voice),

            MessageHandler(Filters.photo, get_rek_photo),
            MessageHandler(Filters.video, get_rek_video),
            MessageHandler(Filters.text, get_rek_text),
            MessageHandler(Filters.voice, get_rek_voice),
        ],
    },
    fallbacks=[CommandHandler('start', start), ]
)

dispatcher.add_handler(handler=hand_command)
update.start_polling()
print('started polling')
update.idle()
