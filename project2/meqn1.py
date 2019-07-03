import PyGnuplot as gp 
import numpy as np 

gp.c('set terminal png size 800,500 enhanced font "Helvetica,20"')
gp.c("set output 'output5.png'")
gp.c('set title "Comparision between DRAW and MFSAM-IComP(m=n)";set xlabel "Number of users";set ylabel "Number of allocations"')
gp.c('set yrange [0:500]')
gp.c('set xrange [0:520]')
gp.c("plot 'mfsam1.txt' using 1:3 w l lw 2 t 'MFSAM-IComP', \'' using 1:4 w l lw 2 t 'DRAW'")
