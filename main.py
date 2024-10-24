from lib.init_database import createDatabaseDir
from lib.tables import Table

createDatabaseDir()

class UserTable(Table):

    def __init__(self) -> None:
        super().__init__(tableName="users")
        self.initTableFile()

    def columns(self) -> list[str]:
        return ["id", "username", "email"]
    
usersTable = UserTable()

usersTable.insertRow([1, "tadiwanashe", "tshxng@gmail.com"])