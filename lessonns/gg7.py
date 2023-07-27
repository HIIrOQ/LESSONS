# Работа с файлами 

# file = open(имя файла,режим доступа к файлу)

# 'r'- read() за чтение файла
# 'w' - write() запись с удалением уже существующих данных
# a - append()  запись без удаления данных в 
# файле в новой строке
# 'x' - ---- создание файла если его не существует
# rb , wb -- чтение и запись в бинарном виде


# file = open('text.txt','r')
# text = file.read()

# print(text)
# file.close()

# file = open('text.txt','w')
# text = file.write('Hello world')

# print(text)
# file.close()

# file = open('text.txt','a')
# text = file.write('\t hello')

# print(text)
# file.close()            



# with open('text.txt', '+a') as file :
#     text = file.write('fwemkfe')


# with open('texts.txt', 'x') as file :
#     text = file.write('fwemkfe')


# with open('image.jpg', 'rb') as file :
#     data = file.read()
# print(data)


# 1)Напишите программу, которая запрашивает у пользователя ввод текста и сохраняет
# его в файл "text.txt". После записи файла программа должна вывести сообщение "Текст успешно записан в файл"

# with open('text.txt', '+a') as file :
#    a=input('запишите текст : ')
#    text = file.write(a)
# print(text)

# 2)Создайте файл "text.txt" и запишите в него произвольный текст. Напишите программу, которая открывает файл 
# "text.txt", считывает содержимое и подсчитывает количество слов в тексте. Выведите результат на экран.

# with open('text.txt', 'r') as file :
#     text = file.read()
#     a = len(text)
# print(a)

# 3)Создайте файл "text.txt" и запишите в него произвольный текст. Напишите программу, которая открывает файл "text.txt", 
# считывает содержимое и подсчитывает количество символов (без учета пробелов). Выведите результат на экран.

# with open('text.txt', 'r') as file :
#     text = file.read()
    
#     a = len(text.replace(" ", ""))
    
   
# print(a)


# 4))Создайте файл "text.txt" и запишите в него произвольный текст. Напишите программу, которая открывает файл 
# "text.txt", считывает содержимое и находит нужное слово в файле.

# file = open('text.txt','r')
# text = file.read().split()
# if input('ввуедите слво: ') in text :
#     print('eсть')
# else :e
#     print('no')
# file.close()
