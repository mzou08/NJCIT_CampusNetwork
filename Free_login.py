from base64 import b64encode
from json import loads
from requests import post
from Inform import inform
from Login_info import log_info, free_error
from colorama import init, Fore

init(autoreset=True)


def free_login():  # 免费端口登录（失效未知）
    username = str(input('请输入账号：'))
    while username == '':
        print(Fore.RED + '账号不能为空！')
        username = str(input('请重新输入账号：'))
    password = str(input('请输入密码：'))
    while password == '':
        print(Fore.RED + '密码不能为空！')
        username = str(input('请重新输入密码：'))
    pw = bytes(password, 'utf-8')
    pwd = b64encode(pw)
    pwd = str(pwd, 'utf-8')
    phone_url = "http://n.njcit.cn/index.php/index/login"
    data = {
        'username': username,
        'password': pwd,
        'domain': 'freestudent',
        'enablemacauth': 0
    }
    res = post(url=phone_url, data=data)
    login_info = loads(res.text)
    if login_info['info'] == '认证成功':
        data = log_info(data)
    else:
        free_error()

    login_info = inform(login_info)


if __name__ == '__main__':
    free_login()
