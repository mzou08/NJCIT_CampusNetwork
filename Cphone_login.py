from json import loads
from requests import post
from Inform import inform


def cphone_login(username, password):  # 手机端口登录
    phone_url = "http://n.njcit.cn/index.php/index/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 \
            (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.13(0x17000d26) NetType/WIFI Language/zh_CN",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        'username': username,
        'password': password,
        'domain': 'studentphone',
        'enablemacauth': 0
    }
    res = post(url=phone_url, headers=headers, data=data)
    login_info = loads(res.text)
    login_info = inform(login_info)


if __name__ == '__main__':
    cphone_login()
