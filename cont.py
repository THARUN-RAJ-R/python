age = 20
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
for i in range(5):
    print(i)
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
for i in range(10):
    if i % 2 == 0:
        pass  
    else:
        print(i)
for i in range(5):
    print(i)
else:
    print("success")

count = 0
while count < 5:
    print(count)
    count += 1
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully.")
