from base64 import b64encode
from json import loads
from requests import post
from Inform import inform
from Login_info import log_info, error_info
from colorama import init, Fore
init(autoreset=True)


def phone_login():  # 手机端口登录
    username = str(input('请输入账号：'))
    if username == '':
        print(Fore.RED + '账号不能为空！')
        username = str(input('请重新输入账号：'))
    password = str(input('请输入密码：'))
    if password == '':
        print(Fore.RED + '密码不能为空！')
        username = str(input('请重新输入密码：'))
    pw = bytes(password, 'utf-8')
    pwd = b64encode(pw)
    pwd = str(pwd, 'utf-8')
    phone_url = "http://n.njcit.cn/index.php/index/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 \
            (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.13(0x17000d26) NetType/WIFI Language/zh_CN",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        'username': username,
        'password': pwd,
        'domain': 'studentphone',
        'enablemacauth': 0
    }
    res = post(url=phone_url, headers=headers, data=data)
    login_info = loads(res.text)
    if login_info['info'] == '认证成功':
        data = log_info(data)
    else:
        error_info()
    login_info = inform(login_info)


if __name__ == '__main__':
    phone_login()
