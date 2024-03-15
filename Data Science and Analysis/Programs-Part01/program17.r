n <- readline("Enter no. of entries : ")
print(paste("Enter ", n, " numbers  : "))

vector = c();

for(i in 1:n) {
  {
    num = readline()
    num = as.integer(num)
    vector = append(vector, num)
  }
}
print(paste(vector))