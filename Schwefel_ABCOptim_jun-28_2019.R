# EXAMPLE 3: 5D sphere, global minimum at about (0,0,0,0,0) -----------------
library(ABCoptim)

fs=function(x) 
{ 
 summ=0;new=0;
 for (i in 1:length(x))
 {
  new=x[i]*sin((abs(x[i]))**0.5);
  summ=summ+new;
  
  }
  return (418.9829*length(x)-summ)   
}
Num=100
x=matrix(0, Num, 4);
for (i in 1:Num)
{
cat("iteracao=",i,"\n");
set.seed(i)
x0=100*runif(3)
ans = abc_optim(x0, fs, lb=-500, ub=500, FoodNumber=175,maxCycle=300,criter=200);
#ans = abc_optim(rep(10,3), fs, lb=-500, ub=500, FoodNumber=10,maxCycle=50,criter=200);
print(ans$par)
x[i,1:3]=ans$par;x[i,4]=ans$value;print(x[i,]);

}
print(x)
setwd("/home/ucfilho/Documents/Doutorados_Mestrados/Doutorado_Raiana/Jun_2019_Raiana")
write.csv(x, file = "Abelha_jun_28_2019.csv")
print(summary(x))