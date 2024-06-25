library(data.table)
item_data1 <- data.table(item_id=c(101,102,103,104),
                        item_name=c('Fridge','TV','AC','Oven'),
                        item_qty=c(35,45,23,18),
                        item_price=c(18000,24000,40000,30000)
)
item_data2 <- data.table(item_name=c('Fridge','TV','AC','Oven'),
                         item_ratings=c(3,4,5,4.5))
x=item_data1[item_data2,on="item_name"]
print(x)
