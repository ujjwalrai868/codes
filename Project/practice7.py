import PyGnuplot as gp 
import numpy as np 

gp.c('set xrange [-0.5:12.75]')
gp.c('set xtic rotate by 0')
gp.c('set boxwidth 0.25')
gp.c('set style fill pattern 2 border lt -1')
gp.c("plot 'file.dat' using ($0):4:5 with boxerrorbars title col, ''using ($0+0.25):2:3 with boxerrorbars title col")

