import PyGnuplot as gp
import numpy as np

#gp.c("set terminal png size 400,300; set output 'xyz.png'")
gp.c('set grid')
gp.c('set style fill transparent solid 0.5 noborder')
gp.c('set title "Result";set xlabel "x-axis";set ylabel "y-axis"')
gp.c('set yrange [0:6000];set key center top')
gp.c('set xrange [10:100];set key center top')
gp.c("set style fill patter 2 border")
gp.c("plot 'feasible_budget.txt' using 1:($2):($4) with filledcurves lc 7 title 'Region 1")
gp.c("replot 'feasible_budget.txt' using 1:($3):($4) with filledcurves lc 3 title 'Region 2")
#gp.c("plot 'budgetfm.py' using 1:$2:$3 with filledcurves lc 10 title 'region 1")
gp.c("replot 'feasible_budget.txt' using 1:($2) with linespoints lc 18 lw 2 title 'Random")
gp.c("replot 'feasible_budget.txt' using 1:($3) with linespoints lc 15 lw 2 title 'Budget")
gp.c("replot 'feasible_budget.txt' using 1:($4) with linespoints lc 25 lw 2 title 'Greedya")
gp.c("replot 'feasible_budget.txt' using 1:($5) with linespoints lc 12 lw 2 title 'utility")

