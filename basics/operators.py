# and operator
age = 12;
print(age > 10 and age < 21);

print(True and True);
print(True and False);

# or operator
print("a" == "b" or 1 < 5);

day = input("What day of the week is it?");
if day == "saturday" or day == "sunday":
    print("it's a weekend");
else:
    print("it's a workday");

# not operator
print(not age >= 12);