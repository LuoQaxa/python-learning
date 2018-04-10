# 问题：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# use on a file


if __name__ == '__main__':
    with open('01.txt', 'r') as f:
        print(f)
        for line, prevline in search(f, 'python', 5):
            for pline in prevline:
                print(pline, end='')
            print(line, end='')
            print('-', *20)


# 总结
# 1. collections集合中的deque也就是double queue，双向管道，在数据量大的时候效率更高
# 2. with open('') as f, 这是一种文件操作的方法，读写文件涉及到操作系统的直接操作磁盘，
# 但是现代的操作系统不允许普通的程序直接操作磁盘，所以读写文件就是请求操作系统打开一个文件对象（文件描述符）
# 然后通过操作系统提供的接口从这个文件对象中读取数据，或者写入这个对象。
# 如果文件打开成功后，可以read 一次性读取文件的内容，python把内容读到内存，用一个str对象表示，
# 最后一步调用close方法关闭文件，文件使用完毕后必须关闭，因为文件对象会占有操作系统的资源，并且操作系统同一时间打开的文件数量也是有限的
# with语句的作用是： 文件读写很有可能产生ioerror，出错后，后面的close将不会被调用，为了保证能正确的关闭文件，可以使用tryfinally来
# 实现，但是这样写很繁琐，既然不管什么情况下都需要close，python就引入了with语句来自动调用close方法
# https://www.cnblogs.com/ymjyqsx/p/6554817.html（文件读写操作）
# 3. __name__ = __main__ 这是什么意思？https://www.zhihu.com/question/49136398
# 简单来说模块被直接执行 __name__ 就等于 __main__ 
