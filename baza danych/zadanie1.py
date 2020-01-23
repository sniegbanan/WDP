import dbm

with dbm.open('cache','c') as db:
    db['pierwsza baza danych'] = 'przykladowy tekst1'
    db['druga baza danych'] = 'przykladowy tekst2'
    db['trzecia baza danych'] = 'przykladowy tekst3'
    
    
    print(db.get('pierwsza baza danych'))
    print(db.get('druga baza danych'))
    print(db.get('trzecia baza danych'))