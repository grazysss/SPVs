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
        # TODO: gerar e armazenar um ID (use uuid.uuid4())
        pass
    def get_id(self):
        # TODO: retornar o ID
        pass


class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        # TODO: imprimir no formato  [LOG] <mensagem>
        pass


# -------------------------------------------------
# 3) Classe base Pessoa                          🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf
        
    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f'{self._nome} ({self._cpf})'

# -------------------------------------------------
# 4) Bagagem — classe simples                    🡇
# -------------------------------------------------
class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg
    def __str__(self):
        return f"{self.descricao} – {self.peso} kg"

# -------------------------------------------------
# 5) Passageiro                                  🡇
# -------------------------------------------------
class Passageiro(Pessoa):
    """Herda de Pessoa e possui bagagens."""
    def __init__(self, nome: str, cpf: str):
        def __init__(nome, cpf, bagagem):
            super().__init__(nome, cpf)
            self.bagagem = []
        
    def adicionar_bagagem(self, bagagem: Bagagem):
        self.bagagem.appen
        
    def listar_bagagens(self):
        # TODO: imprimir as bagagens
        pass


# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)     🡇
# -------------------------------------------------

class Funcionario(Pessoa, IdentificavelMixin, Logavel):
    def __init__(self, nome, cpf, cargo, matricula):
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.matricula = matricula

# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, matricula
# - Métodos:
#   • exibir_dados() → imprime nome, cargo, matrícula e ID
#   • logar_entrada() → registra no log


# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo
        self.capacidade = capacidade

    def resumo_voo(self):
        # TODO: retornar string com modelo e capacidade
        pass


# -------------------------------------------------
# 8) Voo (composição com MiniAeronave)           🡇
# -------------------------------------------------

class Voo:
    def __init__(self, numero_voo, origem, destino, aeronave):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.passageiros = []
        self.tripulacao = []
        aeronave = MiniAeronave

# TODO: Implementar a classe Voo
# - Atributos: numero_voo, origem, destino, aeronave
# - Listas: passageiros, tripulacao

    def adicionar_passageiros(self):
        pass

    def adicionar_tripulante(self):
        pass

    def listar_passageiros(self):
        pass

    def listar_tripulacao(self):
        pass

# - Métodos:
#   • adicionar_passageiro()  (verificar duplicidade e capacidade)
#   • adicionar_tripulante()
#   • listar_passageiros()
#   • listar_tripulacao()


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        if self.valida_nome(nome):
            self._nome = nome
        else: 
            print('Nome inválido')
        self.voos = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if self.valida_nome(novo_nome):
            self._nome = novo_nome

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def buscar_voo(self, numero: str):
        # TODO: retornar voo ou None
        pass

    def listar_voos(self):
       for voo in self.voos:
           print(voo)

    def valida_nome(self, nome):
        if len(nome) >= 3:
            return True

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

