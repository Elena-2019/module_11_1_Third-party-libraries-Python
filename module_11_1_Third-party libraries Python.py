import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


numbers = [1015, 17, 21, 55, 78, 249, 33, 456, 33, 5]

number = np.array(numbers)
max_number = np.max(numbers)
min_number = np.min(numbers)
sum_number = np.sum(numbers)
mean_number = np.mean(numbers)
prod_number = np.prod(numbers)

print(f'Максимальное число: {max_number}')
print(f'Минимальное число: {min_number}')
print(f'Сумма чисел: {sum_number}')
print(f'Среднее значение: {mean_number}')
print(f'Произведение чисел: {prod_number}')


month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
tasks = [4, 2, 1, 1, 4, 3, 5, 3, 6, 4, 1, 3]

plt.plot(month, tasks)

plt.bar(month, tasks, label='Выполненные задачи')
plt.plot(month, tasks, color='red', marker='o', markersize=7)
plt.xlabel('Месяц')
plt.ylabel('Задания')
plt.title('График')
plt.legend()
plt.show()

print('библиотека Python: pillow')


image = Image.open(r'C:\Users\epuziy\Desktop\Python\Lesson01\Photo.jpg')
image.show()
resized_image = image.resize((400, 400))
resized_image.save('resized_image.png')

blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_image.png')

image.save('converted_image.jpg')
image.save('converted_image.gif')
