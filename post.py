import psycopg2


DB_NAME = "crm-project" 
DB_USER = "postgres"            
DB_PASS = "sql321!"           
DB_HOST = "localhost"                
DB_PORT = 5432                      

def create_tables(connection):
    """
    Executes SQL queries to create all CRM project tables.
    Uses the table schemas from 'crm-create-tables-sql-short'.
    """
    cursor = None
    try:
        cursor = connection.cursor()

# SQL for Trainees Table
        create_trainees_sql = """
        CREATE TABLE IF NOT EXISTS Trainees (
            TraineeID SERIAL PRIMARY KEY, FullName VARCHAR(255) NOT NULL,
            EmailAddress VARCHAR(255) UNIQUE NOT NULL, PhoneNumber VARCHAR(20),
            PostalCode VARCHAR(20), StateOfResidence VARCHAR(100)
        );
        """
        cursor.execute(create_trainees_sql)
        print("Trainees table created or already exists.")

# SQL for Applications Table
        create_applications_sql = """
        CREATE TABLE IF NOT EXISTS Applications (
            ApplicationID SERIAL PRIMARY KEY, TraineeID INT NOT NULL, Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CurrentStatus VARCHAR(50), WillJoinITPHTraining BOOLEAN, FinancialStatus VARCHAR(50),
            AttendingLanguageCourse BOOLEAN, EnglishLevel VARCHAR(20), DutchLevel VARCHAR(20),
            UnderPressure BOOLEAN, CompletedBootcamp BOOLEAN, AttendedOnlineITCourse BOOLEAN,
            ITExperience TEXT, IncludedInProject BOOLEAN, WillingnessToWork TEXT,
            MotivationForJoining TEXT, ApplicationTerm VARCHAR(50),
            FOREIGN KEY (TraineeID) REFERENCES Trainees(TraineeID) ON DELETE CASCADE
        );
        """
        cursor.execute(create_applications_sql)
        print("Applications table created or already exists.")

# SQL for Mentors Table
        create_mentors_sql = """
        CREATE TABLE IF NOT EXISTS Mentors (
            MentorID SERIAL PRIMARY KEY, MeetingDate DATE NOT NULL, MentorFullName VARCHAR(255) NOT NULL,
            TraineeID INT, HasRelevantKnowledge BOOLEAN, EligibleForVITProject BOOLEAN,
            Thoughts TEXT, AvailabilityStatus VARCHAR(50), Comments TEXT,
            FOREIGN KEY (TraineeID) REFERENCES Trainees(TraineeID) ON DELETE SET NULL
        );
        """
        cursor.execute(create_mentors_sql)
        print("Mentors table created or already exists.")

# SQL for Users Table
        create_users_sql = """
        CREATE TABLE IF NOT EXISTS Users (
            UserID SERIAL PRIMARY KEY, Username VARCHAR(50) UNIQUE NOT NULL,
            Password VARCHAR(255) NOT NULL, Role VARCHAR(50) NOT NULL
        );
        """
        cursor.execute(create_users_sql)
        print("Users table created or already exists.")

# SQL for ProjectTracking Table
        create_project_tracking_sql = """
        CREATE TABLE IF NOT EXISTS ProjectTracking (
            ProjectTrackingID SERIAL PRIMARY KEY, TraineeID INT NOT NULL,
            ProjectSubmissionDate DATE, ProjectReviewDate DATE,
            FOREIGN KEY (TraineeID) REFERENCES Trainees(TraineeID) ON DELETE CASCADE
        );
        """
        cursor.execute(create_project_tracking_sql)
        print("ProjectTracking table created or already exists.")

        connection.commit() # Commit all table creation changes
        print("\nAll CRM tables setup complete!")

    except psycopg2.Error as e:
        print(f"Error creating tables: {e}")
        if connection:
            connection.rollback() # Rollback changes if an error occurs
    finally:
        if cursor:
            cursor.close()

# --- Main execution block ---
if __name__ == "__main__":
    connection = None
    try:
# create database connection
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        print("Database connection successful!")

# Call the function to create tables
        create_tables(connection)

    except Exception as e:
        print(f"Connection or execution error: {e}")
    finally:
# Close the connection
        if connection:
            connection.close()
            print("Database connection closed.")