import matplotlib.pyplot as pyp
import matplotlib.animation as animation

figure = pyp.figure()

subplot = figure.add_subplot(1, 1, 1)

def animation_function(i):

    cpu_data = open('C:\\Users\\e296631\\Desktop\\Python\\cpu.txt').readlines()

    x = []

    for each_value in cpu_data:
        if len(each_value) > 1:
            x.append(float(each_value))

    subplot.clear()

    subplot.plot(x)

graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)

pyp.show
