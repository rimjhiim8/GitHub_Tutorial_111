# for loop with continue
fruits=["apple","banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)    


#Go through all the numbers up until 99. Print ‘fizz’ for every number that’s divisible by 3, print ‘buzz’ for every number divisible by 5, and print ‘fizzbuzz’ for every number divisible by 3 and by 5! If the number is not divisible either by 3 or 5, print a dash (‘-‘)!

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbizz')
    elif:
        if i % 3 == 0:
            print('fizz')
    elif:
        if i % 5 == 0:
            print('buzz')
    else:
        print('-')  


# Python program to iterate over dictionaries using for loops.

d={"Red":1, "Green":2, "Blue":3}
for color_key, value in d.items():
    print(color_key + "corresponds to" + d[color_key])