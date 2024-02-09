multScalar = function(x) {
    x * 2;
}
print("Enter some numbers : ");
num = scan(what=double());
num = sapply(num, multScalar);
print(num);