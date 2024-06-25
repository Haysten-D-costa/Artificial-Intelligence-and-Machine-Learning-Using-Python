student_marks = data.frame(  # Create data frame
    RollNo = c(1, 2, 3, 4, 5), 
    Sub1 = c(85, 78, 92, 67, 80), 
    Sub2 = c(75, 82, 88, 70, 79), 
    Sub3 = c(90, 85, 95, 72, 88)
)

# Summary statistics for each subject
summary_subject1 = summary(student_marks$Sub1)
summary_subject2 = summary(student_marks$Sub2)
summary_subject3 = summary(student_marks$Sub3)

# Print summaries
cat("\nSummary for Subject 1:\n")
print(summary_subject1)
cat("\n")

cat("Summary for Subject 2:\n")
print(summary_subject2)
cat("\n")

cat("Summary for Subject 3:\n")
print(summary_subject3)
