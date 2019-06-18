import PyGnuplot as gp
import numpy as np

gp.c('set style fill transparent solid 0.5 noborder')
gp.c('set title "Result";set xlabel "x-axis";set ylabel "y-axis"')
gp.c('set yrange [0:1500];set key center top')
gp.c('set xrange [10:100];set key center top')
gp.c('set style fill transparent solid 0.5 noborder')
gp.c('set title "Result";set xlabel "number of tasks";set ylabel "Utility of IOT devices"')
gp.c("plot 'utility_random.txt' using 1:($2) with linespoints lc 10 lw 2 title 'utility random")
gp.c("replot 'utility_random.txt' using 1:($2) with linespoints lc 19 lw 2 title 'utility 1")
gp.c("replot 'utility_random.txt' using 1:($3) with linespoints lc 19 lw 2 title 'utility 2")
gp.c("replot 'utility_random.txt' using 1:($4) with linespoints lc 19 lw 2 title 'utility 3")
gp.c("replot 'utility_random.txt' using 1:($5) with linespoints lc 19 lw 2 title 'utility 4")
gp.c("replot 'utility_random.txt using 1:($4):($5) with filledcurves lc 3 fs transparent solid 0.5")