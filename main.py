from aiogram import Bot, Dispatcher, types, executor
from neiro.neiro_gen import generate_image
from neiro.neiro_assistent import get_response
from neiro.neiro_consult import get_sovet


Api = '7213784132:AAEL-6sezSkpG3QmrjZHgA-h-9xYsVljaCw'
bot = Bot(token= Api)
dp = Dispatcher(bot)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Попробовать нейронку. Напишите что вы хотите увидеть и нейронка вам это нарисует.')

@dp.message_handler(commands= 'sovet')
async def analize_message(message:types.Message):
      user = message.get_args()
      response_text = await get_sovet(user)
      await message.answer(response_text)

@dp.message_handler(commands= 'generate_image')
async def handle_message(message: types.Message):
        user = message.get_args()
        response_text = await get_response(user)
        user_text = response_text
        await message.reply(f'Вот ваш улучшеный пронт {user_text}')
        print(user_text)
        await message.reply('Происходит генерация изображение, пожалуйста подождите')

        try:
            image_data = generate_image(user_text)
            await  message.reply_photo(photo= image_data)
        except Exception as e:
            await  message.reply(f"Произошла ошибка {e}")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)