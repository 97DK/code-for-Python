from pathlib import Path
while 1:
    a=input('Please input your name,input"0"to quit:')
    if a != '0':
        with open('guest_book.txt', 'a') as file:
            file.write(a + "\n")  # 确保每条记录后都有一个换行符
    else:
        break
