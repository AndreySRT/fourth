from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token
from keyboard.keyboards import get_keyboard, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline_2
from database.database import initialize_db, add_user, get_user


bot = Bot(token = telegram_token)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
    types.BotCommand(command='/start', description='Комманда для того, чтобы запустить бота'),
    types.BotCommand(command='/help', description='Комманда для того, чтобы узнать, с чем может помочь наш бот'),
    types.BotCommand(command='/info', description='Комманда для того, чтобы узнать полную информацию о боте'),
    types.BotCommand(command='/chatbot', description='Комманда для того, чтобы поболтать со мной'),
    types.BotCommand(command='/botplay', description='Комманда для того, чтобы сыграть со мной и проверить свои знания')
]  #Создание массива комманд

    await bot.set_my_commands(commands) #Передаем массив комманд в бота


@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, Бонжур, Хеллоу!', reply_markup=get_keyboard())  #Можно использовать тег reply но он будет пересылать твое сообщение, после писать твое сообщение.
    else:
        await message.answer('Привет, Бонжур, Хеллоу!', reply_markup=get_keyboard())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def first_button_click(message: types.message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/originals/12/9a/72/129a7210cd3b24388a377bdb200ff4dc.jpg', caption='Ссылка на сайт с котами', reply_markup=get_keyboard_inline())
    #await message.answer('Ты нажал кнопку 1')

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def second_button_click(message: types.message):
    await message.answer('Тут ты можешь попросить отправить фото собаки', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def third_button_click(message: types.message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.dzeninfra.ru/get-zen_doc/9811263/pub_644f9292283fb47259c7c534_644f94be0d32d312f225ad14/scale_1200', caption='Вот и еще малыш!', reply_markup=get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'Вернуться на первую клавиатуру')
async def second_button_click(message: types.message):
    await message.answer('Тут ты можешь попросить отправить фото кота', reply_markup=get_keyboard())

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Если у тебя возникли вопросы или проблемы при использовании бота, не стесняйся обращаться ко мне.')

@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.answer('Привет! Я - твой персональный бот, готовый помочь с различными задачами. Я обучен выполнять разнообразные команды, от предоставления информации до выполнения действий по твоему запросу. Просто напиши мне, что тебе нужно, и я постараюсь помочь.')

@dp.message_handler(commands='chatbot')
async def chatbot(message: types.Message):
    await message.answer('Если тебе наскучит, я могу с тобой поболтать на любую свободную тему чтобы разрядить обстановку.')

@dp.message_handler(commands='botplay')
async def botplay(message: types.Message):
    await message.answer('Давай поиграем в угадайку: задавай мне вопросы, а я буду отвечать "да" или "нет"')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher): #Вызываем нашу функцию
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)