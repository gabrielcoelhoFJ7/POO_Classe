class Computador:
    def __init__(self, marca, modelo, config, status, garantia, custo):
        self.marca = marca
        self.modelo = modelo
        self.config = config
        self.status = status
        self.garantia = garantia


    def apresentar(self):
        if self.status:
            self.status = 'Em Manutenção'
        else:
            self.status = 'Funcionando'
        if self.garantia:
            self.garantia = "Inclusa"
        else:
            self.garantia = "Não Inclusa"


        print("." * 101)
        print(f' Marca: {self.marca} |'
              f' Modelo: {self.modelo} |'
              f' Config: {self.config} |'
              f' Status: {self.status} |'
              f' Garantia: {self.garantia}')
        print("." * 101)


c1 = Computador("Acer", "Nitro V15", "Gamer", status=True, garantia=True)
c2 = Computador("Lenovo", "IdeaPad", "Home Office", status=False, garantia=False)
c1.apresentar()
c2.apresentar()
