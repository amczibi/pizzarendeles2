tipus = []
meret = []
feltet = []
ar = []

hossz = 20

def disz(minta, db):
    print(minta * db)

def p_tipus(sorszam, fajta):
    valasz = str(sorszam) + " - " + str(fajta)
    print(f"*{valasz:^{hossz - 2}}*")

def p_meret(sorszam, meret):
    valasz = str(sorszam) + " - " + str(meret)
    print(f"*{valasz:^{hossz - 2}}*")

def adatbekeres(kerdes):
    adat = input(kerdes)
    return adat

def pizza():

    lead = "i"
    print("Add meg a pizza adatait!")
    valasz = input("Akar új rendelést rögzíteni? i/n: ")

    if valasz == "i":
        while (lead == "i"):
            disz("*", hossz)
            p_tipus(1, "sajtos")
            p_tipus(2, "gombás")
            p_tipus(3, "sonkás")
            tip = adatbekeres("Milyen típusú pizzát kér? ")

            disz("*", hossz)
            p_meret(1, "kicsi")
            p_meret(2, "normál")
            p_meret(3, "nagy")
            mer = adatbekeres("Milyen méretű pizzát kér? ")
            fel = adatbekeres("Kér extra feltétet? i/n: ")
            lead = adatbekeres("Szeretne még rendelést leadni? i/n ")

            tipus.append(tip)
            meret.append(mer)
            feltet.append(fel)

    kiiras()


def tipar_szamolas():
    sajtos = 1000
    gombas = 1100
    sonkas = 1200
    tip_ar = 0
    if tip == "1":
        tip_ar = sajtos
    elif tip == "2":
        tip_ar = gombas
    elif tip == "3":
        tip_ar = sonkas
    print(tip_ar)


def merar_szamolas():
    mer_ar = 0
    kicsi = tip_ar * 0.9
    normal = tip_ar
    nagy = tip_ar * 1.1
    if mer == "1":
        mer_ar = kicsi
    elif mer == "2":
        mer_ar = normal
    elif mer == "3":
        mer_ar = nagy
    print(int(mer_ar))

def plusz_feltet():
    veg_ar = 0
    feltet_ar = 50
    if fel == "i":
        veg_ar = int(mer_ar) + 50
    else:
        veg_ar = int(mer_ar)

def kiiras():
    i = 0
    while (i < len(tipus)):
        print(f"{tipus[i]}, {meret[i]}, {feltet[i]}")
        i = i + 1
        vegosszeg = veg_ar