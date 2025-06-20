import psycopg2


DB_NAME = "dbtask4" 
DB_USER = "postgres"     
DB_PASS = "sql321!"      
DB_HOST = "localhost"    
DB_PORT = 5432           

conn = None
cursor = None

try:
# 1. establish database connection
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER,
        password=DB_PASS, port=DB_PORT
    )
    print("Database connection successful!")
    cursor = conn.cursor()

# 2. create CRM tables (all 5 tables)
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
        cursor.execute(query)
    conn.commit()
    print("All CRM tables created or already exist.")

# 3. insert Sample Data into Trainees (from TASK 4 example)
    print("\nInserting sample trainee data...")
    insert_trainee_query = """
        INSERT INTO Trainees (FullName, EmailAddress, PhoneNumber, PostalCode, StateOfResidence)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (EmailAddress) DO NOTHING; -- Avoids errors if run multiple times
    """
# this list simulates data you would import from cloud files
    trainee_data_to_insert = [
        ("Ahmet Yılmaz", "ahmet@example.com", "5551234567", "12345", "Istanbul"),
        ("Ayşe Demir", "ayse@example.com", "5559876543", "67890", "Ankara"),
        ("Cem Kaya", "cem@example.com", "5551112233", "54321", "Izmir"),
        ("Buse Can", "buse@example.com", "5554445566", "98765", "İzmir"),
        ("Deniz Arı", "deniz@example.com", "5557778899", "11223", "Bursa")
    ]
    cursor.executemany(insert_trainee_query, trainee_data_to_insert)
    conn.commit()
    print(f"{cursor.rowcount} trainee records inserted/updated.")

# 4. verify data in Trainees table (optional)
    print("\nVerifying trainees in database (first 5):")
    cursor.execute("SELECT TraineeID, FullName, EmailAddress FROM Trainees LIMIT 5;")
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")
    if conn:
        conn.rollback() # Rollback changes if an error occurred
finally:
# 5. close cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Database connection closed.")
