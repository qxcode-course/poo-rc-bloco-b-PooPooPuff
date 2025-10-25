class Watch:
    def __init__(self,hour:int=0,min:int=0,sec:int=0):
        self.__hour=0
        self.__min=0
        self.__sec=0
        self.SetHour(hour)
        self.SetMin(min)
        self.SetSec(sec)
    
    def __str__(self)->str:
        return f"{self.__hour:02d}:{self.__min:02d}:{self.__sec:02d}"
    
    def GetHour(self)->int:
        return self.__hour
    
    def GetMin(self)->int:
        return self.__min
    
    def GetSec(self)->int:
        return self.__sec
    
    def SetHour(self,hour:int):
        if 0<=hour<=23:
            self.__hour=hour
        else:
            print("fail: hora invalida")
    
    def SetMin(self,min:int):
        if 0<=min<=59:
            self.__min=min
        else:
            print("fail: minuto invalido")

    def SetSec(self,sec:int):
        if 0<=sec<=59:
            self.__sec=sec
        else:
            print("fail: segundo invalido")
    
    def NextSec(self):
        self.__sec+=1
        if self.__sec==60:
            self.__sec=0
            self.__min+=1
            if self.__min==60:
                self.__min=0
                self.__hour+=1
                if self.__hour==24:
                    self.__hour=0
        
def main():
    watch=Watch(0,0,0)
    while True:
        line=input()
        print("$"+line)
        args=line.split()
        
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(watch)
        elif args[0]=="set":
            watch.SetHour(int(args[1]))
            watch.SetMin(int(args[2]))
            watch.SetSec(int(args[3]))
        elif args[0]=="init":
            watch=Watch(int(args[1]),int(args[2]),int(args[3]))
        elif args[0]=="next":
            watch.NextSec()
        else:
            print("Comando invalido")

main()
