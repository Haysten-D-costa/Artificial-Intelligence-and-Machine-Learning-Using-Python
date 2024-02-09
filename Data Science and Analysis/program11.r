sumOfNos = function(list) {
    sum = 0;
    for(i in 1:length(list)) {
        sum = sum + list[i];
    }
    return(sum);
}
n = readline("Enter no. of elements in list : ");
list = c(); # creating an empty list...

for(i in 1:n) {
    num = readline();
    num = as.numeric(num);
    list = append(list, num);
}
print(paste("Sum of numbers in list : ", sumOfNos(list)));