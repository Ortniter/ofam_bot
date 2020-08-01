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

exhibition_keyboard = [
    [InlineKeyboardButton("Текущие 🖼", callback_data='current_exhibition'),
     InlineKeyboardButton("Вскоре 🧐", callback_data='future_exhibition')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_menu')]]

events_keyboard = [
    [InlineKeyboardButton("Регулярні екскурсії 🖼", callback_data='regular_events')],
    [InlineKeyboardButton("Авторські екскурсії 🧐", callback_data='authors_events')],
    [InlineKeyboardButton("Дитячі події 🎩", callback_data='child_events')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_menu')]]

visit_keyboard = [
    [InlineKeyboardButton("Загальна Інформація 🖼", callback_data='info')],
    [InlineKeyboardButton("Квитки 🧐", callback_data='tickets')],
    [InlineKeyboardButton("Пільги 🎩", callback_data='benefits')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_menu')]]

tickets_keyboard = [
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_visit')]
]

benefits_keyboard = [
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_visit')]
]

current_exhibition_keyboard = [
    [InlineKeyboardButton("Текущие 🖼", callback_data='current_exhibition'),
     InlineKeyboardButton("Вскоре 🧐", callback_data='future_exhibition')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_menu')]]

future_exhibition_keyboard = [
    [InlineKeyboardButton("Текущие 🖼", callback_data='current_exhibition'),
     InlineKeyboardButton("Вскоре 🧐", callback_data='future_exhibition')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_menu')]]

regular_events_keyboard = [
    [InlineKeyboardButton(
        "Кураторські екскурсії виставкою «Суворі та стильні: мистецтво довгих шістдесятих» 🖼",
        callback_data='first_event')],
    [InlineKeyboardButton("OFAM, nice to meet you 🧐", callback_data='second_event')],
    [InlineKeyboardButton("Екскурсії гротом Одеського художнього 🧐",
                          callback_data='third_event')],
    [InlineKeyboardButton("Позальні екскурсії в Одеському художньому 🧐",
                          callback_data='forth_event')],
    [InlineKeyboardButton("Назад 🖼", callback_data='events_menu')]]

authors_events_keyboard = [
    [InlineKeyboardButton("«Мистецтво розуму: скульптура в Одеському художньому»  🖼", callback_data='fifth_event')],
    [InlineKeyboardButton("Кольорові екскурсії в Одеському художньому 🧐", callback_data='sixth_event')],
    [InlineKeyboardButton("Назад 🖼", callback_data='events_menu')]]

child_events_keyboard = [
    [InlineKeyboardButton("OFAM KIDS CAMP  🖼", callback_data='seventh_event')],
    [InlineKeyboardButton("Назад 🖼", callback_data='events_menu')]]

events_menu_keyboard = [
    [InlineKeyboardButton("Регулярні екскурсії 🖼", callback_data='regular_events')],
    [InlineKeyboardButton("Авторські екскурсії 🧐", callback_data='authors_events')],
    [InlineKeyboardButton("Дитячі події 🎩", callback_data='child_events')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_menu')]]

first_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/538880286738319/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLSc6SWEsu6RyEYNe5eQSGKbyasOcoT-XSyWIynXj9AAjdi5fNQ/viewform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='regular_events')]]

second_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/308296210046368/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLSezxrkte1qkHB-GP-XgW3-dOc9oS7wcvnf2szLF2JNzTS1Mag/viewform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='regular_events')]]

third_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/293791121762617/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLSf4G-m5Vx2aMuHpE3ZVq6OMvRImMQjb1RmpbU7Kctlw3d_Cew/viewform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='regular_events')]]

forth_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/300386311368244/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLSfflChg9l5Udzr4-74GFYt4tMk7AJOJGJ9Q4WTv6rnSnqMeRA/viewform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='regular_events')]]

fifth_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/984245105367667/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLSd2jExc4Ugny-uxDOz4Elq2-51qhngUW0NRvJX6VroGMzACOQ/closedform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='authors_events')]]

sixth_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/913404755841640/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLScaEoKV35RDBtDPyq23stTeC0gPZ1gY9IxFTmA5_IQFFVDUNg/viewform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='authors_events')]]

seventh_event_keyboard = [
    [InlineKeyboardButton("Детальніше 🖼", url='https://www.facebook.com/events/557134108307902/'),
     InlineKeyboardButton("Зареєструватися 🧐",
                          url='https://docs.google.com/forms/d/e/1FAIpQLScnwo8gGfj4iebtGrKBERe5748CikTFz3TTDh-5GK2HDmgjZg/viewform')],
    [InlineKeyboardButton("Назад 🖼", callback_data='child_events')]]

info_keyboard = [
    [InlineKeyboardButton("Подивитися на карті 🖼",
                          url='https://www.google.com/maps/place/Odesa+Fine+Arts+Museum/@46.4933272,30.7264423,17z/data=!3m1!4b1!4m5!3m4!1s0x40c631c0ccd0adcb:0x1b9fed45ed071c6d!8m2!3d46.4933235!4d30.728631')],
    [InlineKeyboardButton("Назад 🖼", callback_data='ofam_visit')]]

mapping_keyboards = {
    'ofam_exhibition': exhibition_keyboard,
    'ofam_events': events_keyboard,
    'ofam_visit': visit_keyboard,
    'ofam_menu': main_keyboard,
    'current_exhibition': current_exhibition_keyboard,
    'future_exhibition': future_exhibition_keyboard,
    'regular_events': regular_events_keyboard,
    'events_menu': events_menu_keyboard,
    'first_event': first_event_keyboard,
    'info': info_keyboard,
    'second_event': second_event_keyboard,
    'third_event': third_event_keyboard,
    'forth_event': forth_event_keyboard,
    'authors_events': authors_events_keyboard,
    'fifth_event': fifth_event_keyboard,
    'sixth_event': sixth_event_keyboard,
    'child_events': child_events_keyboard,
    'seventh_event': seventh_event_keyboard,
    'tickets': tickets_keyboard,
    'benefits': benefits_keyboard
}


def choose_keyboard(query):
    try:
        return mapping_keyboards[query]
    except KeyError:
        return main_keyboard
