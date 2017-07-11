from __future__ import print_function

class GameUnitError(Exception):
    """Custom exceptions class for the `AbstractGameUnit` and its subclasses
    """
    def __init__(self, message='', code=000):
        try:
            super().__init__(message)
        except:
            Exception.__init__(self, message)
        self.error_message = '~'*50 + '\n'

        # Alternative approach is to subclass GameUnitError
        self.error_dict = {
            000: "ERROR-000: Unspecified Error!",
            101: "ERROR-101: Health Meter Problem!",
            102: "ERROR-102: Attack issue! Ignored",
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~'*50
