seconds = int(input("What time is it? (second format):"))
print(f"{(seconds // 3600):02}:{((seconds % 3600) // 60):02}:{((seconds % 3600) % 60):02}")
