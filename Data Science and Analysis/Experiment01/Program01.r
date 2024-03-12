isMultOf3 = function(num) {
  if((num %% 3) == 0) {
    print(paste("Number is a multiple of 3 !"));
  } else {
    print(paste("Number is not a multiple of 3 !"))
  }  
}
num = readline("Enter a number : ");
num = as.integer(num);
isMultOf3(num)
