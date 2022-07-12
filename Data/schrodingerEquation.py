# IMPORTS
import tkinter
import matplotlib.pyplot as plt
import numpy as np



#FUNCTIONS
def Input():
   global n
   n = int(E1.get())    #N
   top.destroy()


# GUI
top = tkinter.Tk()
top.title("Schrodinger Wave Graph Generator")
top.geometry("800x400")
HEADING = tkinter.Label(top, text="\n\nSCHRODINGER WAVE ANIMATION\n", font=("Courier 25 bold"), fg= "Blue").pack()
L1 = tkinter.Label(top, text="Principal Quantum Number",font=("Courier 20"))
L1.pack()
E1 = tkinter.Entry(top, bd =5, width=50, font=("Courier 14"))
E1.pack()
E1.focus_set()
tkinter.Button(top, text= "Animate",width= 20, command= Input,font=("Courier 22 bold"), fg="red").pack(pady=20)
top.mainloop()


# 2D GRAPH
# Variables
L = 100
x = np.linspace(0,L,200)
A = (2/L)**(1/2) # Normalized wavefunction according to sin(n Pi x)
# Functions
def psi(a):
    psi = (np.sin((n * np.pi * a)/L))**2
    return psi
# Plotting
PSI = np.array([psi(a) for a in x])
fig = plt.figure()
ax1 = plt.axes()
ax1.plot(x,PSI, color = 'green')
plt.xlabel('X')
plt.ylabel('Ψ')
plt.title(f'Probability density: n = {n}', color = 'green')
plt.savefig(f'Probability density n = {n}.png', transparent = True)
plt.show()

# 3D GRAPH
L = 100
x,y = np.linspace(0,L,200),np.linspace(0,L,200)
A = (2/L)**(1/2) # Normalized wavefunction according to sin(n Pi x)
# Functions
def psi(a,b):
    psi = (np.sin((n * np.pi * a)/L) * (np.sin((n * np.pi * b)/L)))**2
    return psi
# Plotting
X,Y = np.meshgrid(x,y)
psi = np.array([psi(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])
PSI = psi.reshape(X.shape)
fig = plt.figure()
axis = fig.add_subplot(111, projection = '3d')
axis.plot_surface(X,Y,PSI,cmap = 'winter')
plt.xlabel('X')
plt.ylabel('Y')
axis.set_zlabel('Ψ')
plt.title(f'Probability density: n = {n}', color = 'green')
# plt.savefig(f'Probability density n = {n}.png', transparent = True)
plt.show()
