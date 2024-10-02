student_marks = data.frame(  # Create data frame
  Sub1 = c(85, 78, 92, 67, 80), 
  Sub2 = c(75, 82, 88, 70, 79), 
  Sub3 = c(90, 85, 95, 72, 88)
)

# Plot histograms for each subject
hist(
  student_marks$Sub1,
  main = "Subject 1 Marks",
  xlab = "Marks"
)
hist(student_marks$Sub2,
  main = "Subject 2 Marks",
  xlab = "Marks"
)
hist(student_marks$Sub3,
  main = "Subject 3 Marks",
  xlab = "Marks"
)