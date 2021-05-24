import math
import numpy as np
import scipy.stats as st

S0 = float(input("What is the current stock price?\n"))
k = float(input("What is the strike price?\n"))
V = 0.01*float(input("What is the volatility?\n"))
Q = 0.01*float(input("What is the dividend yield percentage?\n"))
T = float(input("What is the term in years?\n"))
r = 0.01*float(input("what is the risk-free rate?\n"))

class Options():
    print("Welcome to the Black-Scholes model.\n\n\n")
    def __init__(self, S0,k,V,Q,T,r):
        self.S0 = S0
        self.k = k
        self.V = V
        self.Q = Q
        self.T = T
        self.r = r

    def callpredictor(self):
        d1 = ((np.log(self.S0/self.k))+self.T*(self.r-self.Q+((self.V**2)/2)))/(self.V*math.sqrt(self.T))
        d2 = d1- (V*math.sqrt(T))
        Nd1 = st.norm.cdf(d1)
        Nd2 = st.norm.cdf(d2)
        C = (self.S0*(math.e**(-1*self.Q*self.T))*Nd1)-k*(math.e**(-1*self.r*self.T))*Nd2
        print(f"Your call option price is {C}.")

    def putpredictor(self):
        d1 = ((np.log(self.S0 / self.k)) + self.T * (self.r - self.Q + ((self.V ** 2) / 2))) / (
                    self.V * math.sqrt(self.T))
        d2 = d1 - (V * math.sqrt(T))
        NNegd1 = st.norm.cdf(-1 * d1)
        NNegd2 = st.norm.cdf(-1 * d2)
        P = (self.k*math.e**(-1*self.r*self.T)*NNegd2)-(S0*math.e**(-1*self.Q * self.T)*NNegd1)
        print(f"Your put option price is {P}.")

sample = Options(S0,k,V,Q,T,r)
sample.callpredictor()
sample.putpredictor()



