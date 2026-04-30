class Notifica:
    def __init__(self,listaMSG):
        if isinstance(listaMSG,list):
            self.__listaMSG=listaMSG
        else:
            self.__listaMSG=[]
    
    def arriva(self,messaggio):
        self.__listaMSG.append(messaggio)

    def leggi(self):
        if not self.is_empty():
            return self.__listaMSG.pop()
        return "Nessuna notifica"
    
    def prossima(self):
        if not self.is_empty():
            print("Ultima Notifica: ",self.__listaMSG[-1])
            return self.__listaMSG[-1]
        return "Nessuna Notifica"

    def is_empty(self):
        return len(self.__listaMSG)<=0
    
    def stampaMessaggi(self):
        print("-------------")
        print("Lista messaggi: ")
        for m in reversed(self.__listaMSG):
            print(m)
        print("-------------")
        

n= Notifica([])

n.arriva("WhatsApp: Ciao!")
n.arriva("Gmail: Hai un nuovo messaggio")
n.arriva("Instagram: Ti hanno taggato")
n.stampaMessaggi()

n.prossima()   #  "In cima: Instagram: Ti hanno taggato"

print(n.leggi())      #  "Letta: Instagram: Ti hanno taggato"
print(n.leggi())      #  "Letta: Gmail: Hai un nuovo messaggio"
print(n.leggi())      #  "Letta: WhatsApp: Ciao!"
print(n.leggi())      # "Nessuna notifica."
n.prossima()
