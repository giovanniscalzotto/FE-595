import numpy as np
import matplotlib.pyplot as plt

time = np.arange( 0, 2*np.pi, 0.01 )
sine = np.sin( time )
cosine = np.cos( time )
tangent = np.tan(time)


plt.plot( time, sine, label= "Sine" )
plt.plot( time, cosine, label= "Cosine" )
plt.plot( time, tangent, label= "Tangent" )

plt.xlim(0,6.3)
plt.ylim(-1.5,1.5)

plt.title( 'One Period Sine and Cosine' )
plt.xlabel( 'Frequncy' )
plt.ylabel( 'Amplitude' )


plt.axhline( y = 0, color='k' )
plt.axvline( x = 0, color='k', linestyle='-')
plt.legend(loc="upper center")


plt.show( )