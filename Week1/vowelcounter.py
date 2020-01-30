s = 'azcbobobegghakl'
count = 0
for letter in range(len(s)):
    if s[letter] in ['a','e','i','o','u']:
        count = count + 1
print("Number of vowels: ",count)
