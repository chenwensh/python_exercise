#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import tushare as ts
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Scatter
def show_scratter():
	x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
	y_cos = np.cos(x)
	y_sin = np.sin(x)

	plt.figure(figsize = (8, 6))
	plt.title("Scratter")
	plt.grid(True)

	plt.xlabel("x label")

	plt.ylabel("y label")

	plt.scatter(x, y_cos, marker = '.', color = 'blue', label = "cos", linewidth = 2.0)
	plt.scatter(x, y_sin, marker = '*', color = 'red', label = "sin", linewidth = 2.0)
	#set the x_start, x_end, y_start, y_end.
	#plt.axis([0, 10, 0, 10])
	
	plt.legend(loc = "upper right", shadow = True)
	plt.show()

#Line
def show_line():
	x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
	y_cos, y_sin = np.cos(x), np.sin(x)

	plt.figure(figsize = (8, 6), dpi = 80)
	plt.title("plot title")
	plt.grid(True)

	#Plot
	ax_1 = plt.subplot(111)
	ax_1.plot(x, y_cos, color = "blue", linewidth = 2.0, linestyle = "--", label = "cos in left")
	ax_1.legend(loc = "upper left", shadow = True)

	#Set the left Y axis
	ax_1.set_ylabel("y label for cos in left")
	ax_1.set_ylim(-1.0, 1.0)
	ax_1.set_yticks(np.linspace(-1, 1, 9, endpoint = True))

	#Plot
	ax_2 = ax_1.twinx()
	ax_2.plot(x, y_sin, color = "green", linewidth = 2.0, linestyle = "-", label = "sin in right")
	ax_2.legend(loc = "upper right", shadow = True)

	#Set the right Y axis
	ax_2.set_ylabel("y label for sin in right")
	ax_2.set_ylim(-2.0, 2.0)
	ax_2.set_yticks(np.linspace(-2, 2, 9, endpoint = True))

	ax_2.set_xlabel("x label")
	ax_2.set_xlim(-4.0, 4.0)
	ax_2.set_xticks(np.linspace(-4, 4, 9, endpoint = True))

	plt.show()

#Show 4 sub plots in single plot
def show_subplot_plot():
	#define the style of the plots. Defination: Color Sign -
	style_list = ["g+-", "r*-", "b.-", "yo-"]

	for num in range(4):
		x = np.linspace(0.0, 2 + num, num = 10 * (num + 1))
		y = np.sin((5 - num) * np.pi *x)

		#Define 2 cols and 2 rows
		plt.subplot(2, 2, num + 1)
		plt.plot(x, y, style_list[num])

	plt.grid(True)
	plt.show()

	return

#Show the bar plot
def show_bar_plot(oriation):
	means_men = np.linspace(30, 60, 5)
	means_women = np.linspace(20, 50, 5)
	means_total = list((means_men + means_women) / 2)

	index = np.arange(len(means_men))
	bar_width = 0.30
	bar_height = 0.30

	#draw vertical or horization bar plot
	if(oriation == 'h'):
		plt.barh(index, means_men, height = bar_height, alpha = 0.2, color = 'b', label = "Men")
		plt.barh(index + bar_height, means_women, height = bar_height, alpha = 0.8, color = 'r', label = "Women")
		plt.barh(index + 2 * bar_height, means_total, height = bar_height, alpha = 0.6, color = 'g', label = "Total")
		for x, y in zip(index, means_men):
			plt.text(y + 0.3, x + (bar_width / 2), y, ha = 'left', va = 'center')
		for x, y in zip(index, means_women):
			plt.text(y + 0.3, x + bar_width + (bar_width / 2), y, ha = 'left', va = 'center')
		for x, y in zip(index, means_total):
			plt.text(y + 0.3, x + 2 * bar_width + bar_width / 2, y, ha = 'left', va = 'center')		
		plt.xlim(0, 80)
		plt.ylabel('Group')
		plt.xlabel('Scores')
		plt.yticks(index + 3 / 2 * bar_width, ('A', 'B', 'C', 'D', 'E'))	
	else:
		plt.bar(index, means_men, width = bar_width, alpha = 0.2, color = 'b', label = "Men")
		plt.bar(index + bar_width, means_women, width = bar_width, alpha = 0.8, color = 'r', label = "Women")
		plt.bar(index + 2 * bar_width, means_total, width = bar_width, alpha = 0.6, color = 'g', label = "Total")
		for x, y in zip(index, means_men):
			plt.text(x + (bar_width / 2), y + 0.3, y, ha = 'center', va = 'bottom')
		for x, y in zip(index, means_women):
			plt.text(x + bar_width + (bar_width / 2), y + 0.3, y, ha = 'center', va = 'bottom')
		for x, y in zip(index, means_total):
			plt.text(x + 2 * bar_width + bar_width / 2, y + 0.3, y, ha = 'center', va = 'bottom')
		plt.ylim(0, 80)
		plt.xlabel('Group')
		plt.ylabel('Scores')
		plt.xticks(index + 3 / 2 * bar_width, ('A', 'B', 'C', 'D', 'E'))			
	plt.legend(loc = "upper right", shadow = True)

	plt.show()

	return

#Show the advanced bar plot
def show_advanced_bar_plot():
	means_men = np.linspace(30, 60, 5)
	means_women = np.linspace(20, 50, 5)
	
	index = np.arange(len(means_men))
	bar_width = 0.8

	#Define bar
	plt.bar(index, means_men, width = bar_width, alpha = 0.4, color = 'b', label = 'Men')
	plt.bar(index, -means_women, width = bar_width, alpha = 0.4, color = 'r', label = 'Women')

	#Define plot
	plt.plot(index + bar_width / 2, means_men, marker = 'o', linestyle = '-', color = 'r', label = 'Men Line')
	plt.plot(index + bar_width / 2, -means_women, marker = '.', linestyle = '--', color = 'b', label = 'Women line')

	#Define text
	for x, y in zip(index, means_men):
		plt.text(x + bar_width / 2, y + 1, y , ha = 'center', va = 'bottom')
	for x, y in zip(index, means_women):
		plt.text(x + bar_width / 2, -y - 1, y, ha ='center', va = 'top')
	
	plt.ylim(-80, 80)
	plt.legend(loc = 'upper left', shadow = True)
	plt.show()
	return

#Show the table plot
def show_table_plot():
	data = np.array([
		[1, 4, 2, 5, 2],
		[2, 1, 1, 3, 6],
		[5, 3, 6, 4, 1]
	])

	index = np.arange(len(data[0]))
	color_index = ['r', 'g', 'b']

	bottom = np.array([0, 0, 0, 0, 0])

	for i in range(len(data)):
		plt.bar(index + 0.25, data[i], width = 0.5, color = color_index[i], bottom = bottom, alpha = 0.7, label = 'label %d' %i)
		#Set the new bottom baseline for the next data[] row
		bottom += data[i]

	plt.legend(loc = 'upper right', shadow = True)

	plt.show()

	return

#Show the histograms plot
def show_histograms_plot():
	mu, sigma = 100, 15
	x = mu + sigma * np.random.randn(10000)

	num_bins = 50

	n, bins, patches = plt.hist(x, bins = num_bins, normed = 1, color = 'green', alpha = 0.6, label = 'hist')

	#Draw the curle line...
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y , 'r--', label = 'line')

	plt.legend(loc = 'upper right', shadow = True)

	plt.show()

	return

#Show the pie plot
def show_pie_plot():
	sizes = [15, 30, 45, 10]
	explode = [0, 0.05, 0, 0]
	labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

	plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)
	plt.axis('equal')

	plt.show()

	return

#Plot line of stock shanghai
def show_shstock_line():
	df = ts.get_hist_data('sh', start = '2016-01-01')
	df.to_excel('stock_sh.xlsx')
	df.close.plot()
	ax = plt.gca()
	ax.invert_xaxis()
	plt.show()

#Show multiple figures in one picture
def show_multiple_figures():
	fig = plt.figure()

	x = list(range(10, 90))
	y = list(np.sin(y) for y in x)

	p1 = fig.add_subplot(211)
	p1.plot(x, y)

	p2 = fig.add_subplot(212)
	p2.scatter(x, list(np.sin(y + np.random.randn()) for y in x))

	plt.show()

#Show two types figures in single picture
def show_two_in_single():
	x = np.linspace(0, 10, 1000)
	y = np.sin(x)
	z = np.cos(x**2)

	plt.figure(figsize = (8, 4))
	plt.plot(x, y, label = '$sin(x)$', color = "red", linewidth = 2)
	plt.plot(x, z, "b--", label = "$cos(x^2)$")
	plt.xlabel("Time(s)")
	plt.ylabel("Volt")
	plt.title('PyPlot First Example')
	plt.ylim(-1.2, 1.2)
	plt.legend()
	plt.show()

#3D
def show_3d():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	x = [1, 1, 2, 2]
	y = [3, 4, 4, 3]
	z = [1, 100, 1, 1]

	ax.plot_trisurf(x, y, z)
	plt.show()
	return

#Show the three dimension bar
def show_3d_bar():
    xpos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ypos = [2, 3, 4, 5, 1, 6, 2, 1, 7, 2]
    zpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    dx = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #Two kinds of draw
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    #ax = fig.add_subplot(111, projction = '3d')

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, alpha = 0.5)

    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    ax.set_zlabel('Z label')

    plt.show()
    return

if __name__ == "__main__":
	#show_pie_plot()
	#show_histograms_plot()
	#show_table_plot()
	#show_advanced_bar_plot()
	#show_bar_plot('h')
	#show_subplot_plot()
	#show_line()
	#show_scratter()
	#show_shstock_line()
	#show_multiple_figures()
	#show_two_in_single()
	#show_3d()
	show_3d_bar()