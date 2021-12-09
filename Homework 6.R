#Question 1
a = matrix(c(7,2,9,4,12,13), ncol = 3, nrow = 2)
b = matrix(c(1,2,3,7,8,9,12,13,14,19,20,21), ncol = 4, nrow = 3)
a %*% b

#Question 2
mydata=read.csv('~/Desktop/amazon-orders.csv')
head(mydata)
dim(mydata)
colnames(mydata)
mydata$item.total <- gsub("[$]","",as.character(mydata$Subtotal))
mydata$item_total <- as.numeric(mydata$item.total)
mydata$item_total
max(mydata$item_total)
min(mydata$item_total)
sum(mydata$item_total)
mean(mydata$item_total)
median(mydata$item_total)

date<-as.Date(mydata$Order.Date, "%m/%d/%y")
fix(date)
plot(mydata$item_total~date,type="l", col="blue", axes=F)
box()
axis (1,date,format(date, "%m-%y"))


