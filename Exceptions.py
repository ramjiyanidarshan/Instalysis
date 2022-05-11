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

