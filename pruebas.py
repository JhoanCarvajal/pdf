import os

wd = os.getcwd()
print("working directory is ", wd)

filePath = __file__
print("This script file path is ", filePath)

absFilePath = os.path.abspath(__file__)
print("This script absolute path is ", absFilePath)

path, filename = os.path.split(absFilePath)
print("Script file path is {}, filename is {}".format(path, filename))