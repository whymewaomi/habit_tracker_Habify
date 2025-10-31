from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start():
    kb = InlineKeyboardBuilder()
    kb.button("✏️ Создать привычку", callback_data="create_habit")
    kb.button("📒 Редактировать привычку", callback_data="edit_my_habit")
    kb.button("📦 Привычки", callback_data="my_list_habit")
    kb.button("🚫 Удалить привычки", callback_data="remove_habit")
    kb.button("✉️ Помощь", callback_data="help")
    kb.adjust(1, 2, 2)
    kb.as_markup()
    return kb

