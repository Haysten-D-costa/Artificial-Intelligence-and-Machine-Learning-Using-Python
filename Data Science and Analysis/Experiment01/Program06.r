circle_area = function(radius) {
  return(3.14 * radius^2)
}
rectangle_area = function(length, width) {
  return(length * width)
}
square_area = function(side) {
  return(side^2)
}
radius <- 5
length <- 4
width <- 6
side <- 3

circle_result <- circle_area(radius)
rectangle_result <- rectangle_area(length, width)
square_result <- square_area(side)

cat("Area of the circle with radius", radius, "is", circle_result, "\n")
cat("Area of the rectangle with length", length, "and width", width, "is", rectangle_result, "\n")
cat("Area of the square with side", side, "is", square_result, "\n")
