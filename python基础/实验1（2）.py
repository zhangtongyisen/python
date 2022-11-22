str1=list(input().lower())
str2={str1.count(i) for i in str1 if 'a'<=i<='z'}
print(str2)
