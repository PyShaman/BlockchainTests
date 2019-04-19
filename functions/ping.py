import subprocess as sp


def check():
    status, result = sp.getstatusoutput("ping -c1 -w2 localhost")
    if status == 0:
        return True
    else:
        return False
