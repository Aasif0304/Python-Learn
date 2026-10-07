# # learning calss and object-------------

# class goa:
#     name=""
#     drink=""
#     def party(self):
#         print("Lets Party")
#     def beach(self):
#         print("Enjoying the beach")    
        
# ramesh = goa()
# surash= goa()

# ramesh.name="ramesh"
# surash.name="surash"

# ramesh.drink="yes"
# surash.drink="no"

# print(ramesh.name)
# print("drink",ramesh.drink)
# print(surash.name)
# print("drink",surash.drink)

# ramesh.party()
# surash.beach()

# class laptop:
#     price=0
#     processor=""
#     ram=""
# Hp=laptop()
# Dell=laptop()
# Lenova=laptop()  

# Hp.price=80000
# Hp.processor="i5"
# Hp.ram="8GB"

# Dell.price=100000
# Dell.processor="i6"
# Dell.ram="12GB"

# Lenova.price=80000
# Lenova.processor="i7"
# Lenova.ram="16GB"

# class fruit:
#     def __init__(self,col):
#         self.color=col

# apple=fruit("red")
# print(apple.color)

# class teacher:
#     def __init__(self,name,reg):
#         self.name=name
#         self.reg=reg
#     def display(self):
#         print("name",self.name)
#         print("reg",self.reg)
# t1=teacher("Mohan","1")
# t2=teacher("polo","2")

# t1.display()
# t2.display()

# class calcultor:
    
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def Add(self):
#         print(self.a+self.b)
        
#     def sub(self):
#         print(self.a-self.b)
    
#     def mul(self):
#         print(self.a*self.b)
        
#     def div(self):
#         print(self.a/self.b)   
    
# cl = calcultor(10,20)
# cl.Add()
# cl.sub()
# cl.mul()
# cl.div()


# ------------inheritance
# class garndpa():
#     def phone(self):
#         print("grandpa's phone")

# class dad():
#     def laptop(self):
#         print("Dady's Laptop")
        
# class son(dad,garndpa):
#     def car(self):
#         print("MY CAR")
        
# mod=son()
# mod.car()
# mod.laptop()
# mod.phone()

 
#  -----------SUPER KEY___
# class a():
#         print("A")

# class b():
#     def __init__(self):
#         super().__init__()
#         print("B")
        
# class c(b):
#     def __init__(self):
#         super().__init__()
#         print("c")
        
        
        
# ob1=c()



# ----------polymorphism

class Animal():
    def sound(self):
        print("Amimal Make Sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog Braking")
        
class Bird(Animal):
    def sound(self):
        print("Bird sing")
           

a1=Bird()
a1.sound()