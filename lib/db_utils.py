def fileExists(fileName: str):
    """Checks if a file exists"""
    try:
        file = open(fileName, "r")
        return True
    except:
        return False