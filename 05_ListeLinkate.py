class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None


class LinkedList:
    def __init__(self):
        self.__testa = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo        = Nodo(valore)
        nuovo.next   = self.__testa
        self.__testa = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = Nodo(valore)
        if self.__testa is None:
            self.__testa = nuovo
        else:
            corrente = self.__testa
            while corrente.next is not None:
                corrente = corrente.next
            corrente.next = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next is not None:
            if corrente.next.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore       = self.__testa.valore
        self.__testa = self.__testa.next
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        if self.__testa.next is None:
            valore       = self.__testa.valore
            self.__testa = None
            self.__size -= 1
            return valore
        corrente = self.__testa
        while corrente.next.next is not None:
            corrente = corrente.next
        valore        = corrente.next.valore
        corrente.next = None
        self.__size -= 1
        return valore

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " → ".join(elementi) + "])"

lista=LinkedList()
#1. Registra in ordine le prime modifiche: "admin", "mario", "sara"
lista.insertLast("admin")
lista.insertLast("Mario")
lista.insertLast("Sara")
#2. Stampa la cronologia
print(lista)
#3. "guest" ha modificato il file dopo "mario" — inseriscilo nella posizione corretta
lista.insertAfter("Mario","Guest")
print(lista)
#5. "root" ha modificato il file per primo — inseriscilo prima di "admin"
lista.insertFirst("root")
print(lista)
#7. "luca" ha modificato il file prima di "sara" — inseriscilo nella posizione corretta
lista.insertBefore("Sara","Luca")
#9. La modifica più vecchia è stata archiviata — rimuovi il primo elemento
lista.removeFirst()
print(lista)
#11. L'ultima modifica è stata annullata — rimuovi l'ultimo elemento
lista.removeLast()
print(lista)
#13. Stampa quante modifiche sono registrate
print(f"Sono state registrate {lista.size()} modifiche")
#14. Stampa chi ha effettuato la modifica più recente da processare senza rimuoverlo
print(f"{lista.peekFirst()} ha effettuato la modifica più recente!")