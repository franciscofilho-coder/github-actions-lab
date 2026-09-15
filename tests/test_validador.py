import pytest

from src.validador import limpar_cpf, validar_cpf


def test_limpar_cpf_remove_formatacao():
    assert limpar_cpf("529.982.247-25") == "52998224725"

def test_cpf_valido():
    assert validar_cpf('529.982.247-25') is True

def test_cpf_invalido():
    assert validar_cpf('333.111.222-12') is False

def test_validar_cpf_tamanho_invalido():
    assert validar_cpf('123') is False

@pytest.mark.parametrize('cpf', ['000.000.000-00', 'abc', ''])
def test_cpfs_mal_formatados(cpf):
    assert validar_cpf(cpf) is False
