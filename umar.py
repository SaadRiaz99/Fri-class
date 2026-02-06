import string

# Taking input from user
sentence = input("Enter a sentence: ")

# 1️⃣ Length of string (using module + len)
total_characters = len(sentence)

# Counters
alphabets = 0
digits = 0

# 2️⃣ FOR LOOP → counting alphabets and digits
for ch in sentence:
    if ch in string.ascii_letters:
        alphabets += 1
    elif ch in string.digits:
        digits += 1

# 3️⃣ WHILE LOOP → counting total characters again
count = 0
i = 0
while i < len(sentence):
    count += 1
    i += 1

print("\n--- Results ---")
print("Total characters:", total_characters)
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total characters (using while loop):", count)

print("\n--- Nested Loop Output ---")
text = "Saad did 10 push-ups. After completing the 10 push-ups, he felt hungry."

words = text.split()

for word in words:          # Outer loop
    for letter in word:     # Inner loop
        print(letter, end=" ")
    print()