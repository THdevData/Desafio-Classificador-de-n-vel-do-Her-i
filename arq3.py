class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "guerreiro":
            self.ataque = "espada"
        elif self.tipo == "mago":
            self.ataque = "magia"
        elif self.tipo == "monge":
            self.ataque = "artes marciais"
        elif self.tipo == "ninja":
            self.ataque = "shuriken"
        return f"o {self.tipo} atacou usando {self.ataque}"

heroi1 = Heroi("Destruidor de Mundos", 1000, "mago")

print(heroi1.atacar())