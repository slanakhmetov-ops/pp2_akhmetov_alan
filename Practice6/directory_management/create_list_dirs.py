import os

os.makedirs("a/b", exist_ok=True)

print(os.listdir("."))