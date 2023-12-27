import requests

def get_usr_info(user_name):

    url = f"https://api.github.com/users/{user_name}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data)
    else:
        print("Failed to fetch user information.")

get_usr_info("jinyuxin8955")


# import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        # 处理用户数据
        print(f"Username: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Bio: {user_data['bio']}")
        print(f"Followers: {user_data['followers']}")
        # 其他数据字段...

    else:
        print("Failed to fetch user information.")

# 调用函数并传入要查询的GitHub用户名
get_user_info("jinyuxin8955")