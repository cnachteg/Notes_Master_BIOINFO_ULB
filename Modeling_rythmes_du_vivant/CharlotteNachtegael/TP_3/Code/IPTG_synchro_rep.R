repeat_IPTG_rep<-function(run=10,omega=100,s=20,tstart=20,tstop=60){
  colo=c(rainbow(10))
  plot(1,type='n',xlim=c(0,100),ylim=c(0,15000),xlab='Time', ylab='P1')
  for (i in 1:run){
    #parameters
    a0=0*omega
    a1=100*omega
    a2=100*omega
    a3=100*omega
    K1=1*omega
    K2=1*omega
    K3=1*omega
    n=2
    g=1
    b=5
    d=5
    Ks=5
    m=2
    
    #initial conditions
    m1=1*omega
    m2=1*omega
    m3=1*omega
    p1=0*omega
    p2=0*omega
    p3=0*omega
    
    #time
    trans=50
    tend=100
    tech=0.05
    
    
    #initialization
    tout=c()
    p1out=c()
    p2out=c()
    p3out=c()
    iout=c()
    
    t=0
    told=0
    
    w=rep(0,12) #4 reactions
    c=rep(0,12)
    
    #loop
    while(t<trans+tend){
      
      if ((t>tstart+trans) && (t<tstop+trans)){
        S=s
      }
      else{
        S=0
      }
      
      #mRNA
      w[1]=a0+a1*K1^n/(K1^n+p3^n)
      w[2]=g*m1
      w[3]=a0+a2*K2^n/(K2^n+(p1/(1+S/Ks)^m)^n)
      w[4]=g*m2
      w[5]=a0+a3*K3^n/(K3^n+p2^n)
      w[6]=g*m3
      #proteins
      w[7]=b*m1
      w[8]=d*p1
      w[9]=b*m2
      w[10]=d*p2
      w[11]=b*m3
      w[12]=d*p3
      
      #calcul des prob cumul
      c[1]=w[1]
      for (j in 2:12)
        c[j]=c[j-1]+w[j]
      end
      
      #prob cumulée totale
      ct=c[12]
      
      #deux nombres au hasard entre 0 et 1
      z=runif(2,min=0,max=1)
      
      #détermination de delta t
      tau=(-log(z[1]))/ct
      t=t+tau
      
      #which reaction ?
      uct=z[2]*ct
      
      if (uct < c[1]){
        m1=m1+1
      }
      else if (uct <= c[2]){
        m1=m1-1
      }
      else if (uct <= c[3]){
        m2=m2+1
      }
      else if (uct <= c[4]){
        m2=m2-1
      }
      else if (uct <= c[5]){
        m3=m3+1
      }
      else if (uct <= c[6]){
        m3=m3-1
      }
      else if (uct <= c[7]){
        p1=p1+1
      }
      else if (uct <= c[8]){
        p1=p1-1
      }
      else if (uct <= c[9]){
        p2=p2+1
      }
      else if (uct <= c[10]){
        p2=p2-1
      }
      else if (uct <= c[11]){
        p3=p3+1
      }
      else if (uct <= c[12]){
        p3=p3-1
      }
      
      if ((t>trans) && (t>told+tech)){
        tout=c(tout,t-trans)
        p1out=c(p1out,p1)
        p2out=c(p2out,p2)
        p3out=c(p3out,p3)
        iout=c(iout,S)
        told=t
      }
    }
    lines(tout,p1out,type="l",col=colo[i])
  }
}