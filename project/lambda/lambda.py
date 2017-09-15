pairs = [(1,'a'),(2,'c'),(3,'b'),(4,'g'),(5,'e'),(6,'f')]

pairs.sort(key= lambda pair:pair[1],reverse=False)

print(pairs)


#文档字符串

def my_function():
    '''
    自定义文档
    暂用pass占位
    '''
    pass

print(my_function.__doc__)