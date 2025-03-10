import psycopg2
from psycopg2.sql import Composable
from googledrive import GoogleDriveFileManager

class DatabaseConnection:
    def __init__(self, database_name="WeRHere", user="postgres", password="OeM1707G", host="localhost"):
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.connection = None
        self.message = ""
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.database_name,
                user=self.user,
                password=self.password,
                host=self.host
            )
            self.message = "Connection is successful!"
        except psycopg2.Error as e:
            self.message = f"Error: {e}"
    def db_executer(self, query: str | bytes | Composable ):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            self.message = "Query executed successfully!"
        except psycopg2.Error as e:
            self.message = f"Error: {e}"
    def db_select(self, query: str | bytes | Composable):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            self.message = "Query executed successfully!"
            return result
        except psycopg2.Error as e:
            self.message = f"Error: {e}"
            return None
def Crate_Tables():
    db_obj = DatabaseConnection()
    db_obj.db_executer("""
        CREATE TABLE IF NOT EXISTS public.kullanicilar
        (
            kullaniciid serial NOT NULL,
            kullaniciadi character varying(50) COLLATE pg_catalog."default" NOT NULL,
            parola character varying(50) COLLATE pg_catalog."default" NOT NULL,
            yetki character(5) COLLATE pg_catalog."default" NOT NULL DEFAULT USER,
            CONSTRAINT kullanicilar_pkey PRIMARY KEY (kullaniciid)
        )
                       
        """)
    print(db_obj.message)

    db_obj.db_executer("""
        CREATE TABLE IF NOT EXISTS public.kursiyerler
        (
            kursiyerid serial NOT NULL ,
            adsoyad character varying(50) COLLATE pg_catalog."default" NOT NULL,
            mailadresi character varying(100) COLLATE pg_catalog."default" NOT NULL,
            telefonnumarasi character varying(12) COLLATE pg_catalog."default" NOT NULL,
            postakodu character varying(7) COLLATE pg_catalog."default",
            yasadiginizeyalet character varying(20) COLLATE pg_catalog."default",
            CONSTRAINT "Kursiyerler_pkey" PRIMARY KEY (kursiyerid)
        )
        """)
    print(db_obj.message)
    
    db_obj.db_executer("""
        CREATE TABLE IF NOT EXISTS public.basvurular
        (
            basvuruid serial NOT NULL,
            kursiyerid integer NOT NULL,
            zamandamgasi timestamp without time zone NOT NULL,
            suankidurum character varying(100) COLLATE pg_catalog."default" NOT NULL,
            itphegitimkatilmak character varying(100) COLLATE pg_catalog."default",
            ekonomikdurum character varying(100) COLLATE pg_catalog."default",
            dilkursunadevam boolean,
            ingilizceseviye character varying(12) COLLATE pg_catalog."default",
            hollandacaseviye character varying(12) COLLATE pg_catalog."default",
            baskigoruyor character varying(100) COLLATE pg_catalog."default",
            bootcampbitirdi character varying(100) COLLATE pg_catalog."default",
            onlineitkursu boolean,
            ittecrube boolean,
            projedahil boolean,
            calismakistegi character varying(100) COLLATE pg_catalog."default",
            nedenkatilmakistiyor text COLLATE pg_catalog."default",
            basvurudonemi character varying(5) COLLATE pg_catalog."default",
            mentorgorusmesi character varying(10) COLLATE pg_catalog."default"
            CONSTRAINT basvurular_pkey PRIMARY KEY (basvuruid),
            CONSTRAINT "FK_kusiyerid" FOREIGN KEY (kursiyerid)
                REFERENCES public.kursiyerler (kursiyerid) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                NOT VALID
        )  

        """)
    print(db_obj.message)
    db_obj.db_executer("""
            CREATE TABLE IF NOT EXISTS public.mentortablosu
            (
                mentorid serial NOT NULL,
                gorusmetarihi date NOT NULL,
                kursiyerid integer NOT NULL,
                bilgisahibimi smallint,
                dusunce text COLLATE pg_catalog."default",
                yogunlukdurumu text COLLATE pg_catalog."default",
                yorumlar text COLLATE pg_catalog."default",
                mentoradsoyad character varying(50) COLLATE pg_catalog."default" NOT NULL,
                CONSTRAINT mentortablosu_pkey PRIMARY KEY (mentorid),
                CONSTRAINT "FK_kusiyerid" FOREIGN KEY (kursiyerid)
                    REFERENCES public.kursiyerler (kursiyerid) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    NOT VALID
            )        
        """)
    print(db_obj.message)
    db_obj.db_executer("""
            CREATE TABLE IF NOT EXISTS public.projetakiptablosu
            (
                projetakipid serial NOT NULL,
                kursiyerid integer NOT NULL,
                projegonderilistarihi timestamp without time zone,
                projeningelistarihi timestamp without time zone,
                CONSTRAINT projetakiptablosu_pkey PRIMARY KEY (projetakipid),
                CONSTRAINT "FK_kusuyerid" FOREIGN KEY (kursiyerid)
                    REFERENCES public.kursiyerler (kursiyerid) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    NOT VALID
            )          
        """)
    print(db_obj.message)
def Convert_data_users():
    DataObject = GoogleDriveFileManager("Kullanicilar", "seracc.json")
    DataObject.getExcelFile()
    write_data =  DataObject.getExcelFile()

    rows, cols = write_data.shape
    # self.tableWidget.setRowCount(rows)
    # self.tableWidget.setColumnCount(cols)
    # self.tableWidget.setHorizontalHeaderLabels(self.DataObject.getExcelFile().columns)
    query = ""
    db_obj = DatabaseConnection()
    for row in range(rows):
        # value = str(write_data.iat[row, col])
        query = "INSERT INTO kullanicilar (kullaniciadi, parola, yetki) VALUES ("
        query += "'" + write_data.iat[row, 0] + "', "
        query += "'" + write_data.iat[row, 1] + "', "
        query += "'" + write_data.iat[row, 2] + "');"
        db_obj.db_executer(query)
        print(query)
        print(db_obj.message)
def Convert_data_kursiyerler():
    DataObject = GoogleDriveFileManager("Basvurular", "seracc.json")
    DataObject.getExcelFile()
    write_data =  DataObject.getExcelFile()

    rows, cols = write_data.shape
    # self.tableWidget.setRowCount(rows)
    # self.tableWidget.setColumnCount(cols)
    # self.tableWidget.setHorizontalHeaderLabels(self.DataObject.getExcelFile().columns)
    query = ""
    db_obj = DatabaseConnection()
    for row in range(rows):
        # value = str(write_data.iat[row, col])
        kursiyerid = db_obj.db_select("SELECT MIN(kursiyerid) FROM kursiyerler WHERE adsoyad = '" + str(write_data.iat[row, 1]) + "';")
        if kursiyerid[0][0] == None :
            query = "INSERT INTO kursiyerler (adsoyad, mailadresi, telefonnumarasi, postakodu, yasadiginizeyalet) VALUES ("
            query += "'" + str(write_data.iat[row, 1]) + "', "
            query += "'" + str(write_data.iat[row, 2]) + "', "
            query += "'" + str(write_data.iat[row, 3]) + "', "
            query += "'" + str(write_data.iat[row, 4]) + "', "
            query += "'" + str(write_data.iat[row, 5]) + "');"
            db_obj.db_executer(query)
            print(query)
            print(db_obj.message)
        else:
            print("Kursiyer already exists!")
def Convert_data_basvurular():
    DataObject = GoogleDriveFileManager("Basvurular", "seracc.json")
    DataObject.getExcelFile()
    write_data =  DataObject.getExcelFile()

    rows, cols = write_data.shape
   
    query = ""
    db_obj = DatabaseConnection()
    for row in range(rows):
        # value = str(write_data.iat[row, col])
        query = "INSERT INTO basvurular (kursiyerid, zamandamgasi, suankidurum, itphegitimkatilmak, ekonomikdurum, dilkursunadevam, ingilizceseviye, hollandacaseviye, "
        query += "baskigoruyor, bootcampbitirdi, onlineitkursu, ittecrube, projedahil, calismakistegi, nedenkatilmakistiyor, basvurudonemi, mentorgorusmesi) VALUES ("
        kursiyerid = db_obj.db_select("SELECT MIN(kursiyerid) FROM kursiyerler WHERE adsoyad = '" + str(write_data.iat[row, 1]) + "';")
        if  kursiyerid == None:
            print("Kursiyer not found!")
            continue
        query += str(kursiyerid[0][0]) + ", "
        query +="'" + str(write_data.iat[row, 0])+ "', "
        query += "'" + str(write_data.iat[row, 6]) + "', "
        query += "'" + str(write_data.iat[row, 7]) + "', "
        query += "'" + str(write_data.iat[row, 8]) + "', "
        query += "True"+ ", " if write_data.iat[row, 9] == "Evet" else "False" + ", "
        query += "'" + str(write_data.iat[row, 10]) + "', "
        query += "'" + str(write_data.iat[row, 11]) + "', "
        query += "'" + str(write_data.iat[row, 12]) + "', "
        query += "'" + str(write_data.iat[row, 13]) + "', "
        query += "True"+ ", " if write_data.iat[row, 14] == "Evet" else "False" + ", "
        query += "True"+ ", " if write_data.iat[row, 15] == "Evet" else "False" + ", "
        query += "True"+ ", " if write_data.iat[row, 16] == "Evet" else "False" + ", "
        query += "'" + str(write_data.iat[row, 17]) + "', "
        query += "'" + str(write_data.iat[row, 18]) + "', "
        query += "'" + str(write_data.iat[row, 21]) + "',"
        query += "'" + str(write_data.iat[row, 20]) + "');"
        print(query)
        db_obj.db_executer(query)
        print(db_obj.message)

def Convert_data_mentor():
    DataObject = GoogleDriveFileManager("Mentor", "seracc.json")
    DataObject.getExcelFile()
    write_data =  DataObject.getExcelFile()

    rows, cols = write_data.shape
   
    query = ""
    db_obj = DatabaseConnection()
    for row in range(rows):
        # value = str(write_data.iat[row, col])
        query = "INSERT INTO mentortablosu (gorusmetarihi, mentoradsoyad, kursiyerid, bilgisahibimi, dusunce, yogunlukdurumu, yorumlar) VALUES ("
        query +="'" + str(write_data.iat[row, 0])+ "', "
        query +="'" + str(write_data.iat[row, 3])+ "', "
        kursiyerid = db_obj.db_select("SELECT MIN(kursiyerid) FROM kursiyerler WHERE adsoyad = '" + str(write_data.iat[row, 2]) + "';")
        if  kursiyerid == None:
            print("Kursiyer not found!")
            continue
        query += str(kursiyerid[0][0]) + ", "
        query += str(write_data.iat[row, 4]) + ", "
        query += "'" + str(write_data.iat[row, 8]) + "', "
        query += "'" + str(write_data.iat[row, 5]) + "', "
        query += "'" + str(write_data.iat[row, 6]) + "');"
        print(query)
        db_obj.db_executer(query)
        print(db_obj.message)

def Convert_data_interview():
    DataObject = GoogleDriveFileManager("Mulakatlar", "seracc.json")
    DataObject.getExcelFile()
    write_data =  DataObject.getExcelFile()

    rows, cols = write_data.shape
   
    query = ""
    db_obj = DatabaseConnection()
    for row in range(rows):
        # value = str(write_data.iat[row, col])
        query = "INSERT INTO projetakiptablosu (kursiyerid, projegonderilistarihi, projeningelistarihi) VALUES ("
        kursiyerid = db_obj.db_select("SELECT MIN(kursiyerid) FROM kursiyerler WHERE adsoyad = '" + str(write_data.iat[row, 0]) + "';")
        if  kursiyerid == None:
            print("Kursiyer not found!")
            continue
        query += str(kursiyerid[0][0]) + ", "
        query += "'" + str(write_data.iat[row, 1]) + "', "
        if str(write_data.iat[row, 2]) == "" or str(write_data.iat[row, 2]) == "NaT":
            query += "NULL" + ");"
        else:    
            query += "'" + str(write_data.iat[row, 2]) + "');"
        print(query)
        db_obj.db_executer(query)
        print(db_obj.message)

def main():
    db_obj = DatabaseConnection()
    rows = db_obj.db_select("""
       SELECT * FROM kursiyerler ;
                            """)
    for row in rows:
        print(row)
    # print(rows)
    # print(rows[0][0])
    print(db_obj.message)

if __name__ == "__main__":
    # Crate_Tables()
    # Convert_data_users() 
    # Convert_data_kursiyerler()
    # Convert_data_basvurular()
    # Convert_data_mentor()
    # Convert_data_interview()
    main()
    pass
    