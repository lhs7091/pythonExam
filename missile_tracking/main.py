import math
from math import pow, ceil
from matplotlib import pyplot as plt

GRAVITY = 9.81 # m/s^2
INTERVAL = 0.001

'''
define the Time variation per step
'''
def timeArray(start, end, step):
    times = []
    while start < end:
        times.append(start)
        start += step
    return times


'''
drawing graph
'''
def draw_parabola(xVelocity, yVelocity):
    flyTime = 2*yVelocity/GRAVITY
    flyDistance = xVelocity*flyTime
    intervals = timeArray(0, flyTime, INTERVAL)
    x = []
    y = []

    for t in intervals:
        x.append(xVelocity*t)
        y.append((yVelocity*t)-(0.5*GRAVITY*math.pow(t,2)))

    plt.plot(x,y)
    plt.xlabel('x Vector {}(m/s)'.format(xVelocity))
    plt.ylabel('y Vector {}(m/s)'.format(yVelocity))
    plt.title('Fly Time {}(sec), Distance {}m'.format(math.ceil(flyTime), math.ceil(flyDistance)))



if __name__ == '__main__':
    try:
        # input velocity of x vector
        xVelocity = float(input('Enter the x vector velocity(m/s): '))
        # input velocity of y vector
        yVelocity = float(input('Enter the y vector velocity(m/s): '))
    except ValueError:
        print('You Entered an invalid values')
    else:
        draw_parabola(xVelocity, yVelocity)
        plt.show()