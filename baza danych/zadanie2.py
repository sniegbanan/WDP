import sqlite3


# połączenie z bazą danych
connection = sqlite3.connect('baza_danych.db')


# dostęp do kolumn przez nazwy
connection.row_factory = sqlite3.Row

# kursor potrzebny do operacji na bazach danych
kursor = connection.cursor()


# MODEL BAZY DANYCH
    # tabele
kursor.execute("DROP TABLE IF EXISTS klasa;")

kursor.execute("""
    CREATE TABLE IF NOT EXISTS klasa (
        id INTEGER PRIMARY KEY ASC,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT ''
    )""")
# """ - dlatego ze jest kilka instrukcji
# a executescript() bo tez jest duzo isntrukcji
kursor.executescript("""
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

# implementacja danych XD

kursor.execute('INSERT INTO klasa VALUES(NULL, ?, ?);',('1A', 'matematyczny'))
kursor.execute('INSERT INTO klasa VALUES(NULL, ?, ?);',('1B', 'humanistyczny'))
# nie wstawiamy wartosci prosto do sql'a zeby nam program nie wybuchl 
# zamiast tego dajemy pytajniki i przekzaujemy tuple jako drugi argument excuta

#pobieranie id z tabeli klasa dla 1A
kursor.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
klasa_id = kursor.fetchone()[0]
# dajemy 0 zeby wziac pierwszy elemnt listy
# fetchone() zwraca liste pol rekordu

# tworzymy normikow
uczniowie = (
    (None, 'Krzysztof', 'Hołowczyc', klasa_id),
    (None, 'Robert', 'Kubica', klasa_id),
    (None, 'Pierwszy', 'Golec', klasa_id)      
)

# 1 wartosc to klucz glowny, dajemy None zeby baza danych utowrzyla je automatycznie
# wrzucamy normikow do tabelki
kursor.executemany('INSERT INTO uczen VALUES(?,?,?,?)',uczniowie)

# zatwiedzamy zmiany
connection.commit()

# tutaj bedziemy tworzyc kwerende zeby cos zobaczyc
def czytajdane():
    kursor.execute(
            """
            SELECT uczen.id,imie,nazwisko, nazwa FROM uczen,klasa
            WHERE uczen.klasa_id=klasa.id
            """
            )
    uczniowie = kursor.fetchall()
    for uczen in uczniowie:
        print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
    print()
 
    
    
def policzuczniow():
    index = 0 
    kursor.execute(
            """
            SELECT imie nazwa FROM uczen
            """
            )
    uczniowie = kursor.fetchall()
    for uczen in uczniowie:
        index+=1
        
    print("Liczba uczniów", index,"\n")
    
def usun():
    kursor.execute(
            """
            DELETE FROM uczen WHERE uczen.id = 2
            """
            )

    
    
czytajdane()
policzuczniow()

print("Czy chcesz usunąć ucznia (TAK/NIE)")
answer = str(input())
if answer == "TAK":
    usun()
    czytajdane()
    policzuczniow()
else:
    print("Nie to nie")



