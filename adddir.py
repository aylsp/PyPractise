# coding=utf-8
import os


def add_files(n):
    path = r'f:/programming'
    title = 'ping'
    new_title = os.path.join(path, title)
    if not os.path.isdir(new_title):
        os.mkdir(new_title)
    else:
        print('this dir has existed.')
        exit(-1);
    os.chdir(new_title)
    for i in range(100):
        file_name = 'ping' + str(i)
        # file=open(file_name,'w')
        # # file.write('XJTU')
        # file.writelines(['XJTU\n','SJTU\n','THU\n','PKU\n'])
        # file.close()
        with open(file_name, 'w') as file:
            file.writelines(['XJTU\n', 'SJTU\n', 'THU\n', 'PKU\n'])


if __name__ == '__main__':
    add_files(99)
    print('I succeed.')
