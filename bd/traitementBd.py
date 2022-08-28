from sqlalchemy import MetaData, Table, select, insert
from sqlalchemy import Column, Integer, Float, String, Text

class EmployerModel:
    @classmethod
    def createTable(cls, engine):
        metadata = MetaData(bind=engine)

        table = Table('employe', metadata,
                           Column('id', Integer, primary_key=True, autoincrement=True),
                           Column('name', Text, nullable=False),
                           Column('phone', String(50)),
                           Column('email', String(100)),
                           Column('address', Text),
                           Column('latlng', Text),
                           Column('salary', Float),
                           Column('age', Integer),
                           Column('devise', String(100)),
                           Column('salaryXOF', Float),
                           Column('pays', Text)
                    )
        metadata.create_all()
        return table

    @classmethod
    def insererListeEmployer(cls, engine, tableEmploye, listEmployer):
        #engine.execute(table.insert().values(listEmployer))
        with engine.connect() as conn:
            result = conn.execute(
            insert(tableEmploye).values(),
                listEmployer
                 )

        return result


    @classmethod
    def recupererListeEmploye(cls, engine, tableEmploye):
        data = engine.execute(select(tableEmploye)).all()
        column_names = tuple(c.name for c in tableEmploye.c)
        listeEmployer = [dict(zip(column_names, x)) for x in data]
        return listeEmployer




    '''
    utilisation simple sans sqlalchemy
    @classmethod
    def createTable(cls, con):
        cursor = con.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employer(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             name TEXT NOT NULL,
             phone VARCHAR(100),
             email VARCHAR(100),
             address TEXT,
             latlng TEXT,
             salary FLOAT,
             age INTEGER,
             devise VARCHAR(50),
             salaryXOF FLOAT,
             pays VARCHAR(250)
             
        )
        """)
        con.commit()
    

    @classmethod
    def inserer(cls, listEmployer, con):
        cursor = con.cursor()

        cursor.executemany("""
            INSERT INTO employer(name, phone, email, address, latlng, salary, age, devise, salaryXOF, pays)
            VALUES(:name, :phone, :email, :address, :latlng, :salary, :age, :devise, :salaryXOF, :pays)""", listEmployer)
        con.commit()
        
    '''
    '''
    @classmethod
    def recuperer(cls, con):
        cursor = con.cursor()
        res = cursor.execute("SELECT * FROM employer")
        row = res.fetchone()
        resultset = []
        while row is not None:
            row = res.fetchone()
            resultset.append(row)

        return resultset
    '''


