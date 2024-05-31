import requests
import time
import base64
from random import randint
# from aiogram import Bot, Dispatcher, types, executor
#
# Api = '7213784132:AAEL-6sezSkpG3QmrjZHgA-h-9xYsVljaCw'
# bot = Bot(token= Api)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands= 'start')
# async def start(message: types.Message):
#     await message.answer('Попробовать нейронку. Напишите что вы хотите увидеть и нейронка вам это нарисует.')


def generate_image(prompt_text):
    prompt = {
        "modelUri": "art://b1gd7kvlfl6i383mo945/yandex-art/latest",
        "generationOptions": {
            "seed": randint(100000, 100000000000000)
        },
        "messages": [
            {
                "weight": 1,
                "text": prompt_text
            }
        ]
        }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"

    headers = {
            "Content-Type": "application/json",
            "Authorization": "Api-Key AQVNxD2Lje39mfzAjT7JFJFOQ4C_UOCLHHNLUJuV"
        }

    response = requests.post(url= url, headers= headers, json= prompt)
    result = response.json()
    print(result)

    operation_id = result['id']

    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

    while True:
        operation_response = requests.get(url= operation_url, headers= headers)
        operation_result = operation_response.json()
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            print('Ожидайте, изображение скоро появится')
            time.sleep(5)

# @dp.message_handler()
# async def handle_message(message: types.Message):
#     user_text = message.text
#     await message.reply('Происходит генерация изображение, пожалуйста подождите')
#
#     try:
#         image_data = generate_image(user_text)
#         await  message.reply_photo(photo= image_data)
#     except Exception as e:
#         await  message.reply(f"Произошла ошибка {e}")
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates= True)