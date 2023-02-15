from control import *


w1 = tf(1, [3, 0])
w2 = 2
w3 = 3
w4 = tf(2, [1, 0])
w5 = 0.5
w6 = tf(3, [1, 0])

w13 = feedback(w1, w3)
w45 = feedback(w4, w5)

w132 = series(w13, w2)
w456 = series(w45, w6)

w_v = 1 / w132

w16 = series(w132, w456)

w1324 = series(w4, w132)

w14 = feedback(1, w4132)

w46 = series(w14, w16)

w_e = feedback(w46, 1)

W = series(w_v, w_p)
print(W)
