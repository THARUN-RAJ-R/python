class person:
    name= None
    age= None
    def intp(s):
        c=(input("enter:"))
        s.name=c
        b=int(input("enter no:"))
        s.age=b
    def info(s):
        print(s.name)
        print(s.age)    
a=person()
a.name="John"
a.age=30
a.info()
b=person()
b.name="Ram"
b.age=25
b.info()
c=person()
c.intp()
c.info()