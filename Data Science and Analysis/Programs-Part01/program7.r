mathfunc=function(x,y,z)
{ switch( 
  x, 
  "1"=cat("power y^z=",y^z),
  "2"=cat("square of x=",x^2),
  "3"=cat("cube of x=",y^3)
)
}

{ var1 = readline("Enter 1st number : ");
  var2 = readline("Enter 2nd number : ");
  var3 = readline("Enter 3rd number : ");
}
var1=as.integer(var1);
var2=as.integer(var2);
var3=as.integer(var3);
mathfunc(var1,var2,var3)
