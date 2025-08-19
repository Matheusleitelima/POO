# 👩‍💻 Programação Orientada a Objetos (POO) em Python

A **Programação Orientada a Objetos (POO)** organiza o código com base em **classes** e **objetos**, tornando os programas mais claros, reutilizáveis e próximos do mundo real.

---

## 📦 Conceitos Básicos

### ✅ Classe

Uma **classe** é como um **molde** para criar objetos. Dentro da classe, podemos ter:

* **Atributos**: características do objeto (ex: nome, cor, idade)
* **Métodos**: ações que o objeto pode realizar (ex: falar(), comer())

```python
class Funcionarios:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# Criando objetos
usuario1 = Funcionarios('Elena', 'Lima')
usuario2 = Funcionarios('Berg', 'Moura')

print(usuario1.nome)  # Elena
print(usuario2.nome)  # Berg
```

---

## 🧱 O que a Classe Possui?

| Termo    | Explicação                       | Exemplo                     |
| -------- | -------------------------------- | --------------------------- |
| Classe   | Molde para criar algo            | `Ursinho`, `Carro`          |
| Objeto   | Coisa criada com base no molde   | `Ted`, `Fusca`              |
| Atributo | Características do objeto        | `cor`, `nome`, `velocidade` |
| Método   | Ações que o objeto pode realizar | `falar()`, `dirigir()`      |

---

## 🔧 Construtor (`__init__`)

O **construtor** cria e inicializa os objetos.

### 🧸 Analogia:

> É como montar um boneco de LEGO: o construtor define nome, cor e roupa do boneco quando ele nasce.

---

## ➕ Métodos da Classe

```python
class Funcionarios:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

usuario1 = Funcionarios('Elena', 'Lima')
print(usuario1.nome_completo())  # Elena Lima
```

---

## 🎂 Calculando Idade

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
        return datetime.now().year - self.ano_nascimento

usuario1 = Funcionarios('Elena', 'Lima', 2009)
print(usuario1.idade_funcionario())  # idade baseada no ano atual
```

---

## 🧐 Quando Usar POO

### Explicando de forma simples:

Imagine que você está criando **um jogo ou sistema de cadastro**:

* Você tem várias entidades (funcionários, carros, jogadores) que têm **atributos** (nome, idade, cor) e **ações** (falar, dirigir, jogar).
* Cada entidade pode ser representada por uma **classe**, e cada “coisa real” que você cria a partir dela é um **objeto**.

Você deve usar **POO** quando:

1. **Quer modelar algo do mundo real**

   * Pessoas, produtos, carros, cartas de jogo…
   * Ex: Um funcionário do sistema → classe `Funcionario`.

2. **Precisa reaproveitar código**

   * Um molde (classe) pode criar vários objetos sem repetir código.

3. **Quer organizar e manter o código fácil**

   * Cada objeto sabe suas próprias ações.

4. **Quer criar hierarquias e herança**

   * Subclasses herdam atributos e métodos da classe principal.
   * Ex: `Funcionario` → `Gerente` ou `Estagiario`.

5. **Precisa proteger os dados**

   * Você controla como os atributos são acessados ou modificados.

### 💡 Dica prática:

* **Muitos objetos e ações** → use POO.
* **Script simples, poucas funções** → POO pode ser demais.

---

## ✅ Conclusão

A POO ajuda a organizar o código, criar programas mais robustos e próximos do mundo real, com classes, objetos, atributos, métodos e construtores.
