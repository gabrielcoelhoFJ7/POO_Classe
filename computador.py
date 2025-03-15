from datetime import date

class Eletronico:
    def __init__(self, tipo, marca, data_fabricacao, situacao, voltagem, custo, status):
        self.__tipo = tipo
        self.__marca = marca
        self.__data_fabricacao = data_fabricacao
        self.__situacao = situacao
        self.__voltagem = voltagem
        self.__custo = custo
        self.__status = status

    def ligar(self, tomada):
        if self.__voltagem == "bivolt" or self.__voltagem == tomada:
            print(f"{self.__tipo} foi ligado com sucesso!")
        elif self.__voltagem == "220V" and tomada == "110V":
            print(f"{self.__tipo} foi ligado porém não seria a escolha ideal de tomada.")
        elif self.__voltagem == "110V" and tomada == "220V":
            print(f"{self.__tipo} foi sobrecarregado e queimou")
            self.__status = False
        elif self.__situacao != "ligado":
            self.__situacao = "ligado"
            print(f"{self.__tipo} foi ligado!")
        else:
            print(f"{self.__tipo} já está ligado!")

    def desligar(self):
        if self.__situacao != "desligado":
            self.__situacao = "desligado"
            print(f"{self.__tipo} foi desligado!")
        else:
            print(f"{self.__tipo} já está desligado!")

    def levar_manutencao(self):
        if not self.__status:
            self.__status = True
        else:
            print("Já está funcionando")

    def verificar_tempo_uso(self):
        ano_atual = date.today().year
        tempo_uso = ano_atual - self.__data_fabricacao
        print(f"{self.__tipo} foi fabricado há {tempo_uso} anos.")
        return tempo_uso

    # Getters and Setters
    def get_tipo(self):
        return self.__tipo

    def get_marca(self):
        return self.__marca

    def get_data_fabricacao(self):
        return self.__data_fabricacao

    def get_situacao(self):
        return self.__situacao

    def get_voltagem(self):
        return self.__voltagem

    def get_custo(self):
        return self.__custo

    def get_status(self):
        return self.__status

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def set_status(self, status):
        self.__status = status


class Computador(Eletronico):
    def __init__(self, tipo, marca, data_fabricacao, situacao, voltagem, custo, status,
                 processador, memoria_ram, armazenamento, sistema_operacional):
        super().__init__(tipo, marca, data_fabricacao, situacao, voltagem, custo, status)
        self.__processador = processador
        self.__memoria_ram = memoria_ram
        self.__armazenamento = armazenamento
        self.__sistema_operacional = sistema_operacional
        self.__programa_instalado = []
        self.__garantia = True
        self.__status = True

    def instalar_programa(self, programa):
        if self.__status == True:
            self.__programa_instalado.append(programa)
            print(f"{programa} foi instalado com sucesso no {self.get_tipo()}.")
        else:
            print(f"Não é possível instalar {programa}, o computador está em manutenção.")

    def formatar(self):
        if self.__status == True:
            print(f"O {self.get_tipo()} foi formatado, e o sistema {self.__sistema_operacional} foi reinstalado.")
        else:
            print("O computador está em manutenção e não pode ser formatado.")

    def atualizar_sistema(self, nova_versao):
        if self.__status == True:
            self.__sistema_operacional = nova_versao
            print(f"O sistema operacional foi atualizado para {nova_versao}.")
        else:
            print("O computador está em manutenção e não pode ser atualizado.")

    def exibir_configuracoes(self):
        print("." * 80)
        print(f"Tipo: {self.get_tipo()}")
        print(f"Marca: {self.get_marca()}")
        print(f"Data de Fabricação: {self.get_data_fabricacao()}")
        print(f"Situação: {self.get_situacao()}")
        print(f"Voltagem: {self.get_voltagem()}")
        print(f"Custo: R$ {self.get_custo()}")
        print(f"Processador: {self.__processador}")
        print(f"Memória RAM: {self.__memoria_ram}GB")
        print(f"Armazenamento: {self.__armazenamento}")
        print(f"Sistema Operacional: {self.__sistema_operacional}")
        print(f"Programas instalados: {self.__programa_instalado}")
        print(f"Status: {'Está funcionando' if self.__status else 'Não está funcionando'}")
        print(f"Está na Garantia: {'Sim' if self.__garantia else 'Não'}")
        print("." * 80)

    # Getters and Setters
    def get_processador(self):
        return self.__processador

    def get_memoria_ram(self):
        return self.__memoria_ram

    def get_armazenamento(self):
        return self.__armazenamento

    def get_sistema_operacional(self):
        return self.__sistema_operacional

    def set_sistema_operacional(self, sistema_operacional):
        self.__sistema_operacional = sistema_operacional


# Teste
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
