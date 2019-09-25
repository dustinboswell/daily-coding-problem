'''
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.

Answer:
    sample points uniformly in a square of radius 1.  Then test if the point is inside the circle.
    The fraction of time this happens should be = pi / 4.  So estimate pi as 4 * probability.
'''
import random

num_inside = 0
num_samples = 0
for i in range(1000*100*1000):
    x = (random.random() * 2) - 1
    y = (random.random() * 2) - 1
    num_samples += 1
    if x*x + y*y <= 1:
        num_inside += 1

print(f"Estimate of PI is {4*num_inside/num_samples}")
