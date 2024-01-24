import errno

def trigger(err, message):
    print(f"try to simulate {message}: {err}")
    raise OSError(err, message)


def catcher(err, message):
    try:
        trigger(err, message)
    except OSError as e:
        print("I'm here")
        if e.errno != errno.EAGAIN:
            raise
    except OSError as e:
        print("I'm there")
        if e.errno == errno.EPIPE:
            return ''
        raise


if __name__ == "__main__":
    try:
        catcher(errno.EPIPE, "pipe!")
    except Exception as e:
        print(e)
    try:
        catcher(errno.EAGAIN, "again!")
    except Exception as e:
        print(e)
