# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word =input('Input Word: ')
anagram =input('Input Anagram to check: ')

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if (' ' in word):
        word = word.replace(' ', '')
    if  (' ' in anagram):
        anagram = anagram.replace(' ', '')
    
    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return False
            
print(find_anagram(word, anagram))