
class funcionario():
    aumento=1.04
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario

    def dados(self):
        return {'nome':self.nome,'salario':self.salario}

    def appaumento(self):
        self.salario =self.salario * self.aumento

    @classmethod
    def definir_aumento(cls,novo_aumento):
        cls.aumento=novo_aumento

    @staticmethod
    def dia_util(dia):
        if dia==5 or dia==6:
            return False
        return True


class adm(funcionario):
    def __init__(self,nome,salario):
        super(adm, self).__init__(nome,salario)

    def mudarsalario(self,valoramudar):
         self.salario=valoramudar
         return self.dados()

















