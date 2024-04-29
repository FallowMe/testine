# 1 užduotis
# Parašykite funkciją skaiciu_suma(skaiciai), kuri priima sąrašą skaičių ir grąžina jų sumą.
# Parašykite testą, kuris patikrina, ar funkcija teisingai suskaičiuoja skaičių sumą, panaudojant fixture duomenis su įvairiais skaičių sąrašais.

def skaiciu_suma(skaiciai): #gausim skaiciu sarasa lista
    return sum(skaiciai)

# 2 užduotis
# Parašykite funkciją vidurkis(skaiciai), kuri priima sąrašą skaičių ir grąžina jų vidurkį.
# Parašykite testą, kuris tikrina, ar funkcija teisingai skaičiuoja skaičių sąrašo vidurkį, naudojant fixture duomenis su skirtingais skaičių sąrašais.

def vidurkis(skaiciai):
    for sk in skaiciai:
        if not (isinstance(sk, int) or isinstance(sk, float)):  # jeigu ne int ir float, tada grazins 'klaida' 16 eilute net neprieisim jei ismes klaida
            return 'klaida'
    return sum(skaiciai)/len(skaiciai)

# Parašykite funkciją zodziu_skaicius(tekstas), kuri priima teksto eilutę ir grąžina jos žodžių skaičių.
# Parašykite testą, kuris patikrina, ar funkcija teisingai skaičiuoja žodžių skaičių teksto eilutėje, naudojant fixture duomenis su skirtingomis teksto eilutėmis.

def zodziu_skaicius(tekstas):
    return len(tekstas.split())

# 4 užduotis
# Parašykite funkciją unikalios_reiksmes(sarasas), kuri priima sąrašą ir grąžina jo unikalų elementų sąrašą.
# Parašykite testą, kuris patikrina, ar funkcija teisingai grąžina unikalų elementų sąrašą, naudojant fixture duomenis su įvairiais sąrašais.

def unikalios_reiksmes(sarasas):
    sarasas_unikaliu = []
    for elementas in sarasas:
            if not elementas in sarasas_unikaliu:
                sarasas_unikaliu.append(elementas)
    return sarasas_unikaliu
# analogas: return [set(sarasas)]

# 1 užduotis
# Parašykite funkciją patvirtinti_apmokejima(saskaitos_numeris, suma), kuri kreipiasi į kitą funkciją (patikrinti_likutį(sąskaitos_numeris, suma) šioje funkcijoje galite turėti dictionary, kurio viduje saugosite banko sąskaitų numerius ir jų likučius)
# funkcija patikrinti_likutį tiesiog grąžina True, jeigu sąskaitos likutis yra pakankamas, False jeigu lėšų yra per mažai.
# Funkcija patvirtinti_apmokejima grąžins suformuotą tekstą "Banko sąskaita xxxx-xxxx-xxxx gali/negali atlikti mokėjimą", šis pranešimas bus formuojamas priklausomai nuo patvirtinti_apmokėjimą atsakymo
# Parašykite testų, kurie testuoja tik patvirtinti_apmokejima funkcijos veikimą, todėl jums reikės mockinti patikrinti likutį funkcijos veikimą.
            
def patvirtinti_apmokejima(saskaitos_numeris, suma):
    saskaitos = {'LT5555': 300, 'LV5433': 250, 'EE4532': 200}
    if saskaitos[f'{saskaitos_numeris}'] >= suma:
        return True
    return False

def patvirtinti_apmokejima_ar_yra(saskaitos_numeris, suma):
    pakanka = patvirtinti_apmokejima(saskaitos_numeris, suma)   # atsakyks pakanka ar ne. Sita dalis per mokinima isjungiama
    return f'Banko sąskaita {saskaitos_numeris} {'gali' if pakanka else 'negali'} atlikti mokėjimą'

