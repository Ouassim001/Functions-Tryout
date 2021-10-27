# SUBMARINE CRASH 1 #
import time
def start():
    print("""je zit in een onderzeeer, en er is zuurstofgebrek wat doe je 
    a. het luik openmaken
    b. zuurstoffles  zoeken\n """)
    ans = input("a/b ")
    if ans == "a":
        luik()
    else:
        fles()

def luik():
    print("""er stroomt water naar binnen, wat doe je 
    a. zwemmen naar de oppervlakte
    b. terug de onderzeeer in\n  """)
    ans = input("a/b \n")
    if ans == "b":
        terug()
    else:
        zwemmen()

def fles():
    print("""je zit te diep onder water je verdrinkt.""")


def terug():
    print("""goeie keus je haalt het net. toch heb je nog steeds een probleem, want de helft van de onderzeeer zit vol met water. wat nu?
    a. je gebruikt het spoel mechanisme om het water eruit te krijgen
    b. sluit jezelf op in de bunker in de onderzeeer\n""")
    ans = input("a/b \n")
    if ans == "a":
        aankomst()
    else:
        stikken()

def zwemmen():
    print("""je bent te traag je bent dood""")

def aankomst():
    print("""goed gedaan al het water is weg. je hoort vanuit de speakers dat je uit kan stappen en weer aan land kan, maar de deur zit klem wat doe je
    a. je probeert de deur open te maken met een kleine granaat
    b. je probeert de deur open te maken met dunne staafjes dynamiet \n""")
    ans = input("a/b \n")
    if ans == "a":
        victory()
    else:
        death()

def stikken():
    print("foute keus er zit veel te weinig zuurstof in de bunker; de voorraad van de bunker is al gebruikt voor de onderzeeër dus stik je in de bunker")

def victory():
    print("slim om de dunne staafjes dynamiet te gebruiken, zo blaas je alleen de stalen deur op.")
    print("Je hebt SUBMARINE CRASH 1 overleefd ")

def death():
    print("de granaat die je gooit richting de deur veroorzaakt een kettingreactie, waardoor de onderzeeër explodeerd, en jij verslonden wordt door de onderzeeër")

start()
luik()
fles()
terug()
zwemmen()
aankomst()
stikken()
victory()
death()