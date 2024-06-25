min_max = function(numbers) {
  min = numbers[1];
  max = numbers[1];
  for(i in 1:length(numbers)) {
    if(numbers[i] < min) { min = numbers[i]; }
    if(numbers[i] > max) { max = numbers[i]; }
  }
  print(paste("Max : ", max));
  print(paste("Min : ", min));
}
numbers = c();
# numbers = c(12, 5, 8, 20, 3, 15, 7);
n = as.numeric(readline("Enter number of numbers : "));
for(i in 1:n) {
  num = as.numeric(readline());
  numbers = append(numbers, num);
}
min_max(numbers);
