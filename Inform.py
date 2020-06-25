from json import loads
from requests import get
from subprocess import call
from colorama import init, Fore
init(autoreset=True)


def inform(login_info):  # 返回信息处理
    info = login_info['info']  # 读取登录信息
    logout_username = login_info['logout_username']  # 登陆账号
    logout_domain = login_info['logout_domain']  # 登录方式
    logout_ip = login_info['logout_ip']  # 登录IP
    logout_location = login_info['logout_location']  # 登录地点
    logout_account = login_info['logout_account']  # 账户余额
    call("cls", shell=True)
    print(Fore.YELLOW + '正在登陆中……')
    res = get("https://v1.hitokoto.cn/")
    daily = loads(res.text)
    hitokoto = daily['hitokoto']
    print(Fore.YELLOW + '每日一句小骚话:\n', Fore.CYAN + hitokoto)
    print(Fore.GREEN + '认证状态:', Fore.GREEN + info)
    print(Fore.GREEN + '用 户 名:', Fore.GREEN + logout_username)
    print(Fore.GREEN + '认证方式:', Fore.GREEN + logout_domain)
    print(Fore.GREEN + '登录 IP:', Fore.GREEN + logout_ip)
    print(Fore.GREEN + '登录地点:', Fore.GREEN + logout_location)
    print(Fore.GREEN + '账户余额:', logout_account, Fore.GREEN + '元')
    print("\n")
    from Main import main
    main()


if __name__ == '__main__':
    inform()
