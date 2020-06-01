import turtle 

myTurtle = turtle.Turtle()


myTurtle.shape ('turtle')



myTurtle.setposition(100,0) # turtle 위치를 좌표 x,y로 바꿔줌
myTurtle.setposition(100,100)
myTurtle.setposition(0,100)
myTurtle.setposition(0,0) # 포지션으로 직사각형 만들기

#myTurtle.pos() # turtle 현제 위치
print (myTurtle.pos()) # turtle 위치 

turtle.done()

'''
for i in range(4) :
    t.forward(100)
    t.left(90)

t.forward(100)
#t.hideturtle() # turtle 숨김
t.home() # tutle 초기 위치로 옮김
t.clear() # 화면을 초기 상태로 


myTurtle = turtle.Turtle() # 객체선언
myTurtle.fillcolor('red') # 색
myTurtle.shape('turtle') # 객체 타입
myTurtle.shapesize(3,3,1) # 세로w, 가로 h, 윤곽선 b배
myTurtle.forward(100) # 앞으로 100픽셀
myTurtle.left(120) # left 각도 변경
myTurtle.forward(100) 
myTurtle.left(120)
myTurtle.forward(100) 
myTurtle.left(120)
#myTurtle.backward(50) # 뒤로 50 픽셀
#myTurtle.setheading(90) # 원점기준 지정각도 변경
#myTurtle.left(90)
#myTurtle.right(180) # right 각도 변경
'''







