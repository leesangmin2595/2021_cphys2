import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

a=tf.constant([3,4,5])
b=tf.constant([6,7,8])

print(a+b) # 1,1 2,2 3,3 각각 더해짐

c=tf.constant([[1,2],
               [3,4]])

tf.add(a,b) # a+b를 해줌
tf.subtract(a,b) # a-b
tf.divide(a,b) # a/b
tf.multiply(a,b) # a*b
# 굳이 이렇게 안하고 print(a+b, a-b, a*b, a/b) 로도 가능
d=tf.constant([[1,2],
               [2,3]])

tf.matmul(c,d) # c와 d의 행렬곱 

e=tf.zeros(10) # 0이 10개인 텐서
print(e)
f=tf.zeros([2,2]) # 2x2의 0행렬
print(f)
g=tf.zeros([2,2,3]) # 3x2행렬을 2개 만든다는 뜻 (거꾸로해석)
print(g) 

a.shape # a의 shape을 출력

#int는 정수 float는 실수
w=tf.Variable(1.0) # weight를 만들려면 이걸로 해야함
print(w)
w.assign(2) # weight를 수정함
