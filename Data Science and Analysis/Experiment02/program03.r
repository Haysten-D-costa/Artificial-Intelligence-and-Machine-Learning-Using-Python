student_marks = data.frame(  # Create data frame
    RollNo = c(1, 2, 3, 4, 5), 
    Sub1 = c(85, 78, 92, 67, 80), 
    Sub2 = c(75, 82, 88, 70, 79), 
    Sub3 = c(90, 85, 95, 72, 88)
)

# Plot histograms for each subject
par(mfrow=c(1,3))  # Arrange plots in one row
for (i in 2:4) {  # Loop through each subject
  hist(student_marks[,i],
       main = paste("Histogram of Subject", i-1, "Marks"),
       xlab = "Marks",
       ylab = "Frequency",
       col = "lightblue",
       border = "black")
}
