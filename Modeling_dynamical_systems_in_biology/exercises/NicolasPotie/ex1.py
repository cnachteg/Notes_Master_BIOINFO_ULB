import matplotlib.pyplot as plt

def myModele(x0,r, numberOfIt):
    x = [0]
    y = [x0]
    for i in range(1,numberOfIt):
        x.append(i)
        y.append(r * y[i-1] * (1-y[i-1]))
    plt.plot(x,y)
    plt.title("Xn+1 = r*Xn*(1-Xn)"+"\n X0 = "+str(x0)+", r = "+str(r)+", n = "+str(numberOfIt))
    plt.xlabel('valeur du n')
    plt.grid(True)
    plt.ylabel('resultat Xn')
    plt.show()
    
    

if __name__ == "__main__":
    #tester les differentes valeurs
    #effet du parametre r et de x0 ?
    myModele(0.01,1.1,200)