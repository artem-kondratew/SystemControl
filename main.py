from control.matlab import *


w1 = tf(1, [3, 0])
w2 = 2
w3 = 3
w4 = tf(2, [1, 0])
w5 = 0.5
w6 = tf(3, [1, 0])

w13 = feedback(w1, w3)  # w13 = w1 / (1 - w1 * w3)
w45 = feedback(w4, w5)

w132 = series(w13, w2)
w456 = series(w45, w6)

w_v = 1 / w132
w132456 = series(w132, w456)

w45s = feedback(1, w45)

w_end = series(w45s, w132456)

w_s = feedback(w_end, 1)

W = series(w_v, w_s)
print(W)
