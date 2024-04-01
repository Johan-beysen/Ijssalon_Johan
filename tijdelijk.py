prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade":5
}
aanbieding = prijzen["vanille"] * 0.8 
reclame_tekst= f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst3 = (reclame_tekst).upper()
reclame_tekst4 = (reclame_tekst).split()
for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())

