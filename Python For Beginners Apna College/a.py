s = input()

check= 0

for word in range(0,len(s),1):
    for count in range(word+1,len(s)):
        if s[word] == s[count]:
            check+=1

if check >=2:
    print("Yes")
else:
    print("No")
