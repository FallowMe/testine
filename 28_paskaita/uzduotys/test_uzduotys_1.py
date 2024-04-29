import pytest
from uzduotys_1 import skaiciu_suma, vidurkis, zodziu_skaicius, patvirtinti_apmokejima, patvirtinti_apmokejima_ar_yra
from unittest.mock import patch
# 1 UZDUOTIS

@pytest.fixture
def skaiciu_uzpildymas():
    sarasas = [1,2,3,4,5]
    return sarasas

def test_skaiciu_suma(skaiciu_uzpildymas):
    assert skaiciu_suma(skaiciu_uzpildymas) == 15

#=================================================
# 2 UZDUOTIS

@pytest.fixture
def skirtingi_sarasai1():
    sarasas = [1,2,3,4,5,6,7]
    return sarasas

@pytest.fixture
def skirtingi_sarasai2():
    sarasas = [10,20,30,40,50]
    return sarasas

@pytest.fixture
def skirtingi_sarasai3():
    sarasas = [0.1, 0.5, 0.8, 0.7]
    return sarasas


def test_vidurkis(skirtingi_sarasai1, skirtingi_sarasai2, skirtingi_sarasai3):
    assert vidurkis(skirtingi_sarasai1) == sum(skirtingi_sarasai1)/len(skirtingi_sarasai1)
    assert vidurkis(skirtingi_sarasai2) == sum(skirtingi_sarasai2)/len(skirtingi_sarasai2)
    assert vidurkis([1,2, 'p']) == 'klaida'
    assert vidurkis(skirtingi_sarasai3) == sum(skirtingi_sarasai3)/len(skirtingi_sarasai3)



#RASOS
@pytest.fixture
def skaiciu_sarasas():
    skaiciai = [1,5,3,2,4,7,9]
    return skaiciai
@pytest.fixture
def skaiciu_sarasas1():
    skaiciai1 = [1,5,-6,7,-36,5]
    return skaiciai1
@pytest.fixture
def skaiciu_sarasas2():
    skaiciai2 = [1,5,-6,7,'z',-36,5]
    return skaiciai2
@pytest.fixture
def tekstas():
    tekstas = ['Siandien', 'jau', 'penktadienis', 'beveik', 'savaitgalis']
    return tekstas
@pytest.fixture
def tekstas1():
    tekstas = ['Savaitgali', 'zadamas', 'pagaliau', 'siltesnis', 'oras', 'negu', 'siandien']

#=========================================
# 3 UZDUOTIS

@pytest.fixture
def test_zodziu_skaicius(tekstas):
    tiketinas_rezultatas = zodziu_skaicius(tekstas)
    assert tiketinas_rezultatas == 5


#================================================
# 4 UZDUOTIS

@pytest.fixture
def unikalios_reiksmes(skaiciu_sarasas1):
    tiketinas_rezultatas = unikalios_reiksmes(skaiciu_sarasas1)
    assert tiketinas_rezultatas == [1,5,-6,7,-36]

#===============================================

# 1 UZDUOTIS

def test_patvirtinti_apmokejima():
    assert patvirtinti_apmokejima('LT5555', 290) == True
    assert patvirtinti_apmokejima('LT5555', 400) == False


@pytest.fixture
def mock_patvirtinti_apmokejima_atsakymas():
    return True

@patch('uzduotys_1.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_yra(mock_patvirtinti_apmokejima, mock_patvirtinti_apmokejima_atsakymas):
    mock_patvirtinti_apmokejima.return_value = True # arba sita eilute
    mock_patvirtinti_apmokejima.return_value = mock_patvirtinti_apmokejima_atsakymas  # arba sita
    assert patvirtinti_apmokejima_ar_yra('LV5433', 250) == 'Banko sąskaita LV5433 gali atlikti mokėjimą'

#pakeisime duomenis, kad sask. neuztektu pinigu
@patch('uzduotys_1.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_nera(mock_patvirtinti_apmokejima):
    mock_patvirtinti_apmokejima.return_value = False # arba sita eilute
    assert patvirtinti_apmokejima_ar_yra('LV5433', 259) == 'Banko sąskaita LV5433 negali atlikti mokėjimą'

# patestuokim kita banko sask.
@patch('uzduotys_1.patvirtinti_apmokejima')
def test_patikrinam_saskaitos_nr(mock_patvirtinti_apmokejima):
    mock_patvirtinti_apmokejima.return_value = True
    assert patvirtinti_apmokejima_ar_yra('EE4532', 200) == 'Banko sąskaita EE4532 gali atlikti mokėjimą'



