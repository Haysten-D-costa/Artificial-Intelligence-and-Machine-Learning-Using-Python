library(data.table)
item_data <- data.table(item_id=c(101,102,103,104),
                        item_name=c('Fridge','TV','AC','AC'),
                        item_qty=c(35,45,23,18),
                        item_price=c(18000,24000,40000,30000)
)
x=item_data[,mean(item_price),by=item_name]
print(x)
