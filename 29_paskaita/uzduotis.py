# 1 užduotis
# sukurkite funkciją, kuri prideda elementą prie sąrašo, jeigu tas elementas dar neegzistuoja (sąrašas visada yra unikalus)
# jūsų funkcija visada turi grąžinti rikiuoti sąrašą (nuo mažiausio iki didžiausio)
# parašykite šiai funkcijai keletą unit testų, naudokite setUp ir tearDown

def prideti_unikalu(sarasas, elementas):
    if elementas not in sarasas:
        sarasas.append(elementas)
        sarasas.sort()
    return sarasas

#SARUNO SPRENDIMAS:
# def prideti_elementa(elementas,element_sarasas):
#     if elementas not in element_sarasas:
#             element_sarasas.append(elementas)
#     else:
#           return 'Elementas jau yra sarase'
#     return sorted(element_sarasas)


# 2 užduotis
# Parašykite funkciją ar_lyginis, kuri patikrina, ar duotas sveikasis skaičius yra nelyginis.
# Tada parašykite testus, kurie patikrina, ar ši funkcija veikia tinkamai, naudodami assertTrue ir assertFalse.

def ar_lyginis(skaicius):
    if skaicius % 2 == 0:
        return False
    else:
        return True

#MANTVYDO SPRENDIMAS:
def ar_nelyginis (skaicius):
    return skaicius %2 != 0

# 3 užduotis
# Parašykite funkciją ar_palindromas, kuri patikrina, ar duotas tekstas yra palindromas (skaitant atvirkštine tvarka jis vis tiek skaitomas taip pat). 
# Tada parašykite testus, kurie patikrina, ar ši funkcija veikia tinkamai, naudodami assertTrue ir assertFalse.

def ar_palindromas(tekstas):
    return tekstas == tekstas[::-1]

# 4 užduotis
# Parašykite funkciją palyginti_sarasus, kuri patikrina, ar duoti sąrašai yra lygūs. 
# Tada parašykite testus, kurie naudoja assertEqual ir assertNotEqual, kad patikrintų, ar ši funkcija veikia tinkamai.

def palyginti_sarasus(sarasas1, sarasas2):
    return sarasas1 == sarasas2

#ANOS SPRENDIMAS: 
def palyginti_sarasus(sar1, sar2):
    return sar1 == sar2