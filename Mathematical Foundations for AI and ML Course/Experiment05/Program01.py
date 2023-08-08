# PROGRAM TO IMPLEMENT THE TAYLOR SERIES...

from sympy import symbols, diff, pretty_print, factorial, exp
x, y = symbols("x y")
n=10 # NUMBER OF ITERATIONS...
xo=0 # THE VALUE OF 'a' OR THE POINT..
func=exp(x) # THE FUNCTION WE ARE APPROXIMATING..
result=func.subs(x,xo) # INITIALIZiNG RESULT WITH THE FIRST TERM...
for i in range(1,n):
    result+=diff(func,x,i).subs(x,xo)*((x-xo)**i)/(factorial(i))
    # diff(func,x,i) -> THIS DIFFERENTIATES "func" w.r.t, "i-th" TIMES...
    # subs(x,xo) -> THIS IS A METHOD USED ON EXPRESSIONS TO SUBSTITUTE AN UNKNOWN (x) WITH A VALUE (xo)
   
pretty_print(result)