#Delete all occurrences of an element in a list

lst=[12,13,1,4,12,13,12,15,16]
lst.remove(12)
print(lst)





"""Check whether a string is a pangram.
"""




def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True



string = 'the quick brown fox jumps over the lazy dog'
if (ispangram(string) == True):
    print("Yes")
else:
    print("No")
