maxof3nos=function(x,y,z)
{  if(x>y)
  { if(x>z)
    {cat(x," is the largest");}
    else
      {cat(z," is the largest");}
  }
  else
  {if(y>z)
    {cat(y," is the largest");}
    else
      {cat(z," is the largest");}
  }
}

{ var1 = readline("Enter 1st number : ");
  var2 = readline("Enter 2nd number : ");
  var3 = readline("Enter 3rd number : ");
}
var1 = as.integer(var1);
var2 = as.integer(var2);
var3 = as.integer(var3);

maxof3nos(var1,var2,var3)
