#Classe CioccolatoCaldo (estende Cioccolato):

'''
1.Proprietà aggiuntive come temperatura e densità.
2.Override del metodo produce() per includere da quanto ciccolato e stato fatto
'''

from BaseCioccolato import BaseCioccolato


class CioccolataCalda(BaseCioccolato):
    
    ncioccolatecalde=0

    def __init__(self, tipo, perc_cacao, temperatura, densità):
        BaseCioccolato.__init__(self,tipo, perc_cacao)
        self.temperatura=temperatura
        self.densità=densità
        if BaseCioccolato.ncioccolato<=0:
            print("Chiuso day!")
            #print(f"Chiuso day!\nNumero Cioccolatini: {Cioccolatino.ncioccolatini} \nNumero Tavolette: {Tavoletta.ntavolette} \nCioccolate Calde: {self.ncioccolatecalde}")
        else:
            BaseCioccolato.ncioccolato-=20
            CioccolataCalda.ncioccolatecalde+=1

    def produce(self):
        super().produce()
        print(f"Numero tavolette: {self.ncioccolatecalde}")