%fun = @(x)x(1)*exp(-norm(x)^2);

%fun = @[4 - (2.1 * x^2) + (x^4)/3] * x^2 + x*x(1) + (-4 + 4*x(1)^2) * x(1)^2
fun = @equation;

lb = [-5,-5];
ub = [5,5];

rng default  % For reproducibility
nvars = 2;

options = optimoptions('particleswarm','SwarmSize',100,'MaxIterations', 10000, 'PlotFcn', @pswplotbestf);

[x,fval,exitflag,output] = particleswarm(fun,nvars,lb,ub, options)

%(-0.089840, 0.712659) or (0.089840, -0.712659) where z = -1.031628 -
%global minimum lies here

%encode the problem, initialize a population, select a velocity update
%equation, and select a stopping criterion 

%final solution, plot the progress of the average fitness and 
% the best particle fitness for the simple and linear versions



