brux <- function(omega=100){ 

### Simulate the stochastic version of the Bruxellator with the Gillespie algorithm
### Didier Gonze - Created: 18/11/2009 - Updated: 15/4/2016 
### To allocate enough memory, launch R with the following options:
### R --min-vsize=10M --max-vsize=100M --min-nsize=500k --max-nsize=100M 
### Parameter omega is the system size (try omega=10, omega=50, omega=100)

###  Model parameters (concentration)

a=2
b=5.2

###  Initial condition (concentration)

x0=1
y0=1

###  Time parameters

trans=50
tend=100
tech=0.05

###  Initialization

a=a*omega
b=b*omega

x=x0*omega
y=y0*omega

t=0

tout=c()
xout=c()
yout=c()

told=0

w=rep(0,4)
c=rep(0,4)


###  Gillepie loop

while(t<trans+tend){

w[1]=a
w[2]=b*x/omega
w[3]=x*(x-1)*y/omega^2
w[4]=x

c[1]=w[1]
for (j in 2:4)
  c[j]=c[j-1]+w[j]
end

ct=c[4]

z=runif(2,min=0,max=1)

tau=(-log(z[1]))/ct
t=t+tau

uct=z[2]*ct

if (uct < c[1]){
   x=x+1
}
else if (uct <= c[2]){
   x=x-1
   y=y+1
}
else if (uct <= c[3]){
   x=x+1
   y=y-1
}
else if (uct <= c[4]){
   x=x-1
}


if ((t>trans) && (t>told+tech)){
tout=c(tout,t-trans)
xout=c(xout,x)
yout=c(yout,y)
told=t
}


}  # end of the while loop


write.table(array(c(tout,xout,yout),c(length(tout),3)), col.names=F, row.names=F,"test.txt", sep="\t")



### Figure

plot(tout,xout,xlab="Time",ylab="x (blue), y (red)",xlim=c(0,tend),type="l",col="blue")
lines(tout,yout,type="l",col="red")

#plot(xout,yout,xlab="x",ylab="y",type="l",col="black")


}

