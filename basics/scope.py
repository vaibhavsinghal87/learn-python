def print_name(val):
    name = val;
    print(name);
print_name("John Doe");
# name not accessible outside function scope
# print (name);


# variables in conditions and loops are accessible outside
for char in "Octopus":
    color = "magenta";
    print(char);
print(color);
print(char);

# Enclosing scope a is accessible inside inner function
def outer():
    a = 1;
    def inner():
        print(a);
    inner();
outer();

