set autoscale 
set border 3 
set title 'Frequencies of Words from the Wikipedia Article on Heart Attack'
set ylabel 'Word Count'
set xr[0:30]
set xtics border in scale 1,0.5 nomirror rotate by -90 offset character 0, 0, 0
set xlabel 'Words'
unset key
plot "bash-frequencies" using 1:xticlabels(2) with lines
set term postscript
set output 'frequencies.ps'
replot
set term png
set output 'frequencies.png'
replot
set term x11
