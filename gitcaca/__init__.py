import os

AVATAR_STORAGE = '/var/tmp/gitcaca'

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_default_avatar():
    return os.path.join(_ROOT, 'avatars', 'default.png')