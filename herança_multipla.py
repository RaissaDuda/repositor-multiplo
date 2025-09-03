class Funcionario:
  def __init__(self, nome):
    self.nome = nome 
  
  def mostrar_tarefas(self):
    print("Faz tarefas gerais.")

class Desenvolvedor:
  def __init__(self, linguagem):
    self.linguagem = linguagem

def programar(self):
    print(f"Programando em {self.linguagem}.")

class Testador:
  def testar(self):
 print("Testando o sistema.")

class EngenheiroDeSoftware(Funcionario, Desenvolvedor):
    def __init__(self, nome, linguagem):
        Funcionario.nome=nome
        Desenvolvedor.linguagem=linguagem
        #Funcionario.__init__(self, nome)      
        #Desenvolvedor.__init__(self, linguagem)

  def mostrar_tarefas(self):
      
      super().mostrar_tarefas()
      
         self.programar()

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu programo em {self.linguagem}.")
        
        # Testando
#eng = EngenheiroDeSoftware("Ana", "Python")
#eng.mostrar_tarefas()
#eng.apresentar()