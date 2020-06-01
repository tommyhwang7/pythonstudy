import turtle

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

turtle.done()




