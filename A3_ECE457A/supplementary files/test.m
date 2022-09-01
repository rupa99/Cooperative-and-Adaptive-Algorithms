clear 

format shortG; 
[x, fval] = ga(@covid, 2, [], [], [], [], [5000 1000], [50000 10000])

%[x, fval] = ga(@covid, 2)