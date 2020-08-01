from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, \
    InputMediaPhoto, ParseMode
from keyboards import choose_keyboard
from sql_adapters.sqlite import SQLiteAdapter
import keyring

TOKEN = keyring.get_password("Telegram", "ofam_bot")

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    reply_markup = InlineKeyboardMarkup(choose_keyboard('main_keyboard'))

    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://static.tildacdn.com/tild6232-6236-4663-b934-356533636337/Frame.jpg',
                           caption='OFAM_bot Меню:',
                           reply_markup=reply_markup)


def inline_shop(update, context):
    query = update.inline_query.query
    if query == 'ofam_shop':
        results = list()
        db = SQLiteAdapter('ofam_bot.sqlite')
        shop_items = db.select_all('shop_items')
        for item in shop_items[1:25]:
            name, price, description, link, photo = item

            keyboard = [[InlineKeyboardButton("Меню 🖼", callback_data='send_menu')],
                        [InlineKeyboardButton("Нравится товар 🧐", callback_data='authors_events')],
                        [InlineKeyboardButton("Посмотреть на сайте 🧐", url=link)]]

            reply_markup = InlineKeyboardMarkup(keyboard)

            results.append(
                InlineQueryResultArticle(
                    id=name.upper(),
                    title=name,
                    thumb_url=photo,
                    description=f'{price}UAH',
                    reply_markup=reply_markup,
                    input_message_content=InputTextMessageContent(
                        message_text=f'{description}\nPrice: <a href="{photo}">{price} UAH</a>',
                        parse_mode=ParseMode.HTML,
                    )
                )
            )
        context.bot.answer_inline_query(update.inline_query.id, results)


def button(update, context):
    query = update.callback_query
    if query.data == 'send_menu':
        query.answer()

        reply_markup = InlineKeyboardMarkup(choose_keyboard('ofam_menu'))
        context.bot.send_photo(chat_id=update.callback_query.from_user.id,
                               photo='https://static.tildacdn.com/tild6232-6236-4663-b934-356533636337/Frame.jpg',
                               caption='OFAM_bot Меню:',
                               reply_markup=reply_markup)
    else:
        query.answer()

        db = SQLiteAdapter('ofam_bot.sqlite')
        result = db.select_from('buttons_content', '*', {'db_query': query.data})

        _, photo, text = result[0]

        reply_markup = InlineKeyboardMarkup(choose_keyboard(query.data))

        new_photo = InputMediaPhoto(media=photo)

        context.bot.edit_message_media(chat_id=update.effective_chat.id,
                                       message_id=update.callback_query.message.message_id,
                                       media=new_photo)

        context.bot.edit_message_caption(chat_id=update.effective_chat.id,
                                         message_id=update.callback_query.message.message_id,
                                         caption=text,
                                         parse_mode=ParseMode.HTML)

        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=update.callback_query.message.message_id,
                                              reply_markup=reply_markup)


start_handler = CommandHandler('start', start)
inline_shop_handler = InlineQueryHandler(inline_shop)
updater.dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(inline_shop_handler)

updater.start_polling()
