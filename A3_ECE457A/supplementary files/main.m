
%Reference: https://www.youtube.com/watch?v=cKXQS5bOQ1U&ab_channel=AlvinAlexander
%Stage 1:
% clear 
% 
% format shortG; 
% [x, fval] = ga(@perfFCN, 3, [], [], [], [], [2.01 1.06 0.27], [17.99 9.41 2.36])

%Limitations:We want to figure out how to customize the options 

%Stage 2: 

%Original

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
    'CrossoverFraction', 0.6,... %60% of remaining is crossovered
    'CrossoverFcn', @crossoverarithmetic,...   %using arithmetic because this is Real-valued GAS
    'MutationFcn', {@mutationadaptfeasible, 0.25},... %algorithm selects a fraction of the vector entries of an individual for mutation, where each entry has a probability rate of being mutated
    'MaxGeneration', 150); %max no of generations

[x, fval] = ga(@perfFCN, 3, [], [], [], [], [2.01 1.06 0.27], [17.99 9.41 2.36], [], opts)


%question e - less than the original generations 
%suppose g = 20

% clear
% format shortG; 
% rng default; 
% opts = optimoptions('ga',...
%     'PlotFcn', {@gaplotbestf},... %settng visualization to plot best and min fitness every generation
%     'Display', 'final',...
%     'PopulationSize', 50,... %setting the population size
%     'CreationFcn', @gacreationuniform,... %creating the initia population using uniform distribution 
%     'SelectionFcn', @selectionroulette,... %using FPS parent selection strategy
%     'FitnessScalingFcn', @fitscalingrank,...
%     'EliteCount', 2,...      %2 elite individuals carried over to the next generation
%     'CrossoverFraction', 0.6,... %60% of remaining is crossovered
%     'CrossoverFcn', @crossoverarithmetic,...   %using arithmetic because this is Real-valued GAS
%     'MutationFcn', {@mutationadaptfeasible, 0.25},... %algorithm selects a fraction of the vector entries of an individual for mutation, where each entry has a probability rate of being mutated
%     'MaxGeneration', 20); %max no of generations
% 
% [x, fval] = ga(@perfFCN, 3, [], [], [], [], [2.01 1.06 0.27], [17.99 9.41 2.36], [], opts)

%question e - greater than the original generations 
%suppose g = 300

% clear
% format shortG; 
% rng default; 
% opts = optimoptions('ga',...
%     'PlotFcn', {@gaplotbestf},... %settng visualization to plot best and min fitness every generation
%     'Display', 'final',...
%     'PopulationSize', 50,... %setting the population size
%     'CreationFcn', @gacreationuniform,... %creating the initia population using uniform distribution 
%     'SelectionFcn', @selectionroulette,... %using FPS parent selection strategy
%     'FitnessScalingFcn', @fitscalingrank,...
%     'EliteCount', 2,...      %2 elite individuals carried over to the next generation
%     'CrossoverFraction', 0.6,... %60% of remaining is crossovered
%     'CrossoverFcn', @crossoverarithmetic,...   %using arithmetic because this is Real-valued GAS
%     'MutationFcn', {@mutationadaptfeasible, 0.25},... %algorithm selects a fraction of the vector entries of an individual for mutation, where each entry has a probability rate of being mutated
%     'MaxGeneration', 300); %max no of generations
% 
% [x, fval] = ga(@perfFCN, 3, [], [], [], [], [2.01 1.06 0.27], [17.99 9.41 2.36], [], opts)

%question f - greater than the original population 
%suppose p = 100

% clear
% format shortG; 
% rng default; 
% opts = optimoptions('ga',...
%     'PlotFcn', {@gaplotbestf},... %settng visualization to plot best and min fitness every generation
%     'Display', 'final',...
%     'PopulationSize', 200,... %setting the population size
%     'CreationFcn', @gacreationuniform,... %creating the initia population using uniform distribution 
%     'SelectionFcn', @selectionroulette,... %using FPS parent selection strategy
%     'FitnessScalingFcn', @fitscalingrank,...
%     'EliteCount', 2,...      %2 elite individuals carried over to the next generation
%     'CrossoverFraction', 0.6,... %60% of remaining is crossovered
%     'CrossoverFcn', @crossoverarithmetic,...   %using arithmetic because this is Real-valued GAS
%     'MutationFcn', {@mutationadaptfeasible, 0.25},... %algorithm selects a fraction of the vector entries of an individual for mutation, where each entry has a probability rate of being mutated
%     'MaxGeneration', 150); %max no of generations
% 
% [x, fval] = ga(@perfFCN, 3, [], [], [], [], [2.01 1.06 0.27], [17.99 9.41 2.36], [], opts)

%Why use mutation adaptable feasible? 
%Do not use mutationuniform when you have bounds or linear constraints. Otherwise, your population will not necessarily satisfy the constraints. Instead, use 'mutationadaptfeasible' or a
%custom mutation function that satisfies linear constraints.