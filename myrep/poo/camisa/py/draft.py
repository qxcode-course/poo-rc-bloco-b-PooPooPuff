class Roupa:
    def __init__(self):
        self.__tamanho:str=""
    
    def __str__(self):
        if self.__tamanho=="":
            return "size: ()"
        else:
            return f"size: ({self.__tamanho})"

    def GetTamanho(self)->str:
        return self.__tamanho
    
    def SetTamanho(self,tamanho:str):
        tamanho_disponivel=["PP","P","M","G","GG","XG"]
        if tamanho in tamanho_disponivel:
            self.__tamanho=tamanho
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

def main():
    roupa=Roupa()
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        if args[0]=="show":
            print(roupa)
        if args[0]=="size":
            roupa.SetTamanho(args[1])
main()