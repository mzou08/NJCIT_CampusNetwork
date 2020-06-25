from configparser import ConfigParser
from win32api import SetFileAttributes
from win32con import FILE_ATTRIBUTE_HIDDEN
from os import path, remove
from colorama import init, Fore
init(autoreset=True)


def log_info(data):
    if path.exists('config.info'):
        remove('config.info')
    config = ConfigParser()  # 实例化一个配置写入
    config.add_section('information')  # 创建一个选择器
    config.set('information', 'username', data['username'])  # 保存账号
    config.set('information', 'password', data['password'])  # 保存密码
    try:
        with open('config.info', 'w+') as f:  # 写入文件
            config.write(f)
    except ImportError:
        pass
    SetFileAttributes('config.info', FILE_ATTRIBUTE_HIDDEN)


def error_info():
    print(Fore.RED + '认证失败, 请检查密码及账户状态!')
    print("\n")
    print(Fore.YELLOW + "《返回首页菜单》")
    from Main import main
    main()


def free_error():
    print(Fore.YELLOW + '免费端口认证失败，可能失效。')
    print(Fore.RED + '请先检查密码及账户状态或更换接口进行尝试。')
    print("\n")
    print(Fore.YELLOW + "《返回首页菜单》")
    from Main import main
    main()