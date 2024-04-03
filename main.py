from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()


dp.run_polling(bot)
