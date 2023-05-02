with open("primenum.txt", "w") as f:
    for num in range(1, 50):
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            f.write(str(num)+",")

# with open("primenum.txt", "r") as f:
#     print(f.readline())
#     print("-----")
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#


# s = set();
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(1)
# print(s)

# s = list();
# s.append(1)
# s.append(2)
# s.append(3)
# s.append(1)
# print(s)
# print(s.index(1,3))
# # s.remove(1)
# # s.pop()
# print(s.count(1))
# s.
#
# print(s)

# l = {1,2,3,4,5,3,4,5,0,1}
# print(set(l))

def listcom():
    lcpmp = [x.upper() for x in 'python']


listcom()
# lcpmp = [x+x for x in range(1,10)]
# lcpmp = [x+2 for x in range(1,10) if x%2 == 0]
# print(lcpmp)

# def newunique (list_arg):
#     list_set=set(list_arg)
#     unique_list=(list(list_set))
#     for x in unique_list:
#         print (x);
#
#
# list1= [10, 20, 10, 30, 40, 40]
# print("the unique values from 1st list is")
# newunique(list1)
