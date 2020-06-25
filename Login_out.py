from json import loads
from requests import post
from colorama import init, Fore
init(autoreset=True)


def login_out():
    loginout_url = 'http://n.njcit.cn/index.php/index/logout'
    res = post(url=loginout_url)
    out_info = loads(res.text)
    info = out_info['info']
    print(Fore.YELLOW + info)
    print('\n')
    print(Fore.YELLOW + "《返回首页菜单》")
    from Main import main
    main()


if __name__ == '__main__':
    login_out()