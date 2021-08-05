import math
if __name__=='__main__':
    mean,std=map(float,input().split())
    bond_1=float(input().strip())
    bond_2=float(input().strip())
    cdn=lambda value: 0.5*(1+math.erf((value-mean))/(std*math.sqrt(2)))
    print(round(1-cdn(bond_1)*100,2))
    print(round(1-cdn(bond_2)*100,2))
    print(round(cdn(60)*100,2))