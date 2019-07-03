import PyGnuplot as gp 
import numpy as np 

gp.c('set terminal png size 1100,700 enhanced font "Helvetica,20"')
gp.c("set output 'comparison.png'")
gp.c('set title "Comparison between Greedy,our algorithm and econ scheduling";set xlabel "Number of CPU required";set ylabel "number of allocations among 1000 requests"')
gp.c('set yrange [0:800]')
gp.c('set style fill pattern 2 border lt -1')
gp.c('set boxwidth 0.1')
gp.c("plot 'comparison.txt' using ($0):2:xtic(1) with boxes title 'Greedy', \
	''using ($0+0.1):3 with boxes title 'our algo', \
	''using ($0+0.2):4 with boxes title 'econ scheduling'")
