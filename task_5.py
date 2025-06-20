import psycopg2


DB_NAME = "dbtask5"  
DB_USER = "postgres"     
DB_PASS = "sql321!"      
DB_HOST = "localhost"    
DB_PORT = 5432           

class DatabaseManager:
    """Manages PostgreSQL connections and query execution."""
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        """Establishes connection to the database."""
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, user=self.user,
                password=self.password, host=self.host, port=self.port
            )
            print("Database connection successful!")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            self.conn = None
            return False

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
            self.conn = None

    def execute_query(self, sql_query, params=None, fetch_results=False):
        """Executes an SQL query, returning results if specified."""
        if not self.conn:
            print("No database connection available.")
            return None
        
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_query, params)
            if fetch_results:
                return cursor.fetchall()
            else:
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Query execution error: {e}")
            if self.conn:
                self.conn.rollback() # Rollback changes on error
            return None
        finally:
            if cursor:
                cursor.close()

class Trainee:
    """Represents a Trainee entity with its attributes."""
    def __init__(self, trainee_id, full_name, email_address, phone_number, postal_code, state_of_residence):
        self.trainee_id = trainee_id
        self.full_name = full_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.postal_code = postal_code
        self.state_of_residence = state_of_residence

    def __repr__(self):
        return (f"Trainee(ID={self.trainee_id}, Name='{self.full_name}', "
                f"Email='{self.email_address}')")

# --- Main Application Logic ---
if __name__ == "__main__":
    db_manager = DatabaseManager(DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT)

    if db_manager.connect():
        try:
# 1. Create CRM Tables
            print("\nCreating CRM tables...")
            create_table_queries = [
                """
                CREATE TABLE IF NOT EXISTS Trainees (
                    TraineeID SERIAL PRIMARY KEY, FullName VARCHAR(255) NOT NULL,
                    EmailAddress VARCHAR(255) UNIQUE NOT NULL, PhoneNumber VARCHAR(20),
                    PostalCode VARCHAR(20), StateOfResidence VARCHAR(100)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Applications (
                    ApplicationID SERIAL PRIMARY KEY, TraineeID INT NOT NULL, Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    CurrentStatus VARCHAR(50), WillJoinITPHTraining BOOLEAN, FinancialStatus VARCHAR(50),
                    AttendingLanguageCourse BOOLEAN, EnglishLevel VARCHAR(20), DutchLevel VARCHAR(20),
                    UnderPressure BOOLEAN, CompletedBootcamp BOOLEAN, AttendedOnlineITCourse BOOLEAN,
                    ITExperience TEXT, IncludedInProject BOOLEAN, WillingnessToWork TEXT,
                    MotivationForJoining TEXT, ApplicationTerm VARCHAR(50),
                    FOREIGN KEY (TraineeID) REFERENCES Trainees(TraineeID) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Mentors (
                    MentorID SERIAL PRIMARY KEY, MeetingDate DATE NOT NULL, MentorFullName VARCHAR(255) NOT NULL,
                    TraineeID INT, HasRelevantKnowledge BOOLEAN, EligibleForVITProject BOOLEAN,
                    Thoughts TEXT, AvailabilityStatus VARCHAR(50), Comments TEXT,
                    FOREIGN KEY (TraineeID) REFERENCES Trainees(TraineeID) ON DELETE SET NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Users (
                    UserID SERIAL PRIMARY KEY, Username VARCHAR(50) UNIQUE NOT NULL,
                    Password VARCHAR(255) NOT NULL, Role VARCHAR(50) NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS ProjectTracking (
                    ProjectTrackingID SERIAL PRIMARY KEY, TraineeID INT NOT NULL,
                    ProjectSubmissionDate DATE, ProjectReviewDate DATE,
                    FOREIGN KEY (TraineeID) REFERENCES Trainees(TraineeID) ON DELETE CASCADE
                );
                """
            ]
            for query in create_table_queries:
                db_manager.execute_query(query) # Use db_manager to execute
            print("All CRM tables created or already exist.")

# 2. Insert Sample Data into Trainees
            print("\nInserting sample trainee data...")
            insert_trainee_query = """
                INSERT INTO Trainees (FullName, EmailAddress, PhoneNumber, PostalCode, StateOfResidence)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (EmailAddress) DO NOTHING;
            """
            trainee_data_to_insert = [
                ("Ahmet Yılmaz", "ahmet@example.com", "5551234567", "12345", "Istanbul"),
                ("Ayşe Demir", "ayse@example.com", "5559876543", "67890", "Ankara"),
                ("Cem Kaya", "cem@example.com", "5551112233", "54321", "Izmir"),
                ("Buse Can", "buse@example.com", "5554445566", "98765", "İzmir"),
                ("Deniz Arı", "deniz@example.com", "5557778899", "11223", "Bursa")
            ]
# Use cursor.executemany via a temporary cursor to use db_manager for this
            with db_manager.conn.cursor() as temp_cursor:
                temp_cursor.executemany(insert_trainee_query, trainee_data_to_insert)
            db_manager.conn.commit()
            print(f"{temp_cursor.rowcount} trainee records inserted/updated.")


# 3. Fetch and display data from the database (replacing 'cloud queries')
            print("\nFetching and displaying trainees from the database:")
            select_all_trainees_query = "SELECT TraineeID, FullName, EmailAddress, PhoneNumber, PostalCode, StateOfResidence FROM Trainees;"
            results = db_manager.execute_query(select_all_trainees_query, fetch_results=True)
            
            if results:
                trainees = [Trainee(*row) for row in results]
                for trainee in trainees:
                    print(trainee)
            else:
                print("No trainees found in the database.")

        except Exception as e:
            print(f"An error occurred during project execution: {e}")
        finally:
            db_manager.close()