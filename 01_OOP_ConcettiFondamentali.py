#Astrazione: Dichiaro una classe generica MetodoPagamento astratta
from abc import ABC, abstractmethod

#In questo scenario, per semplificare, il metodo di Pagamento ha dentro di se il saldo su cui lavoriamo, idealmente questo andrebbe su una classe ContoCorrente separata
class MetodoPagamento(ABC):
    def __init__(self,saldo):
        self.saldo=saldo
    
    @abstractmethod
    def esegui_transazione(self,valore,metodo):
        #Astrazione: Questo è il metodo che non stiamo implementando nella classe e che ogni sottoclasse dovrà forzatamente definire
        pass

    def stampaRicevuta(self, importo_transazione):
        if importo_transazione>self.saldo:
            print(f"Transazione fallita: €{importo_transazione}")
        else:
            print(f"Transazione eseguita con successo: €{importo_transazione}")
        print(f"Saldo residuo sul conto: €{self.saldo}")

#Incapsulamento: Creo una classe CartaDiCredito che ha due attributi privati:
#Ereditarietà: CartaDiCredito è sottoclasse di MetodoPagamento e ne eredita tutti gli attributi e metodi
class CartaDiCredito(MetodoPagamento):
    def __init__(self,saldo,num_carta,cvv):
        super().__init__(saldo)
        self.num_carta=num_carta
        self.__cvv=cvv

    #Definisco setter e getter per poter lavorare sul numero di carta:
    @property
    def num_carta(self):
        return self.__num_carta

    @num_carta.setter
    def num_carta(self,numero):
        if len(str(numero)) == 16:
            self.__num_carta=numero
        else:
            self.__num_carta="0000000000000000"
            print("Hai inserito un numero di carta non valido")
    
    #Devo per forza sviluppare il metodo esegui_transazione per non generare errori
    #Polimorfismo: Implemento il metodo in modo specifico (Sarà diverso da un altro metodo di pagamento)
    def esegui_transazione(self, valore, metodo):
        if metodo=="preleva" and self.saldo>=valore:
            self.saldo-=valore
            print(f"Pagamento di €{valore} effettuato con carta {self.mostra_anteprima_carta()}")
        elif metodo=="deposita":
            self.saldo+=valore
        else:
            print("Fondi insufficienti sulla carta.")
        self.stampaRicevuta(valore)
    
    # Getter per vedere le ultime 4 cifre della carta
    def mostra_anteprima_carta(self):
        return f"**** **** **** {self.num_carta[-4:]}"
    
#Creo una seconda classe per mostrare il polimorfismo in modo completo
class PayPal(MetodoPagamento):
    def __init__(self, importo,email):
        super().__init__(importo)
        self.email=email
    
    #Polimorfismo: Implemento il metodo in modo diverso da CartaDiCredito
    #Anche qui sono forzato a implementare il metodo
    def esegui_transazione(self, valore, metodo):
        if metodo=="preleva" and self.saldo>=valore:
            self.saldo-=valore
            print(f"Pagamento di  €{valore} effettuato tramite account Paypal: {self.email}")
        elif metodo=="deposita":
            self.saldo+=valore
            print(f"Ricarica di €{valore} eseguita sull'account Paypal: {self.email}")
        else:
            print("Operazione non riuscita")
        self.stampaRicevuta(valore)

#Oggetti: Creo due oggetti uno di tipo PayPal e uno CartadiCredito e mostro come i metodi agiscono diversamente:
miavisa=CartaDiCredito(1000,"1434567564545678","638")
miopaypal=PayPal(500,"mariorossi@gmail.com")

#Mostro le differenze tra le due classi:
miavisa.esegui_transazione(150,"preleva")
miopaypal.esegui_transazione(150,"preleva")
miopaypal.esegui_transazione(400,"preleva")
print("-"*10)
