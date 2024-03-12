scalar=function(vec)
{ vec*2
}

print("enter some values ");
vec1=scan(what=double())
vec1=sapply(vec1,scalar)
print(vec1)
print(length(vec1))