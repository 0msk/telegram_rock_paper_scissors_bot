from aiogram import Router
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboard import keyboard_menu, keyboard_game
from services.services import get_bot_choice, get_winner

from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Этот хэндлер срабатывает на команду старт
@router.message(Command("start"))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=keyboard_menu)


# Этот хэндлер срабатывает на нажатие кнопки правил игры
@router.message(F.text == LEXICON_RU["help"])
async def process_help_answer(message: Message):
    await message.answer(text=LEXICON_RU["rules"])


# Этот хэндлер срабатывает на нажатие кнопки старта игры
@router.message(F.text == LEXICON_RU["begin"])
async def process_beginning_answer(message: Message):
    await message.answer(text=LEXICON_RU["play"], reply_markup=keyboard_game)


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(
    F.text.in_([LEXICON_RU["rock"], LEXICON_RU["paper"], LEXICON_RU["scissors"]])
)
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(
        text=f'{LEXICON_RU["bot_choice"]} ' f"— {LEXICON_RU[bot_choice]}"
    )
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=keyboard_menu)
