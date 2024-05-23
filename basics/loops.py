# while
x = 1;
while x < 10:
    print(x);
    x += 1;

print("---------------------")

# for in
word = "Hello";
for character in word:
    print(character);

print("---------------------")

# break
for char in word:
    if char == "o":
        break;
    print(char);

print("---------------------")

# continue
for char in word:
    if char == "l":
        continue;
    print(char);

print("---------------------")

for num in range(1, 10, 2):
    print(num);

print("---------------------")

# nested loops
for outer in range(1, 5):
    print(outer);
    for inner in range(1, 5):
        print ("\t", inner);
