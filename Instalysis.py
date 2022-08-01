"""
author: DSP
"""

from instaloader import instaloader, Profile
from instaloader.exceptions import *
from Instagram.InstagramAccount import InstagramAccount
from Common import printf, download_posts, fetch_specific_setting


class Instalysis:

    __target_user: InstagramAccount
    __instaloader_context = None

    def __init__(self):
        self.__instaloader_context = instaloader.Instaloader()
        self.__target_user = None
        return

    def set_target_profile(self, target_username: str) -> InstagramAccount:
        self.app_user_login()
        while True:
            try:
                self.__target_user = InstagramAccount(Profile.from_username(self.__instaloader_context.context,
                                                                            target_username))
                printf(f"Target '{target_username}' has been set.", "info")
                break
            except ProfileNotExistsException:
                printf(f"Target username '{target_username}' is not correct.", "error")
                choice = input("Would you like to enter again?[Y/n]\t:\t")
                if choice == "Y" or choice == "y":
                    continue
                else:
                    printf("Task abort", "error")
                    break
            except Exception as e:
                printf(f"Task abort due to unhandled error. Error :- {e.args.__str__()}", "error")
                break
        printf("Exploration in progress...", "info")
        self.__target_user.full_explore()
        printf("Exploration done.", "success")
        return self.__target_user

    def save_own_post(self) -> None:
        download_posts(self.__target_user.get_own_post(), f"IMG-{self.__target_user.get_username()}-OwnPost-")
        return

    def save_saved_post(self):
        download_posts(self.__target_user.get_saved_post(), f"IMG-{self.__target_user.get_username()}-SavedPost-")
        return

    def save_tagged_post(self):
        download_posts(self.__target_user.get_tagged_post(), f"IMG-{self.__target_user.get_username()}-TaggedPost-")
        return

    def app_user_login(self) -> bool:
        from Common import printf

        username: str
        passwd: str = ""

        print("\u001b[34;1m*\tInstagram Login\t*\u001b[0m\n")

        if fetch_specific_setting("IsUserLoggedIn"):
            username = fetch_specific_setting("LoggedInUser")
        else:
            username: str = "ramjiyanidarshan"
            # username = input("Enter Username\t:\t")

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

            except TwoFactorAuthRequiredException:
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
                        printf(e.args.__str__(), "error")
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
                printf(e.args.__str__(), "error")

        return loggedin
