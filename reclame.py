from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    promo_prijs = prijs - korting
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {promo_prijs} euro"


def inkomsten_totaal(Maandag,Dinsdag,Woensdag,Donderdag,Vrijdag,Zaterdag,Zondag,btw: float):
    totaal = Maandag + Dinsdag + Woensdag + Donderdag + Vrijdag + Zaterdag + Zondag
    btw_factor = 1 + btw
    bedrag = round(totaal / btw_factor) * btw
    return f" Het totaal van all inkomsten van deze week is {totaal} euro, waarover {bedrag} btw betaald dient te worden"

def laag_en_hoog(Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag):
    mijn_lijst = [
        max([Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag]),
        min([Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag])
    ]
    return mijn_lijst

def gemiddelde(Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag):
    mijn_lijst = sum ([Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag])/7
        
    return f"De gemiddelde inkomsten van deze week zijn {mijn_lijst} euro."

def meervoudig(*args):
    invoer_lijst=[
        max (args),
        min (args)
    ]
    return invoer_lijst

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer= mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer


#print (aanbieding_1("aardbei", 4, 0.1))
#print(inkomsten_totaal(220,430,125,160,205,90,345,0.03))
#print(laag_en_hoog(220, 430, 125, 160, 205, 90, 345))
#print(gemiddelde(220, 430, 125, 160, 205, 90, 345))
#print(meervoudig(10,5,3,2,1,2,9))


