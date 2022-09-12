#!/usr/bin/env python
# Tämä on aloitusskripti

import henkilö
import vuodet



def pääfunktio():
    syntymävuosi = 1970
    aliisa = henkilö.Henkilö("Aliisa", 1980)
    bob = henkilö.Henkilö(nimi="Bob", syntymävuosi=1967)

    print(aliisa.nimi)
    print(aliisa.syntymävuosi)

    print(aliisa.ikä())

    print("kutsutaan henkilötiedot-funktiota")
    paluuarvo = bob.tiedot(lempiväri="punainen")
    print("palattiin funktiosta, paluuarvo:", paluuarvo)
    print("Joku syntymävuosi:", syntymävuosi)


pääfunktio()

# teksti = input("Anna luku: ")  # input on funktio

# print(teksti)  # "print" on siis funktio



# if teksti.isdigit():  # isdigit = str luokan metodi (method of str class)
#     luku = int(teksti)
# elif teksti == "yksi":
#     luku = 1
# elif teksti == "kaksi":
#     luku = 2
# elif teksti == "kymppi":
#     luku = 10
# else:
#     print("Ei ollu luku. Varmaan 0 käy sitten.")
#     luku = 0

# print("Luku on:", luku)

# if luku > 10:
#     print("suurempi kuin 10")
# elif luku == 10:
#     print("tasan 10")
# else:
#     print("pienempi kuin 10")
