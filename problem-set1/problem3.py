s = input("Enter string: ")
string = ""
prev = 26
for char in s:
    current = ord(char) - 97
    string += char if current >= prev else " " + char
    prev = current
string = string.split(" ")
max = -1
longest = ""
for val in string:
    if len(val) > max:
        max = len(val)
        longest = val
print("Longest substring in alphabetical order is:", longest)
