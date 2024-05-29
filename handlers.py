from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import menu_keyboard


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Добро пожаловать! Это бот-администратор\nВыберите действие", reply_markup=menu_keyboard)

@router.message(F.text == "Оформить заказ") # обработчик нажатия на кнопку "Оформление заказа"
async def add_order(message:Message):
    await message.answer("Оформление заказа...")

@router.message(F.text == "Посмотреть заказы") # обработчик нажатия на кнопку "Посмотреть заказы"
async def add_order(message:Message):
    await message.answer("Загружаю заказы...")

@router.message(F.text == "Добавить тур") # обработчик нажатия на кнопку "Добавить тур"
async def add_order(message:Message):
    await message.answer("Добавление тура...")

@router.message(F.text == "Посмотреть туры") # обработчик нажатия на кнопку "Посмотреть туры"
async def add_order(message:Message):
    await message.answer("Загружаю туры...")

@router.message(F.text == "Клиенты") # обработчик нажатия на кнопку "Клиенты"
async def add_order(message:Message):
    await message.answer("Загружаю данные о клиентах...")

@router.message(F.text == "Города") # обработчик нажатия на кнопку "Города"
async def add_order(message:Message):
    await message.answer("Загружаю информацию о городах...")