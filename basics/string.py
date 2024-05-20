print(type(""));

age = 85;
print(age);

age = "eighty-five"
print(age);

# Type Casting
age = int('19');
print(int(age));

first_name = 'John';
last_name = 'Doe';
print(first_name + last_name);

print("4" + "5");

msg = "Hello World!"
print(msg[0]);
print(msg[-1]);
print(msg[2:6]);         # start index is included, stop index is not
print(msg[6:99]);
print(msg[6:]);
print(msg[:6]);
print((len(msg)));

msg = "ha!ha!ha!ha!"
print(msg[0:10:3]);
print(msg[0:10:5]);

msg = "hello!" * 99;
print(msg);


# Escape characters
msg = "hello \n world"
print(msg);
print("hello \t world");
print("My name is \"John Doe\"");
print("\\");

multiline_str = '''
This is a 
multiline string
''';
print(multiline_str);

# f strings
print(f"there are {24 * 60 * 60} seconds in a day");

user = None;
print(user);

