#6-1
information={'first_name':'段','last_name':'竹','feature':'挂逼','city':'天龙',}
print(information)

#6_2
favorite_num={'1':'一','2':'二','3':'三','4':'四','5':'五',}

for k,v in favorite_num.items():
    print(f'{k}最喜欢的数字是{v}')

#6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
survey_name=['jen','sarah','edward','phil','张三','李四','王五',]
for i in survey_name:
    if i in favorite_languages.keys():
        print(f'{i} thanks')
    else:
        print(f'{i} join in ')

#6_7
information_1={'first_name':'段','last_name':'誉','feature':'盗号','city':'大理',}
information_2={'first_name':'虚','last_name':'竹','feature':'挂逼','city':'西夏',}
information_3={'first_name':'萧','last_name':'峰','feature':'开局满级','city':'契丹',}

information_list=[information_1,information_2,information_3]
for i in information_list:
    print(i)


print(information)



