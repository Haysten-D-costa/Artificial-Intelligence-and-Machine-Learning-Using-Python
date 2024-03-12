vec =c(1,2,3,4,5)
for (i in 1:length(vec))
{ if (i%%2==0)
  { 
    break
  }
  print(i)
}
print("Outside Loop")