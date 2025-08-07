import pytest
from sistema_voos import Pessoa, Voo, CompanhiaAerea, MiniAeronave

def test_pessoa_str_nome_cpf():
    p1 = Pessoa('Alice', '123.456.789-10')
    assert p1.nome == 'Alice'
    assert p1.cpf == '123.456.789-10'
    assert str(p1) == 'Alice (123.456.789-10)'

def test_voo_adicionar_passageiro_e_tripulante():
    aeronave = MiniAeronave('Boeing', 2)
    voo = Voo('001', 'São Paulo', 'RIO', aeronave)
    p1 = Pessoa('Alice', '123.456.789-10')
    p2 = Pessoa('Grazy', '109.876.543-21')

    voo.adicionar_passageiro(p1)
    assert p1 in voo.passageiros

    voo.adicionar_tripulante(p2)
    assert p2 in voo.tripulacao

def test_voo_limite_passageiros():
    aeronave = MiniAeronave('Airbus', 1)
    voo = Voo('002', 'Natal', 'Fortaleza', aeronave)
    p1 = Pessoa('Yonara', '233.123.426-12')
    p2 = Pessoa('Simon', '123.397.328-82')

    voo.adicionar_passageiro(p1)
    assert p1 in voo.passageiros

    # Tentativa de adicionaer além da capacidade
    voo.adicionar_passageiro(p2)
    assert p2 not in voo.passageiros # Não deve entrar

def test_companhia_aerea():
    comp = CompanhiaAerea('AZUL')
    assert comp.nome == 'AZUL'

    comp.nome = 'LATAM'
    assert comp.nome == 'LATAM'

    with pytest.raises(ValueError):
        comp.nome = 'abc'

def test_companhia_aerea_adicionar_buscar_voo():
    comp = CompanhiaAerea('AZUL')
    aeronave = MiniAeronave('AK47', 3)
    voo = Voo('003', 'Brasília', 'Recife', aeronave)

    comp.adicionar_voo(voo)
    buscado = comp.buscar_voo('003')
    assert buscado == voo

    assert comp.buscar_voo('999') is None


def test_companhia_aerea_voos_adicionados():
    comp = CompanhiaAerea('GRAYO')
    aeronave1 = MiniAeronave('Yolly', 2)
    aeronave2 = MiniAeronave('Llyon', 2)
    voo1 = Voo('004', 'Riacho de Santana', 'Martins', aeronave1)
    voo2 = Voo('005', 'Martins', 'Riacho de Santana', aeronave2)

    comp.adicionar_voo(voo1)
    comp.adicionar_voo(voo2)

    assert voo1 in comp.voos
    assert voo2 in comp.voos
    assert len(comp.voos) == 2