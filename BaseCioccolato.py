# Classe Base Cioccolato:

''' 
1. Proprietà comuni come tipo di cioccolato e percentuale di cacao e MAX 100 day.
2. Metodo produce() che stampa il tipo di cioccolato e la percentuale di cacao. 
'''

class BaseCioccolato:

    ncioccolato=100

    def __init__(self, tipo, perc_cacao):
        self.tipo_cioccolato=tipo
        self.percentuale_cacao=perc_cacao
        

    def produce(self):
        print(f"Tipo di cioccolato: {self.tipo_cioccolato} \nPercentuale cacao: {self.percentuale_cacao}")