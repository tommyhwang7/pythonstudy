class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

#print(cal1.add(3))
#print(cal1.add(4))
#print(cal2.add(3))
#print(cal2.add(7))


class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result



a= FourCal()
b= FourCal()

a.setdata(4,2)
b.setdata(3,7)

print (a.add())
print (a.mul())
print (a.sub())
print (a.div())