num = readline("Enter a number : ")
num = as.integer(num)

fact = 1
while (num > 0) {
  fact = fact * num
  num = num - 1
}
print(paste(fact))