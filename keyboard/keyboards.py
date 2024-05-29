from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    first_button = KeyboardButton('Отправь фото кота')
    second_button = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(first_button, second_button)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    third_button = KeyboardButton('Отправь фото собаки')
    fourth_button = KeyboardButton('Вернуться на первую клавиатуру')
    keyboard_2.add(third_button, fourth_button)
    return keyboard_2