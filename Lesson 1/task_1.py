# Test variable
var_auto_tuple = ("val_test", 23.3)
var_int: int = 20
var_float: float = 2.2
var_string: str = "string"
var_bool: bool = True
var_list: list = ["test_string", 35, 3.4]
var_tuple: tuple = ("value_1", 1)
var_dict: dict = {"name": "Maria", "age": 99}

print(f"var_auto_tuple = {var_auto_tuple} type = {type(var_auto_tuple)}")
print(f"var_int = {var_int} type = {type(var_int)}")
print(f"var_float = {var_float} type = {type(var_float)}")
print(f"var_string = {var_string} type = {type(var_string)}")
print(f"var_bool = {var_bool} type = {type(var_bool)}")
print(f"var_list = {var_list} type = {type(var_list)}")
print(f"var_tuple = {var_tuple} type = {type(var_tuple)}")
print(f"var_dict = {var_dict} type = {type(var_dict)}")

# Test user input
name = str(input("Enter your name:"))
age = int(input("How old are you?:"))
country = str(input("Where are your from?"))
print(f"Your name's {name} and you're {age} years old. Your country is {country}")
