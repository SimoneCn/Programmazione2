import random
import importlib
liste_linkate = importlib.import_module("05_ListeLinkate")
from datetime import datetime
import time

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left   = None   # figlio sinistro — valori minori
        self.right  = None   # figlio destro — valori maggiori


class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            # partiamo dalla radice e scendiamo nell'albero
            # la funzione chiamerà se stessa finché non trova un posto libero
            self.__insertRicorsivo(self.__radice, valore)


    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            # il valore è minore — dobbiamo andare a sinistra
            if nodo.left is None:
                # CASO BASE: posto libero a sinistra — inseriamo qui
                nodo.left = NodoBST(valore)
            else:
                # CASO RICORSIVO: c'è già un nodo a sinistra
                # richiamiamo la stessa funzione sul figlio sinistro
                # il problema si riduce: scendiamo di un livello
                self.__insertRicorsivo(nodo.left, valore)
        else:
            # il valore è maggiore — dobbiamo andare a destra
            if nodo.right is None:
                # CASO BASE: posto libero a destra — inseriamo qui
                nodo.right = NodoBST(valore)
            else:
                # CASO RICORSIVO: c'è già un nodo a destra
                # richiamiamo la stessa funzione sul figlio destro
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        # partiamo dalla radice
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):
        # CASO BASE 1: nodo inesistente — il valore non è nell'albero
        if nodo is None:
            return False

        # CASO BASE 2: trovato — il valore corrisponde
        if nodo.valore == valore:
            return True

        if valore < nodo.valore:
            # il valore è minore — non può essere a destra
            # CASO RICORSIVO: cerchiamo solo nel sottoalbero sinistro
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            # il valore è maggiore — non può essere a sinistra
            # CASO RICORSIVO: cerchiamo solo nel sottoalbero destro
            return self.__searchRicorsivo(nodo.right, valore)

    def inOrder(self):
        # inOrder restituisce i valori in ordine crescente
        # perché visita prima sinistra, poi radice, poi destra
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi

    def __inOrderRicorsivo(self, nodo, elementi):
        # CASO BASE: nodo inesistente — non c'è nulla da visitare
        if nodo is None:
            return

        # CASO RICORSIVO:
        # 1. visita prima tutto il sottoalbero sinistro (valori minori)
        self.__inOrderRicorsivo(nodo.left, elementi)

        # 2. poi aggiungi il valore del nodo corrente
        elementi.append(nodo.valore)

        # 3. poi visita tutto il sottoalbero destro (valori maggiori)
        self.__inOrderRicorsivo(nodo.right, elementi)

    def isEmpty(self):
        return self.__radice is None

    def __repr__(self):
        return f"BST(inOrder={self.inOrder()})"
    
# 1). Genera una lista di 1000 numeri casuali tra 1 e 10k usando una list comprehnsion
random.seed(int(datetime.now().strftime("%Y%m%d")))
valori=[]
for n in range(1000):
    valori.append(random.randint(1,10000))
# 2). Inserisci gli stessi 1000 numeri sia nella lista linkata che nel BST
albero=BST()
listalinkata=liste_linkate.LinkedList()
for n in range(1000):
    albero.insert(valori[n])
    listalinkata.insertLast(valori[n])
# 3). Scegli un numero da cercare - prendi il 500esimo elemento della lista generata
scelta=valori[499]
"""
#Se volessi farlo scegliere all'utente
try:
    scelta=int(input("Inserisci un valore da cercare: "))
except ValueError:
    print("Scelta non valida, seleziono 5")
    scelta=5
"""
# 4). Misura il tempo di ricerca nella lista collegata usando time.perf_counter()
inizio = time.perf_counter()
listalinkata.search(scelta)
fine = time.perf_counter()
tempoListaLinkata = fine - inizio
# 5). Misura il tempo di ricerca nel BST usando time.perf_counter()
inizio=time.perf_counter()
albero.search(scelta)
fine=time.perf_counter()
tempoAlbero=fine-inizio
# 6). Stampa i due tempi e calcola quante volte una struttura è più veloce dell'altra
print(f"La ricerca nella Lista Linkata ha impiegato: {tempoListaLinkata*1000:.4f} ms per essere completata")
print(f"La ricerca nell'Albero BST ha impiegato: {tempoAlbero*1000:.4f} ms per essere completata")

if tempoAlbero>0:
    print(f"L'albero è {tempoListaLinkata / tempoAlbero:.2f} volte più veloce")
else:
    print("L'albero è stato troppo veloce per essere misurato singolarmente!")
