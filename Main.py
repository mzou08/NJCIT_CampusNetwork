from ctypes import windll
from colorama import init, Fore
from subprocess import call
from Login import login as login
from Get_info import get_info
from Click_login import login as clogin
from Login_out import login_out

windll.kernel32.SetConsoleTitleW("校园网登录 V3.0.2 ----by UnKnownMaster")
init(autoreset=True)


def main():
    password = get_info()
    print(Fore.GREEN + ' ==================')
    print(Fore.GREEN + " ||【1】一键登录 ||")
    print(Fore.GREEN + " ||【2】手动登录 ||")
    print(Fore.GREEN + " ||【3】注销登录 ||")
    print(Fore.GREEN + " ||【4】退出界面 ||")
    print(Fore.GREEN + ' ==================')
    tool = input('请输入功能序号：')
    if tool == '1':
        call("cls", shell=True)
        username = password['username']
        password = password['password']
        clogin(username, password)
    elif tool == '2':
        call("cls", shell=True)
        login()
    elif tool == '3':
        call("cls", shell=True)
        login_out()
    elif tool == '4':
        print(Fore.YELLOW + '请按任意键退出……')
        input()
    else:
        call("cls", shell=True)
        print(Fore.RED + '输入无效，请输入有效序号!!!')
        main()


if __name__ == '__main__':
    print(Fore.LIGHTRED_EX + '3.0.2版已修复若干Bug……')
    print(Fore.LIGHTRED_EX + '体验中若存在Bug,请联系。')
    main()
