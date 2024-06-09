def return_true():
    try:
        raise Exception("This is an exception")
        return True
    except Exception as e:
        return False


result = return_true()
print(result)
