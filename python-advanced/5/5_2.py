import re
fp1 = open("input.txt","r")
s = fp1.read()
print("\nInitially------> "+s)
s1 = re.sub("\s+"," ",s)
print("\nAfter 5_2.a------> "+s1)
print("------------------------------------------------------------")
s1 = re.sub(r"([.!?])",r"\1 ",s1)
print("\nAfter 5_2.b------> "+s1)
print("------------------------------------------------------------")
m =  re.split('([.!?] *)', s1)
print(m)
for i in m:
	print(i)
s1 = ''.join([each.capitalize() for each in m])
print("\nAfter 5_2.c------> "+s1)
print("------------------------------------------------------------")
s1 = re.sub(r" ([A-Za-z]*) \1",r" \1",s1)
print("\nAfter 5_2.d------> "+s1)
print("------------------------------------------------------------")
fp2 = open("output.txt","w")
fp2.write(s1)
fp1.close()
fp2.close()
