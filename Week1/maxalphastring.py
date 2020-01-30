s = 'azcbobobegghakl'
lstring = s[0]
slen = 1

for i in range(len(s)):
    for j in range(i,len(s)-1):
            if s[j+1] >= s[j]:
                    if (j+1)-i+1 > slen:
                        lstring = s[i:(j+1)+1]
                        slen = (j+1)-i+1
            else:
                        break

print("Longest substring in alphabetical order is: " + lstring)
