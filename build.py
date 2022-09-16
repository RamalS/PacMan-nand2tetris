import os
import shutil

path = os.getcwd()
build = os.path.join(path, "build")

def MoveFiles(path):
    for filename in os.listdir(path):
        if filename.endswith(".jack"):
            try:
                shutil.copy(os.path.join(path, filename),
                            os.path.join(build, filename))
            except:
                pass
        elif os.path.isdir(os.path.join(path, filename)):
            MoveFiles(os.path.join(path, filename))


if __name__ == "__main__":
    if os.path.exists(build):
        for files in os.listdir(build):
            os.remove(os.path.join(build, files))
    else:
        os.mkdir(build)

    MoveFiles(path)

    os.system(f'JackCompiler.bat "{build}"')

    for item in os.listdir(build):
        if item.endswith(".jack"):
            os.remove(os.path.join(build, item))
