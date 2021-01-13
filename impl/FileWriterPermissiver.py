import os.path

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(isNoAll = False, isYesAll = False)
def canWriteToFile(filePath):
    if os.path.isfile(filePath):
        if canWriteToFile.isNoAll:
            return False
        elif canWriteToFile.isYesAll:
            return True
        else:
            while True:
                print("File ", filePath, " already exists, override ? (y/n [all])")
                answ = str(input()).strip();
                if answ == "y":
                    return True
                elif answ == "n":
                    return False
                elif answ == "n all":
                    canWriteToFile.isNoAll = True
                    return False
                elif answ == "y all":
                    canWriteToFile.isYesAll = True
                    return True
    else:
        return True