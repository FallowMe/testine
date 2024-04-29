import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 užduotis
# naudojant selenium parašykite testą, kuris bandytų nuskaityti informaciją iš jūsų pasirinkto puslapio
# "ištraukite keletą elementų iš puslapio" ir testuokite ar juose  yra tekstas, kurio jūs tikitės

def test_autoplius():
    driver = webdriver.Chrome()
    driver.get('https://autoplius.lt/skelbimai/naudoti-automobiliai')
    automobiliai = driver.find_elements(By.CLASS_NAME, 'announcement-title')
    automobiliiu_reiksmes = []
    for automobilis in automobiliai:
        automobiliiu_reiksmes.append(automobilis.text)
    print(automobiliai)
    print('================================')
    print(len(automobiliiu_reiksmes))
    print('===============================')
    assert not automobiliiu_reiksmes == []  # klausiu pythono ar kainos_reiksmes nera tuscias listas
    assert len(automobiliiu_reiksmes) == 20   # patikrinom ar sarase yra 25 reiksmes
    #for automobilis in automobiliiu_reiksmes:
        #assert kaina[-1] == '€'
        #assert kaina.endswith('€')  # tas pats kas auksciau tik be slaisinimo

    # plotai = driver.find_elements(By.CLASS_NAME, 'list-AreaOverall-v2')
    # plotu_reiksmes = []
    # for plotas in plotai:
    #     plotu_reiksmes.append(plotas.text)
    #     #print(plotas.text)
    # plotelis = plotu_reiksmes[2:]
    # print(plotelis)
    # print('========================')
    # assert not plotelis == []
    # assert len(plotelis) == 25
    # for plotas in plotelis:
    #     assert plotas.replace('.', '').isnumeric()
    #     #assert plotas.isnumeric(), f'{plotas}'  




    driver.quit()

test_autoplius()

