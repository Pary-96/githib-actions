import sys


def return_true():
    try:
        raise Exception("This is an exception")
        return True
    except Exception as e:
        return False


result = return_true()
if not result:
    sys.exit(1)  # Exit with status code 1 if result is False
else:
    sys.exit(0)  # Exit with status code 0 if result is True
