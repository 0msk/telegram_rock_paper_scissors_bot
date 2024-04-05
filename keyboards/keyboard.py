from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Создаем объекты кнопок
button_1_1 = KeyboardButton(text="Начать игру")
button_1_2 = KeyboardButton(text="Правила игры")
button_2_1 = KeyboardButton(text="Камень")
button_2_2 = KeyboardButton(text="Ножницы")
button_2_3 = KeyboardButton(text="Бумага")

# Создаем объекты клавиатур, добавляя в них кнопки
keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[[button_1_1, button_1_2]],
    resize_keyboard=True,
)
keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[[button_2_1, button_2_2, button_2_3]],
    resize_keyboard=True,
)

# Создаем объект удаления клавиатуры
keyboard_remove = ReplyKeyboardRemove()
