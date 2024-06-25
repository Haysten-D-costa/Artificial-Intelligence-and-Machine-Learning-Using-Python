# 6) Create two data frames and demonstrate left outer join,right outer join,outer join ,cross join,set difference and intersect operation

df1 <- data.frame(
  ID = c(1, 2, 3, 4),
  Name = c("John", "Alice", "Bob", "Emma"),
  Age = c(25, 30, 28, 22)
)

df2 <- data.frame(
  ID = c(1, 2, 5),
  Gender = c("M", "F", "F"),
  Salary = c(50000, 60000, 55000)
)

# Left outer join
left_join_df <- merge(df1, df2, by = "ID", all.x = TRUE)
print(left_join_df)
cat("\n")

# Right outer join
right_join_df <- merge(df1, df2, by = "ID", all.y = TRUE)
print(right_join_df)
cat("\n")

# Outer join
outer_join_df <- merge(df1, df2, by = "ID", all = TRUE)
print(outer_join_df)
cat("\n")

# Cross join
cross_join_df <- merge(df1, df2, by = NULL)
print(cross_join_df)
cat("\n")

# Set difference
set_difference_df <- df1[!df1$ID %in% df2$ID, ]
print(set_difference_df)
cat("\n")

# Intersect operation
intersect_df <- df1[df1$ID %in% df2$ID, ]
print(intersect_df)
cat("\n")
