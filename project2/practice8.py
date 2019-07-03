import PyGnuplot as gp 
import numpy as np 

gp.c('set terminal png size 800,500 enhanced font "Helvetica,20"')
gp.c("set output 'output.png'")
#gp.c('red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB""');
gp.c('set yrange [0:20]')
gp.c('set style data histogram')
gp.c('set style histogram cluster gap 1')
gp.c('set style fill solid')
gp.c('set boxwidth 0.9')
gp.c('set xtics format ""')
gp.c('set grid ytics')
gp.c('set title "A Sample Bar Chart"')
gp.c("plot 'bar.dat' using 2:xtic(1) title 'Dan', \'' using 3 title 'Sophia'")