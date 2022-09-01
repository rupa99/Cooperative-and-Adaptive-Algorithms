%using crossover prob 0.9 - more than the original

clear
format shortG; 
rng default; 
opts = optimoptions('ga',...
    'PlotFcn', {@gaplotbestf},... %settng visualization to plot best and min fitness every generation
    'Display', 'final',...
    'PopulationSize', 50,... %setting the population size
    'CreationFcn', @gacreationuniform,... %creating the initia population using uniform distribution 
    'SelectionFcn', @selectionroulette,... %using FPS parent selection strategy
    'FitnessScalingFcn', @fitscalingrank,...
    'EliteCount', 2,...      %2 elite individuals carried over to the next generation
    'CrossoverFraction', 0.9,... %60% of remaining is crossovered
    'CrossoverFcn', @crossoverarithmetic,...   %using arithmetic because this is Real-valued GAS
    'MutationFcn', {@mutationadaptfeasible, 0.25},... %algorithm selects a fraction of the vector entries of an individual for mutation, where each entry has a probability rate of being mutated
    'MaxGeneration', 150); %max no of generations

[x, fval] = ga(@perfFCN, 3, [], [], [], [], [2.01 1.06 0.27], [17.99 9.41 2.36], [], opts)