from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup
from keyboards import main_keyboard
import keyring

TOKEN = keyring.get_password("Telegram", "ofam_bot")

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    reply_markup = InlineKeyboardMarkup(main_keyboard)

    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://static.tildacdn.com/tild6232-6236-4663-b934-356533636337/Frame.jpg',
                           caption='OFAM_bot Меню:',
                           reply_markup=reply_markup)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
