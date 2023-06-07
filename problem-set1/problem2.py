# Get input from user
word = input("Enter a word: ").lower()
bob_count = 0
word_len = len(word)
index = 0
i = 0
# check if bob exists in word
if "bob" in word:
    # iterate over the input counting the number of bob in it
    while i < word_len:
        # find the index which bob can be found from index i
        #  to end of input
        index = word.find("bob", i, word_len)
        # if bob not in index, exit else increment bob_count
        # and set i to the first index where bob was found #
        if index != -1:
            bob_count += 1
            i = index
        else:
            break
        # exit if i is 2 index away from the last index
        if word_len - i == 3:
            break
        # increment i so as to point to the next position
        # after the bob index and to avoid an infinite loop #
        i += 1
print(bob_count)
