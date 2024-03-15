student_marks = data.frame(  # Create data frame
    RollNo = c(1, 2, 3, 4, 5), 
    Sub1 = c(85, 78, 92, 67, 80), 
    Sub2 = c(75, 82, 88, 70, 79), 
    Sub3 = c(90, 85, 95, 72, 88)
)

# Function to compute summary statistics for each subject
compute_summary_stats <- function(subject_marks) {
  mean_mark <- mean(subject_marks)
  median_mark <- median(subject_marks)
  mark_range <- range(subject_marks)
  mark_variance <- var(subject_marks)
  mark_sd <- sd(subject_marks)
  mark_iqr <- IQR(subject_marks)
  
  return(list(
    Mean = mean_mark,
    Median = median_mark,
    Range = mark_range,
    Variance = mark_variance,
    Standard_Deviation = mark_sd,
    Interquartile_Range = mark_iqr
  ))
}

# Compute summary statistics for each subject
summary_subject1 <- compute_summary_stats(student_marks$Subject1)
summary_subject2 <- compute_summary_stats(student_marks$Subject2)
summary_subject3 <- compute_summary_stats(student_marks$Subject3)

# Print summaries
cat("Summary for Subject 1:\n")
print(summary_subject1)

cat("Summary for Subject 2:\n")
print(summary_subject2)

cat("Summary for Subject 3:\n")
print(summary_subject3)
