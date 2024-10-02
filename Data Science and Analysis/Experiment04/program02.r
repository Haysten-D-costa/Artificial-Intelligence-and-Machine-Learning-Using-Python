#Writing to a file
rating <- 1:4
animal <- c('koala', 'hedgehog', 'sloth', 'panda')
country <- c('Australia', 'Italy', 'Peru', 'China')
avg_sleep_hours <- c(21, 18, 17, 10)
super_sleepers <- data.frame(rating, animal, country, avg_sleep_hours)
data=super_sleepers;
write.table(super_sleepers, "data.txt")
example <- read.table('data.txt', header = TRUE, sep = " ")
x=mean(as.numeric(example$avg_sleep_hours),na.rm = TRUE)
print(x)
