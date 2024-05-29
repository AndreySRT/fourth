from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    bot_inline_1 = InlineKeyboardButton('Посмотреть', url='https://cattish.ru/breed/?ysclid=lwq86rccq0176056340')
    bot_inline_2 = InlineKeyboardButton('Посмотреть', url='https://lapkins.ru/cat/')
    keyboard_inline.add(bot_inline_1, bot_inline_2)
    return keyboard_inline

def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
    bot2_inline_1 = InlineKeyboardButton('Посмотреть', url='https://doge.ru/?ysclid=lwrnp5us1v261817248')
    bot2_inline_2 = InlineKeyboardButton('Посмотреть', url='https://lapkins.ru/dog/')
    keyboard_inline_2.add(bot2_inline_1, bot2_inline_2)
    return keyboard_inline_2