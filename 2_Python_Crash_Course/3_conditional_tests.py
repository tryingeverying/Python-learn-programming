car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5-5
alien_color ='yellow'

if alien_color =='green':
    print('五个点')
elif alien_color == 'blue':
    print('十个点')
elif alien_color == 'yellow':
    print('十五个点')
    
#5-8/9
name_1=['admin','admin-1','admin-2','admin-3','admin-4']
# del name_1[:]
name_1.clear()
if not name_1:
    print('We need to find some users    !”')
for i in name_1:
    if i=='admin':
        print(f'Hello {i}, would you like to see a status report?')
    else:
        print(f'“Hello {i}, thank you for logging in again')

#5-10
current_users=['a','2','3','4','5']
new_users=['A','3','4','b','c']

for i in new_users:
    if (i in current_users)or(i.lower() in current_users)or(i.upper()in current_users)or(i.title ()in current_users):
        print('用户名已被占用')
    else:
         print('用户名没有被占用')

# 5-11
num_1=['1','2','3','4','5','6','7','8','9',]
for i in num_1:
    if i =='1':
        print(i+'st')
    elif i=='2':
        print(i+'nd')
    elif i=='3':
        print(i+'rd')
    else:
        print(i+'th')






















