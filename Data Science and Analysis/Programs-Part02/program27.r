marks.data=data.frame(
  sem=c(5,5,5),
  sub=c("sub1","sub2","sub3"),
  mks=c(78,56,79),
  stringsAsFactors = FALSE
)
print(marks.data)
for(i in 1:ncol(marks.data))
{ row=marks.data[,i]
  print(row)
}
for(i in 1:nrow(marks.data))
{ row=marks.data[i,]
#row=marks.data[i,]$sem
print(row)
}
cat("average=",mean(marks.data$mks),"\n")
