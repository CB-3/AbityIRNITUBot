#Настройки
import apiai, json #Библиотека apiai (Отвечает за DialogFlow)
import telebot #Библиотека telebot (Основная библиотека)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters#Импортируем модули из telegramapi (Обработка команд, сообщений,а также фильтры)
from telebot import types#Импортируем types из telebot
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton#Библиотека отвечающая за клавиатуру
bot = telebot.TeleBot('981156430:AAFLH8w6tIWGkaXC5iPkU7CMXvYI2R4uS8M')#API бота
updater = Updater(token='981156430:AAFLH8w6tIWGkaXC5iPkU7CMXvYI2R4uS8M')#API бота
dispatcher = updater.dispatcher


@bot.message_handler(commands=["start","back"])#Главное меню
def start(m):
	msg = bot.send_message(m.chat.id, "Вас приветствует AbityBot. Помощь /help")
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*[types.KeyboardButton(name) for name in ['Информация о направлениях']])
	keyboard.add(*[types.KeyboardButton(name) for name in ['Подобрать специальность']])
	keyboard.add(*[types.KeyboardButton(name) for name in ['Часто задаваемые вопросы']])
	bot.send_message(m.chat.id, 'Выбери что тебе нужно.',
		reply_markup=keyboard)
	bot.register_next_step_handler(msg, name)#Назначаем переменную name = ответ пользователя


def name(m):								#Обработка переменной name
	if m.text == 'Информация о направлениях':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['СПО']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Бакалавриат, специалитет']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Магистратура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Аспирантура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'На какой уровень образования собираешься поступать?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name1)#Назначаем переменную name1 = ответ пользователя
	elif m.text == 'Часто задаваемые вопросы':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Введите /q + вопрос',
			reply_markup=keyboard)
	elif m.text == 'Подобрать специальность':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Математика (профильный уровень)']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Математика (профильный уровень), Обществознание']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Математика (профильный уровень), Физика']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Математика (профильный уровень), Информатика и информационно коммуникационные технологии']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Математика (профильный уровень), Английский язык']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Математика (профильный уровень), Химия']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Обществознание, История']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Обществознание']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Выбери какие предметы ты сдавал или планируешь сдавать.(Русский язык нужен для всех специальностей)',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, spec)#Назначаем переменную spec = ответ пользователя


def spec(m):								#Обработка переменной spec
	if m.text == 'Математика (профильный уровень)':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '07.03.01 - Архитектура, 07.03.02 - Реконструкция и реставрация архитектурного наследия, 07.03.03 - Дизайн архитектурной среды, 29.03.04 - Технология художественной обработки материалов',
			reply_markup=keyboard)
	elif m.text == 'Математика (профильный уровень), Обществознание':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '07.03.04 - Градостроительство, 8.03.01 - Экономика, 38.05.01 - Экономическая безопасность, 40.05.01 - Правовое обеспечение национальной безопасности ',
			reply_markup=keyboard)
	elif m.text == 'Математика (профильный уровень), Физика':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '08.03.01 - Строительство, 11.03.01 - Радиотехника,'+
			' 11.03.02 - Инфокоммуникационные технологии и системы связи, 13.03.01 - Теплоэнергетика и теплотехника, 13.03.02 - Электроэнергетика и электротехника,'+
			' 15.03.01 - Машиностроение, 15.03.04 - Автоматизация технологических процессов и производств, 15.03.05 - Конструкторско-технологическое обеспечение машиностроительных производств,'+
			' 15.03.06 - Мехатроника и робототехника, 20.03.01 - Техносферная безопасность, 21.03.01 - Нефтегазовое дело, 21.03.02 - Землеустройство и кадастры, 22.03.02 - Металлургия,'+
			' 23.03.01 - Технология транспортных процессов, 23.03.03 - Эксплуатация транспортно-технологических машин и комплексов,'+
			' 25.03.01 - Техническая эксплуатация летательных аппаратов и двигателей, 27.03.05 - Инноватика, 28.03.01 - Нанотехнологии и микросистемная техника,'+
			' 08.05.01 - Строительство уникальных зданий и сооружений, 21.05.01 - Прикладная геодезия, 21.05.02 - Прикладная геология, 21.05.03 - Технология геологической разведки,'+
			' 21.05.04 - Горное дело, 23.05.01 - Наземные транспортно-технологические средства, 24.05.07 - Самолето- и вертолетостроение',
			reply_markup=keyboard)
	elif m.text == 'Математика (профильный уровень), Информатика и информационно коммуникационные технологии':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '09.03.01 - Информатика и вычислительная техника, 09.03.02 - Информационные системы и технологии, 10.03.01 - Информационная безопасность',
			reply_markup=keyboard)
	elif m.text == 'Математика (профильный уровень), Английский язык':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '13.03.02 - Электроэнергетика и электротехника (англоязычная программа), 38.03.01 - Экономика (англоязычная программа), 38.03.02 - Менеджмент (англоязычная программа)',
			reply_markup=keyboard)
	elif m.text == 'Математика (профильный уровень), Химия':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '18.03.01 - Химическая технология, 19.03.02 - Продукты питания из растительного сырья',
			reply_markup=keyboard)
	elif m.text == 'Обществознание, История':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '40.03.01 - Юриспруденция',
			reply_markup=keyboard)
	elif m.text == 'Обществознание':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		bot.send_message(m.chat.id, 'Тебе подходят:' + '42.03.02 - Журналистика, 54.03.01 - Дизайн, 54.05.01 - Монументально-декоративное искусство (живопись)',
			reply_markup=keyboard)


def name1(m):								#Обработка переменной name1
	if m.text == 'СПО':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная СПО']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)#Назначаем переменную name2 = ответ пользователя
	elif m.text == 'Бакалавриат, специалитет':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная Бакалавриат, специалитет']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Заочная Бакалавриат, специалитет']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)#Назначаем переменную name2 = ответ пользователя
	elif m.text == 'Магистратура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная Магистратура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Заочная Магистратура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)#Назначаем переменную name2 = ответ пользователя
	elif m.text == 'Аспирантура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Очная Аспирантура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Заочная Аспирантура']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Форма обучения?',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, name2)#Назначаем переменную name2 = ответ пользователя


def name2(m):								#Обработка переменной name2
	if m.text == 'Очная Аспирантура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/aspirantura ' ,
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя
	elif m.text == 'Заочная Аспирантура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/aspirantura_zaoch ',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя
	elif m.text == 'Очная Бакалавриат, специалитет':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/bakalavriat ',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя
	elif m.text == 'Заочная Бакалавриат, специалитет':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/bakalavriat_zaoch ',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя
	elif m.text == 'Очная СПО':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/spo ',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя
	elif m.text == 'Очная Магистратура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/magistratura ',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя
	elif m.text == 'Заочная Магистратура':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(*[types.KeyboardButton(name) for name in ['Все направления']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Стоимость']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Минимальные баллы']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Контрольные цифры приёма']])
		keyboard.add(*[types.KeyboardButton(name) for name in ['Чтобы вернуться в главное меню введите /back']])
		msg = bot.send_message(m.chat.id, 'Специальности: https://www.istu.edu/abiturientu/napravleniya/magistratura_zaoch ',
			reply_markup=keyboard)
		bot.register_next_step_handler(msg, vib)#Назначаем переменную vib = ответ пользователя


def vib(m):								#Обработка переменной vib
	if m.text == 'Все направления':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Держи все направления: https://www.istu.edu/abiturientu/napravleniya ',
			reply_markup=keyboard)
	elif m.text == 'Стоимость':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Держи стоимость обучения: https://www.istu.edu/abiturientu/stoimost',
			reply_markup=keyboard)
	elif m.text == 'Минимальные баллы':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Минимальные баллы для поступления: https://www.istu.edu/abiturientu/prokhodnye_bally',
			reply_markup=keyboard)
	elif m.text == 'Контрольные цифры приёма':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(m.chat.id, 'Контрольные цифры приёма: https://www.istu.edu/abiturientu/kcp/bakalavriat_ochn',
			reply_markup=keyboard)

##Все команды

@bot.message_handler(commands = ['url'])#Команда url
def url(message):
	markup = types.InlineKeyboardMarkup()
	btn_my_site= types.InlineKeyboardButton(text='Сайт Ирниту', url='https://www.istu.edu/')
	markup.add(btn_my_site)
	bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
@bot.message_handler(commands = ['help'])#Команда help
def text(message):
	markup = types.InlineKeyboardMarkup()
	bot.send_message(message.chat.id, "/start - начать работу , /q + вопрос - общие вопросы , /help - помощь , /url - сайт Ирниту, /back - вернутся в главное меню", reply_markup = markup)
@bot.message_handler(commands = ['q'])#Команда q
def text_message(message):#ИИ DialogFlow
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