repeat_IPTG_tog<-function(run=5,omega=100,s=2,tstart=20,tstop=60){
  Time=c()
  colo=c(rainbow(10))
  plot(1,type='n',xlim=c(0,100),ylim=c(0,250),xlab='Time', ylab='X')
  for (i in 1:run){
    #parameters
    a1=2*omega
    a2=2*omega
    K1=1*omega
    K2=1*omega
    n=4
    d1=1
    d2=1
    Ks=5
    m=2
    S=0
    
    #initial conditions
    x0=1*omega
    y0=2*omega
    
    #time
    trans=50
    tend=100
    tech=0.05

    #initialization
    tout=c()
    xout=c()
    yout=c()
    iout=c()
    
    x=x0
    y=y0
    
    t=0
    told=0
    
    w=rep(0,4) #4 reactions
    c=rep(0,4)
    
    #loop
    while(t<trans+tend){
      
      if ((t>tstart+trans) && (t<tstop+trans)){
        S=s
      }
      else{
        S=0
      }
      
      w[1]=a1*K1^n/(K1^n+(y/(1+S/Ks)^m)^n)
      w[2]=d1*x
      w[3]=a2*K2^n/(K2^n+x^n)
      w[4]=d2*y
      
      #calcul des prob cumul
      c[1]=w[1]
      for (j in 2:4)
        c[j]=c[j-1]+w[j]
      end
      
      #prob cumulée totale
      ct=c[4]
      
      #deux nombres au hasard entre 0 et 1
      z=runif(2,min=0,max=1)
      
      #détermination de delta t
      tau=(-log(z[1]))/ct
      t=t+tau
      
      #which reaction ?
      uct=z[2]*ct
      
      if (uct < c[1]){
        x=x+1
      }
      else if (uct <= c[2]){
        x=x-1
      }
      else if (uct <= c[3]){
        y=y+1
      }
      else if (uct <= c[4]){
        y=y-1
      }
      
      if ((t>trans) && (t>told+tech)){
        tout=c(tout,t-trans)
        xout=c(xout,x)
        yout=c(yout,y)
        iout=c(iout,S)
        told=t
      }
    }
    lines(tout,xout,type="l",col=colo[i])
  }
}