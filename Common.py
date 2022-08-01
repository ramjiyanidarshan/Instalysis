"""
author: DSP
"""

import json
from os.path import exists

from Exceptions import SettingFileNotFound, InvalidMessageType

# -*- Global Variables -*-

banner_ascii_text = """\u001b[32;1m
  _____           _        _           _     
 |_   _|         | |      | |         (_)    
   | |  _ __  ___| |_ __ _| |_   _ ___ _ ___ 
   | | | '_ \/ __| __/ _` | | | | / __| / __|
  _| |_| | | \__ \ || (_| | | |_| \__ \ \__ \ 
 |_____|_| |_|___/\__\__,_|_|\__, |___/_|___/
                              __/ |\u001b[0m\u001b[33;1mBy Mr. DSP\u001b[0m          
                             \u001b[32;1m|___/\u001b[0m"""

app_folder: str = "~/Instalysis"
result_folder: str = "~/Documents/Instalysis"
settings_file_location: str = app_folder + "/settings.json"

default_setting: dict = {
    "ShowPasswordOnStdOutDevice": True,
    "IsUserLoggedIn": False,
    "LoggedInUser": None,
    "OSEnvironment": None,
    "ClearCommands": None,
    "LogsLocation": app_folder + "/.logs/"
}


# -*- Common Functions definitions -*-
def fetch_settings() -> dict:
    from os.path import expanduser

    if exists(expanduser(settings_file_location)):
        settings = json.load(open(expanduser(settings_file_location)))
        return settings

    else:
        raise SettingFileNotFound()


def fetch_specific_setting(setting_string: str):
    settings: dict = fetch_settings()
    if setting_string in settings.keys():
        return settings[setting_string]
    else:
        raise IndexError("Invalid setting index '" + setting_string + "'.")


def write_user(username: str) -> None:
    from os.path import expanduser
    settings: dict = fetch_settings()

    settings['LoggedInUser'] = username
    settings['IsUserLoggedIn'] = True

    with open(expanduser(settings_file_location), "w") as setting_file:
        setting_file.write(json.dumps(settings, indent=4, sort_keys=True))
    setting_file.close()


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


def download_image(image_url: str, file_name: str):
    import requests
    import shutil
    from os.path import exists, expanduser

    if exists(expanduser(file_name)):
        file_name = file_name.partition(".")[0] + "-1." + file_name.partition(".")[2]

    res = requests.get(image_url, stream=True)

    if res.status_code == 200:
        print(f"Downloading post - {file_name}...", end="")
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print("done")
    else:
        printf(f"HTTP request error code : {res.status_code}", "error")
    return


def download_posts(post_list: list, file_name_pattern: str):
    if post_list is None or []:
        printf("No posts to download and save.", "info")
    else:
        count = 1
        for post in post_list:
            download_image(post, file_name_pattern + str.zfill(str(count), 3) + ".jpg")
            count += 1
