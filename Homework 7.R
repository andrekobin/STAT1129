#Q1
#(a)
Data_Frame1 <- data.frame (
  id = c(1,2,3,4,5),
  name = c("Peter", "Amy", "Ryan", "Gary", "Michelle"),
  salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)
Data_Frame1
#(b)
New_col <- data.frame(
  department = c("IT", "Finance", "Human Resources", "Computer Science", "Statistics")
)
Data_Frame2 <- cbind(Data_Frame1,New_col)
Data_Frame2
#(c)
Data_Frame3 <- Data_Frame2[-c(2), -c(1)]
Data_Frame3
Data_Frame3 <- Data_Frame3[-c(3), -c(3)]
Data_Frame3
#(d)
x <- c("Peter", "Gary", "Michelle")
y <- c(623.30, 729.00, 843.25)
barplot(y,names.arg=x)
#(e)
summary(Data_Frame1)
mylabel <- c("Highest", "Lowest", "Median")
colors <- c("Blue", "Red", "Green")
x <- c(843.25, 611.00, 623.30)
pie(x, label = mylabel, main = "Salary", col = colors)
legend("bottomright", mylabel, fill = colors)

#Q2
#if else function
symbols <- c("S", "R", "P")
comp <- "P"
user <- readline("Type R for rock, P for paper, or S for scissors: ")
result <- if (comp == "R" && user == "P") {"win"
} else if (comp == "P" && user == "S") {"win"
} else if (comp == "S" && user == "R") {"win"
} else if (comp == user) {"tie"
} else {"loss"}

result

#For loop function - my project had no for loops in it so I made a small Yahtzee game
dice <- 1:6

for(x in dice) {
  if (x == 6) {
    print(paste("The dice number is", x, "Yahtzee!"))
  } else {
    print(paste("The dice number is", x, "Not Yahtzee"))
  }
}

