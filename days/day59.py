# program to check if a string is a palindrome

# get word from user, strip any leading/trailing space
#+and turn all letters to lowercase for comparison
word = input("Check if palindrome: ").strip().lower()

# create list to hold all characters
charList = []

# fill charList and exclude space
for letter in word:
    if letter == " ":
        pass
    else:
        charList.append(letter)

while len(charList) > 0:
    # compare the ends of the word/string
    start = charList[0]
    end = charList[-1]
    # if the word is 1 letter, or the length of it has reached 1
    # the word is thought of as being a palindrome and exit loop
    if len(charList) == 1:
        print("The word is a palindrome.")
        break
    # while the start and end chars match, continue to strip the
    #+start and the end characters of the string
    if start == end:
        charList.pop(0)
        charList.pop(-1)
        #print(charList)
    # if any of the compared chars don't match, exit loop
    # the word is not a palindrome
    else:
        print("The word is not a palindrome.")
        break


# as a recursive solution (not my own, but i want it here)
def palindrome(word):
    if int(len(word)) == 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


print()
print(f'Recursive result.\nIs "{word}" a palindrome?\n{palindrome(charList)}')
