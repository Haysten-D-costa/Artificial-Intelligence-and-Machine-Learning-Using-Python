print("enter a number")
x=readline();
x=as.integer(x);
fact=1;
temp=1;
while (temp <= x) {
  fact=fact*temp;
  # update expression 
  temp=temp+1;
}
print(fact)