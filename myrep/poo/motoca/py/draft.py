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
    def __init__(self,power:int=1):
        self.__power=power
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
        
    def Leave(self):
        if self.__person==None:
            print("fail: empty motorcycle")
            return None
        else:
            person=self.__person
            self.__person=None
            return person
        
    def BuyTime(self,time:int)->int:
        self.__time+=time

    def Drive(self,distance:int)->int:
        if self.__time==0:
            print("fail: buy time first")
        elif distance>self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time=0
        elif self.__person==None:
            print("fail: empty motorcycle")
        elif self.__person.GetAge()>10:
            print("fail: too old to drive")
        else:
            self.__time-=distance


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
            power=int(args[1])
            motoquinha=Motoca(power)
        if args[0]=="leave":
            person=motoquinha.Leave()
            if person!=None:
                print(person)                
        if args[0]=="buy":
            time=int(args[1])
            motoquinha.BuyTime(time)
        if args[0]=="drive":
            distance=int(args[1])
            motoquinha.Drive(distance)
        
        #if args[0]=="honk":
main()