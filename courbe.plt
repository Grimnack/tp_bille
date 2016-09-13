set title ""
set xlabel "Nombre de particules"
set ylabel "Temps d'éxécution (secondes) "

plot "courbe.txt" using 1:2  with linespoints lt rgb "red" title ''