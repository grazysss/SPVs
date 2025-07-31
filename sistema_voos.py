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
    def __init__(self, id):
        self.id = self.gerar_id()

    def gerar_id(self):
        return uuid.uuid4()

    def get_id(self):
        return self.id

class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        print(f'[LOG] {evento}')

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
        super().__init__(nome, cpf)
        self.bagagens = []
        
    def adicionar_bagagem(self, bagagem: Bagagem):
        self.bagagens.append(bagagem)
        
    def listar_bagagens(self):
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
        print(f'{self._nome}, {self.cargo}, {self.matricula}, {self.get_id}')

    def logar_entrada(self):
        print(f'Entrada de {self._nome} registrada no LOG')

# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo
        self.capacidade = capacidade

    def resumo_voo(self):
        return f'{self.modelo}: {self.capacidade} passageiros'

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

    def adicionar_passageiros(self, passageiro):
        if passageiro in self.passageiros:
            print('Passageiro já está no voo')
        elif len(self.passageiros) >= self.aeronave.capacidade:
            print('Capacidade máxima atingida')
        else:
            self.passageiros.append(passageiro)

    def adicionar_tripulante(self, funcionario):
        if funcionario not in self.tripulacao:
            self.tripulacao.append(funcionario)

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
        for voo in self.voos:
            if numero == voo.numero_voo:
                return voo
            else:
                None
        
    def listar_voos(self):
       for voo in self.voos:
           print(f'Voo {voo.numero_voo}: {voo.origem} -> {voo.destino}')

    def valida_nome(self, nome):
        if len(nome) >= 3:
            return True

# -------------------------------------------------
# 10) Auditor (Identificável + Logável)          🡇
# -------------------------------------------------

class Auditor(IdentificavelMixin, Logavel):
    def __init__(self, nome):
        self.nome = nome

    def logar_entrada(self):
        print(f'Entrada de {self._nome} registrada no LOG')
    
    def auditar_voo(self, voo):
        print(f'Auditoria do Voo {voo.numero_voo}:')
        print(f'Passageiros: {len(voo.passageiros)}/{voo.aeronave.capacidade}')
        print(f'Tripulantes: {len(voo.tripulacao)}')

        conformidade = True
        if len(voo.passageiros) > voo.aeronave.capacidade:
            print('Excesso de passageiros!')
            conformidade = False
            if len(voo.tripulacao) < 1:
                print('Sem tripulação mínima!')
                conformidade = False

        if conformidade:
            print('✅ Voo conforme')

    def __str__(self):
        return f'Auditor {self.nome} (ID: {self.get_id()})'
        


# 
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

