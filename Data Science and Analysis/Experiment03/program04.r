# 4) For the above mentioned dataframe display the student name,dept,sem and attendance

data <- data.frame(
  Rollno = c(1, 2, 3, 4, 5),
  Sname = c("John", "Alice", "Bob", "Emma", "Michael"),
  dept = c("Computer Engineering", "IT", "Computer Engineering", "IT", "Computer Engineering"),
  Sem = c(3, 3, 5, 5, 3),
  Subject1_IT_marks = c(85, 78, 90, 82, 88),
  Subject2_IT_marks = c(75, 80, 85, 77, 79),
  Subject3_IT_marks = c(88, 82, 91, 79, 83),
  Subject1_Semester_Theory_marks = c(75, 80, 85, 77, 79),
  Subject2_Semester_Theory_marks = c(70, 75, 80, 73, 76),
  Subject3_Semester_Theory_marks = c(80, 85, 90, 83, 86),
  Attendance = c(90, 85, 92, 88, 91),
  Grade = c("A", "B", "A", "B", "A")
)
student_info <- data[, c("Sname", "dept", "Sem", "Attendance")]
print(student_info)