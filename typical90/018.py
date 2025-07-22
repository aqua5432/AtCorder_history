"""import math
import numpy as np
t = int(input()) #t <= 10^9
l, x, y = map(int, input().split()) # <= 10^9
q = int(input())
t1 = t // 4
t2 = t // 2
t3 = 3 * t // 4
position = [x, y]
for i in range(q): # q <= 1000
    e = int(input())
    lookpoint = 0
    lookposition = [0]
    if e <= t1:
        lookposition.append(-l*e//2//t1)
        lookpoint = (l*e//2//t1)
    elif e > t1 and e <= t2:
        lookposition.append(-l//2+l*e//2//t1)
        lookpoint = (l//2+l*e//2//t1)
    elif e > t2 and e <= t3:
        lookposition.append(l*e//2//t1)
        lookpoint = (l-l*e//2//t1)
    else:
        lookposition.append(l//2-l*e//2//t1)
        lookpoint = (l//2-l*e//2//t1)
    X = np.array(position)
    Y = np.array(lookposition)
    dist = np.linalg.norm(X-Y)
    print(math.atan2(dist, lookpoint))"""

import math

PI = 3.14159265358979

def query(I, T, L, X, Y):
    cx = 0
    cy = -(L / 2.0) * math.sin(I / T * 2.0 * PI)
    cz = (L / 2.0) - (L / 2.0) * math.cos(I / T * 2.0 * PI)
    d1 = math.sqrt((cx - X)**2 + (cy - Y)**2)
    d2 = cz
    kaku = math.atan2(d2, d1)
    return kaku * 180.0 / PI

def main():
    T = float(input())
    L, X, Y = map(float, input().split())
    Q = int(input())
    for _ in range(Q):
        E = float(input())
        angle = query(E, T, L, X, Y)
        print(f"{angle:.12f}")

if __name__ == "__main__":
    main()
