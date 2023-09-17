from caesar.caesar import encripta


def test_encripta_mateus_retorna_zngrhf():
    assert encripta("Mateus") == "zngrhf"


def test_encripta_zngrhf_retorna_mateus():
    assert encripta("zngrhf") == "mateus"


def test_encripta_deve_retornar_minusculas():
    assert encripta("A").islower()


def test_encripta_deve_preservar_os_espacos():
    resultado = encripta("e a")
    assert resultado[1] == " "
