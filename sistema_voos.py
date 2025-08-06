from abc import ABC, abstractmethod
import uuid

# -------------------------------------------------
# 1) Interface                                   🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass

# -------------------------------------------------
# 2) Mixins                                      🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self):
        self.id = self.gerar_id()

    def gerar_id(self):
        return uuid.uuid4()

    def get_id(self):
        return self.id
class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento):
        print(f'[LOG] {evento}')

# -------------------------------------------------
# 3) Classe base Pessoa                          🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    def __str__(self):
        return (f'{self.nome} ({self.cpf})')

# -------------------------------------------------
# 4) Bagagem — classe simples                    🡇
# -------------------------------------------------
class Bagagem:
    def __init__(self, descricao, peso):
        self.descricao = descricao
        self.peso = peso  # kg

    def __str__(self):
        return (f'{self.descricao} - {self.peso} kg')

# -------------------------------------------------
# 5) Passageiro                                  🡇
# -------------------------------------------------
class Passageiro(Pessoa):
    """Herda de Pessoa e possui bagagens."""
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.bagagens = []

    def adicionar_bagagem(self, bagagem):
        self.bagagens.append(bagagem)

    def listar_bagagens(self):
        if len(self.bagagens) > 0:
            for bagagem in self.bagagens:
                print(bagagem)

# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)     🡇
# -------------------------------------------------
class Funcionario(Pessoa, IdentificavelMixin, Logavel):
    def __init__(self, nome, cpf, cargo, matricula):
        Pessoa.__init__(self, nome, cpf)
        IdentificavelMixin.__init__(self)
        self.cargo = cargo
        self.matricula = matricula     

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}')
        print(f'Matrícula: {self.matricula}')
        print(f'ID: {self.get_id}')

    def logar_entrada(self):
        print(f'[LOG] Entrada de {self.nome} registrada no LOG.')

# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo, capacidade):
        self.modelo = modelo
        self.capacidade = capacidade
        
    def resumo_voo(self):
        return (f'{self.modelo} - {self.capacidade}')


# -------------------------------------------------
# 8) Voo (composição com MiniAeronave)           🡇
# -------------------------------------------------

class Voo:
    def __init__(self, numero_voo, origem, destino, MiniAeronave):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.aeronave =  MiniAeronave
        self.passageiros = []
        self.tripulacao = []

    def adicionar_passageiro(self, passageiro):
        embarca = True
        if len(self.passageiros) >= self.aeronave.capacidade:
            print('A capacidade da aeronave esgotou.')
            embarca = False
        elif passageiro in self.passageiros:
            print('Passageiro já está no voo.')
            embarca = False

        if embarca:
            self.passageiros.append(passageiro)
            print(f'Passageiro {passageiro.nome} adicionado ao voo!')

    def adicionar_tripulante(self, funcionario):
        self.tripulacao.append(funcionario)
        print(f'Funcionário {funcionario.nome} adicionado na tripulação!')

    def listar_passageiros(self):
        for passageiro in self.passageiros:
            print(passageiro)

    def listar_tripulacao(self):
        for tripulante in self.tripulacao:
            print(tripulante)


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome):
        if len(nome) <= 3:
            raise ValueError ("O nome tem que ter mais de 3 caracteres")
        else:
            self._nome = nome
            self.voos = []
    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) <= 3:
            raise ValueError ("Nome tem que ter mais de 3 caracteres.")
        else:
            self._nome = novo_nome

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def buscar_voo(self, numero: str):
        for voo in self.voos:
            if numero == voo.numero_voo:
                return voo
        return None
    
    def listar_voos(self):
        for voo in self.voos:
            print(F"Voo de numero: {voo.numero_voo} que sai do {voo.origem}")


# -------------------------------------------------
# 10) Auditor (Identificável + Logável)          🡇
# -------------------------------------------------
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_voo(voo) → verifica:
#       ▸ passageiros ≤ capacidade
#       ▸ existe ao menos 1 tripulante
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"

class Auditor(IdentificavelMixin, Logavel):
    def __init__(self, nome):
        IdentificavelMixin.__init__(self)
        self.nome = nome

    def logar_entrada(self):
        print("Auditor logou no sistema")

    def auditar_voo(self, voo):
        if len(voo.passageiros) <= voo.aeronave.capacidade and len(voo.tripulacao) >= 1:
            print("Voo está apto a ser feito")

    def __str__(self):
        return f"Auditor de nome: {self.nome} com ID: {self.get_id()}"