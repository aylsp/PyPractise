# coding=utf-8


files = open('f:\\programming\\PyPractise\\test_files\\filter_word2.txt')
get_line = files.readline()
# file_word=get_line.split('\n')[0]
file_word = get_line.split()
print file_word
print 'Please enter a sentence:'
sens_input = raw_input()
for i in file_word:
    print i
    # print sens_input.find(i)
    if (sens_input.find(i) > 1):
        # print sens_input.split(i)[0]
        # sens_input
        # sens_input.split(i)
        sens_input = sens_input.split(i)[0] + '**' + sens_input.split(i)[1]
print sens_input
