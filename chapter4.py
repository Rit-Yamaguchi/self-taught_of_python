#1
def squared():
    """
    入力した値を２乗して返します
    """
    n = input("type a number")
    n = int(n)
    print(n**2)
squared()

#2
def string():
    """
    入力された文字列を返します
    """
    n = input("type strings")
    n = str(n)
    print(n)
string()

#3
def cul(a = 2, b = 3):
    """
    3つの変数を入力するとあらかじめ定義された2つの変数と合わせて5つの数値の合計を返します
    """
    c = input("define c ")
    c = int(c)
    d = input("define d ")
    d = int(d)
    e = input("define e ")
    e = int(e)
    print("total from a to e is")
    print(a+b+c+d+e)
cul()

#4
def second():
    """
    与えられた数値を2で割ります
    割った値に4をかけます
    """
    a = input("define a")
    a = int(a)
    b = a // 2
    print("b is defined as")
    print(b)
    c = b * 4
    c = int(c)
    print("and c is defined as")
    print(c)
second()

#5
def judge():
    """
    与えられた数値をfloat型で返します
    入力されたものが数値でない場合、数値を入力する旨を伝えます
    """
    try:
        n = input("type something")
        n = float(n)
        print(n)
    except(ValueError):
        print ("strings are not accepted")
judge()
