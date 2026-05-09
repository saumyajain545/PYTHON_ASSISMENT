#taking input
sentence = input("Enter sentence: ").lower()

vowels = []
consonants = []
#cheking for vowel and consonants
for ch in sentence:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels.append(ch)
        else:
            consonants.append(ch)

print("Vowels:", vowels)
print("Consonants:", consonants)

'''
output
Enter sentence: Apple
Vowels: ['a','e']
Consonants: ['p','p','l']
'''
