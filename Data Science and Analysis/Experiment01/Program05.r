is_even_odd = function(x) {
  if (x %% 2 == 0) {
    print(paste(x, ": Even"))
  } else {
    print(paste(x, ": Odd"))
  }
}
n = readline("Enter no. of entries : ");
numbers = c();

print(paste("Enter ", n," numbers : "))
for(i in 1:n) {
  num = readline();
  num = as.numeric(num);
  numbers = append(numbers, num);
}
cat("Vector:", numbers, "\n")
for(i in 1:length(numbers)) {
  is_even_odd(numbers[i])
}
