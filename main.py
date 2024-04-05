from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers

import logging
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

# Конфигурируем логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
    "[%(asctime)s] - %(name)s - %(message)s",
)

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Выводим в консоль информацию о начале запуска бота
logger.info("Starting bot")

# Загружаем конфиг в переменную config
config: Config = load_config()

default = DefaultBotProperties()

# Инициализируем бот и диспетчер
# bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
bot = Bot(
    token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Регистриуем роутеры в диспетчере
dp.include_router(user_handlers.router)

# Запускаем polling
dp.run_polling(bot)
