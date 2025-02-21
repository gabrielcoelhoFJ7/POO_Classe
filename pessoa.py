class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando, trabalhando, salario):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = salario

    def apresentar(self):

        if self.estudando:
            estudando_status = "Estudando"
        else:
            estudando_status = "Não Estudando"
        if self.trabalhando:
            trabalhando_status = "Trabalhando"
        else:
            trabalhando_status = "Não Trabalhando"

        print("." * 150)
        print(f'Olá sou {self.nome}'
              f' minha data de nascimento {self.data_nascimento}'
              f' meu codigo é {self.codigo}'
              f' atualmente {estudando_status} e {trabalhando_status}'
              f' meu salário é {self.salario}')
        print("." * 150)

    def estudar(self):
        self.estudando = True
        if self.estudando:
            self.salario += 1000
        elif self.estudando and self.trabalhando:
            self.salario = self.salario * 0.1
        elif not self.estudando and not self.trabalhando:
            self.salario = self.salario * 0

    def trabalhar(self):
        while not self.trabalhando:
            self.salario += 1200
            self.trabalhando = True


class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, codigo, estudando=False, trabalhando=False, salario=0):
        super().__init__(nome,data_nascimento, codigo , estudando , trabalhando, salario)
        self.fome = True
        self.chorando = True
        self.dormindo = False

    def apresentar(self):
        fome_status = "com fome" if self.fome == True else "satisfeito"
        chorando_status = "chorando" if self.chorando == True else "sem chorar"
        dormindo_status = "dormindo" if self.dormindo == True else "sem dormir"
        print(f"O {self.nome} está {fome_status}, {chorando_status} e {dormindo_status}")

    def trabalhar(self):
        print("Bebê não pode trabalhar.")

    def estudar(self):
        print("Bebê não pode estudar.")

    def mamar(self):
        if self.dormindo:
            print(f"O {self.nome} está dormindo e não pode mamar")
        elif self.chorando:
            self.fome = False
            self.chorando = False
            print(f"{self.nome} mamou e agora está satisfeito!")
        else:
            print(f"O {self.nome} já mamou demais")

    def chorar(self):
        if self.dormindo:
            print(f"O {self.nome} está dormindo")
        elif self.fome:
            self.chorando = True
            print(f"O {self.nome} está chorando")
        else:
            print(f"O {self.nome} não está chorando")

    def dormir(self):
        if self.dormindo:
            print(f"O {self.nome} já está dormindo")
        elif not self.fome:
            self.dormindo = True
            print(f"O {self.nome} está dormindo")
        else:
            print(f"O {self.nome} não pode dormir")
    def acordar(self):
        if self.dormindo:
            print(f"O {self.nome} acordou")
            self.fome = True
            self.dormindo = False
        else:
            print(f"O {self.nome} já está acordado")


print("\n\n\n\n\n\n\n\n\n")
p1 = Pessoa("Lucas", "23/09/1990", "Home_Office", estudando=False, trabalhando=False, salario=1200)

bb1 = Bebe("guilherme", "11/09/01", "asd123", estudando=False, trabalhando=False, salario=0)

