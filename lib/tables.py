def fileExists(fileName: str):
    """Checks if a file exists"""
    try:
        file = open(fileName, "r")
        return True
    except:
        return False

class Table:

    def __init__(self, tableName: str) -> None:
        self.tableName = tableName
        pass

    def columns(self) -> list[str]:
        pass

    def initTableFile(self):
        """Initializes the csv file storing the table"""


        fileName = f"./.db/{self.tableName}.csv"
        if fileExists(fileName):
            pass
        else:

            hStr = ""
            for column in self.columns(): hStr += f",{column}"
            hStr = hStr[1:]
            hStr += "\n"

            file = open(fileName, "w")
            file.write(hStr)
            file.close()

    def insertRow(self, values: list):
        """Inserts values into table
        parameter values is a list of values
        """

        if len(values) == len(self.columns()):
            rowStr = ""

            for value in values:
                rowStr += f",{value}"

            rowStr = rowStr[1:]
            rowStr += "\n"

            fileName = f"./.db/{self.tableName}.csv"
            file = open(fileName, "a")
            file.write(rowStr)
