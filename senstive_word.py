# -*- coding: utf-8 -*-

def wordJudge(input):
    file = open(r'/f/programming/PyPractise/test_files/filter_word.txt', 'r')
    # list = []
    # for line in file:
    #     list.append(line)
    # file.close()
    # if (input + '\n') in list:
    #     return True
    # else:
    #     return False

    for line in file:
    	if(line == input+'\n'):
    		return True
    return False

if __name__ == '__main__':
    print ('Please enter the word:')
    input = input()
    if (wordJudge(input)):
        print ('Freedom')
    else:
        print ('Human Rights')