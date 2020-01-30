s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if s[i:i+3] in ['bob']:
        count = count + 1
print("Number of times bob occurs: ",count)
