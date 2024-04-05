from aiogram import Bot, Dispatcher
from handlers import user_handlers

from config_data.config import Config, load_config

# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

# Регистриуем роутеры в диспетчере
dp.include_router(user_handlers.router)

# Запускаем polling
dp.run_polling(bot)
