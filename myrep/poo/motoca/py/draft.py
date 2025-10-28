class Person:
    def __init__(self, name:str, age:int):
        self.__age=age
        self.__name=name
        
    def __str__(self)->str:
        return f"{self.__name}:{self.__age}"
    
    def GetAge(self)->int:
        return self.__age
    
    def GetName(self)->str:
        return self.__name

class Motoca:
    def __init__(self):
        self.__power=1
        self.__time=0
        self.__person=None

    def __str__(self)->str:
            return f"power:{self.__power}, time:{self.__time}, person:({self.GetPerson()})"
    
    def GetPerson(self):
        if self.__person==None:
            return "empty"
        else:
            return f"{self.__person}"

    def Enter(self, person:Person)->bool:
        if self.__person!=None:
            print("fail: busy motorcycle")
            return False
        else:
            self.__person=person
            return True
def main():
    motoquinha=Motoca()
    while True:
        line=input()
        print("$"+line)
        args=line.split()
            
        if args[0]=="end":
            break
        if args[0]=="show":
            print(motoquinha)
        if args[0]=="enter":
            name=args[1]
            age=int(args[2])
            person=Person(name,age)
            motoquinha.Enter(person)
        if args[0]=="init":
            
        #if args[0]=="leave":
        
        #if args[0]=="buy":
        
        #if args[0]=="drive":
        
        #if args[0]=="honk":
main()