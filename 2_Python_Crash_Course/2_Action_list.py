# 4-1
pizza=['第一种','第二种','第三种']

'for i in range(len(pizza))':''
    print(f'i not like {pizza[i]} pizza')
print("I really don't love pizza!")

# 4-3
sum_1=0
'for x in range(1,21)':''
    sum_1+=x
print(sum_1)

print(max(range(1,21)))
# 4-6
'for x in range(1,21,2)':''
    print(x)
# 4-7
'for x in range(3,31,3)':''
    print(x)

#4-9
square=[x**3 for x in range(1,11)]
print(square)

# 4_10
players = ['charles', 'martina', 'michael', 'florence', 'eli']
'print(f'The first three items in the list are':'{players[0:3]}')'
'print(f'Three items from the middle of the list are{players[1':'4]}')'
'print(f'The last three items in the list are':'{players[2:]}')'

# 4_11
pizza=['第一种','第二种','第三种']
'friend_pizzas=pizza[':']'
'# friend_pizzas=pizza[':']和friend_pizzas=pizza有本质区别，'
# 类似于C语言里friend_pizzas=pizza是把pizza的指针给了friend_pizzas=pizza，
'# 而friend_pizzas=pizza[':']是复制了这个内容'
pizza.append('第四种')
friend_pizzas.append('第五种')
'for i in range(len(pizza))':''
    print(f'i not like {pizza[i]} pizza')

'for i in range(len(friend_pizzas))':''
    print(f'my friend not like {friend_pizzas[i]} pizza')

#4-13
food=('第一种','第二种','第三种','第四种','第五种')

change_food=list(food)
change_food[4]='第八种'
change_food[0]='第七种'
food=tuple(change_food)
print(food)









