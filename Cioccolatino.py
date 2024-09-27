# Classe Cioccolatino (estende Cioccolato):

'''
1. Proprietà aggiuntive come forma e ripieno.
2. Override del metodo produce() per includere un calcolo di quanti cioccolato.
'''

from BaseCioccolato import BaseCioccolato
    
class Cioccolatino(BaseCioccolato):

    ncioccolatini=0

    def __init__(self, tipo, perc_cacao, forma, ripieno):
        BaseCioccolato.__init__(self,tipo, perc_cacao)
        self.forma=forma
        self.ripieno=ripieno
        if BaseCioccolato.ncioccolato<=0:
            print("Chiuso day!")
            #print(f"Chiuso day!\nNumero Cioccolatini: {self.ncioccolatini} \nNumero Tavolette: {Tavoletta.ntavolette} \nCioccolate Calde: {CioccolataCalda.ncioccolatecalde}")
        else:
            BaseCioccolato.ncioccolato-=2
            Cioccolatino.cioccolatini+=1
        
        
    
    def produce(self):
        super().produce()
        print(f"Numero cioccolatini: {self.ncioccolatini}")
        