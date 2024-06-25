library(dplyr);
rollno<-c(2,33,55,15);
it1 <- c(17,17,16,18);
it2 <- c(12,16,16,18);
attendance <- c(40,75,78,88);
marks_summary1 <- data.frame(rollno,it1,it2,attendance)
z=arrange(marks_summary1,rollno)
print(z)

