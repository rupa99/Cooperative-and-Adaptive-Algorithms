ObjectiveFunction = @simple_objective;

%initial_x1_value = randi([-100 100],1,1)
%initial_x2_value = randi([-100 100],1,1)

no_of_times = 10;

%%%%%%%%%% Question b.i %%%%%%%%%%%%%%%%
disp("Question b.i ")
for i = 1:no_of_times

    initial_x1_value = randi([-100 100],1,1);
    initial_x2_value = randi([-100 100],1,1);

    x0 = [initial_x1_value initial_x2_value];   % Starting point
    [x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100]);
    disp("the x value is")
    disp(x)
    disp("the f value is")
    disp(fval)
    disp("the exit flag is")
    disp(exitFlag)
    disp("the output is")
    disp(output)
end

%{
%%%%%%%%%% Question b.ii %%%%%%%%%%%%%%%%
disp("Question b.ii ")
initial_x1_value = randi([-100 100],1,1); %TODO: Encode this to select the best 2 initial points
initial_x2_value = randi([-100 100],1,1);

%TODO: put more constraint on the range for the temperature
for i = 1:no_of_times
    temp_x1 = randi([4000 5000],1,1);

     x0 = [initial_x1_value initial_x2_value];   % Starting point
    options = optimoptions(@simulannealbnd,...
        'InitialTemperature', temp_x1); 
    [x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);
    disp("the x value is")
    disp(x)
    disp("the f value is")
    disp(fval)
    disp("the exit flag is")
    disp(exitFlag)
    disp("the output is")
    disp(output)

end


%%%%%%%%%% Question b.iii %%%%%%%%%%%%%%%%
disp("Question b.iii: Case - Linear ")

initial_x1_value = randi([-100 100],1,1); %TODO: Encode this to select the best 2 initial points
initial_x2_value = randi([-100 100],1,1);
x0 = [initial_x1_value initial_x2_value];   % Starting point

%%%%%% Linear - dec = 10 %%%%%%%%
disp("Question b.iii: Case - Linear, 10")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @linear_alpha1); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)

%%%%%% Linear - dec = 15 %%%%%%%%
disp("Question b.iii: Case - Linear, 15")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @linear_alpha2); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)


%%%%%% Linear - dec = 25 %%%%%%%%
disp("Question b.iii: Case - Linear, 25")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @linear_alpha3); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)

%%%%%%%%%% Question b.iii %%%%%%%%%%%%%%%%
disp("Question b.iii: Case - Exponential ")

initial_x1_value = randi([-100 100],1,1); %TODO: Encode this to select the best 2 initial points
initial_x2_value = randi([-100 100],1,1);
x0 = [initial_x1_value initial_x2_value];   % Starting point


%%%%%% exp - multiplier = 2 %%%%%%%%
disp("Question b.iii: Case - Exponential, 2")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @exponential_alpha1); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)

%%%%%% exp - multiplier = 8 %%%%%%%%
disp("Question b.iii: Case - Exponential, 8")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @exponential_alpha2); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)

%%%%%% exp - multiplier = 20 %%%%%%%%
disp("Question b.iii: Case - Exponential, 20")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @exponential_alpha3); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)



%%%%%%%%%% Question b.iii %%%%%%%%%%%%%%%%
disp("Question b.iii: Case - slow ")
initial_x1_value = randi([-100 100],1,1); %TODO: Encode this to select the best 2 initial points
initial_x2_value = randi([-100 100],1,1);
x0 = [initial_x1_value initial_x2_value];   % Starting point

%%%%%% slow - alpha = 5 %%%%%%%%
disp("Question b.iii: Case - slow 5")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @slow_alpha1); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)


%%%%%% slow - alpha = 10 %%%%%%%%
disp("Question b.iii: Case - slow 10")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @slow_alpha2); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)

%%%%%% slow - alpha = 15 %%%%%%%%
disp("Question b.iii: Case - slow 15")
options = optimoptions(@simulannealbnd,...
        'TemperatureFcn', @slow_alpha3); 
[x,fval,exitFlag,output] = simulannealbnd(ObjectiveFunction,x0, [-100 -100], [100 100], options);

disp("the x value is")
disp(x)
disp("the f value is")
disp(fval)
disp("the exit flag is")
disp(exitFlag)
disp("the output is")
disp(output)

%}


