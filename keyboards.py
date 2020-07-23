from telegram import InlineKeyboardButton

main_keyboard = [
    [InlineKeyboardButton("Виставки 🖼", callback_data='ofam_exhibition'),
     InlineKeyboardButton("Події 🧐", callback_data='ofam_events')],

    [InlineKeyboardButton("Візит 🎩", callback_data='ofam_visit'),
     InlineKeyboardButton("OFAM Online 👨‍💻",
                          url='https://www.ofam.org.ua/ua/online#popup:3d_transmuseum')],

    [InlineKeyboardButton("Магазин 🛍 ", switch_inline_query_current_chat='ofam_shop'),
     InlineKeyboardButton("Допомогти 🤝", url='https://www.ofam.org.ua/ua/donate')]
]
