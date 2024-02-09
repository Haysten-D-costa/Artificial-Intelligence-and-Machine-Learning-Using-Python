max = function(num1, num2, num3) {
    if(num1 == num2 && num2 == num3) {
        print(paste("All 3 numbers are equal !"));
    }
    else if(num1 > num2) {
        if(num1 > num3) {
            print(paste("Largest is ", num1));
        } else {
            print(paste("Largest is ", num3));
        }
    } else {
        if(num2 > num3) {
            print(paste("Largest is ", num2));
        } else {
            print(paste("Largest is ", num3));
        }
    }
}
{
    num1 = readline("Enter 1st number : ");
    num2 = readline("Enter 2nd number : ");
    num3 = readline("Enter 3rd number : ");
}
num1 = as.integer(num1);
num2 = as.integer(num2);
num3 = as.integer(num3);

max(num1, num2, num3);