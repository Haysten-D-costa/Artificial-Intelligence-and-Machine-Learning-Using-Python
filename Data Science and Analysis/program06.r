mathFunc = function(num1, num2) {
    choice = readline("1 <- power\n2 <- square\n3 <- cube\n\nEnter your choice : ");
    switch ( 
        choice,
        "1" : print(paste("power of ", num1, " and ", num2, " : ", (num1 ^ num2))),+
        "2" : print(paste("square of ", num1, " : ", (num1 ^ 2))),
        "3" : print(paste("cube of ", num1, " : ", (num1 ^ 3))), 
    )
}
{
    num1 = readline("Enter 1st number : ");
    num2 = readline("Enter 2nd number : ");
}
num1 = as.integer(num1);
num2 = as.integer(num2);

mathFunc(num1, num2);