import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from config_data.config import Config, load_config
from config_data.set_menu import delete_main_menu
from handlers import other_handlers, user_handlers

# Конфигурируация логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логгера начинается с INFO
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
    "[%(asctime)s] - %(name)s - %(message)s",
)

# Инициализация логгера
logger = logging.getLogger(__name__)

# Вывод в консоль информации о начале запуска бота
logger.info("Starting bot")

# Загрузка конфига в переменную config
config: Config = load_config()


# Инициализация бота и диспетчера
bot = Bot(
    # Указывая parse_mod, мы определяем, что некоторые HTML-теги,
    # поддерживаемые API Telegram, нужно воспринимать именно как HTML-теги
    token=config.tg_bot.token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

# Регистрация роутеров в диспетчере
dp.startup.register(delete_main_menu)  # Удаляет меню команд
dp.include_router(user_handlers.router)
dp.include_router(other_handlers.router)

# Запуск
dp.run_polling(bot)
