# coding=utf-8

test_file = open(r'C:\Users\ping\Desktop\prepare.txt')
context = test_file.read()
context_list = context.split(' ')
# print context_list
context_dict = {}
for i in context_list:
    context_dict[i] = 0
for j in context_list:
    context_dict[j] += 1
for k, n in context_dict.items():
    print k + ' ' + str(n)
