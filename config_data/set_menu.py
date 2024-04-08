from aiogram import Bot
from aiogram.types import BotCommand


# Функция удаления кнопки Menu бота
async def delete_main_menu(bot: Bot):
    await bot.delete_my_commands()
