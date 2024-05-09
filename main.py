import asyncio
import requests
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from tok import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
def price_btc():
    symbol='BTCUSDT'
    url = f'https://api.binance.com/api/v1/ticker/price?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return data["price"]

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Здравствуйте! Чтобы узнать курс биткоина введите команду /price_btc")

@dp.message(Command('price_btc'))
async def start(message: Message):
    priceBTC = price_btc()
    await message.answer(f'Текущий курс биткоина(BTC) к доллару(USDT): {priceBTC}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
