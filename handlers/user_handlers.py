from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.keyboard import keyboard_1, keyboard_2, keyboard_remove
from functions.functions import bot_response_func

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Давай играть?", reply_markup=keyboard_1)


@router.message(F.text == "Правила игры")
async def process_help_answer(message: Message):
    await message.answer(
        text="Играешь с роботом.\nНужно выбрать камень, ножницы или бумагу.\nКамень побеждает ножницы. Ножницы побеждают бумагу. Бумага побеждает камень.\nДо одной победы. Если ничья, нужно выбрать снова."
    )


@router.message(F.text == "Начать игру")
async def process_beginning_answer(message: Message):
    await message.answer(
        text="Выбери одно из трех: камень, ножницы или бумагу", reply_markup=keyboard_2
    )


@router.message((F.text == "Камень") | (F.text == "Ножницы") | (F.text == "Бумага"))
async def user_response_func(message: Message):
    bot_response = bot_response_func()
    await message.answer(
        text=f"Ответ бота:\n{bot_response}",
    )
    if message.text == bot_response:
        await message.answer(text="Ничья. Ответь еще раз.")
    elif message.text == "Камень" and bot_response == "Ножницы":
        await message.answer(text="Твоя победа!", reply_markup=keyboard_remove)
    elif message.text == "Ножницы" and bot_response == "Бумага":
        await message.answer(text="Твоя победа!", reply_markup=keyboard_remove)
    elif message.text == "Бумага" and bot_response == "Камень":
        await message.answer(text="Твоя победа!", reply_markup=keyboard_remove)
    else:
        await message.answer(text="Увы, не в этот раз.", reply_markup=keyboard_remove)


@router.message()
async def user_message_answer(message: Message):
    await message.answer(text="Не понимаю тебя. Выбирай пункты из меню")
