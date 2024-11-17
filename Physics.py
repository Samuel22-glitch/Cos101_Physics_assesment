def area_of_circle():
    radius = float(input('Enter radius'))
    area = 2 * 22/7 * radius
    print(area)

#area_of_circle()

def calculate_velocity():
    distance = float(input('Enter your distance: '))
    time = int(input('Enter your time: '))
    velocity = distance/time
    print(velocity)
#calculate_velocity()

print ('Welcome to physics 101')
topic = input('We have the best way of answering question under the topic: Dimension of Physical Quantity')


print ('we provide simple and adequate answer on whatever equation writen on the topic Physical Quantity')
print ('We have formulae on the topic Physical Quantities')
print('(a) calculate Power')
print('(b) calculate Newton second law')
print('(c) calculate Weight')
print('(d) calculate Pressure')
print('(e) calculate Impulse')


def a():
    work = float(input('Enter your work'))
    time = int(input('Enter your time'))
    a = work/time
    print(a)


def b():
    mass = float(input('Enter your mass'))
    acceleration = int(input('Enter your acceleration'))
    b = mass * acceleration
    print(b)


def c():
    mass = float(input('Enter your mass'))
    gravity = int(input('Enter your gravity'))
    c = mass * gravity
    print(c)


def d():
    force = float(input('Enter your force'))
    area = int(input('Enter your area'))
    d = force / area
    print(d)


def e():
    force = float(input('Enter your force'))
    time = int(input('Enter your time'))
    e = force * time
    print(e)

def main():
    choice = input("Choose option")

    if choice == "a":
        a()

    if choice == "b":
        b()

    if choice == "c":
        c()

    if choice == "d":
        d()

    if choice == "e":
        e()


if __name__ == '__main__':
    main()




