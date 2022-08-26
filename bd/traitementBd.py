
class EmployerModel:
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
