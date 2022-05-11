"""
author: DSP
"""

from os import path
from os.path import expanduser, exists
from Exceptions import *
import json


# -*- Global Variables -*-
banner_ascii_text ="""\u001b[32;1m
  _____           _        _           _     
 |_   _|         | |      | |         (_)    
   | |  _ __  ___| |_ __ _| |_   _ ___ _ ___ 
   | | | '_ \/ __| __/ _` | | | | / __| / __|
  _| |_| | | \__ \ || (_| | | |_| \__ \ \__ \ 
 |_____|_| |_|___/\__\__,_|_|\__, |___/_|___/
                              __/ |          
                             |___/\u001b[0m\u001b[37;1mBy Mr. DSP\u001b[0m            """

settings_file_location: path = expanduser("C:\\Instalysis\\settings.json")
settings: dict


# -*- Common Functions definations -*-

def fetch_settings() -> None:
    global settings

    if exists(settings_file_location):
        with open(settings_file_location, "w") as setting_file:
            settings = json.load(setting_file)
        setting_file.close()
        return

    else:
        raise SettingFileNotFound()


def printf(message: str, message_type: str = "normal") -> None:
    supported_message_types: list = ["info", "warning", "error", "normal", "success"]
    message_type = message_type.lower()

    if message_type not in supported_message_types:
        raise InvalidMessageType(message_type)

    if message_type == "info":
        print(f"[\u001b[34;1mInfo\u001b[0m]\t\t:\t\u001b[34m{message.title()}\u001b[0m")
        return

    elif message_type == "warning":
        print(f"[\u001b[33;1mWarning\u001b[0m]\t:\t\u001b[33m{message.title()}\u001b[0m")
        return

    elif message_type == "error":
        print(f"[\u001b[31;1mError\u001b[0m]\t\t:\t\u001b[31m{message.title()}\u001b[0m")
        return

    elif message_type == "normal":
        print(f"[\u001b[37;1mMessage\u001b[0m]\t:\t\u001b[37m{message.title()}\u001b[0m")
        return

    elif message_type == "success":
        print(f"[\u001b[32;1mSuccess\u001b[0m]\t:\t\u001b[32m{message.title()}\u001b[0m")
        return


def neofetch():
    print(banner_ascii_text)
    return


if __name__ == '__main__':
    neofetch()
    printf("Hello")
    printf("Hello", "info")
    printf("Hello", "warning")
    printf("Hello", "error")
    printf("Hello", "success")
