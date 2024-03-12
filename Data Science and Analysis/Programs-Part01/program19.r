checkvowel=function(vec)
{ for(i in 1:length(vec))
  { if((vec[i]=='a')| (vec[i]=='e'))
    {print("vowel")}
}
}

n=readline("enter no of values ");
cat("enter ",n," values")
vec1=scan(what=character())
checkvowel(vec1)