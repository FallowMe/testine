import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_get_todo():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    assert response.status_code == 200
    data = response.json()
    print(response.json())
    print(type(response.json()))
    assert data['userId'] == 1
    assert 'title' in data
    assert 'delectus' in data['title']
    print('OK')

test_get_todo()

# def test_puslapis():
#     driver = webdriver.Chrome()
#     driver.get("https://delfi.lt")
#     elementas = driver.find_element(By.CLASS_NAME, 'C-button__content')
#     tekstas = elementas.text
#     assert "Prenumeruoti" in tekstas
#     assert "Delfi" in driver.title
#     print('Nuskaitymas baigtas')
#     driver.quit()

# test_puslapis()

def test_aruodas():
    driver = webdriver.Chrome()
    driver.get('https://www.aruodas.lt/butai/vilniuje/')
    kainos = driver.find_elements(By.CLASS_NAME, 'list-item-price-v2')
    kainos_reiksmes = []
    for kaina in kainos:
        kainos_reiksmes.append(kaina.text)
    print(kainos_reiksmes)
    print('================================')
    print(len(kainos_reiksmes))
    print('===============================')
    assert not kainos_reiksmes == []  # klausiu pythono ar kainos_reiksmes nera tuscias listas
    assert len(kainos_reiksmes) == 25   # patikrinom ar sarase yra 25 reiksmes
    for kaina in kainos_reiksmes:
        assert kaina[-1] == '€'
        #assert kaina.endswith('€')  # tas pats kas auksciau tik be slaisinimo

    plotai = driver.find_elements(By.CLASS_NAME, 'list-AreaOverall-v2')
    plotu_reiksmes = []
    for plotas in plotai:
        plotu_reiksmes.append(plotas.text)
        #print(plotas.text)
    plotelis = plotu_reiksmes[2:]
    print(plotelis)
    print('========================')
    assert not plotelis == []
    assert len(plotelis) == 25
    for plotas in plotelis:
        assert plotas.replace('.', '').isnumeric()
        #assert plotas.isnumeric(), f'{plotas}'  




    driver.quit()

test_aruodas()



# 1 užduotis
# naudojant selenium parašykite testą, kuris bandytų nuskaityti informaciją iš jūsų pasirinkto puslapio
# "ištraukite keletą elementų iš puslapio" ir testuokite ar juose  yra tekstas, kurio jūs tikitės