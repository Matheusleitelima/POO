
# 👩‍💻 Programação Orientada a Objetos (POO) em Python

A **Programação Orientada a Objetos (POO)** é um modelo de programação que organiza o código com base em **classes** e **objetos**. Ela permite escrever códigos mais organizados, reutilizáveis e que representam elementos do mundo real.

---

## 📦 Conceitos Básicos

### ✅ Classe

Uma **classe** é como um **molde** para criar objetos. Dentro da classe, podemos definir:
- **Atributos**: características da classe (ex: nome, cor, idade)
- **Métodos**: funções dentro da classe (ex: falar(), comer())

```python
class Funcionarios:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# Criando objetos a partir da classe
usuario1 = Funcionarios('Elena', 'Lima')
usuario2 = Funcionarios('Berg', 'Moura')

# Acessando atributos
print(usuario1.nome)  # Elena
print(usuario2.nome)  # Berg
```

---

## 🧱 O que a Classe Possui?

| Termo        | Explicação                                | Exemplo                     |
|--------------|--------------------------------------------|-----------------------------|
| Classe       | O molde para criar algo                    | `Ursinho`, `Biscoito`       |
| Objeto       | A coisa criada com base no molde           | `um ursinho chamado Ted`    |
| Atributo     | As características da coisa                | `cor`, `nome`, `sabor`      |
| Método       | As ações que o objeto pode realizar        | `falar()`, `comer()`        |

---

## 🔧 Construtor (`__init__`)

O **construtor** é um método especial que roda automaticamente quando um objeto é criado. Ele é responsável por **inicializar os atributos** da classe.

### 🧸 Analogia:
> Imagine que você está montando um boneco de LEGO. O construtor é quem define o nome, a cor e a roupa do boneco na hora que ele nasce.

---

## ➕ Adicionando Funções (Métodos) à Classe

```python
class Funcionarios:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

# Objetos
usuario1 = Funcionarios('Elena', 'Lima')
usuario2 = Funcionarios('Berg', 'Moura')

# Acessando dados e métodos
print(usuario1.nome)  # Elena
print(usuario2.nome)  # Berg

print(Funcionarios.nome_completo(usuario1))  # Elena Lima
```

---

## 🎂 Calculando a Idade do Funcionário

```python
from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = int(ano_nascimento)

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

# Objetos
usuario1 = Funcionarios('Elena', 'Lima', 2009)
usuario2 = Funcionarios('Berg', 'Moura', 2005)

# Acessando informações
print(usuario1.nome)  # Elena
print(usuario2.nome)  # Berg

print(usuario1.nome_completo())           # Elena Lima
print(usuario1.idade_funcionario())       # idade baseada no ano atual
```

---

## ✅ Conclusão

A Programação Orientada a Objetos ajuda você a escrever códigos mais organizados, reaproveitáveis e que refletem elementos do mundo real. Com classes, objetos, atributos, métodos e construtores, você tem uma estrutura poderosa para criar programas mais robustos.

---
