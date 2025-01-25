#import packages
from datetime import datetime
import os
import pandas as pd
import csv
import re
from connect_to_db import ConnectToDB


class UpdateCSVDataSourceGenres:
    def __init__(self):
        self.export_file_path = os.path.abspath("API/Data-Sources/PlaylistGenres.csv")
        self.data_source_path = os.path.abspath("API/Data-Sources/Genre-Specific-Playlists/")
        self.data_source_list = [file for file in os.listdir(self.data_source_path) if file.endswith(".csv")]
        self.sql_statements_path = os.path.abspath("API/Data-Sources/SQL-Statements")
        self.headers = ["id","genre"]
        self.update_file()
        self.update_playlist_genres()
        self.convert_to_sql_statement()
        
    def update_file(self):
        """Get a list of csv files from the data source and update the genre's csv file with each playlist genre type."""
        counter = 0 
        with open(self.export_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.headers)
            for file in self.data_source_list:
                file_string = file.lower().removesuffix('.csv')
                writer.writerow([counter,file_string])
                counter+=1
                
    def update_playlist_genres(self):
        """Updates individual genre playlist tables to include the id of the genre the link to."""
        for file in self.data_source_list:
           file_path = f"{self.data_source_path}/{file}"
           csv_input = pd.read_csv(file_path)
           if("genre" in csv_input.columns):
               csv_input.drop("genre", axis=1, inplace=True)
           if("id" not in csv_input.columns):
                csv_input.insert(0, 'id', [i for i in range(len(csv_input))])
           csv_genre_input = pd.read_csv(self.export_file_path)
           genre_id = csv_genre_input['id'][csv_genre_input['genre']==f"{file.lower().removesuffix('.csv')}"].values[0]
           csv_input['genre_id'] = genre_id
           csv_input.to_csv(file_path, index=False)
           
    def convert_to_sql_statement(self):
        """Converts csv tables into individual sql tables."""
        self.generate_sql_statements(self.export_file_path)
        for file in self.data_source_list:
            self.generate_sql_statements(f"{self.data_source_path}/{file}")
            
    def convert_file_name(self, fileName):
        """Converts the csv file name to the common sql naming sequence."""
        return re.sub(r"([a-z])([A-Z])", r"\1_\2", fileName).lower()
    
    def convert_column_name(self, columnName):
        """Converts the given column name into the sql syntax."""
        new_string = str(columnName).replace(" ", "_")
        return re.sub(r'[^a-zA-Z0-9_]', '', new_string).lower()
    
    def generate_sql_statements(self, csvFile):
        """Generate SQL statements with a given csv table."""
        file_name_text = os.path.splitext(os.path.basename(csvFile))[0]
        with open(csvFile, 'r') as table:
            reader = csv.reader(table)
            header = next(reader)
            table_name = self.convert_file_name(file_name_text)
            create_table_string =f"""IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' AND xtype='U')
            CREATE TABLE {table_name} (
{self.create_table_values(csvFile, header)})
"""
            header_string = ""
            for column in header:
                header_string += f"{self.convert_column_name(column)},"
            header_string = header_string.rstrip(",")
            insert_query_string = ""
            for row in reader:
                values = ", ".join(f"'{self.replace_apostrophe(value)}'" if "'" in value else f"'{value}'" for value in row)
                insert_query_string += f"INSERT INTO {table_name} ({header_string}) VALUES ({values})\n"
            add_fk = ""
            if table_name != "playlist_genres":
                add_fk = self.join_sql_table_to_genre(table_name, "genre_id", "playlist_genres", "id")
            export_sql_txt_path = f"{self.sql_statements_path}/{file_name_text}.txt"
            with open(export_sql_txt_path, "w") as sql_output:
                sql_output.write(create_table_string)
                sql_output.write(insert_query_string)
                sql_output.write(add_fk)
            db = ConnectToDB("DESKTOP-LOBD6GT\SQLEXPRESS","PlaylistPitcher")
            db.database_setup(export_sql_txt_path)
            db.close_connection()
            
    def create_table_values(self, csvFile, headers):
        """Create the table values for MSSQL Server based on the value of each item in the chart."""
        table_value_queries = ""
        df = pd.read_csv(csvFile)
        for column in headers:
            new_val = self.find_first_val(df, column)
            column = self.convert_column_name(column)
            match new_val:
                case bool():
                    table_value_queries+=f"\t\t\t\t{column} bit,\n"
                case int():
                    if column == "id":
                        table_value_queries+=f"\t\t\t\t{column} int NOT NULL,\n"
                    else:
                        table_value_queries+=f"\t\t\t\t{column} int,\n"
                case float():
                    table_value_queries+=f"\t\t\t\t{column} real,\n"
                case datetime():
                    table_value_queries+=f"\t\t\t\t{column} date,\n"
                case str():
                    table_value_queries += f"\t\t\t\t{column} varchar(255),\n"
                case _:
                    table_value_queries += f"\t\t\t\t{column} varchar(255),\n" 
        table_value_queries += "\t\t\t\tPRIMARY KEY (id)\n"
        return table_value_queries
        
    def join_sql_table_to_genre(self, table, key, referenceTable, referenceTableKey):
        """Link each sql tables with given foreign key and reference table."""
        export_string = f"""
ALTER TABLE {table}
ADD FOREIGN KEY ({key})
REFERENCES {referenceTable}({referenceTableKey})"""
        return export_string
        
    def find_first_val(self, dataFrame, column):
        """Find the first nonempty value in a pandas dataframe column."""
        for val in dataFrame[column]:
            if val != '' and val != None and not pd.isnull(val):
                return val
        return ''
            
    def replace_apostrophe(self, string):
        """Replace apostrophe's for insert sql statements"""
        return str(string).replace("'", "''")
        
UpdateCSVDataSourceGenres()