calculator = function(val1, val2, op) {
  result = switch (
    op,
    "A"= cat("Addition = ", val1 + val2),   
    "D"= cat("Subtraction = ", val1 - val2),   
    "R"= cat("Division = ", val1 / val2),   
    "S"= cat("Multiplication = ", val1 * val2), 
    "M"= cat("Modulus = ", val1 %% val2), 
  )
  print(result);  
}
print(paste("A <- Addition"))
print(paste("D <- Subtraction"))
print(paste("R <- Division"))
print(paste("S <- Addition"))
print(paste("M <- Modulus"))

num1 = readline("Enter 1st number : ");
num1 = as.integer(num1);
num2 = readline("Enter 2nd number : ");
num2 = as.integer(num2);

op = readline("Enter operator : ");
calculator(num1, num2, op)
