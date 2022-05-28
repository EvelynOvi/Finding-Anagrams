# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word =input('Input Word: ')
anagram =input('Input Anagram to check: ')

def find_anagram(word, anagram):
    # [assignment] Add your code here
    return sorted(word.lower()) == sorted(anagram.lower())
            
print(find_anagram(word, anagram))