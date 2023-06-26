class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def saludo(self):
        print(f"Hola mi nombre es {self.name} y mi edad es {self.age}")
    @property
    def age(self):
        return F"{self._age} añios"
    @age.setter
    def age(age, self):
        self._age=age
        
p1=Person("Jose", 20)
p2=Person("joaquin", 15)
p1.saludo()
p2.saludo()