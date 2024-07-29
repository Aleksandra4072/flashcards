import random
import string


class _Utils:
    @staticmethod
    def random_string():
        s = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.sample(s, 25))


utils = _Utils()
