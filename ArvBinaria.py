class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerdo = None
    self.direito = None

class ArvoreBinaria:
  def __init__(self):
    self.raiz = None

  def inserir(self, valor):
    novo_no = No(valor)
    if self.raiz is None:
      self.raiz = novo_no
      return
    else:
      elemento = self.raiz
      while True:
        if valor < elemento.valor:
          if elemento.esquerdo is None:
            elemento.esquerdo = novo_no
            return
          else:
            elemento = elemento.esquerdo
        else:
          if elemento.direito is None:
            elemento.direito = novo_no
            return
          else:
            elemento = elemento.direito
#optei por fazer essa função usando laço de repetição pois achei mais compreensivel para mim;
#e tambem achei mais fácil de implementar a lógica de contar os passos e elementos que foram percorridos, com este modo
  def buscar(self, valor):
    elemento = self.raiz
    passos=0
    while elemento is not None:
        print(f"ELemento que foi percorrido: {elemento.valor}")
        if valor == elemento.valor:
            print(f"Número de passos: {passos}")
            return True
        elif valor < elemento.valor:
            elemento = elemento.esquerdo
        else:
            elemento = elemento.direito
        passos+=1
    return False



  def em_ordem(self, item):
    if item is not None:
      self.em_ordem(item.esquerdo)
      print(item.valor, end=" ")
      self.em_ordem(item.direito)


arvore = ArvoreBinaria()
#adicionei considerando que a arvore foi listada em_ordem para se assemelhar com os slides
arvore.inserir(21)
arvore.inserir(14)
arvore.inserir(28)
arvore.inserir(11)
arvore.inserir(5)
arvore.inserir(12)
arvore.inserir(18)
arvore.inserir(15)
arvore.inserir(19)
arvore.inserir(32)
arvore.inserir(25)
arvore.inserir(23)
arvore.inserir(27)
arvore.inserir(30)
arvore.inserir(37)


print("\nEm-ordem:", end=" ")
arvore.em_ordem(arvore.raiz)

print("\n")
arvore.buscar(27)


