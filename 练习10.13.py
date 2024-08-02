import json
def save_user_info(filename, user_info):
    with open(filename, 'w') as file:
        json.dump(user_info, file)
def load_user_info(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def main():
    # 假设用户输入了以下信息
    username = input("请输入用户名: ")
    email = input("请输入电子邮件: ")
    age = input("请输入年龄: ")
    user_info = {
        'username': username,
        'email': email,
        'age': age
    }
    filename = 'user_info.json'

    save_user_info(filename, user_info)

    loaded_info = load_user_info(filename)

    # 打印摘要消息
    if loaded_info:
        print(
            f"程序记住了以下信息: 用户名={loaded_info['username']}, 电子邮件={loaded_info['email']}, 年龄={loaded_info['age']}")
    else:
        print("没有找到用户信息。")


if __name__ == "__main__":
    main()