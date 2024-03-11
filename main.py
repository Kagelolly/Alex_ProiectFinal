import os
import time
import csv
import json
import datetime
from flask import Flask, request   # pentru JSON endpoint
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup ( SQLite)
# SQL
# CREATE TABLE utilizatori (
#     id INTEGER PRIMARY KEY,
#     nume TEXT,
#     prenume TEXT,
#     companie TEXT,
#     id_manager INTEGER
# );

# CREATE TABLE access (
#     id INTEGER PRIMARY KEY,
#     id_persoana INTEGER,
#     data DATE,
#     ora TIME,
#     sens TEXT,
#     id_poarta INTEGER,
#     FOREIGN KEY (id_persoana) REFERENCES utilizatori (id)
# );

engine = create_engine("sqlite:///baza_date.db", echo=True)  # echo=True for debugging
Base = declarative_base()

class Utilizator(Base):
    __tablename__ = "utilizatori"
    id = Column(Integer, primary_key=True)
    nume = Column(String)
    prenume = Column(String)
    companie = Column(String)
    id_manager = Column(Integer)

class Acces(Base):
    __tablename__ = "access"
    id = Column(Integer, primary_key=True)
    id_persoana = Column(Integer)
    data = Column(DateTime)
    ora = Column(DateTime)
    sens = Column(String)
    id_poarta = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

app = Flask(__name__)

#  (inregistrare_utilizator)
def inregistrare_utilizator():
    
    print("Introduceți detaliile utilizatorului:")
    id = int(input("ID: "))
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    companie = input("Companie: ")
    id_manager = int(input("ID Manager: "))

# Valideaza datele utilizatorului introduse.
    def inregistrare_utilizator():
        try:
            id = int(input("ID: "))
            id_manager = int(input("ID Manager: "))
        except ValueError:
                print("ID și ID Manager trebuie să fie numere întregi.")
                return

    if not isinstance(nume, str) or not isinstance(prenume, str) or not isinstance(companie, str):
        print("Numele, prenumele și compania trebuie să fie șiruri.")
        return

    query = f"""
        INSERT INTO utilizatori (id, nume, prenume, companie, id_manager)
        VALUES ({id}, '{nume}', '{prenume}', '{companie}', {id_manager})
    """
    session.execute(query)

# Salveaza datele in baza de date.
    query = f"""
        INSERT INTO utilizatori (id, nume, prenume, companie, id_manager)
        VALUES ({id}, '{nume}', '{prenume}', '{companie}', {id_manager})
    """
    session.execute(query)

# Mesaj de confirmare.
    print(f"Utilizatorul {nume} a fost inregistrat cu succes!")



class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filename = event.src_path
        if filename.endswith(".csv") or filename.endswith(".txt"):
            procesare_fisier(filename)

def procesare_fisier(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f) if filename.endswith(".csv") else open(filename, "r")
        for row in reader:
# Extrage datele din fișier.
            id_persoana = row[0]
            data = datetime.datetime.strptime(row[1], "%Y-%m-%d")
            ora = datetime.datetime.strptime(row[2], "%H:%M:%S")
            sens = row[3]
            id_poarta = row[4]

# Salveaza in baza de date.
            query = f"""
                INSERT INTO access (id_persoana, data, ora, sens, id_poarta)
                VALUES ({id_persoana}, '{data}', '{ora}', '{sens}', {id_poarta})
            """
            session.execute(query)

# Mutați fișierul procesat in "backup_intrari".
    shutil.move(filename, os.path.join("backup_intrari", filename))

@app.post('/access_data')
def receive_access_data():
    data = request.get_json()
# ... validate data
def validate_data(data):
    try:
        id_persoana = int(data["id_persoana"])
        data_timp = datetime.datetime.strptime(data["data_timp"], "%Y-%m-%d %H:%M:%S")
        sens = data["sens"]
        id_poarta = int(data["id_poarta"])
    except ValueError:
        return False, "Tipuri de date invalide."
    # Verificați valorile permise.
    if sens not in ("in", "out"):
        return False, "Valoare invalidă pentru 'sens'."

    return True, "Date valide."
    def validate_data(data):

        from jsonschema import validate

def validate_json_schema(data, schema_file):
    """
    Funcție pentru validarea datelor JSON conform unei scheme JSON definite.

    Args:
        data: Dicționarul cu datele JSON de validat.
        schema_file: Calea către fișierul JSON care definește schema.

    Returns:
        True dacă datele sunt valide, False altfel.
    """

    try:
        with open(schema_file) as f:
            schema = json.load(f)
        validate(data, schema)
        return True
    except Exception as e:
        print(f"Eroare la validarea schemei JSON: {e}")
        return False

import requests

def get_json_schema(schema_url):
    """
    Funcție pentru a obține schema JSON de la o adresă URL.

    Args:
        schema_url: Adresa URL a fișierului JSON care definește schema.

    Returns:
        Dicționarul cu schema JSON, None dacă apare o eroare.
    """

    try:
        response = requests.get(schema_url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            print(f"Eroare la obținerea schemei JSON: {response.status_code}")
            return None
    except Exception as e:
        print(f"Eroare la obținerea schemei JSON: {e}")
        return None
# Verifica tipurile de date.
    try:
        id_persoana = int(data["id_persoana"])
        data_timp = datetime.datetime.strptime(data["data_timp"], "%Y-%m-%d %H:%M:%S")
        sens = data["sens"]
        id_poarta = int(data["id_poarta"])
    except ValueError:
        return False, "Tipuri de date invalide."

# Verifica valorile permise.
    if sens not in ("in", "out"):
        return False, "Valoare invalidă pentru 'sens'."


    return True, "Date valide."
    
    return 'Data received', 200 

def calculate_work_hours():
# Obține toate intrările/ieșirile din baza de date.
    query = """
        SELECT a.id_persoana, a.data, a.ora, a.sens, u.nume, u.companie, u.id_manager
        FROM access a
        INNER JOIN utilizatori u ON a.id_persoana = u.id
    """
    results = session.execute(query).fetchall()

# Grupeza inregistrările după ID-ul persoanei, data și calculați orele lucrate.
    for id_persoana, data, _, _, nume, companie, id_manager in results:
        entries = [entry for entry in results if entry[0] == id_persoana and entry[1] == data]
        start_time = min(entry[2] for entry in entries if entry[3] == "in")
        end_time = max(entry[2] for entry in entries if entry[3] == "out")
        if end_time and start_time:
            total_hours = (end_time - start_time).total_seconds() / 3600
            if total_hours < 8:
                # Trimiteți o alertă managerului.
                alert_managers(nume, companie, id_manager, total_hours)
#  Obține toate intrările/ieșirile din baza de date.
    query = """
        SELECT a.id_persoana, a.data, a.ora, a.sens, u.nume, u.companie, u.id_manager
        FROM access a
        INNER JOIN utilizatori u ON a.id_persoana = u.id
    """
    results = session.execute(query).fetchall()

# Grupeaza inregistrările după ID-ul persoanei, data și calculați orele lucrate.
    for id_persoana, data, _, _, nume, companie, id_manager in results:
        entries = [entry for entry in results if entry[0] == id_persoana and entry[1] == data]
        start_time = min(entry[2] for entry in entries if entry[3] == "in")
        end_time = max(entry[2] for entry in entries if entry[3] == "out")
        if end_time and start_time:
            total_hours = (end_time - start_time).total_seconds() / 3600
            if total_hours < 8:
 # Functie de trimitere mail
             alert_managers(nume, companie, id_manager, total_hours)

def alert_managers(nume, companie, id_manager, total_hours):
    def alert_managers(nume, companie, id_manager, total_hours):
        query = f"""
            SELECT email
            FROM utilizatori
            WHERE id = {id_manager}
        """
        email = session.execute(query).scalar()

    if email:
        subject = f"{nume} din {companie} nu a lucrat 8 ore astăzi!"
        message = f"""
            Bună ziua,

            Vă informăm că {nume} din compania {companie} a lucrat doar {total_hours} ore astăzi, {data.strftime('%Y-%m-%d')}.

            Vă rugăm să luați la cunoștință această informație.

            Cu stimă,

            Sistemul de monitorizare a orelor lucrate
        """
        send_email(email, subject, message)
