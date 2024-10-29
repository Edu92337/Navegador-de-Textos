import curses
from curses import wrapper
# criação dos Nós e da Lista duplamente encadeada 
class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None # referencia ao proximo nó
        self.prev = None # referencia ao nó anterior
class lista:
    def __init__(self) -> None:
        self.head = None # referencia o inicio da lista
        self.tail = None # referencia o final da lista 
        
    def append(self,data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

def iniciar_janela(janela):
    janela.clear()
    janela.refresh()
    
def digitar_texto(janela):
    texto = ""
    while True:
        tecla = janela.getch()
        if tecla in (curses.KEY_ENTER, 10, 13):  
            break  
        elif tecla == 127:  # backspace
            texto = texto[:-1]  # remove o último caractere
            janela.clear()  
            janela.addstr(0, 0, texto)
        else:
            texto += chr(tecla)
            janela.addstr(0, 0, texto)
        janela.refresh()
    return texto 

def main(janela):
    historico = lista()
    iniciar_janela(janela)
    janela.addstr("Digite suas frases, aperte ENTER e navegue pelo histórico.")
    janela.addstr(2, 0, "Use as setas para navegar. Pressione 'q' para sair.")
    janela.refresh()
    janela.getch()
    janela.clear()

    atual = historico.tail
    posi = 0
    while True:
        janela.clear()
        texto = digitar_texto(janela)
        if texto.strip():  # adiciona apenas textos não vazios
            historico.append(texto)
            atual = historico.tail  # atualiza o atual para o novo nó no final da lista
        while True:
            tecla = janela.getch()
            if tecla in (curses.KEY_ENTER, 10, 13) :
                break  # sai do segundo loop
            elif tecla == ord('q'):
                return # sai da função main
            elif tecla == curses.KEY_LEFT and atual and atual.prev:
                atual = atual.prev
                posi -= 1
            elif tecla == curses.KEY_RIGHT and atual and atual.next:
                atual = atual.next
                posi += 1
            janela.clear()
            janela.addstr(0, 0, f"Texto atual: {atual.data}")
            janela.addstr(2, 0, f"Escrito à {abs(posi)} Enters atrás")

            janela.refresh()



if __name__ == '__main__':
    wrapper(main)
