import numpy as np
import matplotlib.pyplot as plt
def ecdf(data):
    n=len(data)
    #Sort the data ecdf
    x=np.sort(data)
    #y data for ecdf
    y=np.arange(1,n+1)/n
    return x,y
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers,y_vers= ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers,y_vers,marker='.',linestyle='none')
# Label the axes
_=plt.xlabel('counts')
_=plt.ylabel('ECDF')

# Display the plot
plt.show()
