computeGrade = function(marks) {
  sum = 0;
  for(i in 1:length(marks)) {
    sum = sum + marks[i];
  }
  percentage = sum / length(marks);
  if(percentage >= 80 && percentage <= 100) { print(paste("Secured A+ Grade")); }
  else if(percentage >= 61 && percentage <= 79) { print(paste("Secured A Grade")); }
  else if(percentage >= 51 && percentage <= 60) { print(paste("Secured B Grade")); }
  else if(percentage >= 40 && percentage <= 50) { print(paste("Secured C Grade")); }
  else if(percentage < 40) { print(paste("Secured F Grade")); }
}

n = readline("Enter no. of subjects : ");
marks = c();

for(i in 1:n) {
  num = readline();
  num = as.numeric(num);
  marks = append(marks, num);
}
computeGrade(marks);