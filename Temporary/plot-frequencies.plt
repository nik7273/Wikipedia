set autoscale 
set border 3 
set ylabel 'Word Count'
set xr[0:60]
set xtics border in scale 1,0.5 nomirror rotate by -90 offset character 0, 0, 0
set xlabel 'Words'
unset key
plot "bash-frequencies" using 1:xticlabels(2) with histogram
set term postscript
set output 'frequencies.ps'
replot
set term x11