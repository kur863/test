print("--------作業1--------")
str1 = "abcde"
str2 = "ABCDE"
str1 = str1.replace("c", "")
str2 = str2.replace("C", "")

print("合併" ,str1+str2)
print("--------作業2--------")

q2ans = []
q2ans.append("a")
q2ans.append("b")
print(q2ans)

print("--------作業3--------")
q3ans = {"k0":"v0"}
a = {"k1":"v1"}
b = {"k2":"v2"}

print(a,b)


print("--------作業4--------")

list1 = [["a" , "b"] , ["c" , "d"]] 
print(list1[0][1])

print("--------作業5--------")


ans5 =0
for i in range(1,1025):
    ans5+=i
print(ans5)