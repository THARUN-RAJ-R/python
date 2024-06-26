def dec1(fs):
    def mfx(*a,**b):
        print("hello")
        fs(*a,**b)
        print("end")
    return mfx


@dec1
def add(a,b):
    print( a+b)
@dec1   
def sub(    ):
    print("hello2")

add(3,2)