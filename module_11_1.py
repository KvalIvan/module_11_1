import requests
from PIL import Image

response = requests.get('https://www.ya.ru')  # get-запрос
print(response.text)
# вывод содержимого страницы


headers = {'user-agent': 'my-app/0.0.1'}
payload = {'key1': 'value1', 'key2': 'value2'}
response_1 = requests.post('https://www.ya.ru', data=payload, headers=headers)
print(response_1.text)
# Тут мы получаем ссылки на картинки


# PIL

image = Image.open('image.jpg')
image.show()
# В результате выполнения кода автоматически открывается картинка

img = Image.open('image2.jpg')
# получаем ширину и высоту
width, height = img.size
print(width, height)
img = img.resize((700, 700))
# открываем картинку в окне
img.show()
img.save('image3.jpg')
# тут записывается новая картинка с размером поменьше

old_img = Image.open('image3.jpg')
# создание нового изображения
new_image = Image.new(old_img.mode, (old_img.size[0] + 50, old_img.size[1] + 50), 'white')
# вставляем старой изображение в новое
new_image.paste(old_img, (25, 25))
new_image.show()
new_image.save('image4.jpg')
# а тут устанавливаем рамки белого цвета
