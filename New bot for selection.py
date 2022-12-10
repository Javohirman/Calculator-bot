import math
import telebot
from telebot import types

bot = telebot.TeleBot('5885688211:AAF5eoEShQ8WNDc0lc5dQuQdbTrdglR-Uv4')


value = ''
old_value = ''

keyboard = types.InlineKeyboardMarkup()
keyboard.row(types.InlineKeyboardButton('^2', callback_data='^2'),
             types.InlineKeyboardButton('C', callback_data='C'),
             types.InlineKeyboardButton('<=', callback_data='<='),
             types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(types.InlineKeyboardButton('7', callback_data='7'),
             types.InlineKeyboardButton('8', callback_data='8'),
             types.InlineKeyboardButton('9', callback_data='9'),
             types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(types.InlineKeyboardButton('4', callback_data='4'),
             types.InlineKeyboardButton('5', callback_data='5'),
             types.InlineKeyboardButton('6', callback_data='6'),
             types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(types.InlineKeyboardButton('1', callback_data='1'),
             types.InlineKeyboardButton('2', callback_data='2'),
             types.InlineKeyboardButton('3', callback_data='3'),
             types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(types.InlineKeyboardButton('Ildiz osti', callback_data='sqr'),
             types.InlineKeyboardButton('0', callback_data='0'),
             types.InlineKeyboardButton('.', callback_data='.'),
             types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start', 'calcni'])
def getMessage(message):

    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)




@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == '^2':
        value = str(int(value)*int(value))
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == 'sqr':
        value = str(math.sqrt(int(value)))
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = "xatolik yuz berdi"

    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value =='':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text= value,  reply_markup=keyboard)
            old_value = value
    old_value = value
    if value == "xatolik yuz berdi": value =''





bot.polling(none_stop=False, interval=0)
