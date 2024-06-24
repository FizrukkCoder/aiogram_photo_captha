import random
from aiogram.utils.keyboard import (
    InlineKeyboardButton,
    InlineKeyboardMarkup, 
    InlineKeyboardBuilder
)

# Импортируем словарь капчи, чтобы из ключей сделать список эмоджи для клавиатуры
from config import captcha_dict_file_id

# как раз сам список эмоджи для клавиатуры
emojis = list(captcha_dict_file_id.keys())

async def captha_keyboard(succes_emoji: str, lang_code: str) -> InlineKeyboardMarkup:
    
    # перемешиваем список эмоджи
    random.shuffle(emojis)
    keyboard = InlineKeyboardBuilder()
    
    for item in emojis:
        if item == succes_emoji: # Если эмоджи из списка совпал с эмоджи изображенным на картинке устанавливаем колбэк успеха
            callback_data = f"SUCCES_CAPTCHA*{lang_code}"
        else: # колбэк, если не совпал эмоджи
            callback_data = f"BAD_CAPTCHA*{lang_code}"
            
        keyboard.add(
            InlineKeyboardButton(
                text=item, 
                callback_data=callback_data
            )
        )
        
    return keyboard.adjust(3).as_markup() # возвращаем клавиатуру с 3 эмоджи в строке