# friend.data <- data.frame(
#   friend_id = c(11:15), 
#   friend_name = c("Sachin", "Sourav", 
#                   "Dravid", "Sehwag", 
#                   "Dhoni"),
#   stringsAsFactors = FALSE
# )
# # print the data frame
# print(friend.data)
x<-c(10,20,30,40,50,60,70,80,90,100) 

res<-quantile(x,probs=0.1) 

print(res) 