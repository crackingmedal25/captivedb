import os
from lib.db_utils import fileExists

def initGitRepo():
    command = "git init"
    os.popen(command, mode="w").close()


def createGitIgnore():
    """Adds a gitignore file or appends to it"""

    ignoreStr = "\n# Adds the database directory to the git ignore list\n/.db"
    fileName = ".gitignore"

    if fileExists(fileName):
        file = open(fileName, "a")
        file.write(ignoreStr)
        file.close()
    else:
        file = open(fileName, "w")
        file.write(ignoreStr)
        file.close()

def createDatabaseDir():

    """Creates the initial database directory"""

    try:
        createGitIgnore()
        initGitRepo()
        
        path = "./.db"
        os.mkdir(path)

    except:
        pass