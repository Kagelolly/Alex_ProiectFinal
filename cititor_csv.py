import csv

def citire_date_csv(filename):

    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    except FileNotFoundError as e:
        print(f"Eroare: Fișierul {filename} nu a fost găsit.")
        return None
    except Exception as e:
        print(f"Eroare la citirea fișierului CSV: {e}")
        return None

filename = "date_de_intrare.csv"
data = citire_date_csv(filename)

if data:

    print("Datele din fișier:")
    for row in data:
        print(row)
else:
    print("A apărut o eroare la citirea fișierului.")
