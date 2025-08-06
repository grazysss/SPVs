from sistema_voos import *

# OS ZEROTWO - Objetos da Classe Pessoa
p1 = Pessoa('Alice', '123.456.789-10')
p2 = Pessoa('Simon', '109.876.543-21')

p3 = Pessoa('Grazy', '121.212.343-32')
p4 = Pessoa('Yonara', '125.834.242-88')

# Testando os métodos da Classe Pessoa
print(p1.nome)
print(p2.nome)

print()

print(p1.__str__())
print(p2.__str__())


# Criando objetos para a Classe Bagagem
b1 = ('Brownie', '5kg')
b2 = ('Fone', '0.1kg')
b3 = ('Thor', '5kg')
b4 = ('Computador', '1kg')

print()

# Testando o método de conversão para String
print(b1.__str__())
print(b2.__str__())

print()


# Criando objetos da Classe Passageiro
pass1 = Passageiro(p1.nome, p1.cpf)
pass2 = Passageiro(p2.nome, p2.cpf)

# Testando os métodos da Classe Passageiro em relação a Class Bagagem
pass1.adicionar_bagagem(b1)
pass1.adicionar_bagagem(b3)
pass2.adicionar_bagagem(b2)
pass2.adicionar_bagagem(b4)

pass1.listar_bagagens()
pass2.listar_bagagens()


# Criando objetos para a Classe Funcionário
f1 = Funcionario(p3.nome, p3.cpf, 'Serva', '1234-5')
f2 = Funcionario(p4.nome, p4.cpf, 'Serva', '5432-1')

print()

# Testando os métodos da CLasse Funcionário
f1.exibir_dados()
f2.exibir_dados()

print()

f1.logar_entrada()
f2.logar_entrada()


# Criando objetos da Classe MiniAeronave
ma1 = MiniAeronave('boeing-777', 20)
ma2 = MiniAeronave('boeing-444', 30)

print()

# Criando objetos da Classe Voo
voo1 = Voo('1', 'Brasil', 'Itália', ma1)
voo2 = Voo('2', 'Brasil', 'Suiça', ma2)

voo1.adicionar_passageiro(pass1)
voo2.adicionar_passageiro(pass2)

print()

voo1.adicionar_tripulante(f1)
voo2.adicionar_tripulante(f2)

print()

voo1.listar_passageiros()
voo1.listar_tripulacao()
voo2.listar_tripulacao()
voo2.listar_passageiros()

print()

comp = CompanhiaAerea("PEDRO")
print(comp.nome)
comp.nome = "Yonara" 
print(comp.nome)

comp.adicionar_voo(voo1)
voo3 = comp.buscar_voo("1")
print(voo3.numero_voo)
comp.listar_voos()

print()

a1 = Auditor("Samuel")
a1.logar_entrada()
a1.auditar_voo(voo3)
print(a1)