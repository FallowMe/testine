from send_email import pranesti_vartotojui, skaiciavimas, nuskaityti_faila, saraso_suma_2
from unittest.mock import patch, mock_open
import pytest

@pytest.fixture
def mock_send_email():
    with patch('send_email.send_email') as mocked_send_email:
        yield mocked_send_email   #yield grazina ivyki ,kas iskviete, kodel iskviete ir pan...

def test_pranesti_vartotojui(mock_send_email):
    email = 'siuntejas@gmail.com'
    ivykis = 'susitikimas'
    pranesti_vartotojui(email, ivykis)
    mock_send_email.assert_called_once() # testuoja ar mokinama funkcija buvo iskviesta tik viena karta
    args, kwargs = mock_send_email.call_args # [], <..>
    #assert kwargs == {}
    assert args[0] == 'antanas@gmail.com'   #args[0] yra siuntejes
    assert len(args) == 4
    assert ivykis in args[3]

#================================
@pytest.fixture
def mock_daugyba():
    with patch('send_email.daugyba') as mocked_daugyba:  #send_email yra tiesiog failo pavadinimas, taip sutapo... patch metodas uztikrins, kad bus sukurtas ivykio objektas(kas kviete, kiek kartu, kaip kviete...) is kurio galesime pasiimti veiksmus/uztikrins, kad nurodyta funkcija nebus iskvieciama.
        yield mocked_daugyba  # yield reiskia, kad galesime pasiimti visada kada mums tik reikes svieziausia rezultata

def test_skaiciavimas(mock_daugyba):
    skaiciavimas(1,1)
    mock_daugyba.assert_not_called() # tikrina ar nekvietem funkcijos esancios viduje (daugyba)
    skaiciavimas(2,5)
    mock_daugyba.assert_called_once()

#================================
from pytest_mock import mocker

def test_nuskaityti_faila(mocker):
    mocker.patch('builtins.open', mock_open(read_data='Cia yra tekstas, kuri mes teigiam, kad nuskaite open'))
    rezultatas_kurio_tikimes = 'Cia yra tekstas, kuri mes teigiam, kad nuskaite open'
    rezultatas = nuskaityti_faila('test.txt')
    assert rezultatas_kurio_tikimes == rezultatas

#========================================

def test_saraso_suma_2():
    duomenys = [1, 'a']
    with pytest.raises(Exception) as e:
        saraso_suma_2(duomenys)
    #assert e == 'Saraso nariai privalo buti skaiciai'
    assert str(e.value) == 'Saraso nariai privalo buti skaiciai'

