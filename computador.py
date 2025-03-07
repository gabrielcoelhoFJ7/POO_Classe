from datetime import date

class Eletronico:
    def __init__(self, tipo, marca, data_fabricacao, situacao, voltagem, custo, status):
        self.__tipo = tipo
        self.__marca = marca
        self.__data_fabricacao = data_fabricacao
        self._situacao = situacao
        self.__voltagem = voltagem
        self._custo = custo
        self._status = status

    def ligar(self, tomada):
        if self.voltagem == "bivolt" or self.voltagem == tomada:
            print(f"{self.tipo} foi ligado com sucesso!")
        elif self.voltagem == "220V" and tomada == "110V":
            print(f"{self.tipo} foi ligado porém não seria a escolha ideal de tomada.")
        elif self.voltagem == "110V" and tomada == "220V":
            print(f"{self.tipo} foi sobrecarregado e queimou")
            self.status = False
        elif self.situacao != "ligado":
            self.situacao = "ligado"
            print(f"{self.tipo} foi ligado!")
        else:
            print(f"{self.tipo} já está ligado!")

    def desligar(self):
        if self.situacao != "desligado":
            self.situacao = "desligado"
            print(f"{self.tipo} foi desligado!")
        else:
            print(f"{self.tipo} já está desligado!")

    def levar_manutencao(self):
        if not self.status:
            self.status = True
        else:
            print("Já está funcionando")

    def verificar_tempo_uso(self):
        ano_atual = date.today().year
        tempo_uso = ano_atual - self.data_fabricacao
        print(f"{self.tipo} foi fabricado há {tempo_uso} anos.")
        return tempo_uso

#     Getters and Setters





class Computador(Eletronico):
    def __init__(self, tipo, marca, data_fabricacao, situacao, voltagem, custo, status,
                 processador, memoria_ram, armazenamento, sistema_operacional):
        super().__init__(tipo, marca, data_fabricacao, situacao, voltagem, custo, status)
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.armazenamento = armazenamento
        self.sistema_operacional = sistema_operacional
        self.programa_instalado = []
        self.garantia = True
        self.status = True

    def instalar_programa(self, programa):
        if self.status == True:
            self.programa_instalado.append(programa)
            print(f"{programa} foi instalado com sucesso no {self.tipo}.")
        else:
            print(f"Não é possível instalar {programa}, o computador está em manutenção.")

    def formatar(self):
        if self.status == True:
            print(f"O {self.tipo} foi formatado, e o sistema {self.sistema_operacional} foi reinstalado.")
        else:
            print("O computador está em manutenção e não pode ser formatado.")

    def atualizar_sistema(self, nova_versao):
        if self.status == True:
            self.sistema_operacional = nova_versao
            print(f"O sistema operacional foi atualizado para {nova_versao}.")
        else:
            print("O computador está em manutenção e não pode ser atualizado.")

    def exibir_configuracoes(self):
        print("." * 80)
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Data de Fabricação: {self.data_fabricacao}")
        print(f"Situação: {self.situacao}")
        print(f"Voltagem: {self.voltagem}")
        print(f"Custo: R$ {self.custo}")
        print(f"Processador: {self.processador}")
        print(f"Memória RAM: {self.memoria_ram}GB")
        print(f"Armazenamento: {self.armazenamento}")
        print(f"Sistema Operacional: {self.sistema_operacional}")
        print(f"Programas instalados: {self.programa_instalado}")
        print(f"Status: {"Está funcionando" if self.status else "Não está funcionando"}")
        print(f"Está na Garantia: {'Sim' if self.garantia else 'Não'}")
        print("." * 80)



tv = Eletronico(
    tipo="TV",
    marca="Samsung",
    data_fabricacao=2020,
    situacao="desligado",
    voltagem="110V",
    custo=1500,
    status=True
)


pc = Computador(
    tipo="Computador",
    marca="Dell",
    data_fabricacao=2021,
    situacao="desligado",
    voltagem="110V",
    custo=4000,
    processador="Intel i7",
    memoria_ram=16,
    armazenamento="512GB SSD",
    sistema_operacional="Windows 10",
    status=True
)

print("=== Testando o Eletrônico ===")
tv.verificar_tempo_uso()
tv.ligar("110V")
tv.desligar()

print("\n")


print("=== Testando o Computador ===")
pc.ligar("220V")
pc.levar_manutencao()
pc.ligar("110V")
pc.exibir_configuracoes()
pc.instalar_programa("Photoshop")
pc.instalar_programa("Thonny")
pc.instalar_programa("Pycharm")
pc.atualizar_sistema("Windows 11")
pc.formatar()
pc.exibir_configuracoes()
pc.desligar()


