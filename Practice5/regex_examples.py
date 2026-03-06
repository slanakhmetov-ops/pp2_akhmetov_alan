import re

# 1. search example
text = input("1. Enter text containing at least one number (e.g., 'My number is 123'): ")
match = re.search(r"\d+", text)
print("Search result:", match.group() if match else "No match")

# 2. findall example
text = input("\n2. Enter text containing numbers separated by anything (e.g., '12, 45, 78'): ")
matches = re.findall(r"\d+", text)
print("Findall result:", matches)

# 3. split example
text = input("\n3. Enter text with spaces, commas, or dots to split (e.g., 'Hello, world. How are you'): ")
parts = re.split(r"[ ,\.]+", text)
print("Split result:", parts)

# 4. sub example
text = input("\n4. Enter text with numbers to replace them with '#' (e.g., 'Phone: 123-456'): ")
replaced = re.sub(r"\d", "#", text)
print("Sub result:", replaced)

# 5. Metacharacters
text = input("\n5. Enter text containing patterns like 'acb', 'a1b', 'a_b' (match 'a' + any char + 'b'): ")
matches = re.findall(r"a.b", text)
print("Metacharacters result:", matches)

# 6. Special sequences
text = input("\n6. Enter text containing numbers to extract using \\d+ (e.g., 'Order 12, 34, 56'): ")
matches = re.findall(r"\d+", text)
print("Special sequences result:", matches)

# 7. Quantifiers
text = input("\n7. Enter text with patterns like 'ab', 'abb', 'abbb', 'abbbb' (match 'a' followed by 2-3 'b'): ")
matches = re.findall(r"ab{2,3}", text)
print("Quantifiers result:", matches)