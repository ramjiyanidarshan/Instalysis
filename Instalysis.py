"""
author: DSP
"""
from os.path import expanduser

from instaloader import instaloader, Profile
from instaloader.exceptions import *

import Exceptions
from Instagram.InstagramAccount import InstagramAccount
from Common import printf


class Instalysis:
    __app_user: InstagramAccount
    __instaloader_context: instaloader.Instaloader

    __target_profile: Profile = None

    def __init__(self):
        self.__app_user = InstagramAccount()
        self.__instaloader_context = instaloader.Instaloader()
        return

    def set_target_profile(self, target_username):
        while True:
            try:
                self.__target_profile = Profile.from_username(self.__instaloader_context, target_username)
            except ProfileNotExistsException:
                printf(f"Target username '{target_username}' is not correct.", "error")
                choice = input("Would you like to enter again?[Y/n]\t:\t")
                if choice == "Y" or choice == "y":
                    continue
                else:
                    printf("Task abort", "error")
                    break
            except Exception as e:
                printf(f"Task abort due to unhandled error. Error :- {e.args}", "error")
        return

    def explore_target(self, target_username: str) -> InstagramAccount:
        target: InstagramAccount = InstagramAccount()

        target.set_username(self.__target_profile.username)
        target.set_followers(set(self.__target_profile.get_followers()))
        target.set_followings(set(self.__target_profile.get_followees()))
        target.set_unfollowers()
        target.set_unfollowings()
        target.set_hd_profile_picture_link(self.__target_profile.get_profile_pic_url())
        target.set_instagram_profile_link()
        target.set_name(self.__target_profile.full_name)
        return target

    def save_post(self, target_username: str) -> None:
        if self.__target_profile is not None:
            self.__target_profile.get_posts()
        else:
            raise Exceptions.NoneTargetProfile()
        return

    def get_tagged_post(self):
        if self.__target_profile is not None:
            self.__target_profile.get_tagged_posts()
        else:
            raise Exceptions.NoneTargetProfile()
        return

    def get_saved_post(self):
        if self.__target_profile is not None:
            self.__target_profile.get_saved_posts()
        else:
            raise Exceptions.NoneTargetProfile()
        return

    def check_for_app_user(self):
        pass

    def app_user_login(self) -> bool:
        from Common import printf

        username: str
        passwd: str = None

        print("\u001b[34;1m*\tInstagram Login\t*\u001b[0m\n")
        username = input("Enter Username\t:\t")

        while True:
            loggedin: bool = False
            try:
                try:
                    self.__instaloader_context.load_session_from_file(username)
                    printf("Login successfully using session.", "success")
                    loggedin = True
                    break
                except FileNotFoundError:
                    if passwd is None or passwd == "":
                        passwd = input("Enter Password\t:\t")
                    self.__instaloader_context.login(username, passwd)
                    printf("Login successfully.", "success")
                    loggedin = True
                    break

            except TwoFactorAuthRequiredException as e:
                printf("Two factor authentication required.", "warning")
                while True:
                    try:
                        tfa_code: str = input("Enter verification Code\t:\t")
                        self.__instaloader_context.two_factor_login(tfa_code)
                        loggedin = True
                    except BadCredentialsException:
                        printf("TFA verification code is not matched.Try again.", "error")
                        continue
                    except InstaloaderException as e:
                        printf(e.args, "error")
                if loggedin:
                    break
                else:
                    continue
            except InvalidArgumentException:
                printf("Username is invalid.", "error")
                choice = input("Would you like to enter again[Y/n] : ")
                if choice == 'Y' or choice == 'y':
                    username = input("Enter Username again\t:\t")
                    continue
                else:
                    printf("Task abort.", "error")
                    break
            except BadCredentialsException:
                printf("Password is incorrect.", "error")
                choice = input("Would you like to enter again[Y/n] : ")
                if choice == 'Y' or choice == 'y':
                    passwd = input("Enter Password again\t:\t")
                    continue
                else:
                    printf("Task abort.", "error")
                    break
            except ConnectionException:
                printf("Internet connection not available.Press \n1 - After fixing connection resume process\nAny Key "
                       + "- Abort", "error")
                choice = int(input())
                if choice == 1:
                    continue
                else:
                    printf("Task abort.", "error")
                    break
            except InstaloaderException as e:
                printf(e.args, "error")

        return loggedin
