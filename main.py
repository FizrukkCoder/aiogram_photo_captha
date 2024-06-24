""" ___________________________
    |                         |
    |   Project by Fizrukk    |
    |          good luck)     |
    |_________________________| 
"""

import asyncio

# Импорт aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

# Импорт токена 
from config import TOKEN

# Импорт роутера
from app.handler import router


# Инициализация бота и диспетчера
async def create_bot_and_dispatcher():
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    dp = Dispatcher()
    
    # Подклчюаем роутер
    dp.include_router(
        router
    )
    return bot, dp

# Точка входа 
async def main():
    bot, dp = await create_bot_and_dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, polling_timeout=10)


# запуск скрипта
if __name__ == '__main__':
    try:
        print('Hello World!')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')