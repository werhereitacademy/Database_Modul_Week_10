from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io, os
import pandas as pd
import psycopg2

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CLIENT_SECRETS_FILE = r'task_2_crm\python_files\credentials.json'
TOKEN_FILE = r'task_2_crm\python_files\token.json'

if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
else:
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())

service = build('drive', 'v3', credentials=creds)
folder_id = '1LFAU6uVOLzYatC5J_moXNOaNVL5SNGIt'
results = service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
files = results.get('files', [])
excelDicts = {}

for file in files:
    file_id = file['id']
    file_name = file['name'].split('.')[0] 
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)
    df = pd.read_excel(fh)

    df = df.astype(str).replace({'NaT': None, 'nan': None})

    
    excelDicts[file_name] = df 

conn = psycopg2.connect(
    dbname="CRM",
    user="postgres",
    password="",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

for table_name, df in excelDicts.items():
    try:
        columns_with_types = ', '.join([f'"{col}" TEXT' for col in df.columns.tolist()])
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});'
        cur.execute(create_table_query)

        columns = [f'"{col}"' for col in df.columns.tolist()]
        for _, row in df.iterrows():
            values = tuple(row)
            placeholders = ', '.join(['%s'] * len(columns))
            query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
            cur.execute(query, values)

        conn.commit()
    except Exception as e:
        print("Hata oluştu:", e)
        conn.rollback()

basvurularTable = """
    ALTER TABLE Basvurular ADD COLUMN id SERIAL PRIMARY KEY;
    ALTER TABLE Mentor ADD COLUMN id SERIAL PRIMARY KEY;
    ALTER TABLE Mulakatlar ADD COLUMN id SERIAL PRIMARY KEY;
"""
cur.execute(basvurularTable)

cur.execute('ALTER TABLE Mentor ADD COLUMN basvuru_id INT;')
cur.execute("""
    ALTER TABLE Mentor 
    ADD CONSTRAINT fk_basvuru FOREIGN KEY (basvuru_id) 
    REFERENCES Basvurular(id) ON DELETE CASCADE;
""")

cur.execute('ALTER TABLE Mulakatlar ADD COLUMN basvuru_id INT;')
cur.execute("""
    ALTER TABLE Mulakatlar 
    ADD CONSTRAINT fk_mulakat FOREIGN KEY (basvuru_id) 
    REFERENCES Basvurular(id) ON DELETE CASCADE;
""")

conn.commit()
cur.close()
conn.close()
