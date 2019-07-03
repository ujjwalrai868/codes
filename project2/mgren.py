import PyGnuplot as gp 
import numpy as np 

gp.c('set terminal png size 900,600 enhanced font "Helvetica,20"')
gp.c("set output 'output7.png'")
gp.c('set title "Comparision between FSAM-IComP and MFSAM-IComP(m<n)";set xlabel "Number of users";set ylabel "Number of allocations"')
gp.c('set yrange [0:500]')
gp.c('set xrange [0:520]')
gp.c("plot 'partdraw2.txt' using 1:3 w l lw 2 t 'FSAM-IComP', \'' using 1:4 w l lw 2 t 'MFSAM-IComP'")
#gp.c("replot 'mfsam.txt' u 1:3 w l t 'mfsam'")
'''gp.c("replot 'normal.txt' u 1:2 w l t 'Payment normal")
gp.c("replot 'bid_sum.txt' u 1:2 w l t 'bid_sum" )'''
