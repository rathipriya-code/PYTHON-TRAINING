
'''PYTHON DATA STRUCTURES'''
List=[]#empty list
Tuple=()#empty tuple
set=()#empty set
dict={}#empty dict



#List
List=[67,76,89,88,0,99,2,1,5]
List.append(7)
List.extend([1,2,3])
List.insert(1,60)
List.pop(5)
List.remove(76)
del List[9]
print(List)
print(len(List))
print(List.count(99))
Nums=["even" if x%2==0 else "not even" for x in List ]#list comprehension
print(Nums)



#Tuple
Tuple=(10,20,30,40)
Result=sorted(Tuple,reverse=True)
print(Result)
print(min(Tuple))
print(max(Tuple))
print(sum(Tuple))
print(len(Tuple))
print(Tuple.index(30))
print(Tuple.count(40))
Num=tuple("greater than 10"if x>10 else "not greater than 10" for x in Tuple)#converting into tuple (comprehension by using generator)
print(Num)



#set
set={0,0,11,22,33,44,44,55,55,55}
set1={1,1,2,3,33,3,44,4,4,5}
set2={33,3,44,4,4,5}
set.add(100)
set.remove(11)
print(set,set1,set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1 | set2)#union symbol
print(set1 & set2)#intersection symbol
print(set1 - set2)#difference symbol
print(set1 ^ set2)#symmetric difference symbol
print(set1.issuperset(set2))
print(set2.issubset(set1))
print(sorted(set,reverse=False))



#dict
dict={"country 1":"India","city 1":"chennai", "country 2":"Japan","city 2":"Tokyo","country 3":"USA","city 3":"chicago"}
dict["country 4"]="China"
dict["city 4"]="Beijing"
print(dict)
values_list=list(dict.values())
keys_list=list(dict.keys())
print(values_list)
print(keys_list)
del dict["country 1"]
del dict["city 1"]
print(dict)
dict.popitem()
print(dict)
dict1={"India","USA","Japan","china"}
New_dict={x: len(x) for x in dict1}#dict comprehension
print(New_dict)



'''string and raw strings'''
filepath1="c:users\newrathipriya\desktop\txt.file"
print(filepath1)
filepath2=r"c:users\newrathipriya\desktop\txt.file"
print(filepath2)



''' strings operations'''
name="RathiPriya"
age=22
print("name is :",name,"\nage is :",age)
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and my age is %d" % (name,age))




'''for,while loops'''
for x in range(0,10):
    print(x)
for x in range(0,10,2):
    print(x)
numbers=[1,2,3,4]
for i,x in enumerate(numbers):
    print(i,x)
count=0
while(count<=10):
    print(count)
    count += 1
    
    
    
''''Error handling'''
try:
    x1=int(input("enter any num1:"))
    x2=int(input("enter any num2:"))
    division=x1/x2
    print("Division of two numbers is:",division)    
except ZeroDivisionError:
    print("It is zerdivisionerror , it cant divide by 0 ")
except:
    print("Except zerodivision error is occured")
    
try:
    with open("file.txt","r",encoding="utf-8")as f:
         f.read()
    print(f"successfully read file.txt")
except FileNotFoundError:
    print("your file is not existed")
except:
    print("The Error is not filenotfound error,something went wrong need to check")
    
'''File Handling'''
with open("file.txt","w",encoding="utf-8")as f:
    f.write("Hello\tworld!!")
with open("file.txt","r",encoding="utf-8")as f1:
    data=f1.read()
    print(data)
lines="This is line1\nThis is line2\nThis is line3"
with open("file1.txt","w",encoding="utf-8")as f2:
    f2.write(lines + "\n")
with open("file1.txt","r",encoding="utf-8")as f3:
    with open("file2.txt","w",encoding="utf-8")as f4:
        for lines in f3:
            f4.write(lines)
            
            
            
'''Pandas'''

import pandas as pd
import json
with open("file.json","r",encoding="utf-8")as file:
    data=json.load(file)
df=pd.DataFrame(data)
df.to_csv("file.csv", index=False)
df1=pd.read_csv("file.csv")
filter_columns=df1[["Name","Age"]]
filter_columns.to_csv("filter_columns.csv",index=False)
data1={"name":"rathi","age":22}
data2={"name":["priya","rathi","priyanka","shivanya"],"age":[22,23,22,24]}
df1=pd.Series(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)