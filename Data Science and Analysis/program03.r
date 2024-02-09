isEven = function(x) {
    if((x %% 2) == 0) 
    {
        print(paste(x, " is Even !"));
    } else {
        print(paste(x, " is Odd  !"));
    }
}
num = readline("Enter number : ");
num = as.integer(num);
isEven(num);