import pyodbc
from getpass import getpass

class ConnectToDB:
    def __init__(self, server, database):
        """Initialize class with MSSQL database values."""
        self.server = server
        self.database = database
        self.connection = None
        self.cursor = None
        self.establish_connection()
        #self.test_connection()

        
    def establish_connection(self):
        """Create the connection string and establish the connection to the db."""
        self.connection = pyodbc.connect(driver='{SQL Server}', server=self.server, database=self.database, trusted_connection='yes')
        self.cursor = self.connection.cursor()
        
    def test_connection(self):
        """Test the connection to the SQL DB"""
        query="SELECT * FROM playlist_genres"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
            
    def database_setup(self, sqlFile):
        """Function sets up a table with a given txt file containing sql statements."""
        with open(sqlFile, 'r') as sql:
            sql_statements = sql.read()
        self.cursor.execute(sql_statements)
        self.connection.commit()
        
    def pull_all_data(self, table):
        """Generate data from given table"""
        
    def pull_specific_fields(self, table, params):
        """Select given fields from the given table"""
        
    def close_connection(self):
        """Close the connection to the server."""
        self.connection.close()
        
#DESKTOP-LOBD6GT\SQLEXPRESS
# user_input_server = input("Please enter server name: ")
#PlaylistPitcher
# user_input_db = input("Please input database name: ")

# ConnectToDB(user_input_server,user_input_db)