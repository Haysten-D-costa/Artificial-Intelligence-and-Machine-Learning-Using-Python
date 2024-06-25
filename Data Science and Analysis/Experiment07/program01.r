library(data.table)
item_data <- data.table(item_id=c(101,102,103,104),
                 item_name=c('Fridge','TV','AC','OVEN'),
                 item_qty=c(35,45,23,18),
                 item_price=c(18000,24000,40000,10000)
                )
x=subset(item_data,item_qty>40)
print(x)
