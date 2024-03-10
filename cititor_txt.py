def citire_date_text(filename):

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return [line.strip() for line in lines]

    except FileNotFoundError as e:
        print(f"Eroare: Fișierul {filename} nu a fost găsit.")  
        return None
    except Exception as e:
        print(f"Eroare la citirea fișierului text: {e}")
        return None

filename = "date_de_intrare.txt"
date = citire_date_text(filename)

if date:

    print("Datele din fișier:")
    for line in date:
        print(line)
else:
    print("A apărut o eroare la citirea fișierului.")
