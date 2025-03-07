class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando, trabalhando, salario):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def apresentar(self):

        print("." * 150)
        print(f'Olá sou {self.get_nome()}'
              f' minha data de nascimento {self.get_data_nascimento()}'
              f' meu codigo é {self.get_codigo()}'
              f' trabalhando: {'Sim' if self.is_trabalhando() else 'Não'}'
              f' estudando: {'Sim' if self.is_estudando() else 'Não'}'
              f' meu salário é {self.get_salario()}')
        print("." * 150)

    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_codigo(self):
        return self.__codigo
    def is_estudando(self):
        return self._estudando
    def is_trabalhando(self):
        return self._trabalhando
    def get_salario(self):
        return self._salario


    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print("Salario inválido")


    def set_trabalhar(self, status):
        if self._trabalhando and status:
            print("Já está trabalhando")
        elif not self._trabalhando and not status:
            print("Que vida boa")
        elif not self._trabalhando and status:
            self._trabalhando = status
            self.set_salario(1200)
        else:
            self._trabalhando = status


    def set_estudar(self, status):
        self._estudando = status
        if status:
            self.set_salario(self.get_salario() + 400)


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

