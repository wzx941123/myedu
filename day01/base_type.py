def test1():
    print('test1')

def test2():
    print('test2')


def test3():
    print('test3')

def xiao():
    # 声明一个变量 = 前面的就是变量名 = 后面的就是变量值
    aint = 5
    # 打印
    # aint变量
    print(aint)


def str_demo():
    astr = '5'
    print(astr)
    print(type(astr))
def float_demo():
    afloat = 2.3
    print(afloat)
    print(type(afloat))
def add_demo(a,b):
    print(a+b)
def type_mo():
    aint = 8
    print(type(aint))
    print(type(str(aint)))
    print(type(int(aint)))
def str_join():
    a = 1314
    b = '我'
    c = 20
    print(str(a) + b + str(c) )
    print('a是%s b是%s c是%s'%(a,b,c))
def jianf_demo(a,b):
    c = a - b
    return c
if __name__ == '__main__':
    # test3()
    # test1()
    # test2()
    # xiao()
    # str_demo()
    # float_demo()
    # add_demo(4,5)
    # add_demo('小沫','好漂亮')
    # type_mo()
    # str_join()
    c = jianf_demo(8,3)

    d = add_demo(9, 3)
    print(c)
    print(d)
    print(type(d))

