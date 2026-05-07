"""
Simula un sistema di controllo accessi integrato in un router. Per ogni pacchetto in arrivo il router deve decidere in tempo reale se 
l'IP sorgente è nella blacklist e bloccarlo.
Gli IP sono nella forma 192.168.1.1 - prima di inserirli nel BST vanno convertiti in interi usando la libreria ipaddress. Il BST lavora con interi, 
ma all'utente mostriamo sempre la forma leggibile.
"""

import ipaddress, random
from datetime import datetime
import time

#Codice Coda:
from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()         # deque privato — O(1) per enqueue e dequeue

    def enqueue(self, item):
        self.__data.append(item)      # aggiunge in fondo

   
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()  # rimuove dalla testa — O(1)

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty queue")
        return self.__data[0]         # guarda la testa senza rimuoverla

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Queue({list(self.__data)})"


#Codice BST:
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


# 1). Scrivi due funzioni di conversione - ipToInt(ip) e intToIp(n) - usando ipaddress.ip_address()
def ipToInt(ip):
    return int(ipaddress.ip_address(ip))

def intToIPp(n):
    return ipaddress.ip_address(n)
# 2). Genera 1000 IP casuali per la blacklist usando una list comprehension, convertili in interi e inseriscili nel BST
random.seed(int(datetime.now().strftime("%Y%m%d")))
albero=BST()
blacklist=set()
while len(blacklist)<1000:
    valore=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    if not valore in blacklist:
        blacklist.add(valore)
        albero.insert(ipToInt(valore))
blacklist=list(blacklist)

# 3) Genera 20 pacchetti in arrivo - 10 IP presi dalla blacklist e 10 IP nuovi mai visti - mescolali casualmente e inseriscili nella Queue
inArrivo=random.sample(blacklist,10)
nuoviIp=set()
while len(nuoviIp)<10:
    valore=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    if valore not in blacklist:
        nuoviIp.add(valore)
nuoviIp=list(nuoviIp)
inArrivo+=nuoviIp
# Mescolo i valori
random.shuffle(inArrivo)

codaMessaggi=Queue()
for v in inArrivo:
    codaMessaggi.enqueue(v)

# 4) Processa i pacchetti dalla Queue uno per uno - per ognuno cerca l'IP nel BST e stampa BLOCCATO o PERMESSO
bloccati=permessi=0
print(f"Processo di {codaMessaggi.size()} in corso")
while not codaMessaggi.isEmpty():
    prossimoIP=ipToInt(codaMessaggi.dequeue())
    if albero.search(prossimoIP):
        print(f"{prossimoIP} - BLOCCATO")
        bloccati+=1
    else:
        print(f"{prossimoIP} - PERMESSO")
        permessi+=1

# 5) Stampa il riepilogo finale - quanti pacchetti bloccati e quanti permessi
print(f"In totale ho bloccato {bloccati} pacchetti e permesso {permessi} pacchetti")

#6) Misura e confronta il tempo di ricerca nel BST e in una lista Python con gli stessi 1000 IP - stampa quante volte una struttura è più veloce dell'altra.
valore=blacklist[random.randint(0,999)]
print ("Confronto tra BST e Lista Python del valore: ")
#ALbero
inizio=time.perf_counter()
albero.search(ipToInt(valore))
fine=time.perf_counter()
tempoAlbero=fine-inizio
print(f"La ricerca nell'Albero BST ha impiegato: {tempoAlbero*1000:.4f} ms per essere completata")
#Lista:
inizio=time.perf_counter()
valore in blacklist
fine=time.perf_counter()
tempoLista=fine-inizio
print(f"La lista python ha impiegato: {tempoLista*1000:.4f} ms per essere completata")

if tempoAlbero>0:
    print(f"L'albero è {tempoLista / tempoAlbero:.2f} volte più veloce")
else:
    print("L'albero è stato troppo veloce per essere misurato singolarmente!")