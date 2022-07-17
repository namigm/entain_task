from configparser import ConfigParser

config = ConfigParser()
config.read(r'C:\Users\99455\Desktop\Automation\Selenium\entain_task\configurations\config.ini')


class ReadConfig:
    @staticmethod
    def get_url():
        url = config['common info']['main_url']
        return url

    @staticmethod
    def imdb_login():
        imdb_login = config['common info']['imdb_login']
        return imdb_login

    @staticmethod
    def imdb_password():
        imdb_password = config['common info']['imdb_password']
        return imdb_password
