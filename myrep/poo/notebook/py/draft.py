class Notebook:
    def __init__(self):
        self.__ligado:bool=False

    def ligar(self):
        if self.__ligado:
            print("Notebook ja tava ligado")
        else:
            self.__ligado=True
            print("Notebook ligoou")

    def desligar(self):
        if not self.__ligado:
            print("fail: notebook ja ta desligado ze")
        else:
            self.__ligado=False
            print("notebook deeesligado")

    def getstatus(self):
        if self.__ligado==False:
            return "Notebook está desligado"
        else:
            return "Notebook está ligado"

    def usar(self, tempo:int):
        if self.__ligado==False:
            print("fail: notebook desligado bro")
            return
        elif tempo<0:
            print("fail: tempo inválido")
            return
        elif tempo==0:
            print("notebook não foi utilizado")
            return
        else:
            print(f"notebook sendo utilizado por {tempo} minutos")

def main():
    notebook=Notebook()
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        if args[0]=="mostrar":
            print(f"{notebook.getstatus()}")
        if args[0]=="usar":
            tempo=int(args[1])
            notebook.usar(tempo)
        if args[0]=="ligar":
            notebook.ligar()
        if args[0]=="desligar":
            notebook.desligar()
main()