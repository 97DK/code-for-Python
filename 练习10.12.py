from pathlib import Path

path = Path('favorite_number.txt')
# 检查文件是否存在
if path.exists():
    # 如果文件存在，读取并显示数字
    with path.open('r') as file:
        favorite_number = file.read().strip()  # 读取并去除可能的空白字符
        print(f"I know your favorite number! It's {favorite_number}.")
else:
    # 如果文件不存在，提示用户输入数字并存储
    favorite_number = input("Please input your favorite number: ")
    with path.open('w') as file:
        file.write(favorite_number)  # 直接写入，不需要json.dumps，因为我们只是存储一个数字
    print(f"Your favorite number, {favorite_number}, has been saved.")
