d = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(d)
print("Name:", d['name'])
print("Age:", d.get('age'))
d['email'] = 'alice@example.com'
print(d)
del d['age']
print( d)
email = d.pop('email')
print(d)
d = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Initial dictionary d:", d)
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())
d.update({'age': 26, 'city': 'Boston'})
print(d)
print('email' in d)
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")
d.clear()
print(d)
