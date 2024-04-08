from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU

# Объекты кнопок
button_begin = KeyboardButton(text=LEXICON_RU["begin"])
button_help = KeyboardButton(text=LEXICON_RU["help"])
button_rock = KeyboardButton(text=LEXICON_RU["rock"])
button_paper = KeyboardButton(text=LEXICON_RU["paper"])
button_scissors = KeyboardButton(text=LEXICON_RU["scissors"])

# Объект клавиатуры меню
keyboard_menu = ReplyKeyboardMarkup(
    keyboard=[[button_begin, button_help]],
    resize_keyboard=True,
)

# Объект клавиатуры игры
keyboard_game = ReplyKeyboardMarkup(
    keyboard=[[button_rock, button_paper, button_scissors]],
    resize_keyboard=True,
)
