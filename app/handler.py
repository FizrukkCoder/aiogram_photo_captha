from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

# Импорты внутренние 
from app.keyboard import captha_keyboard
from app.utils import get_random_emoji_for_captcha

router = Router()

@router.message(CommandStart())
async def start_by_user(message: Message) -> Message:
    
    user_id = message.from_user.id
    message_id = message.message_id
    
    # удаляем команду старт для красоты
    await message.bot.delete_message(
        chat_id = user_id,
        message_id = message_id
    )
    
    # Получаем эмоджи которое нужно выбрать и файл айди фото этого эмоджи
    emoji, file_id = await get_random_emoji_for_captcha()
    
    # создание клавиатуры капчи
    keyboard = await captha_keyboard(succes_emoji=emoji)
    
    # Отправка сообщения с фото и клавиатурой выбора эмоджи
    await message.answer_photo(photo=file_id, reply_markup=keyboard)
    
# Обработчик если верный выбран эмоджи
@router.callback_query(F.data.startswith("SUCCES_CAPTCHA"))
async def succse_captha(callback: CallbackQuery) -> Message:
    await callback.answer(text='Все правильно')

# Обработчик если не верный выбран эмоджи
@router.callback_query(F.data.startswith("BAD_CAPTCHA"))
async def succse_captha(callback: CallbackQuery) -> Message:
    
    # Получаем новое эмоджи которое нужно выбрать и файл айди фото этого эмоджи
    emoji, file_id = await get_random_emoji_for_captcha()

    # Изменение фото для выбора эмоджи
    media = InputMediaPhoto(media=file_id)
    
    # создание новой клавиатуры капчи 
    keyboard = await captha_keyboard(succes_emoji=emoji)
    
    # изменение сообщения с капчей
    await callback.message.edit_media(media=media, reply_markup=keyboard)

# @start_rt.message(F.photo)
# async def get_file_id_photo(message: Message):
#     await message.answer(f'<code>"{message.photo[-1].file_id}"</code>')
    