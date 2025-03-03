from random import choice, randint
class perceptron():
    def __init__(self):
        self.w0 = 0
        self.w1 = 0
    f = lambda self, x1: self.w0+x1*self.w1>0
    def learning_step(self, x1, y):
        s = self.f(x1)
        if s!=y:
            if s==0:
                self.w0+=1
                self.w1+=x1
            else:
                self.w0-=1
                self.w1-=x1
    predict = lambda self, x: self.f(x)
q = perceptron()
for j in range(20000):
    i = 0.001*choice((1,-1))*randint(-4000, 20001)
    #print(i)
    if i>3.4:
        q.learning_step(i, 1)
    else:
        q.learning_step(i, 0)
n1, n2 = 0, 0
print(q.w0, q.w1)
for i in range(10001):
    p = choice((1,-1))*0.001*i
    n1 += q.predict(p)!=(p>3.4)
    n2+=1
print("Процент отклонений: ", n1/n2*100)
print(q.predict(3.41))
