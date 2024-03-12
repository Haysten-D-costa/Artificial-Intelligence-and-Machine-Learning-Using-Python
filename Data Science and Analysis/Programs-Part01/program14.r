result <- c("Hello World") 
i <- 1

# test expression  
repeat { 
  
  print(result) 
  
  # update expression  
  i <- i + 1
  
  # Breaking condition 
  if(i >5) { 
    break
  } 
} 