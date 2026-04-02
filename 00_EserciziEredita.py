class persona:
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
    
    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni"
    
class dottore(persona):
    def __init__(self,nome,cognome,eta,specializzazione,matricola,reparto,listaPazienti=None):
        super().__init__(nome,cognome,eta)
        self.specializzazione=specializzazione
        self.matricola=matricola
        self.reparto=reparto
        self.listaPazienti=listaPazienti or []

    def __str__(self):
        return super().__str__()+f" Specializzazione: {self.specializzazione}, matricola: {self.matricola}, reparto: {self.reparto}"
    
    def mostraPazienti(self):
        if not self.listaPazienti:
            print("Non ci sono pazienti al momento")
        else:
            print("Ecco la lista dei pazienti: ")
            for paziente in self.listaPazienti:
                print(paziente)
            print("-------------------------")

    #Usa il codice che dovrebbe essere univoco per rimuovere il paziente
    def rimuoviPaziente(self,paziente):
        print("Controllo: ")
        for p in self.listaPazienti:
            if p.codice==paziente.codice:
                self.listaPazienti.remove(p)
                break
                

    def aggiungiPaziente(self,paziente):
        self.listaPazienti.append(paziente)

class pazienti(persona):
    def __init__(self,nome,cognome,eta,codice,grupposanguigno,patologie,allergie):
        super().__init__(nome,cognome,eta)
        self.codice=codice
        self.grupposanguigno=grupposanguigno
        self.patologie=patologie
        self.allergie=allergie

    def __str__(self):
        return super().__str__()+f" Codice: {self.codice}, Gruppo Sanguigno: {self.grupposanguigno}"
    
    def aggiungiPatologia(self,patologia):
        if patologia not in self.patologie:
            self.patologie.append(patologia)

    def rimuoviPatologia(self,patologia):
        if patologia in self.patologie:
            self.patologie.remove(patologia)
    
    def mostraPatologie(self):
        print("Lista delle patologie: ")
        for patologia in self.patologie:
            print(patologia)
        print("-------------------------")

    def aggiungiAllergia(self,allergia):
        if allergia not in self.allergie:
            self.allergie.append(allergia)

    def rimuoviAllergia(self,allergia):
        if allergia in self.allergie:
            self.allergie.remove(allergia)
            
    def mostraAllergie(self):
        print("Lista delle allergie: ")
        for allergia in self.allergie:
            print(allergia)
        print("-------------------------")

d= dottore("Mario","DiPaola",35,"Tuttofare","ABCDE","Odontoiatria",[])
print(d)
marco=pazienti("Marco","Carta 2",45,"12346","A",["Infiammazione alla cute"],["Pesca"])
d.aggiungiPaziente(pazienti("Marco","Carta",45,"12345","A",[],[]))
d.aggiungiPaziente(pazienti("Marco","Carta 2",45,"12346","A",[],[]))
d.mostraPazienti()
d.rimuoviPaziente(marco)
d.mostraPazienti()
