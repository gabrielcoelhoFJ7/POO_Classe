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
            self.estudando = "Estudando"
        else:
            self.estudando = "Not Estudando"
        if self.trabalhando:
            self.trabalhando = "Trabalhando"
        else:
            self.trabalhando = "Not Trabalhando"

        print("." * 150)
        print(f'Olá sou {self.nome}'
              f' minha data de nascimento {self.data_nascimento}'
              f' meu codigo é {self.codigo}'
              f' atualmente {self.estudando} e {self.trabalhando}'
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
            self.trabalhando = True
            if self.trabalhando:
                self.salario += 1200
            if not self.estudando and not self.trabalhando:
                self.salario = self.salario * 0






print("\n\n\n\n")
p1 = Pessoa("Lucas", "23/09/1990", "Home_Office", estudando=False, trabalhando=False, salario=1200)
p2 = Pessoa("Luciano", "12/04/1980", "Pai_Familia", estudando=True, trabalhando=False, salario=1200)
p3 = Pessoa("Alvaro", "15/02/1950", "Mestre_TI", estudando=False, trabalhando=True, salario=1200)
p4 = Pessoa("Gustavo", "15/10/2007", "Cartonizando", estudando=True, trabalhando=False, salario=1200)
p1.apresentar()
p2.apresentar()
p3.apresentar()


p1.estudar()
p1.apresentar()
p1.estudar()
p1.apresentar()
p1.apresentar()



# Trabalhador
p4.trabalhar()
p4.trabalhar()
p4.trabalhar()
p4.apresentar()



