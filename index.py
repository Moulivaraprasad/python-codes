print("1.Print numbers from 1 to 10 using a loop.")
for i in range(1,11):
    print(i)
print("--------------------------------------------------------------------------------------------------------------------")
print("2.Print all even numbers between 1 and 20.")
for j in range(2,21,2):
    print(j)
print("--------------------------------------------------------------------------------------------------------------------")
print("3.Print the characters of the string"+" Python"+" one by one using a loop.")
for k in "python":
    print(k)
print("--------------------------------------------------------------------------------------------------------------------")
print("4.Print the sum of numbers from 1 to 100.")
sum =0
for l in range(1,101):
    sum+=l
print(sum)
print("--------------------------------------------------------------------------------------------------------------------")
print("5.Print multiplication table of 5 (like 5 x 1 = 5, ... 5 x 10 = 50).")
for m in range(1,11):
    print(f'5*{m}={5*m}')
print("--------------------------------------------------------------------------------------------------------------------")
list = ["apple", "banana", "cherry"]
print("6.Print all elements of a list using a loop. List: ["+"apple"+", "+"banana"+"," +"cherry"+"]")
for n in list:
    print(n) 
print("--------------------------------------------------------------------------------------------------------------------")
print("7.Print only the vowels from the string "+" education" +" using a loop.")
for o in "education":
    if o in "aeiou":
        print(o)
count = 0
print("--------------------------------------------------------------------------------------------------------------------")
print("8.Count how many times the letter 'a' appears in the string "+" banana" +" using a loop.")
for p in "banana":
    if(p=="a"):
        count+=1
print(count)
print("---------------------------------------------------------------------------------------------------------------")
print("9.Print numbers from 10 to 1 using a loop (reverse order).")
for q in range(10,0,-1):
    print(q)
num = 5
add = 0
print("--------------------------------------------------------------------------------------------------------------------")
print("10.Ask the user to enter 5 numbers using a loop and print their sum.")
for r in range(5):
    r=int(input("enter a number"))
    add+=r
print(add)
