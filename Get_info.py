# 获取账户信息
import configparser
from Login import login


def get_info():
    config = configparser.ConfigParser()
    try:
        config.read('config.info')
        username = config['information']['username']
        password = config['information']['password']
    except BaseException:
        login()
        config.read('config.info')
        username = config['information']['username']
        password = config['information']['password']

    return {
        'username': username,
        'password': password
    }


if __name__ == '__main__':
    get_info()
