"""
author: DSP
"""

class InstagramAccount:
    __username: str
    __followers: set
    __followings: set
    __unfollowers: set
    __unfollowees: set
    __name: str
    def __init__(self):
        self.__username = None
        self.__name = None
        self.__followers = set()
        self.__unfollowers = set()
        self.__followings = set()
        self.__unfollowees = set()
        
    def __init__(self, instagram_username: str) -> None:
        self.__init__()
        self.__username = instagram_username
    
    def set_username(self, instagram_username: str) -> None:
        self.__username = instagram_username

    def set_followers(self, follower: set) -> None:
        self.__followers = follower

    def set_followings(self, followings: set) -> None:
        self.__followings = followings

    def set_unfollowers(self, follower: set) -> None:
        self.__unfollowers = self.__followings.difference(self.__followers)

    def set_unfollowings(self, followings: set) -> None:
        self.__unfollowees = self.__followers.difference(self.__followings)

    def set_name(self, name: str) -> None:
        self.__name = name

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

