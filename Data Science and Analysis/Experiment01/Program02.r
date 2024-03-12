min = function(num1, num2, num3) {
  if(num1 < num2) {
    if(num1 < num3) { print(paste("Number 1 smallest ! : ", num1)); }
    else { print(paste("Number 3 smallest ! : ", num3)); }
  }
  else {
    if(num2 < num3) { print(paste("Number 2 smallest ! : ", num2)); }
    else { print(paste("Number 3 smallest ! : ", num3)); }
  }
}
num1 = readline("Enter 1st number : ");
num1 = as.integer(num1);
num2 = readline("Enter 2nd number : ");
num2 = as.integer(num2);
num3 = readline("Enter 3rd number : ");
num3 = as.integer(num3);
min(num1, num2, num3)
