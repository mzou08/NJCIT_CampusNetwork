from Phone_login import phone_login
from Free_login import free_login
from subprocess import call
from colorama import init, Fore
init(autoreset=True)


def login():
    print(Fore.RED + '警告:本软件仅供学习交流使用,下载后请于24小时内删除,严禁用于商业及非法用途!')
    print(Fore.GREEN + '手机接口登入（月租6元） 《请按' + '1' + Fore.GREEN + '》')
    print(Fore.GREEN + '免费接口登入（过期未知）《请按' + '2' + Fore.GREEN + '》')
    login_ = input("请输入接口序号：")
    if login_ == '1':
        call("cls", shell=True)
        phone_login()
    elif login_ == '2':
        call("cls", shell=True)
        free_login()
    else:
        call("cls", shell=True)
        print(Fore.RED + '输入无效，请输入有效序号!!!')
        login()


if __name__ == '__main__':
    login()