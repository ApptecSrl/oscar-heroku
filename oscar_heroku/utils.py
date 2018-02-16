import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


def getenv(e, *args):
    """
    Workaround Django's braindead import error silencing, by emitting
    an error when an environment variable missing would cause an exception
    """
    have_default = len(args) > 0
    try:
        return os.environ[e]
    except:
        if have_default:
            return args[0]
        print("ERROR: cannot find environment variable: {0}".format(e))
        raise
