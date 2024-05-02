import unittest
import pytest
from parduotuve import Preke, Parduotuve

@pytest.fixture
def sukurti_parduotuve():
    parduotuve = Parduotuve()
    parduotuve.prideti_preke(Preke('Spinta', 600, 15))
    parduotuve.prideti_preke(Preke('Sofa', 450, 35))
    return parduotuve


def test_gauti_preke(sukurti_parduotuve):
    prekei = sukurti_parduotuve.gauti_preke_pagal_index(0)
    assert 'Spinta' == prekei.pavadinimas
    assert 600 == prekei.kaina
    assert 15 == prekei.kiekis

def test_gauti_antra_preke(sukurti_parduotuve):
    prekei = sukurti_parduotuve.gauti_preke_pagal_index(1)
    assert 'Sofa' == prekei.pavadinimas
    assert 450 == prekei.kaina
    assert 35 == prekei.kiekis

def test_istrinti_preke(sukurti_parduotuve):
    pavadinimai = [preke.pavadinimas for preke in sukurti_parduotuve.prekes]
    assert 'Spinta' in pavadinimai
    sukurti_parduotuve.istrinti_preke(0)
    pavadinimai = [preke.pavadinimas for preke in sukurti_parduotuve.prekes]
    assert 'Spinta' not in pavadinimai


# valdymas.prideti_recepta(Receptas('Cepelinai', 180, ['bulves', 'mesa']))
#     valdymas.prideti_recepta(Receptas('Cezario salotos', 30, []))
#     valdymas.prideti_recepta(Receptas('Karbonadas', 45, []))
#     return valdymas