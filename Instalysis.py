"""
author: DSP
"""
from os.path import expanduser

from instaloader import instaloader
from Instagram.InstagramAccount import InstagramAccount


class Instalysis(instaloader):
    __app_user: InstagramAccount

    def Instalysis(self):
        self.__app_user = InstagramAccount()
