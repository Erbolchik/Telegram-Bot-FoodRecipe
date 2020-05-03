import telebot
from telebot import  types
bot=telebot.TeleBot('1293189035:AAGMMCKPxcwKrjFjvwzSZOv4KuF49dIy4FI') # токен для подключения

@bot.message_handler(commands=["start"])# команда /start
def start_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True) # создание кнопок
    user_markup.row("🍰Торты", "🍪Печенья","🥧Пироги","🍭Конфеты") # создание 4 разных кнопок
    bot.send_message(message.chat.id, "Добрый день,выберите раздел", reply_markup=user_markup) # вывод сообщения

@bot.message_handler(regexp="🍰Торты")  # при выборе раздела Торты
def value_message(message):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text="Шоколадный торт ", callback_data="tort1")
    b1 = types.InlineKeyboardButton(text="Ванильный торт", callback_data="tort2")
    c1 = types.InlineKeyboardButton(text="Яблочный торт", callback_data="tort2")
    d1 = types.InlineKeyboardButton(text="Торт 'БЕАТРИС'", callback_data="tort3")
    keyboard1.add(a1, b1, c1, d1) # Создаем 4 кнопки
    bot.send_message(message.chat.id, "Выберите рецепт торта: ", reply_markup=keyboard1) #Выводим сообщение пользователю

@bot.message_handler(regexp="🍪Печенья")
def selectCounrty(message):
    keyboard2 = telebot.types.InlineKeyboardMarkup()
    a2 = types.InlineKeyboardButton(text="ШОКОЛАДНО-ОВСЯНОЕ ПЕЧЕНЬЕ", callback_data="cake1")
    b2 = types.InlineKeyboardButton(text="Трубочки", callback_data="cake2")
    c2 = types.InlineKeyboardButton(text="Творожное печенье", callback_data="cake3")
    d2 = types.InlineKeyboardButton(text="Сметанное печенье", callback_data="cake4")
    keyboard2.add(a2,b2,c2,d2)
    bot.send_message(message.chat.id, "Выберите рецепт печенье:", reply_markup=keyboard2)

@bot.message_handler(regexp="🥧Пироги")
def selectCounrty(message):
    keyboard3 = telebot.types.InlineKeyboardMarkup()
    a3 = types.InlineKeyboardButton(text="Тыквенный пирог", callback_data="pie1")
    b3 = types.InlineKeyboardButton(text="Рыбный пирог", callback_data="pie2")
    c3 = types.InlineKeyboardButton(text="Лимонный пирог ", callback_data="pie3")
    d3 = types.InlineKeyboardButton(text="Малиново-миндальный перевернутый пирог", callback_data="pie4")
    keyboard3.add(a3, b3, c3, d3)
    bot.send_message(message.chat.id, "Выберите рецепт пирога:  ", reply_markup=keyboard3)

@bot.message_handler(regexp="🍭Конфеты")
def value_message(message):
    keyboard4 = telebot.types.InlineKeyboardMarkup()
    a4 = types.InlineKeyboardButton(text="Конфеты 'гламур'", callback_data="candy1")
    b4 = types.InlineKeyboardButton(text="Плитка шоколада", callback_data="candy2")
    c4 = types.InlineKeyboardButton(text="Шоколадные конфеты", callback_data="candy3")
    d4 = types.InlineKeyboardButton(text="Конфеты 'Ассорти'", callback_data="candy4")
    keyboard4.add(a4, b4, c4, d4)
    bot.send_message(message.chat.id, "Выберите рецепт конфеты: ", reply_markup=keyboard4)




tortes={"tort1":{"Шоколадный торт":"https://sun9-61.userapi.com/c855232/v855232478/2275a4/2RTxnlmpI-4.jpg"},
        "tort2":{"Ванильный торт":"https://sun9-39.userapi.com/c855216/v855216050/22cc91/4SQNWBw4S4w.jpg"},
        "tort3":{"Яблочный  торт":"https://sun9-4.userapi.com/c855216/v855216260/22f552/mfqFiycJcPk.jpg"},
        "tort4":{"Торт 'БЕАТРИС'":"https://sun9-26.userapi.com/c858020/v858020972/1e2644/agRZ0jELyUs.jpg"}}

cakes={"cake1":{"ШОКОЛАДНО-ОВСЯНОЕ ПЕЧЕНЬЕ":"https://sun9-36.userapi.com/c846419/v846419942/18e95d/-UEi2qyhPIo.jpg"},
        "cake2":{"Трубочки":"https://sun9-57.userapi.com/c851420/v851420513/1060d/G_EbuPiOWgw.jpg"},
        "cake3":{"Творожное печенье":"https://sun9-67.userapi.com/c831308/v831308965/ea977/3uM-QfGHNao.jpg"},
        "cake4":{"Сметанное печенье":"https://sun9-16.userapi.com/c847019/v847019048/2043f/xFg8mN-1uCU.jpg"}}

pies={"pie1":{"Тыквенный пирог":"https://sun3-11.userapi.com/c857220/v857220581/182cbc/SI1KnoFYKPg.jpg"},
        "pie2":{"Рыбный пирог":"https://sun9-24.userapi.com/c857720/v857720260/1eac78/ellNd-LtWUo.jpg"},
        "pie3":{"Лимонный пирог":"https://sun9-71.userapi.com/c855224/v855224286/2252d7/ff1g01EMdUA.jpg"},
        "pie4":{"Малиново-миндальный перевернутый пирог":"https://sun9-29.userapi.com/c857728/v857728575/1cef42/hsHwn_EYtyg.jpg"}}

candys={"candy1":{"Конфеты 'гламур'":"https://sun9-62.userapi.com/c206720/v206720436/2fc80/hFTeKRX2MlU.jpg"},
        "candy2":{"Плитка шоколада":"https://sun9-9.userapi.com/c855324/v855324989/1f839e/AuuaIsYRuRA.jpg"},
        "candy3":{"Шоколадные конфеты":"https://sun9-7.userapi.com/c206620/v206620800/8e2fd/Qt6VOzeIC8E.jpg"},
        "candy4":{"Ассорти":"https://sun3-11.userapi.com/xdA2s16h5Fx1YccUvKpqUrBagGPUpx4Bm6lf-g/dUiqHmWrulw.jpg"}}

@bot.callback_query_handler(func=lambda c:True) # Тут идет алгоритм вывода сообщения исходя из прередущих выводов
def inline(callback):
    for key,value in tortes.items():
        if(key==callback.data):
            for key1,value1 in value.items():
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text=key1)  # Выводим сообщение о том что выбрал пользователь
                bot.send_photo(chat_id=callback.message.chat.id,photo=value1)
    for key,value in cakes.items():
        if (key == callback.data):
            for key1, value1 in value.items():
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                      text=key1)  # Выводим сообщение о том что выбрал пользователь
                bot.send_photo(chat_id=callback.message.chat.id, photo=value1)
    for key,value in candys.items():
        if (key == callback.data):
            for key1, value1 in value.items():
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                      text=key1)  # Выводим сообщение о том что выбрал пользователь
                bot.send_photo(chat_id=callback.message.chat.id, photo=value1)
    for key,value in pies.items():
        if (key == callback.data):
            for key1, value1 in value.items():
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                      text=key1)  # Выводим сообщение о том что выбрал пользователь
                bot.send_photo(chat_id=callback.message.chat.id, photo=value1)



bot.polling() # Отправка сообщения