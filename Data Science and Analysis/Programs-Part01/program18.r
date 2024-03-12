sumofnos=function(vec1)
{ sum1=0;
  for(i in 1:length(vec1))
  {  sum1=sum1+vec1[i];
  }
  return (sum);
}
n=readline("enter no of elements")
cat("enter ",n," values")
vec=c()
for(i in 1:n)
{
  t=readline();
  t=as.numeric(t);
  vec=append(vec,t);
}
cat("sum of ",n," nos: ",sumofnos(vec))