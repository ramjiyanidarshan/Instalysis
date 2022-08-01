"""
author: DSP
"""

import os

import Common
from Common import *
from Instalysis import Instalysis


def initialization():
    from os.path import exists, expanduser
    from os import mkdir

    neofetch()
    printf("Getting this machine ready. Please wait...", "info")
    if not exists(expanduser(Common.app_folder)):
        mkdir(expanduser(Common.app_folder))

    if not exists(expanduser(Common.result_folder)):
        mkdir(expanduser(Common.result_folder))

    if not exists(expanduser(Common.settings_file_location)):
        file = open(expanduser(Common.settings_file_location), "w")
        file.write(json.dumps(Common.default_setting, indent=4, sort_keys=True))
        file.close()


if __name__ == '__main__':
    initialization()
    
    os.system("cls")
    
    neofetch()
    
    instalysis = Instalysis()
    
    instagramAccount = instalysis.set_target_profile("ramjiyanidarshan")
    
    print(instagramAccount.get_unfollowers())
