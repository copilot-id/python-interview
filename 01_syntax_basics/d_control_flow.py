# control flow
# if, elif, else
# for, while
# break, continue
# pass

# if-elif-else
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
    
# Output
# x is less than y

# for loop
for i in range(5):
    print(i)
    
# Output
# 0
# 1
# 2
# 3
# 4

# while loop
i = 0
while i < 5:
    print(i)
    i += 1
    
# Output
# 0
# 1
# 2
# 3
# 4

# break statement
for i in range(5):
    if i == 3:
        break
    print(i)
    
# Output
# 0
# 1
# 2

# continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)
    
# Output
# 0
# 1
# 2
# 4

# pass statement
for i in range(5):
    if i == 3:
        pass
    print(i)
    
# Output
# 0
# 1
# 2
# 3
# 4
#
