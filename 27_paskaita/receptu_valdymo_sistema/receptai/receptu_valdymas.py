class Receptas:
    def __init__(self, pavadinimas, ruosimo_laikas, ingridientu_sarasas):
        self.pavadinimas = pavadinimas
        self.ruosimo_laikas = ruosimo_laikas
        self.ingridientu_sarasas = ingridientu_sarasas

class ReceptuValdymas:
    def __init__(self):
        self.receptai = []

    def gauti_pavadinimus(self):
        return [receptas.pavadinimas for receptas in self.receptai]

    def prideti_recepta(self, receptas):
        self.receptai.append(receptas)

    def gauti_receptus_pagal_laika(self, maksimalus_laikas):
        return [receptas for receptas in self.receptai if receptas.ruosimo_laikas <= maksimalus_laikas] 

    def atrinkti_pagal_ingridientus(self, ingridientas):
        atrinkti = []
        for receptas in self.receptai:
            for produktas in receptas.ingridientu_sarasas:
                if produktas == ingridientas:
                    atrinkti.append(receptas)
                    break
        return atrinkti


            
    # def pasalinti_recepta(self, pavadinimas):
    #     if pavadinimas in self.receptai:
    #         del self.receptai[pavadinimas]

# 1 užduotis
# papildykite klasę ReceptųValdymas pridedant metodą pasalinti_recepta, šis metodas turi panaikinti receptą iš receptų sąrašo,
# pagal pateiktą pavadinimą
# parašykite testą, kad įsitikintumėte ar jūsų metodas veikia tinkamai

    # def pasalinti_recepta(self, pavadinimas):
    #     for receptas in self.receptai:
    #         if receptas.pavadinimas == pavadinimas:
    #             self.receptai.remove(receptas)
    #             break

    def pasalinti_recepta(self, pavadinimas):
        self.receptai = [receptas for receptas in self.receptai if receptas.pavadinimas != pavadinimas]
        rezultatai = []
        for receptas in self.receptai:
            if receptas.pavadinimas != pavadinimas:
                rezultatai.append(receptas)
        self.receptai = rezultatai


# 2 užduotis
# Sukurkite metodą gauti_receptus_pagal_zodi(), kuris grąžina sąrašą receptų, kurių pavadinimuose yra nurodytas žodis.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą
    def gauti_receptus_pagal_zodi(self, zodis):
        return [receptas.pavadinimas for receptas in self.receptai if zodis in receptas.pavadinimas]

# 3 užduotis
# Sukurkite metodą gauti_bendra_ruosimo_laika(), kuris grąžina visų receptų bendrą ruošimo laiką.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą
    def gauti_bendra_ruosimo_laika(self):
        laiku_sarasas = [receptas.ruosimo_laikas for receptas in self.receptai]
        return sum(laiku_sarasas)

# 4 užduotis
# Pridėkite metodą isvalyti_receptus(), kuris išvalytų visus receptus iš sąrašo.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą
    def isvalyti_receptus(self):
        self.receptai = []



