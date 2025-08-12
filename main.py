
class Carros:
    def __init__(self,nome, marca, ano, valor):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.valor = valor

    def calcular_valor(self):
        valor_cliente = 50000
        self.valor = float(self.valor - valor_cliente)
        return self.valor


#criando os objetos

carro1 = Carros('Civic','Honda', '2018', 100000)
carro2 = Carros('Corolla','Toyota', '2010', 90000)

print(f'Nome {carro1.nome} / Marca {carro1.marca} / Valor: {carro1.valor} / Valor com desconto {Carros.calcular_valor(carro1)} \n')

print(f'Nome {carro2.nome} / Marca {carro2.marca} / Valor: {carro2.valor} / Valor com desconto {Carros.calcular_valor(carro2)}')

        
