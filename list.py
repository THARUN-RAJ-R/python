a=['1','2','3','4']
print(a[2]) 
a.insert(2,"4")
print(a)
print(a.count("4"))
b=['6','7','8','9']
a.append(b)
print(a)        
a.insert(4,b)
print(a)    
c=a 
c.pop()
print(a)
d=a.copy()
d.pop()
d.pop()
print(d)
e=['a','b','c','d']
d.extend(e)
print(d)
d.sort(reverse=True)
print(d)