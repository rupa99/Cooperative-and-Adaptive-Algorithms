function f = covid(x)


for i = 1:size(x, 1)
    f(i) = 0.063 * x(i, 1) - 0.058*x(i,2) + 3487.89; 
end