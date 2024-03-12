n=readline("enter no of elements")
cat("enter ",n," values")
vec=c()
for(i in 1:n)
{
  t=readline();
  t=as.numeric(t);
  vec=append(vec,t);
  print(t)
}
print(vec)