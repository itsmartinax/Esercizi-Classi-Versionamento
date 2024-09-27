# Classe Tavoletta (estende Cioccolato):

'''
1. Proprietà aggiuntive come peso e se contiene o meno aggiunte (nocciole, ecc.).
2. Override del metodo produce() per includere da quanti cioccalatini e composta.
'''

from BaseCioccolato import BaseCioccolato
    
class Tavoletta(BaseCioccolato):
    ntavolette=0
    def __init__(self, tipo, perc_cacao, peso, aggiunte):
        BaseCioccolato.__init__(self,tipo, perc_cacao)
        self.peso=peso
        self.aggiunte=aggiunte
        if BaseCioccolato.ncioccolato<=0:
            print("Chiuso day!")
            #print(f"Chiuso day!\nNumero Cioccolatini: {Cioccolatino.ncioccolatini} \nNumero Tavolette: {self.ntavolette} \nCioccolate Calde: {CioccolataCalda.ncioccolatecalde}")
        elif self.peso<=80:
            BaseCioccolato.ncioccolato-=4
            Tavoletta.ntavolette+=1
        elif 80<self.peso<=100:
            BaseCioccolato.ncioccolato-=10
            Tavoletta.ntavolette+=1
        elif 100<self.peso<=200:
            BaseCioccolato.ncioccolato-=16
            Tavoletta.ntavolette+=1
        else:
            BaseCioccolato.ncioccolato-=24
            Tavoletta.ntavolette+=1
        
    
    def produce(self):
        super().produce()
        print(f"Numero tavolette: {self.ntavolette}")