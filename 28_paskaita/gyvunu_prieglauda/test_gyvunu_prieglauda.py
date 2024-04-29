import pytest
from gyvunu_prieglauda import Gyvunas, GyvunuPrieglauda


@pytest.fixture
def prieglaudu_kurimas():
    gyvunas1 = Gyvunas(2015, 'suo', 'Reksas', 20)
    prieglauda1 = GyvunuPrieglauda('Lese')        
    prieglauda1.prideti_gyvuna(gyvunas1)
    prieglauda1.prideti_gyvuna(Gyvunas(2020, 'kate', 'Mice', None))
    return prieglauda1

def test_gauti_pagal_rusi(prieglaudu_kurimas):
    sunys = prieglaudu_kurimas.gauti_pagal_rusis('suo')
    kates = prieglaudu_kurimas.gauti_pagal_rusis('kate')
    assert sunys == [prieglaudu_kurimas.gyvunai[0]]
    assert len(sunys) == 1    #patikrinam, kad yra tik vienas suo
    assert len(prieglaudu_kurimas.gyvunai) == 2
    assert kates == [prieglaudu_kurimas.gyvunai[1]]