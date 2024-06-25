#reading from a file
data = read.csv("data.csv",header = FALSE, sep = ",")
data=as.numeric(data)
x=mean(data, na.rm = TRUE)
print(x)
