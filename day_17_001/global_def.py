a=10
strdata = 'Global Variable'

def funcl():
    strdata = 'Local Variable'
    a=5
    print (strdata)

def funcl2():
    global strdata
    strdata = 'GGlobal Variable'
    global a
    a= 50
    print (strdata)

funcl() # 지역변수 출력
print (a) # 10 출력 
funcl2()
print (a) # 전역변수 50으로 수정되어 표기됨.
