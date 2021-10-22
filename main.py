# for num in range(100,200):
#     if all(num%i!=0 for i in range(2,num)):
#         print(num)
#
# l = [1, 23, 56, 100, 22, 3, 7, 39]
# l.sort(reverse = True)
# print(l)
#
# task 3
# list1 = [1, 23, 56, 100, 22, 3, 7, 39]
# new_list = []
#
# while list1:
#     minimum= list1[0]
#     for x in list1:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     list1.remove(minimum)
#
# print(new_list)

# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-2) + f(n-1)
#
#
# for i in range(0,20):
#     print(f(i))

list1 = [1, 23, 56, 100, 22, 3, 7, 39]
print(list1[::-1])

print(list1[:])