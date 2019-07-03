import PyGnuplot as gp 
import numpy as np 

gp.c('set terminal png size 1100,700 enhanced font "Helvetica,20"')
gp.c("set output 'wbp.png'")
gp.c('set title "Comparision between with base price and without base price in econ scheduling";set xlabel "Number of CPU";set ylabel "Minimum Price(in Rs)"')
gp.c('set yrange [0:28000]')
gp.c('set style fill pattern 2 border lt -1')
gp.c('set boxwidth 0.1')
gp.c("plot 'wbp.txt' using ($0):2:xtic(1) with boxes title 'Without base price', \
	''using ($0+0.1):3 with boxes title 'With base price'")
