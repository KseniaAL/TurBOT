from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [
        KeyboardButton(text="Посмотреть заказы"),
        KeyboardButton(text="Оформить заказ")
    ],
    [
        KeyboardButton(text="Посмотреть туры"),
        KeyboardButton(text="Добавить тур")
    ],
    [
        KeyboardButton(text="Клиенты"),
        KeyboardButton(text="Города")
    ]
]
menu_keyboard = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True, input_field_placeholder="Выберите действие")