user_value = input("User integer value:")

counter = 0
max_value = 0

while user_value[counter:]:
    if max_value < int(user_value[counter]):
        max_value = int(user_value[counter])
    counter += 1

print(f"Max value: {max_value}")
