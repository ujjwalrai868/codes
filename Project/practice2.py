import PyGnuplot as gp 
import numpy as np 

gp.c('set title "Result";set xlabel "x-axis";set ylabel "y-axis"')
gp.c('set yrange [0:6000]')
gp.c('set xrange [10:100]')
gp.c("plot 'total_budget.txt' u 1:2 w l t 'Budget")
gp.c("replot 'normal.txt' u 1:2 w l t 'Payment normal")
gp.c("replot 'bid_sum.txt' u 1:2 w l t 'bid_sum" )
