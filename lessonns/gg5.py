# range(start:stop:step) - функция генерации чисел 
# list()
# dict()
# set()
# tuple()
# b = {1:3}
# x = [1,2,3,4,5,6,7,8,9,10]
# # b = [a**2 for a in range(1,2)]
# # print(b)
sqr = {x: x**2 for x in range(1,6)}
print(sqr)


# sqr = { x**2 for x in range(1,15)}
# print(sqr)



# x = [1,2,3,4,5,6,7,8,9,10]
# sqr = { x**3 for x in range(1,6)}
# print(sqr)



# words = 'hello how are you'
# sent = [word[0] for word in words.split()  ]
# print(sent)



# sentens = 'hello i am good and you , so what is your name '
# sent = [len(i) for i in sentens.split()  ]
# print(sent)
