#Настройки
import apiai, json
import telebot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telebot import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('981156430:AAFLH8w6tIWGkaXC5iPkU7CMXvYI2R4uS8M')
updater = Updater(token='981156430:AAFLH8w6tIWGkaXC5iPkU7CMXvYI2R4uS8M') 
dispatcher = updater.dispatcher

@bot.message_handler(commands=["start"])
def start(m):
	msg = bot.send_message(m.chat.id, "Вас приветствует AbityBot помощь /help")
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*[types.KeyboardButton(name) for name in ['Информация о направлениях']])
	keyboard.add(*[types.KeyboardButton(name) for name in ['Подобрать специальность']])
	keyboard.add(*[types.KeyboardButton(name) for name in ['Часто задаваемые вопросы']])
	bot.send_message(m.chat.id, 'Выбери что тебе нужно.',
		reply_markup=keyboard)
	bot.register_next_step_handler(msg, name)


def name(m):
	if m.text == 'Информация о направлениях':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['СПО']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Бакалавриат, специалитет']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Магистратура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Аспирантура']])
		msg = bot.send_message(m.chat.id, 'На какой уровень образования собираешься поступать?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name1)
	elif m.text == 'Часто задаваемые вопросы':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Введите /v + вопрос',
			reply_markup=keyboard)

def name1(m):
	if m.text == 'СПО':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная СПО']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)
	elif m.text == 'Бакалавриат, специалитет':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная Бакалавриат, специалитет']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Заочная Бакалавриат, специалитет']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)
	elif m.text == 'Магистратура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная Магистратура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Заочная Магистратура']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)
	elif m.text == 'Аспирантура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная Аспирантура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Заочная Аспирантура']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2) #отправляем в name1
	print(m.text)
#направление в name1
def name2(m):
	print(m.text)
	if m.text == 'Очная Аспирантура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/aspirantura ',
			reply_markup=keyboard)
	elif m.text == 'Заочная Аспирантура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/aspirantura_zaoch ',
			reply_markup=keyboard)
	elif m.text == 'Очная Бакалавриат, специалитет':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/bakalavriat ',
			reply_markup=keyboard)
	elif m.text == 'Заочная Бакалавриат, специалитет':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/bakalavriat_zaoch ',
			reply_markup=keyboard)
	elif m.text == 'Очная СПО':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/spo ',
			reply_markup=keyboard)
	elif m.text == 'Очная Магистратура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/magistratura ',
			reply_markup=keyboard)
	elif m.text == 'Заочная Магистратура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/magistratura_zaoch ',
			reply_markup=keyboard)





@bot.message_handler(commands = ['url'])
def url(message):
	markup = types.InlineKeyboardMarkup()
	btn_my_site= types.InlineKeyboardButton(text='Сайт Ирниту', url='https://www.istu.edu/')
	markup.add(btn_my_site)
	bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
@bot.message_handler(commands = ['help'])
def text(message):
	markup = types.InlineKeyboardMarkup()
	bot.send_message(message.chat.id, "/start - начать работу , /v + вопрос - общие вопросы , /help - помощь", reply_markup = markup)
@bot.message_handler(commands = ['v'])
def text_message(message):
    request = apiai.ApiAI('af519e66270f48249a973bb8ddb5317d').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'AbityTest_bot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(message.chat.id, text=response)
    else:
        bot.send_message(message.chat.id, text='Я Вас не совсем понял!')



bot.polling()
