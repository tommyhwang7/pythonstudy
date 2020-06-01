#문자 슬라이싱

jumin = "820307-1234567"
print ("jendor:" + jumin[7])
print ("year : " + jumin[0:2]) # 0부터 2 직전까지
print ("month : "+ jumin[2:4]) # 2부터 4직전까지

#문자열 처리 함수

python = "Python is Amazing"
print (python.lower()) # 소문자 변환
print (python.upper()) # 대문자 변환
print (python[0].isupper()) # python 0번째 가 대문자 이면 true
print (len(python)) # 문자 길이 출력
print (python.replace("Python","java")) #Python 을 찾아서 java로 변환

index = python.index("n") # n이란 글자가 몇번째 있는지
print (index)
index = python.index("n", index + 1) # 5란을 위치에서 1나를 더한 (2번째n)
print (index)

print (python.find("n")) #원한는 문자 포함되어있는 위치
print (python.find("Java")) #find는 원하는 문자가 없을시 '-1'을소환 , 프로그램은 돌아감
#print (python.index("Java")) #index는 원하는 문자가 없을때는 종료됨
print (python.count('n')) # n이란 문자가 몇번 나오는지