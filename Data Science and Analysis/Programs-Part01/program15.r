areaRect=function(length,breadth)
{
  return (length*breadth);
}

l=readline("enter length");
b=readline("enter breadth");
l=as.numeric(l);
b=as.numeric(b);
cat("area of rect=",areaRect(l,b))