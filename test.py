from sistema_voos import *

# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":
    gol = CompanhiaAerea("GOL")
    latam = CompanhiaAerea("LATAM")
    
    # Create aircraft
    boeing737 = MiniAeronave("Boeing 737", 150)
    airbus320 = MiniAeronave("Airbus A320", 180)
    
    # Create flights
    voo_gol1 = Voo("GOL123", "São Paulo", "Rio de Janeiro", boeing737)
    voo_gol2 = Voo("GOL456", "Rio de Janeiro", "Brasília", boeing737)
    voo_latam1 = Voo("LAT789", "São Paulo", "New York", airbus320)
    voo_latam2 = Voo("LAT012", "New York", "Miami", airbus320)
    
    # Add flights to airlines
    gol.adicionar_voo(voo_gol1)
    gol.adicionar_voo(voo_gol2)
    latam.adicionar_voo(voo_latam1)
    latam.adicionar_voo(voo_latam2)
    
    # Create passengers
    passenger1 = Passageiro("João Silva", "111.222.333-44")
    passenger2 = Passageiro("Maria Santos", "222.333.444-55")
    passenger3 = Passageiro("Carlos Oliveira", "333.444.555-66")
    passenger4 = Passageiro("Ana Pereira", "444.555.666-77")
    
    # Add baggage to passengers
    passenger1.adicionar_bagagem(Bagagem("Mala grande", 23.5))
    passenger1.adicionar_bagagem(Bagagem("Mochila", 5.0))
    passenger2.adicionar_bagagem(Bagagem("Mala média", 15.0))
    passenger3.adicionar_bagagem(Bagagem("Mala pequena", 10.0))
    
    # Create employees
    employee1 = Funcionario("Pedro Alves", "555.666.777-88", "Piloto", "MAT001")
    employee2 = Funcionario("Luiza Costa", "666.777.888-99", "Comissária", "MAT002")
    employee3 = Funcionario("Marcos Rocha", "777.888.999-00", "Co-piloto", "MAT003")
    
    # Add passengers to flights
    voo_gol1.adicionar_passageiros(passenger1)
    voo_gol1.adicionar_passageiros(passenger2)
    voo_gol2.adicionar_passageiros(passenger3)
    voo_latam1.adicionar_passageiros(passenger4)
    
    # Try to add passenger beyond capacity
    for i in range(149):  # Already has 2 passengers, adding 149 more (total 151 > 150 capacity)
        temp_passenger = Passageiro(f"Passenger{i}", f"000.000.000-{i:02d}")
        voo_gol1.adicionar_passageiros(temp_passenger)
    
    # Add crew to flights
    voo_gol1.adicionar_tripulante(employee1)
    voo_gol1.adicionar_tripulante(employee2)
    voo_latam1.adicionar_tripulante(employee1)
    voo_latam1.adicionar_tripulante(employee3)
    
    # Create auditor
    auditor = Auditor("Roberto Auditório")
    
    # Log employee entries
    employee1.logar_entrada()
    employee2.logar_entrada()
    
    # Audit flights
    print("\nAuditing flights:")
    auditor.auditar_voo(voo_gol1)
    auditor.auditar_voo(voo_latam1)
    
    # List flights
    print("\nGOL flights:")
    gol.listar_voos()
    
    print("\nLATAM flights:")
    latam.listar_voos()
    
    # List passengers and their baggage
    print("\nPassengers on GOL123:")
    voo_gol1.listar_passageiros()
    
    print("\nPassenger1's baggage:")
    passenger1.listar_bagagens()
    
    # Show employee data
    print("\nEmployee data:")
    employee1.exibir_dados()
    employee2.exibir_dados()
    
    # Show auditor info
    print("\nAuditor info:")
    print(auditor)