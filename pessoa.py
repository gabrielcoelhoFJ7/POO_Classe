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
        super().__init__(nome, data_nascimento, codigo, estudando, trabalhando, salario)
        self.__fome = True
        self.__chorando = True
        self.__dormindo = False

    def is_faminto(self):
        return self.__fome

    def is_chorando(self):
        return self.__chorando

    def is_dormindo(self):
        return self.__dormindo

    def apresentar(self):
        print(f"O {self.get_nome()} {'está com fome' if self.is_chorando() else 'Não está com fome'},"
              f" {'está chorando' if self.is_chorando() else 'Não está chorando'}"
              f" e {'está dormindo' if self.is_dormindo() else 'Não está dormindo'}")

    def set_trabalhar(self, **kwargs):
        print("Bebê não pode trabalhar.")

    def set_estudar(self, **kwargs):
        print("Bebê não pode estudar.")

    def set_fome(self):
        if self.__dormindo:
            print(f"O {self.get_nome()} está dormindo e não pode mamar")
        elif self.is_chorando():
            self.__fome = True
        else:
            print(f"O {self.get_nome()} está satisfeito")

    def set_chorar(self):
        if self.is_dormindo():
            print(f"O {self.get_nome()} está dormindo")
        elif self.is_faminto():
            self.__chorando = True
            print(f"O {self.get_nome()} está chorando")
        else:
            print(f"O {self.get_nome()} não está com fome")

    def set_dormir(self):
        if self.is_dormindo():
            print(f"O {self.get_nome()} já está dormindo")
        elif not self.is_faminto():
            self.__dormindo = True
            print(f"O {self.get_nome()} está dormindo")
        else:
            print(f"O {self.get_nome()} não pode dormir")

    def set_acordar(self):
        if self.is_dormindo():
            print(f"O {self.get_nome()} acordou")
            self.__fome = True
            self.__dormindo = False
        else:
            print(f"O {self.get_nome()} já está acordado")


p1 = Pessoa("Lucas", "23/09/1990", "Home_Office", estudando=False, trabalhando=False, salario=1200)
bb1 = Bebe("guilherme", "11/09/01", "asd123", estudando=False, trabalhando=False, salario=0)

bb1.apresentar()
bb1.set_trabalhar()
bb1.set_estudar()
