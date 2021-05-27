from mysql.connector import connect, connection

class Connection :
    
    def connection(self) :
        self.db = connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'kampus'
        )

        return self.db
