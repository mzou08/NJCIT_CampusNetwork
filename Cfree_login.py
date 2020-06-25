from json import loads
from requests import post
from Inform import inform
from Login_info import free_error


def cfree_login(username, password):   # 免费端口登录（失效未知）
    phone_url = "http://n.njcit.cn/index.php/index/login"
    data = {
        'username': username,
        'password': password,
        'domain': 'freestudent',
        'enablemacauth': 0
    }
    res = post(url=phone_url, data=data)
    login_info = loads(res.text)
    login_info = inform(login_info)
    if login_info['info'] == '认证失败, 请检查密码及账户状态':
        free_error()

if __name__ == '__main__':
    cfree_login()