import numpy as np
import matplotlib.pyplot as plt

time = np.arange( 0, 2*np.pi, 0.01 )
sine = np.sin( time )
cosine = np.cos( time )
tan = np.tan( time )
#new change


plt.plot( time, sine, label= "Sine" )
plt.plot( time, cosine, label= "Cosine" )


plt.title( 'One Period Sine and Cosine' )
plt.xlabel( 'Frequncy' )
plt.ylabel( 'Amplitude' )

def tan_graph():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # start,stop,step
    y = np.tan(x)
    # test
    plt.plot(x, y)
    plt.xlabel('x values from')  # string must be enclosed with quotes '  '
    plt.ylabel('tan(x)')
    plt.title('Plot of tan')
    plt.legend(['tan(x)'])
    plt.show()


plt.axhline( y = 0, color='k' )
plt.axvline( x = 0, color='k', linestyle='-')
plt.legend(loc="upper center")


plt.show( )
tan_graph()