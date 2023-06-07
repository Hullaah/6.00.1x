s = 'luwscraoflpr'
alphabet = "abcdefghijklmnopqrstuvwxyz"
arr_longest, longest = [], []
j, len_s, prev = 0, len(s), 0
while j < len_s:
    for i in range(26):
        if alphabet[i] == s[j]:
            break
    if j == 0:
        longest.append(s[j])
    else:
        if prev > i:
            arr_longest.append(longest)
            longest = []
            longest.append(s[j])
        elif prev < i or prev == i:
            longest.append(s[j])
    prev = i
    j += 1
if not arr_longest:
    arr_longest.append("".join(longest)) 
long = [-1, 0]
for i in range(len(arr_longest)):
    len_elem = len(arr_longest[i])
    if len_elem > long[0]:
        long[0] = len_elem
        long[1] = i

print("Longest substring in alphabetical order is:", "".join(arr_longest[long[1]]))
