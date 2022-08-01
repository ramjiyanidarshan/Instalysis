"""
author: DSP
"""


class SettingFileNotFound(Exception):

    def __init__(self):
        super().__init__('Setting file not found at installation location.')
        return


class InvalidMessageType(Exception):

    def __init__(self, message_type):
        super().__init__(f"Invalid message type '{message_type}'.")
        return


class AppUserNotFound(Exception):

    def __int__(self):
        super().__init__("App user is not set.")
        return


class NoneTargetProfile(Exception):

    def __int__(self):
        super.__init__("Target profile is None. Please set it first.")
        return


class EmptyRequiredPropertyException(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
