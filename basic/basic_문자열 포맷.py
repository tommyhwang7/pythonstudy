#문자열 포맷

#방법1
print ("I am %d years old" %7 ) # %d는 정수
print ('I love %s' %"python" ) # %s 는 문자열 스트링
print ('Apple is starting %c' %"A") # %s는 한문자

print ("I am %s years old" %7 ) # %s로 다쓸수 있다.

print ('I love %s and %s'%('blue','red')) #2개를 쓸려고 할때

#방법2

print ('i am {}years old'.format(20)) #format으로 쓸수있음.
print ('I love {} and {}'.format('blue','red'))
print ('I love {0} and {1}'.format('blue','red')) #숫자의 위치로 선택가능
print ('I love {1} and {0}'.format('blue','red')) #숫자의 위치로 선택가능

#방법3
print ('I love {age} and {color}'.format(age=20,color='red')) #변수로 위치 선정가능