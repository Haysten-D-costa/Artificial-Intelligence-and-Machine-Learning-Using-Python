data(iris)
cat("summary:\n",summary(iris))
cat("\nnames:",names(iris))
cat("\ndim:",dim(iris))
hist(iris$Sepal.Length,
     col='steelblue',
     main='Histogram',
     xlab='Length',
     ylab='Frequency')
par(mar=c(6,6,6,6))


