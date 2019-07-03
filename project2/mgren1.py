import PyGnuplot as gp 
import numpy as np 

gp.c('set terminal png size 1000,700 enhanced font "Helvetica,20"')
gp.c("set output 'output.png'")
gp.c('set title "Comparision between FSAM-IComP and MFSAM-IComP(m>n)";set xlabel "Number of users";set ylabel "Number of allocations"')
gp.c('set yrange [0:520]')
gp.c('set style fill pattern 2 border lt -1')
gp.c('set boxwidth 0.1')
gp.c("plot 'mfsam.txt' using ($0):3:xtic(1) with boxes title 'MFSAM-IComP', \
	''using ($0+0.1):4 with boxes title 'FSAM-IComP'")
#, \
#	''using ($0+0.2):2 with boxes title 'service providers'")