# 17. Define an abstract class IDatabaseOperations with methods insert(), update(), and delete().
#  Implement this in SQLDatabase and NoSQLDatabase.\



from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def update(self, value, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, value):
        print(f"{value} inserted in SQLDatabase")

    def update(self, value, id):
        print(f"{id} in SQLDatabase updated to {value}")

    def delete(self, id):
        print(f"{id} in SQLDatabase deleted")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, value):
        print(f"{value} inserted in NoSQLDatabase")

    def update(self, value, id):
        print(f"{id} in NoSQLDatabase updated to {value}")

    def delete(self, id):
        print(f"{id} in NoSQLDatabase deleted")


def main():
    sql = SQLDatabase()
    sql.insert(1)
    sql.update(2, 3)
    sql.delete(4)

    nosql = NoSQLDatabase()
    nosql.insert(5)
    nosql.update(6, 7)
    nosql.delete(8)

main()