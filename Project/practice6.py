import PyGnuplot as gp 
import numpy as np 

#gp.c("set terminal png size 3000,3000; set output 'boxerrorbars.png'")
gp.c('set yrange [0:10000]')
gp.c('set xrange [0:110]')
gp.c('set xrange [-0.5:12.75]')
gp.c('set xtic rotate by 0')
gp.c('set boxwidth 0.4')
gp.c('set style fill pattern 6 border lt 8')
#gp.c("plot 'budgetfm.txt' using ($0):2:4:xtic(1) with boxerrorbars title col, ''using ($0+0.4):3:4:xtic(1) with boxerrorbars title col")
gp.c("plot 'budgetfm.txt' using ($0):2:3:xtic(1) with boxerrorbars title col")
gp.c("replot 'budgetfm.txt' using ($0+0.4):3:4 with boxerrorbars title col")
#gp.c("plot 'file.dat' using ($0):4:5 with boxerrorbars title col, ''using ($0+0.25):2:3 with boxerrorbars title col")
