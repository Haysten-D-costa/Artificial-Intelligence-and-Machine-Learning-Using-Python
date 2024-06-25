student_marks = data.frame(  # Create data frame
    RollNo = c(1, 2, 3, 4, 5), 
    Sub1 = c(85, 78, 92, 67, 80), 
    Sub2 = c(75, 82, 88, 70, 79), 
    Sub3 = c(90, 85, 95, 72, 88)
)

# Box plot for each subject
boxplot(
    student_marks[,2:4],
    main="Boxplot of Marks Distribution",
    xlab="Subject",
    ylab="Marks",
    names=c("Subject 1", "Subject 2", "Subject 3")
)
