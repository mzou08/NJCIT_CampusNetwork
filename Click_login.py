from subprocess import call
from Cphone_login import cphone_login
from Cfree_login import cfree_login
from colorama import init, Fore
init(autoreset=True)


def login(username, password):
    print(Fore.RED + '警告:本软件仅供学习交流使用,下载后请于24小时内删除,严禁用于商业及非法用途!')
    print(Fore.GREEN + '手机接口登入（月租6元） 《请按' + '1' + Fore.GREEN + '》')
    print(Fore.GREEN + '免费接口登入（过期未知）《请按' + '2' + Fore.GREEN + '》')
    clogin = input("请输入接口序号：")
    if clogin == '1':
        cphone_login(username, password)
    elif clogin == '2':
        cfree_login(username, password)
    else:
        call("cls", shell=True)
        print(Fore.RED + '输入无效，请输入有效序号!!!')
        login(username, password)


if __name__ == '__main__':
    login()
