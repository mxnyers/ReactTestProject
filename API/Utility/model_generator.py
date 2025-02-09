from sqlalchemy.sql import text

class ModelGenerator:
    def __init__(self, db):
        self.db =db
        self.models = self.generate_models_for_all_tables()
        
    def generate_models_for_all_tables(self):
        tables_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
        table_names = self.db.session.execute(text(tables_query)).fetchall()
        models = {}
        for (table_name,) in table_names:
            models[table_name] = self.generate_model_from_query(table_name)
        return models
        
    def generate_model_from_query(self, table_name):
        query = f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
        results = self.db.session.execute(text(query)).fetchall()
        
        attrs = {'__tablename__': table_name, 'id': self.db.Column(self.db.Integer, primary_key=True)}
        for column_name, data_type in results:
            if data_type in ['varchar', 'text']:
                attrs[column_name] = self.db.Column(self.db.String(255))
            elif data_type in ['int', 'bigint']:
                if column_name == "id":
                    attrs[column_name] = self.db.Column(self.db.Integer,primary_key=True)
                else:
                    attrs[column_name] = self.db.Column(self.db.Integer)                    
            elif data_type in ['float', 'decimal']:
                attrs[column_name] = self.db.Column(self.db.Float)
        
        return type(table_name, (self.db.Model,), attrs)