def hello_world(words):
    size = max(len(word) for word in words)
    print("*"*(size+4))

    for i in words:
        print("*"+" "+i+" "*((size+4)-len(i)-3)+"*")

    print("*"*(size+4))

hello_world(["Hello","world","in","a","frame"])
print(2**3 + (5 + 6)**(1 + 1))
a = 3
b = 1 
print(a, b)
a, b = b, a 
print(a, b)

numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
odd_numbers = [x for x in sorted_numbers if x % 2 != 0]
print(odd_numbers)

def tester(*argv):
       for arg in argv:
        print(arg, end = ' ')
tester('Sunday', 'Monday', 'Tuesday', 'Wednesday')

def tester(**kwargs):
       for key, value in kwargs.items():
        print(key, value, end = " ")
tester(Sunday = 1, Monday = 2, Tuesday = 3, Wednesday = 4)

s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 6}
print(s1 ^ s2)

