# write a programe to swap to numbers in lamda function

# def swap0(s1, s2):
#     assert type(s1) == list and type(s2) == list
#     tmp = s1[:]
#     s1 = s2[:]
#     s2 = tmp
#     return

# s1 = [1]
# s2 = [2]
# swap0(s1, s2)
# print (s1, s2)

# def swap0(s1, s2):
#     assert type(s1) == list and type(s2) == list
#     tmp = s1[:]
#     s1[:] = s2
#     s2[:] = tmp

a = lambda y: y
b = lambda x: x

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

result = a(y,x)
print("Sum is:", result)