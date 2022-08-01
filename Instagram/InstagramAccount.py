"""
author: DSP
"""

from instaloader import Profile


class InstagramAccount:

    # -*- Private Members -*-

    __username: str
    __followers: set
    __followings: set
    __unfollowers: set
    __unfollowees: set
    __name: str
    __saved_post: list
    __own_post: list
    __tagged_post: list
    __hd_profile_picture_link: str
    __instagram_profile_link: str
    __account_profile: Profile
    __similar_profiles: list

    # -*- Constructor -*-

    def __init__(self, target_profile):
        self.__account_profile = target_profile
        self.__username = ""
        self.__name = ""
        self.__hd_profile_picture_link = ""
        self.__instagram_profile_link = ""
        self.__followers = set()
        self.__unfollowers = set()
        self.__followings = set()
        self.__unfollowees = set()
        self.__saved_post = list()
        self.__own_post = list()
        self.__tagged_post = list()

    # -*- Setter Methods -*-

    def set_username(self) -> None:
        self.__username = self.__account_profile.username

    def set_followers(self) -> None:
        for account in self.__account_profile.get_followers():
            self.__followers.add(account.username)

    def set_followings(self) -> None:
        for account in self.__account_profile.get_followees():
            self.__followings.add(account.username)

    def set_unfollowers(self) -> None:
        self.__unfollowers = self.__followings.difference(self.__followers)

    def set_unfollowings(self) -> None:
        self.__unfollowees = self.__followers.difference(self.__followings)

    def set_name(self) -> None:
        self.__name = self.__account_profile.full_name

    def set_instagram_profile_link(self) -> None:
        self.__instagram_profile_link = f"https://www.instagram.com/{self.__username}"

    def set_hd_profile_picture_link(self) -> None:
        self.__hd_profile_picture_link = self.__account_profile.get_profile_pic_url()

    def set_own_post(self) -> None:
        for post in self.__account_profile.get_posts():
            self.__own_post.append(post.url)

    def set_tagged_post(self) -> None:
        for post in self.__account_profile.get_tagged_posts():
            self.__tagged_post.append(post.url)

    def set_saved_post(self) -> None:
        for post in self.__account_profile.get_saved_posts():
            self.__saved_post.append(post.url)

    def set_similar_profiles(self) -> None:
        for profile in self.__account_profile.get_similar_accounts():
            self.__similar_profiles.append(profile.username)

    # -*- Getter Methods -*-

    def get_username(self) -> str:
        return self.__username

    def get_name(self) -> str:
        return self.__name

    def get_followers(self) -> set:
        return self.__followers

    def get_followings(self) -> set:
        return self.__followings

    def get_unfollowers(self) -> set:
        return self.__unfollowers

    def get_unfollowees(self) -> set:
        return self.__unfollowees

    def get_followers_count(self) -> int:
        return len(self.__followers)

    def get_followings_count(self) -> int:
        return len(self.__followings)

    def get_unfollowers_count(self) -> int:
        return len(self.__unfollowers)

    def get_unfollowees_count(self) -> int:
        return len(self.__unfollowees)

    def get_instagram_profile_link(self) -> str:
        return self.__instagram_profile_link

    def get_hd_profile_picture_link(self) -> str:
        return self.__hd_profile_picture_link

    def get_own_post(self) -> list:
        return self.__own_post

    def get_tagged_post(self) -> list:
        return self.__tagged_post

    def get_saved_post(self) -> list:
        return self.__saved_post

    def get_similar_profiles(self) -> list:
        return self.__similar_profiles

    def full_explore(self):
        self.set_followers()
        self.set_followings()
        self.set_unfollowers()
        self.set_unfollowings()
        self.set_name()
        self.set_username()
        self.set_own_post()
        # self.set_tagged_post()
        self.set_instagram_profile_link()
        self.set_hd_profile_picture_link()
