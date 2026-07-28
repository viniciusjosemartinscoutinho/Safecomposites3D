# -*- coding: utf-8 -*-
#  & "C:/Program Files/Python311/python.exe" C:\Users\ucfil\Desktop\desktop\codes\all\composites\Safecomposites\Interfaces\Interface_of_Calcul_EN.py  #serie
# Start-Process "C:/Program Files/Python311/python.exe"  -ArgumentList "C:\Users\ucfil\Desktop\desktop\codes\all\composites\Safecomposites\Interfaces\Interface_of_Calcul_EN.py"  #parallelism




#________________________________________________ LIBRARIES ______________________________________________
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
#____________________________________________________________________________________________________________



#________________________________________________ FUNCTION definitions ______________________________________________
def reset_entry_BLOCK1():
    EL_tf.delete(0,'end')
    ET_tf.delete(0,'end')
    GLT_tf.delete(0,'end')
    VLT_tf.delete(0,'end')
    Nx_tf.delete(0,'end')
    Ny_tf.delete(0,'end')
    Nz_tf.delete(0,'end')
    Mt_tf.delete(0,'end')
    Mfy_tf.delete(0,'end')
    Mfz_tf.delete(0,'end')

    
    
def Draw1():
    about_window = Toplevel(ws)
    about_window.title("Graphical representation")
    n = Liste_nb_layer.get()
    lb = Label(about_window, text=f"Graphical representation of strains in the {n}-layer laminate")
    lb.pack()

    # Center the window
    screen_x = int(about_window.winfo_screenwidth())
    screen_y = int(about_window.winfo_screenheight())
    window_x = 1200
    window_y = 600
    posX = (screen_x//2) - (window_x//2)
    posY = (screen_y//2) - (window_y//2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    about_window.geometry(geo)    

    canvas=Canvas(about_window, width=1200, height=500, bg="white")
    canvas.pack()
    
    # Drawing the chart
    draw_samples(canvas)
    Plot_eps_laminate(canvas)

 
def Draw2():
    about_window = Toplevel(ws)
    about_window.title("Graphical representation")
    n = Liste_nb_layer.get()
    lb = Label(about_window, text=f"Graphical representation of strains in each layer ({n} layers)")
    lb.pack()
    
    # Center the window
    screen_x = int(about_window.winfo_screenwidth())
    screen_y = int(about_window.winfo_screenheight())
    window_x = 1200
    window_y = 600
    posX = (screen_x//2) - (window_x//2)
    posY = (screen_y//2) - (window_y//2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    about_window.geometry(geo)    

    canvas=Canvas(about_window, width=1200, height=500, bg="white")
    canvas.pack()
    
    # Drawing the chart
    draw_samples(canvas)
    Tracer_eps_layer(canvas)
   
 
def Validation1():
    """"Creates n layers with their associated entry fields"""    
    Nb_layer = int(Liste_nb_layer.get())
    
    # Label for angles and thicknesses
    Angle_lb = Label(
        frame1,
        text="Angles (in °)")
    Angle_lb.grid(row=10, column=2)    
    Thickness_lb = Label(
        frame1,
        text="Thicknesses (in mm)")
    Thickness_lb.grid(row=10, column=3, sticky='w') 

    global Angle1_ent
    global Thickness1_ent
    global Angle2_ent
    global Thickness2_ent
    global Angle3_ent
    global Thickness3_ent
    global Angle4_ent
    global Thickness4_ent
    global Angle5_ent
    global Thickness5_ent
    global Angle6_ent
    global Thickness6_ent
    global Angle7_ent
    global Thickness7_ent
    global Angle8_ent
    global Thickness8_ent
    
## For 1 layer :
    if Nb_layer==1:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e')
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w')    
    
## For 2 layers :
    if Nb_layer==2:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e')
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w')    
        Layer2 = Label(frame1, text="Layer 1")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.grid(row=12, column=2, sticky='w')         
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.grid(row=12, column=3, sticky='w') 

## For 3 layers :
    if Nb_layer==3:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e') 
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w') 
        Layer2 = Label(frame1, text="Layer 2")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.grid(row=12, column=2, sticky='w') 
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.grid(row=12, column=3, sticky='w') 
        Layer3 = Label(frame1, text="Layer 3")
        Layer3.grid(row=13, column=1, sticky='e') 
        Angle3_ent = Entry(frame1)
        Angle3_ent.grid(row=13, column=2, sticky='w') 
        Thickness3_ent = Entry(frame1)
        Thickness3_ent.grid(row=13, column=3, sticky='w') 

## For 4 layers :
    elif Nb_layer==4:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e') 
        Angle1_ent = Entry(frame1)
        Angle1_ent.insert(0, "15")
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.insert(0, "1.5")
        Thickness1_ent.grid(row=11, column=3, sticky='w') 
        Layer2 = Label(frame1, text="Layer 2")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.insert(0, "-30")
        Angle2_ent.grid(row=12, column=2, sticky='w') 
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.insert(0, "1")
        Thickness2_ent.grid(row=12, column=3, sticky='w') 
        Layer3 = Label(frame1, text="Layer 3")
        Layer3.grid(row=13, column=1, sticky='e') 
        Angle3_ent = Entry(frame1)
        Angle3_ent.insert(0, "-15")
        Angle3_ent.grid(row=13, column=2, sticky='w') 
        Thickness3_ent = Entry(frame1)
        Thickness3_ent.insert(0, "1.5")
        Thickness3_ent.grid(row=13, column=3, sticky='w')
        Layer4 = Label(frame1, text="Layer 4")
        Layer4.grid(row=14, column=1, sticky='e') 
        Angle4_ent = Entry(frame1)
        Angle4_ent.insert(0, "30")
        Angle4_ent.grid(row=14, column=2, sticky='w') 
        Thickness4_ent = Entry(frame1)
        Thickness4_ent.insert(0, "1")
        Thickness4_ent.grid(row=14, column=3, sticky='w') 

## For 5 layers :
    elif Nb_layer==5:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e') 
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w') 
        Layer2 = Label(frame1, text="Layer 2")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.grid(row=12, column=2, sticky='w') 
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.grid(row=12, column=3, sticky='w') 
        Layer3 = Label(frame1, text="Layer 3")
        Layer3.grid(row=13, column=1, sticky='e') 
        Angle3_ent = Entry(frame1)
        Angle3_ent.grid(row=13, column=2, sticky='w') 
        Thickness3_ent = Entry(frame1)
        Thickness3_ent.grid(row=13, column=3, sticky='w')
        Layer4 = Label(frame1, text="Layer 4")
        Layer4.grid(row=14, column=1, sticky='e') 
        Angle4_ent = Entry(frame1)
        Angle4_ent.grid(row=14, column=2, sticky='w') 
        Thickness4_ent = Entry(frame1)
        Thickness4_ent.grid(row=14, column=3, sticky='w') 
        Layer5 = Label(frame1, text="Layer 5")
        Layer5.grid(row=15, column=1, sticky='e') 
        Angle5_ent = Entry(frame1)
        Angle5_ent.grid(row=15, column=2, sticky='w') 
        Thickness5_ent = Entry(frame1)
        Thickness5_ent.grid(row=15, column=3, sticky='w')

## For 6 layers :
    elif Nb_layer==6:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e') 
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w') 
        Layer2 = Label(frame1, text="Layer 2")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.grid(row=12, column=2, sticky='w') 
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.grid(row=12, column=3, sticky='w') 
        Layer3 = Label(frame1, text="Layer 3")
        Layer3.grid(row=13, column=1, sticky='e') 
        Angle3_ent = Entry(frame1)
        Angle3_ent.grid(row=13, column=2, sticky='w') 
        Thickness3_ent = Entry(frame1)
        Thickness3_ent.grid(row=13, column=3, sticky='w')
        Layer4 = Label(frame1, text="Layer 4")
        Layer4.grid(row=14, column=1, sticky='e') 
        Angle4_ent = Entry(frame1)
        Angle4_ent.grid(row=14, column=2, sticky='w') 
        Thickness4_ent = Entry(frame1)
        Thickness4_ent.grid(row=14, column=3, sticky='w') 
        Layer5 = Label(frame1, text="Layer 5")
        Layer5.grid(row=15, column=1, sticky='e') 
        Angle5_ent = Entry(frame1)
        Angle5_ent.grid(row=15, column=2, sticky='w') 
        Thickness5_ent = Entry(frame1)
        Thickness5_ent.grid(row=15, column=3, sticky='w')
        Layer6 = Label(frame1, text="Layer 6")
        Layer6.grid(row=16, column=1, sticky='e') 
        Angle6_ent = Entry(frame1)
        Angle6_ent.grid(row=16, column=2, sticky='w') 
        Thickness6_ent = Entry(frame1)
        Thickness6_ent.grid(row=16, column=3, sticky='w') 

## For 7 layers :
    elif Nb_layer==7:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e') 
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w') 
        Layer2 = Label(frame1, text="Layer 2")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.grid(row=12, column=2, sticky='w') 
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.grid(row=12, column=3, sticky='w') 
        Layer3 = Label(frame1, text="Layer 3")
        Layer3.grid(row=13, column=1, sticky='e') 
        Angle3_ent = Entry(frame1)
        Angle3_ent.grid(row=13, column=2, sticky='w') 
        Thickness3_ent = Entry(frame1)
        Thickness3_ent.grid(row=13, column=3, sticky='w')
        Layer4 = Label(frame1, text="Layer 4")
        Layer4.grid(row=14, column=1, sticky='e') 
        Angle4_ent = Entry(frame1)
        Angle4_ent.grid(row=14, column=2, sticky='w') 
        Thickness4_ent = Entry(frame1)
        Thickness4_ent.grid(row=14, column=3, sticky='w') 
        Layer5 = Label(frame1, text="Layer 5")
        Layer5.grid(row=15, column=1, sticky='e') 
        Angle5_ent = Entry(frame1)
        Angle5_ent.grid(row=15, column=2, sticky='w') 
        Thickness5_ent = Entry(frame1)
        Thickness5_ent.grid(row=15, column=3, sticky='w')
        Layer6 = Label(frame1, text="Layer 6")
        Layer6.grid(row=16, column=1, sticky='e') 
        Angle6_ent = Entry(frame1)
        Angle6_ent.grid(row=16, column=2, sticky='w') 
        Thickness6_ent = Entry(frame1)
        Thickness6_ent.grid(row=16, column=3, sticky='w')
        Layer7 = Label(frame1, text="Layer 7")
        Layer7.grid(row=17, column=1, sticky='e') 
        Angle7_ent = Entry(frame1)
        Angle7_ent.grid(row=17, column=2, sticky='w') 
        Thickness7_ent = Entry(frame1)
        Thickness7_ent.grid(row=17, column=3, sticky='w')

## For 8 layers :
    elif Nb_layer==8:
        Layer1 = Label(frame1, text="Layer 1")
        Layer1.grid(row=11, column=1, sticky='e') 
        Angle1_ent = Entry(frame1)
        Angle1_ent.grid(row=11, column=2, sticky='w') 
        Thickness1_ent = Entry(frame1)
        Thickness1_ent.grid(row=11, column=3, sticky='w') 
        Layer2 = Label(frame1, text="Layer 2")
        Layer2.grid(row=12, column=1, sticky='e') 
        Angle2_ent = Entry(frame1)
        Angle2_ent.grid(row=12, column=2, sticky='w') 
        Thickness2_ent = Entry(frame1)
        Thickness2_ent.grid(row=12, column=3, sticky='w') 
        Layer3 = Label(frame1, text="Layer 3")
        Layer3.grid(row=13, column=1, sticky='e') 
        Angle3_ent = Entry(frame1)
        Angle3_ent.grid(row=13, column=2, sticky='w') 
        Thickness3_ent = Entry(frame1)
        Thickness3_ent.grid(row=13, column=3, sticky='w')
        Layer4 = Label(frame1, text="Layer 4")
        Layer4.grid(row=14, column=1, sticky='e') 
        Angle4_ent = Entry(frame1)
        Angle4_ent.grid(row=14, column=2, sticky='w') 
        Thickness4_ent = Entry(frame1)
        Thickness4_ent.grid(row=14, column=3, sticky='w') 
        Layer5 = Label(frame1, text="Layer 5")
        Layer5.grid(row=15, column=1, sticky='e') 
        Angle5_ent = Entry(frame1)
        Angle5_ent.grid(row=15, column=2, sticky='w') 
        Thickness5_ent = Entry(frame1)
        Thickness5_ent.grid(row=15, column=3, sticky='w')
        Layer6 = Label(frame1, text="Layer 6")
        Layer6.grid(row=16, column=1, sticky='e') 
        Angle6_ent = Entry(frame1)
        Angle6_ent.grid(row=16, column=2, sticky='w') 
        Thickness6_ent = Entry(frame1)
        Thickness6_ent.grid(row=16, column=3, sticky='w')
        Layer7 = Label(frame1, text="Layer 7")
        Layer7.grid(row=17, column=1, sticky='e') 
        Angle7_ent = Entry(frame1)
        Angle7_ent.grid(row=17, column=2, sticky='w') 
        Thickness7_ent = Entry(frame1)
        Thickness7_ent.grid(row=17, column=3, sticky='w')
        Layer8 = Label(frame1, text="Layer 8")
        Layer8.grid(row=18, column=1, sticky='e') 
        Angle8_ent = Entry(frame1)
        Angle8_ent.grid(row=18, column=2, sticky='w') 
        Thickness8_ent = Entry(frame1)
        Thickness8_ent.grid(row=18, column=3, sticky='w') 



def Calcul_height():
    Nb_layer = int(Liste_nb_layer.get())  
    global Z
    if Nb_layer==1:
        e = float(Thickness1_ent.get())
        E = [e]
        z0 = -(sum(E)/2)
        z1 = z0+E[0]
        Z = [z0, z1]
        return(Z)

    if Nb_layer==2:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        E = [e1,e2]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)

    if Nb_layer==3:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        E = [e1,e2,e3]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)

    if Nb_layer==4:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        E = [e1,e2,e3,e4]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)

    if Nb_layer==5:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        E = [e1,e2,e3,e4,e5]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)

    if Nb_layer==6:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        E = [e1,e2,e3,e4,e5,e6]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)

    if Nb_layer==7:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        e7 = float(Thickness7_ent.get())
        E = [e1,e2,e3,e4,e5,e6,e7]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)

    if Nb_layer==8:
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        e7 = float(Thickness7_ent.get())
        e8 = float(Thickness8_ent.get())
        E = [e1,e2,e3,e4,e5,e6,e7,e8]
        z0 = -(sum(E)/2)
        Z = [z0]
        i=1
        while i<=Nb_layer:
            z = Z[i-1]+E[i-1]
            Z.append(z)
            i = i+1
        return(Z)



def Display_height():
    Nb_layer = int(Liste_nb_layer.get())  
    Z = Calcul_height()   
    for i in range(Nb_layer+1):
        a = "Height Z"+f'{i}'+" = "+str(Z[i])
        lbl = Label(frame1, text=a)
        r = 10+i
        lbl.grid(row=r, column=4, sticky='w')
       
 
   

# Calculate the stiffness constants in the principal axes    
def Calcul_Q():
    EL = EL_tf.get()
    EL = float(EL)
    ET = ET_tf.get()
    ET = float(ET)
    GLT = GLT_tf.get()
    GLT = float(GLT)
    VLT = VLT_tf.get()
    VLT = float(VLT)
    global Q11
    global Q22
    global Q12
    global Q66
    Q11 = (EL)/(1-(ET/EL)*(VLT)**2)
    Q22 = (ET/EL)*Q11
    Q12 = VLT*Q22
    Q66 = GLT
    # messagebox.showinfo('Stiffness constants, principal axes', f' Q11 = {Q11} GPa \n Q22 = {Q22} GPa \n Q12 = {Q12} GPa \n Q66 = {Q66} GPa')
    return(Q11,Q22,Q12,Q66)

    

def Calcul_Q_prime(Angle):
    """Calls the Calcul_Q() function"""
    Q11, Q22, Q12, Q66 = Calcul_Q()
    Angle_rad = Angle*(np.pi/180)
    c = np.cos(Angle_rad)
    s = np.sin(Angle_rad)
    Qxx = Q11*c**4 + 2*(Q12+2*Q66)*s**2*c**2 + Q22*s**4
    Qxy = (Q11+Q22-4*Q66)*s**2*c**2 + Q12*(s**4+c**4)
    Qyy = Q11*s**4 + 2*(Q12+2*Q66)*s**2*c**2 + Q22*c**4
    Qxz = (Q11-Q12-2*Q66)*s*c**3 + (Q12-Q22+2*Q66)*s**3*c
    Qyz = (Q11-Q12-2*Q66)*s**3*c + (Q12-Q22+2*Q66)*s*c**3
    Qzz = (Q11+Q22-2*Q12-2*Q66)*s**2*c**2 + Q66*(s**4 + c**4)
    Q_prime = [Qxx, Qyy, Qxy, Qxz, Qyz, Qzz]
    # messagebox.showinfo('Stiffness constants, layer axes', f' Qxx_prime = {Qxx} GPa \n Qyy_prime = {Qyy} GPa \n Qxy_prime = {Qxy} GPa \n Qxz_prime = {Qxz} GPa \n Qyz_prime = {Qyz} GPa \n Qzz_prime = {Qzz} GPa')
    return(Q_prime)



def Calcul_A():
    Nb_layer = int(Liste_nb_layer.get())  
    
    if Nb_layer==1:
        Z = Calcul_height()
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        A11 = Q_prime1[0]*(Z[1]-Z[0])
        A22 = Q_prime1[1]*(Z[1]-Z[0])
        A12 = Q_prime1[2]*(Z[1]-Z[0])
        A16 = Q_prime1[3]*(Z[1]-Z[0])
        A26 = Q_prime1[4]*(Z[1]-Z[0])
        A66 = Q_prime1[5]*(Z[1]-Z[0])
        A_c1 = [A11, A22, A12, A16, A26, A66]
        return(A_c1)

    if Nb_layer==2:
        # Loading the data
        Z = Calcul_height()
        print(Z)
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)             
        # Calcul
        A_c2 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1]
            A_c2.append(a)
        return(A_c2)
        
    if Nb_layer==3:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        # Calculation part
        A_c3 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2]
            A_c3.append(a)
        return(A_c3)        

    if Nb_layer==4:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        # Calculation part
        A_c4 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]
            A_c4.append(a)
        return(A_c4)

    if Nb_layer==5:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        # Calculation part
        A_c5 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4]
            A_c5.append(a)
        return(A_c5)    
  
    if Nb_layer==6:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        # Calculation part
        A_c6 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3] + Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5]
            A_c6.append(a)
        return(A_c6)     
  
    if Nb_layer==7:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Angle7 = int(Angle7_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        Q_prime7 = Calcul_Q_prime(Angle7)
        # Calculation part
        A_c7 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5] + Q_prime7[i]*Coeff[6]
            A_c7.append(a)
        return(A_c7)      
  
    if Nb_layer==8:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Angle7 = int(Angle7_ent.get())
        Angle8 = int(Angle8_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        Q_prime7 = Calcul_Q_prime(Angle7)
        Q_prime8 = Calcul_Q_prime(Angle8)
        # Calculation part
        A_c8 = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1] - Z[i]
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5] + Q_prime7[i]*Coeff[6] + Q_prime8[i]*Coeff[7]
            A_c8.append(a)
        return(A_c8)  
    
      

def Calcul_B():
    Nb_layer = int(Liste_nb_layer.get())  
    
    if Nb_layer==1:
        Z = Calcul_height()
        print(Z)
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        print(Q_prime1)
        B11 = (1/2)*Q_prime1[0]*(Z[1]**2-Z[0]**2)
        B22 = (1/2)*Q_prime1[1]*(Z[1]**2-Z[0]**2)
        B12 = (1/2)*Q_prime1[2]*(Z[1]**2-Z[0]**2)
        B16 = (1/2)*Q_prime1[3]*(Z[1]**2-Z[0]**2)
        B26 = (1/2)*Q_prime1[4]*(Z[1]**2-Z[0]**2)
        B66 = (1/2)*Q_prime1[5]*(Z[1]**2-Z[0]**2)
        B = [B11, B22, B12, B16, B26, B66]
        return(B)

    if Nb_layer==2:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)             
        # Calcul
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)           
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1])
            B.append(a)
        return(B)
        
    if Nb_layer==3:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)          
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2])
            B.append(a)
        return(B)        

    if Nb_layer==4:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)           
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3])
            B.append(a)
        return(B)

    if Nb_layer==5:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)           
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4])
            B.append(a)
        return(B)    
  
    if Nb_layer==6:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)          
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3] + Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5])
            B.append(a)
        return(B)     
  
    if Nb_layer==7:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Angle7 = int(Angle7_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        Q_prime7 = Calcul_Q_prime(Angle7)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)          
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5] + Q_prime7[i]*Coeff[6])
            B.append(a)
        return(B)      
  
    if Nb_layer==8:    
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Angle7 = int(Angle7_ent.get())
        Angle8 = int(Angle8_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        Q_prime7 = Calcul_Q_prime(Angle7)
        Q_prime8 = Calcul_Q_prime(Angle8)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = Z[i+1]**2 - Z[i]**2
            Coeff.append(e)           
        for i in range(6):
            a = (1/2)*(Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5] + Q_prime7[i]*Coeff[6] + Q_prime8[i]*Coeff[7])
            B.append(a)
        return(B)      



def Calcul_D():
    Nb_layer = int(Liste_nb_layer.get())  
    
    if Nb_layer==1:
        Z = Calcul_height()
        print(Z)
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        print(Q_prime1)
        D11 = (1/3)*Q_prime1[0]*(Z[1]**3-Z[0]**3)
        D22 = (1/3)*Q_prime1[1]*(Z[1]**3-Z[0]**3)
        D12 = (1/3)*Q_prime1[2]*(Z[1]**3-Z[0]**3)
        D16 = (1/3)*Q_prime1[3]*(Z[1]**3-Z[0]**3)
        D26 = (1/3)*Q_prime1[4]*(Z[1]**3-Z[0]**3)
        D66 = (1/3)*Q_prime1[5]*(Z[1]**3-Z[0]**3)
        D = [D11, D22, D12, D16, D26, D66]
        return(D)

    if Nb_layer==2:
        # Loading the data
        Z = Calcul_height()
        print(Z)
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)             
        # Calcul
        D = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)           
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1]
            D.append(a)
        return(D)
        
    if Nb_layer==3:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)         
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2]
            B.append(a)
        return(B)        

    if Nb_layer==4:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)          
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]
            B.append(a)
        return(B)

    if Nb_layer==5:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)          
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4]
            B.append(a)
        return(B)    
  
    if Nb_layer==6:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)         
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3] + Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5]
            B.append(a)
        return(B)     
  
    if Nb_layer==7:
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Angle7 = int(Angle7_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        Q_prime7 = Calcul_Q_prime(Angle7)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)         
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5] + Q_prime7[i]*Coeff[6]
            B.append(a)
        return(B)      
  
    if Nb_layer==8:    
        # Loading the data
        Z = Calcul_height()
        Angle1 = int(Angle1_ent.get())
        Angle2 = int(Angle2_ent.get())
        Angle3 = int(Angle3_ent.get())
        Angle4 = int(Angle4_ent.get())
        Angle5 = int(Angle5_ent.get())
        Angle6 = int(Angle6_ent.get())
        Angle7 = int(Angle7_ent.get())
        Angle8 = int(Angle8_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle1)
        Q_prime2 = Calcul_Q_prime(Angle2)
        Q_prime3 = Calcul_Q_prime(Angle3)
        Q_prime4 = Calcul_Q_prime(Angle4)
        Q_prime5 = Calcul_Q_prime(Angle5)
        Q_prime6 = Calcul_Q_prime(Angle6)
        Q_prime7 = Calcul_Q_prime(Angle7)
        Q_prime8 = Calcul_Q_prime(Angle8)
        # Calculation part
        B = []
        Coeff = []
        for i in range(Nb_layer):
            e = (1/3)*(Z[i+1]**3 - Z[i]**3)
            Coeff.append(e)          
        for i in range(6):
            a = Q_prime1[i]*Coeff[0] + Q_prime2[i]*Coeff[1] + Q_prime3[i]*Coeff[2] + Q_prime4[i]*Coeff[3]+ Q_prime5[i]*Coeff[4] + Q_prime6[i]*Coeff[5] + Q_prime7[i]*Coeff[6] + Q_prime8[i]*Coeff[7]
            B.append(a)
        return(B)  
    


def Calcul_H():
    A_0 = Calcul_A()
    A_1 = np.array(A_0)
    A = A_1*1000000
    
    B_0 = Calcul_B()
    B_1 = np.array(B_0)
    B = B_1*1000
    
    D = Calcul_D()
    
    H = np.array(([A[0],A[2],A[3],B[0],B[2],B[3]],
                  [A[2],A[1],A[4],B[2],B[1],B[4]],
                  [A[3],A[4],A[5],B[3],B[4],B[5]],
                  [B[0],B[2],B[3],D[0],D[2],D[3]],
                  [B[2],B[1],B[4],D[2],D[1],D[4]],
                  [B[3],B[4],B[5],D[3],D[4],D[5]]))    
    return(H)
# H_inv = np.linalg.inv(H)   



def Loads_vector():
    """
    Nx, Ny, Nz are entered as TOTAL forces (N) applied on the part.
    Classical Laminate Theory (CLT) works with running loads, i.e. force
    PER UNIT WIDTH (N/mm), because the A/B/D stiffness matrices are
    themselves computed per unit width (see Calcul_A/B/D). So the total
    force must be divided by the part's width (Largeur_tf, in mm) before
    it goes into the CI vector. If Largeur_tf is left at 1 mm, Nx/Ny/Nz
    are used exactly as entered (i.e. already treated as running loads).
    Mt, Mfy, Mfz are left untouched (entered directly in N.m as before).
    """
    Largeur = float(Largeur_tf.get())
    Nx = 1000*int(Nx_tf.get())/Largeur
    Ny = 1000*int(Ny_tf.get())/Largeur
    Nz = 1000*int(Nz_tf.get())/Largeur
    Mt = 1000*int(Mt_tf.get())
    Mfy = 1000*int(Mfy_tf.get())
    Mfz = 1000*int(Mfz_tf.get()) 
    CI = np.array(([Nx],
                   [Ny],
                   [Nz],
                   [Mt],
                   [Mfy],
                   [Mfz]))
    return(CI)



def Calcul_epsilon_kappa0():
    H = Calcul_H()
    H_inv = np.linalg.inv(H)    
    CI = Loads_vector()    
    Epsilon_kappa = np.dot(H_inv,CI)
    return(Epsilon_kappa)



# Calculate the strains in the principal axes of the LAMINATE
def Calcul_epsilon(z):
    """Enter z in mm"""
    a = z*10**(-3)
    Eps_kappa0 = Calcul_epsilon_kappa0()
    Epsxx = Eps_kappa0[0,0] + a*Eps_kappa0[3,0]
    Epsyy = Eps_kappa0[1,0] + a*Eps_kappa0[4,0]
    Gammaxy = Eps_kappa0[2,0] + a*Eps_kappa0[5,0]

    Epsxx_epsyy_gammaxy = np.array(([Epsxx],
                                    [Epsyy],
                                    [Gammaxy]))
    return(Epsxx_epsyy_gammaxy)



def Calcul_T(Angle):
    Angle_rad = Angle*(np.pi/180)
    cos= np.cos(Angle_rad)
    sin = np.sin(Angle_rad)
    
    a, b, c = cos**2, sin**2, cos*sin
    d, e, f = sin**2, cos**2, -cos*sin
    g, h, i = -2*cos*sin, 2*cos*sin, cos**2-sin**2
    
    T = np.array(([a,b,c],
                  [d,e,f],
                  [g,h,i]))
    return(T)



def Calcul_eps_layer(z, Angle):
    """Returns Eps_L, Eps_T and Gamma_LT"""
    n = int(Liste_nb_layer.get())     
    # Invariants
    Eps_kap0 = Calcul_epsilon_kappa0()    
    Eps0 = np.array((Eps_kap0[0],
                     Eps_kap0[1],
                     Eps_kap0[2]))
    Kappa0 = np.array((Eps_kap0[3],
                     Eps_kap0[4],
                     Eps_kap0[5]))
    
    z = float(z)*10**(-3)
    T = Calcul_T(Angle) 
    Eps_k = np.dot(T,Eps0)
    Kappa_k = np.dot(T,Kappa0)
    Eps_layer = np.array(([Eps_k[0]+z*Kappa_k[0]],
                           [Eps_k[1]+z*Kappa_k[1]],
                           [Eps_k[2]+z*Kappa_k[2]]))
    return(Eps_layer)



def Calcul_eps_layer_totales():
    """Returns a matrix with 3 rows and 2*n columns"""
    n = int(Liste_nb_layer.get())
    Z = Calcul_height()
    
    if n==1: 
        z = float(Z[0])
        Angle = int(Angle1_ent.get())
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Angle = int(Angle1_ent.get())
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        M = np.array(([Eps_layer0, Eps_layer1]))            
        return(M)

    if n==2:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)             
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2]))            
        return(M)

    if n==3:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)    

        Angle = int(Angle3_ent.get())
        z = float(Z[2])        
        Eps_layer2_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[3])        
        Eps_layer3 = Calcul_eps_layer(z, Angle)      
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2, Eps_layer2_bis, Eps_layer3]))            
        return(M)

    if n==4:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)    

        Angle = int(Angle3_ent.get())
        z = float(Z[2])        
        Eps_layer2_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[3])        
        Eps_layer3 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle4_ent.get())
        z = float(Z[3])        
        Eps_layer3_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[4])        
        Eps_layer4 = Calcul_eps_layer(z, Angle)   
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2, Eps_layer2_bis, Eps_layer3, Eps_layer3_bis, Eps_layer4]))            
        return(M)

    if n==5:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)    

        Angle = int(Angle3_ent.get())
        z = float(Z[2])        
        Eps_layer2_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[3])        
        Eps_layer3 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle4_ent.get())
        z = float(Z[3])        
        Eps_layer3_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[4])        
        Eps_layer4 = Calcul_eps_layer(z, Angle)   
        
        Angle = int(Angle5_ent.get())
        z = float(Z[4])        
        Eps_layer4_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[5])        
        Eps_layer5 = Calcul_eps_layer(z, Angle)          
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2, Eps_layer2_bis, Eps_layer3, Eps_layer3_bis, Eps_layer4, Eps_layer4_bis, Eps_layer5]))            
        return(M)

    if n==6:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)    

        Angle = int(Angle3_ent.get())
        z = float(Z[2])        
        Eps_layer2_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[3])        
        Eps_layer3 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle4_ent.get())
        z = float(Z[3])        
        Eps_layer3_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[4])        
        Eps_layer4 = Calcul_eps_layer(z, Angle)   
        
        Angle = int(Angle5_ent.get())
        z = float(Z[4])        
        Eps_layer4_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[5])        
        Eps_layer5 = Calcul_eps_layer(z, Angle)     
        
        Angle = int(Angle6_ent.get())
        z = float(Z[5])        
        Eps_layer5_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[6])        
        Eps_layer6 = Calcul_eps_layer(z, Angle)          
        
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2, Eps_layer2_bis, Eps_layer3, Eps_layer3_bis, Eps_layer4, Eps_layer4_bis, Eps_layer5, Eps_layer5_bis, Eps_layer6]))            
        return(M)

    if n==7:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)    

        Angle = int(Angle3_ent.get())
        z = float(Z[2])        
        Eps_layer2_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[3])        
        Eps_layer3 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle4_ent.get())
        z = float(Z[3])        
        Eps_layer3_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[4])        
        Eps_layer4 = Calcul_eps_layer(z, Angle)   
        
        Angle = int(Angle5_ent.get())
        z = float(Z[4])        
        Eps_layer4_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[5])        
        Eps_layer5 = Calcul_eps_layer(z, Angle)     
        
        Angle = int(Angle6_ent.get())
        z = float(Z[5])        
        Eps_layer5_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[6])        
        Eps_layer6 = Calcul_eps_layer(z, Angle)          

        Angle = int(Angle7_ent.get())
        z = float(Z[6])        
        Eps_layer6_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[7])        
        Eps_layer7 = Calcul_eps_layer(z, Angle) 
        
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2, Eps_layer2_bis, Eps_layer3, Eps_layer3_bis, Eps_layer4, Eps_layer4_bis, Eps_layer5, Eps_layer5_bis, Eps_layer6, Eps_layer6_bis, Eps_layer7]))            
        return(M)    

    if n==8:
        Angle = int(Angle1_ent.get())
        z = float(Z[0])        
        Eps_layer0 = Calcul_eps_layer(z, Angle)
        z = float(Z[1])
        Eps_layer1 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle2_ent.get())
        z = float(Z[1])        
        Eps_layer1_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[2])        
        Eps_layer2 = Calcul_eps_layer(z, Angle)    

        Angle = int(Angle3_ent.get())
        z = float(Z[2])        
        Eps_layer2_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[3])        
        Eps_layer3 = Calcul_eps_layer(z, Angle)
        
        Angle = int(Angle4_ent.get())
        z = float(Z[3])        
        Eps_layer3_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[4])        
        Eps_layer4 = Calcul_eps_layer(z, Angle)   
        
        Angle = int(Angle5_ent.get())
        z = float(Z[4])        
        Eps_layer4_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[5])        
        Eps_layer5 = Calcul_eps_layer(z, Angle)     
        
        Angle = int(Angle6_ent.get())
        z = float(Z[5])        
        Eps_layer5_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[6])        
        Eps_layer6 = Calcul_eps_layer(z, Angle)          

        Angle = int(Angle7_ent.get())
        z = float(Z[6])        
        Eps_layer6_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[7])        
        Eps_layer7 = Calcul_eps_layer(z, Angle) 
        
        Angle = int(Angle8_ent.get())
        z = float(Z[7])        
        Eps_layer7_bis = Calcul_eps_layer(z, Angle)        
        z = float(Z[8])        
        Eps_layer8 = Calcul_eps_layer(z, Angle)        
        
        M = np.array(([Eps_layer0, Eps_layer1, Eps_layer1_bis, Eps_layer2, Eps_layer2_bis, Eps_layer3, Eps_layer3_bis, Eps_layer4, Eps_layer4_bis, Eps_layer5, Eps_layer5_bis, Eps_layer6, Eps_layer6_bis, Eps_layer7, Eps_layer7_bis, Eps_layer8]))            
        return(M)  


def Calcul_stress_axe_strat(z, Angle):
    print("Calculating stress")
    Eps = Calcul_epsilon(z)
    print("Epsilon = ", Eps, "\n")
    
    Qp = Calcul_Q_prime(Angle)
    Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Qp[0], Qp[1], Qp[2], Qp[3], Qp[4], Qp[5]
    Q_prime = np.array(([Qxx, Qxy, Qxz],
                        [Qxy, Qyy, Qyz],
                        [Qxz, Qyz, Qzz]))
    print("Qprime = ", Q_prime)

    Sigma = np.dot(Q_prime, Eps)
    print("Sigma = ", Sigma, "\n")
    
    print("Type of sigma:", Sigma)
    return(Sigma)



def Show_info():
    A = Calcul_A()
    B = Calcul_B()
    D = Calcul_D()
    
    # Display the calculated values
    Q11, Q22, Q12, Q66 = Calcul_Q()
    messagebox.showinfo('Stiffness constants, principal axes', f' Q11 = {Q11} GPa \n Q22 = {Q22} GPa \n Q12 = {Q12} GPa \n Q66 = {Q66} GPa')

    Angle = int(Angle1_ent.get())
    Q_prime = Calcul_Q_prime(Angle)
    Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime[0], Q_prime[1], Q_prime[2], Q_prime[3], Q_prime[4], Q_prime[5]
    messagebox.showinfo('Stiffness constants, LAYER 1 axes', f' Qxx_prime = {Qxx} GPa \n Qyy_prime = {Qyy} GPa \n Qxy_prime = {Qxy} GPa \n Qxz_prime = {Qxz} GPa \n Qyz_prime = {Qyz} GPa \n Qzz_prime = {Qzz} GPa')

    Angle = int(Angle2_ent.get())
    Q_prime = Calcul_Q_prime(Angle)
    Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime[0], Q_prime[1], Q_prime[2], Q_prime[3], Q_prime[4], Q_prime[5]
    messagebox.showinfo('Stiffness constants, LAYER 2 axes', f' Qxx_prime = {Qxx} GPa \n Qyy_prime = {Qyy} GPa \n Qxy_prime = {Qxy} GPa \n Qxz_prime = {Qxz} GPa \n Qyz_prime = {Qyz} GPa \n Qzz_prime = {Qzz} GPa')
 
    Angle = int(Angle3_ent.get())
    Q_prime = Calcul_Q_prime(Angle)
    Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime[0], Q_prime[1], Q_prime[2], Q_prime[3], Q_prime[4], Q_prime[5]
    messagebox.showinfo('Stiffness constants, LAYER 3 axes', f' Qxx_prime = {Qxx} GPa \n Qyy_prime = {Qyy} GPa \n Qxy_prime = {Qxy} GPa \n Qxz_prime = {Qxz} GPa \n Qyz_prime = {Qyz} GPa \n Qzz_prime = {Qzz} GPa')
 
    Angle = int(Angle4_ent.get())
    Q_prime = Calcul_Q_prime(Angle)
    Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime[0], Q_prime[1], Q_prime[2], Q_prime[3], Q_prime[4], Q_prime[5]
    messagebox.showinfo('Stiffness constants, LAYER 4 axes', f' Qxx_prime = {Qxx} GPa \n Qyy_prime = {Qyy} GPa \n Qxy_prime = {Qxy} GPa \n Qxz_prime = {Qxz} GPa \n Qyz_prime = {Qyz} GPa \n Qzz_prime = {Qzz} GPa')
    
    messagebox.showinfo('Matrix A', f' A = {A} *10e6 N/m \n')
    messagebox.showinfo('Matrix B', f' B = {B} *10e3 N \n')
    messagebox.showinfo('Matrix D', f' D = {D} N.m \n')
    
    H = Calcul_H()
    messagebox.showinfo('Matrix H', f' H = {H} \n')

    Eps_kap0 = Calcul_epsilon_kappa0()
    messagebox.showinfo('Strain and kappa matrix', f' Eps_kap0 = {Eps_kap0} \n')



def Display_Q():
    Q11, Q22, Q12, Q66 = Calcul_Q()
    Q = np.array(([round(Q11,2), round(Q12,2), 0],
                  [round(Q12,2), round(Q22,2), 0],
                  [0, 0, round(Q66,2)]))
    messagebox.showinfo('Displaying Q (GPa)', f' Q = \n{Q}')       
   
    

def Display_Q_prime():
    Nb_layer = int(Liste_nb_layer.get())    
    
    if Nb_layer==1:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==2:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo("Displaying Q' layer 1 (GPa)", f" Q1' = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==3:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 3 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==4:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 3 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 4 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==5:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 3 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 4 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 5 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==6:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 3 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 4 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 5 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle6_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 6 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==7:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 3 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 4 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 5 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle6_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 6 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle7_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 7 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")

    elif Nb_layer==8:
        Angle = int(Angle1_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 1 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle2_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 2 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle3_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 3 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle4_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 4 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle5_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 5 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle6_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 6 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle7_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 7 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")
        Angle = int(Angle8_ent.get())
        Q_prime1 = Calcul_Q_prime(Angle)
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = Q_prime1[0], Q_prime1[1], Q_prime1[2], Q_prime1[3], Q_prime1[4], Q_prime1[5]
        Qxx, Qyy, Qxy, Qxz, Qyz, Qzz = round(Qxx,3), round(Qyy,3), round(Qxy,3), round(Qxz,3), round(Qyz,3), round(Qzz,3)
        Q_prime1 = np.array(([Qxx, Qxy, Qxz],
                            [Qxy, Qyy, Qyz],
                            [Qxz, Qyz, Qzz]))
        messagebox.showinfo(f"Displaying Q'_{Angle}° layer 8 (GPa)", f" Q'_{Angle}° = \n{Q_prime1}")



def Display_H():
    H = Calcul_H()
    messagebox.showinfo('Displaying H', f' H = \n{H}')  
    
    

def Display_eps_kap0():
    Epsilon_kappa0 = Calcul_epsilon_kappa0()
    Epsilon_kappa0 = Epsilon_kappa0
    messagebox.showinfo('Displaying Epsilon and Kappa 0', f' Vecteur Epsilon_kappa0 (eps en mm) = \n{Epsilon_kappa0}')  
    


def Display_eps_axe_laminate():  
# Creating window 1: global strain calculation (laminate axes)    
    # ws1 is the window that displays strains in the laminate axes (global)
    global ws1
    ws1 = Toplevel(ws)
    ws1.title("Strain calculations in the laminate axes")
    n = Liste_nb_layer.get()
    # Center the window
    screen_x = int(ws1.winfo_screenwidth())
    screen_y = int(ws1.winfo_screenheight())
    window_x = 500
    window_y = 200
    posX = (screen_x//2) - (window_x//2)
    posY = (screen_y//2) - (window_y//2) - 75
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    ws1.geometry(geo)    

# Displaying the results
    # Column titles
    decalageX = 20
    decalageY = 5
    Eps_xx = Label(ws1, text="Epsilon XX:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_xx.grid(row=0, column=0, sticky='e', ipady=decalageY)   
    Eps_yy = Label(ws1, text="Epsilon YY:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_yy.grid(row=0, column=1, sticky='e', ipady=decalageY)    
    Gamma_xy = Label(ws1, text="Gamma XY:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_xy.grid(row=0, column=2, sticky='e', ipady=decalageY)

    # Entry zone and instructions
    Z_label = Label(ws1, text="Enter height z (in mm):")
    Z_label.grid(row=4, column=0, columnspan=2, ipadx=5, pady=5)
    
    global Z_ent
    Z_ent = DoubleVar()
    Z_ent = Entry(ws1)
    Z_ent.insert(0,"2.5") # CHANGE HERE
    Z_ent.grid(row=4, column=1, columnspan=2)

    Eps_xx_lbl = Label(ws1, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_xx_lbl.grid(row=1, column=0)
    Eps_yy_lbl = Label(ws1, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_yy_lbl.grid(row=1, column=1)        
    Gamma_xy_lbl = Label(ws1, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_xy_lbl.grid(row=1, column=2)

    Calcul1_btn = Button(ws1, text="Calculate", command=Calcul1)
    Calcul1_btn.grid(row=5, column=0, columnspan=4, ipadx=35, ipady=4)


def Calcul1():
    print("Running Calculation 1")
    decalageX = 20
    z = float(Z_ent.get())
    Liste_Z = Calcul_height()
    Zinf, Zsup = float(Liste_Z[0]), float(Liste_Z[-1])
    Res = Calcul_epsilon(z)
    Eps_xx = Res[0]
    Eps_xx = round(1000*Eps_xx[0],2)
    Eps_yy = Res[1]
    Eps_yy = round(1000*Eps_yy[0],2)
    Gamma_xy = Res[2]
    Gamma_xy = round(1000*Gamma_xy[0],2)

# New strain display
    if z>=Zinf and z<=Zsup:    
        Eps_xx_lbl = Label(ws1, text=f'{Eps_xx}'+" mm", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
        Eps_xx_lbl.grid(row=1, column=0)
        Eps_yy_lbl = Label(ws1, text=f'{Eps_yy}'+" mm", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
        Eps_yy_lbl.grid(row=1, column=1)       
        Gamma_xy_lbl = Label(ws1, text=f'{Gamma_xy}'+" mm", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
        Gamma_xy_lbl.grid(row=1, column=2)
    else:
        messagebox.showerror('Python Error', 'Error: the value of z is invalid (outside the material)! \n It must satisfy '+f'{Zinf}'+" < z < "+f'{Zsup}')

        
    
def Display_eps_axe_layer():
# Creating window 2: strain calculation in each layer, in its own local axes    
    # ws2 is the window that displays strains in each layer's own axes
    global ws2
    ws2 = Toplevel(ws)
    ws2.title("Strain calculations in each layer's axes")
    n = int(Liste_nb_layer.get())
    # Center the window
    screen_x = int(ws2.winfo_screenwidth())
    screen_y = int(ws2.winfo_screenheight())
    window_x = 504
    window_y = 500
    posX = (screen_x//2) - (window_x//2)
    posY = (screen_y//2) - (window_y//2) - 75
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    ws2.geometry(geo)  

# Displaying the results
    # Column titles
    decalageX = 21
    decalageY = 20
    Eps_L = Label(ws2, text="Epsilon L:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_L.place(x=0, y=0)   
    Eps_T = Label(ws2, text="Epsilon T:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_T.place(x=165, y=0)    
    Gamma_LT = Label(ws2, text="Gamma LT:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_LT.place(x=330, y=0)
    # Label for displaying results
    Eps_L_lbl = Label(ws2, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_L_lbl.place(x=0, y=decalageY) 
    Eps_T_lbl = Label(ws2, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_T_lbl.place(x=165, y=decalageY)          
    Gamma_LT_lbl = Label(ws2, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_LT_lbl.place(x=330, y=decalageY)

# Creating the entry zones and instructions
    # Which layer is the calculation for?
    Liste_layer_lbl = Label(ws2, text="◉ Which layer?")
    Liste_layer_lbl.place(x=110, y=2.5*decalageY)    
    global Liste_layer
    Liste_layer = IntVar()
    Nb_layer = []
    for i in range(n):
        Nb_layer.append(i+1)   
    Liste_layer = ttk.Combobox(ws2, values=Nb_layer)
    Liste_layer.current(n-1)
    Liste_layer.place(x=260, y=2.5*decalageY)
    
    # Angle handling
    c = int(Liste_layer.get())
    Angle_ws2_lbl = Label(ws2, text="◉ Layer angle (in °)?")
    Angle_ws2_lbl.place(x=110, y=4*decalageY)     
    global Angle_ws2
    Angle_ws2 = IntVar()
    Angle_ws2 = Entry(ws2, text="")
    Angle_ws2.insert(0,"30")
    Angle_ws2.place(x=260, y=4*decalageY)    

    # Height z handling
    Z_lbl = Label(ws2, text="◉ Height z (in mm)?")
    Z_lbl.place(x=110, y=5.5*decalageY) 
    global Z_ent
    Z_ent = DoubleVar()
    Z_ent = Entry(ws2)
    Z_ent.insert(0,"2.5") # CHANGE HERE
    Z_ent.place(x=260, y=5.5*decalageY) 

    # Entry validation button
    Validation_ws2_btn = Button(ws2, text="Validate", height=1, width=15, command=Calcul2)
    Validation_ws2_btn.place(x=201, y=7.2*decalageY)

# Block separator
    Separator = Label(ws2, text="_____________________________________________________________________________________________________")
    Separator.place(x=0, y=8.5*decalageY)



#___________________________________ Decision-support info for entry selection _______________________________________
    Title_aide = Label(ws2, text="Laminate data summary", font=("ar 10 bold", 11))
    Title_aide.place(x=150, y=9.8*decalageY)
    # Label for angles and thicknesses
    h=1
    w=17
    decalageY2 = 20
    Angle_lb = Label(ws2, text="Angles", height=h, width=w, borderwidth=2, relief="ridge")
    Angle_lb.place(x=100, y=11.2*decalageY2)   
    Thickness_lbl = Label(ws2, text="Thicknesses", height=h, width=w, borderwidth=2, relief="ridge")
    Thickness_lbl.place(x=220, y=11.2*decalageY2)
    Height_lbl = Label(ws2, text="Heights Zi", height=h, width=w, borderwidth=2, relief="ridge")
    Height_lbl.place(x=340, y=11.2*decalageY2)    

    if n==1:
        x1 = int(Angle1_ent.get())
        Angles=[x1]       
        e1 = float(Thickness1_ent.get())
        Thicknesses=[e1]         
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    elif n==2:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        Angles=[x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        Thicknesses=[e2,e1]       
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    elif n==3:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        Angles=[x3,x2,x1]     
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        Thicknesses=[e3,e2,e1]      
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
    
    elif n==4:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        Angles=[x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        Thicknesses=[e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
            
    elif n==5:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        Angles=[x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        Thicknesses=[e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
            
    elif n==6:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        x6 = int(Angle6_ent.get())
        Angles=[x6,x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        Thicknesses=[e6,e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
            
    elif n==7:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        x6 = int(Angle6_ent.get())
        x7 = int(Angle7_ent.get())
        Angles=[x7,x6,x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        e7 = float(Thickness7_ent.get())
        Thicknesses=[e7,e6,e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    elif n==8:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        x6 = int(Angle6_ent.get())
        x7 = int(Angle7_ent.get())
        x8 = int(Angle8_ent.get())
        Angles=[x8,x7,x6,x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        e7 = float(Thickness7_ent.get())
        e8 = float(Thickness8_ent.get())
        Thicknesses=[e8,e7,e6,e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])


    indices = []      
    for i in range(n):
        indices.insert(0,i+1)
      
    for i in range(n):
        j=i+1
        indic = indices[i]
        Layer = Label(ws2, text="Layer "+f'{indic}'+" :", height=h, width=13, borderwidth=2, relief="ridge")
        Layer.place(x=0, y=(11.2+1.2*j)*decalageY2)      
        
        Var = Angles[i]
        Angle = Label(ws2, text=f"{Var}"+"°", borderwidth=3, width=w-1, relief="sunken")
        Angle.place(x=100, y=(11.2+1.2*j)*decalageY2) 

        Var = Thicknesses[i]
        Thickness = Label(ws2, text=f"{Var}"+" mm", borderwidth=3, width=w-1, relief="sunken")
        Thickness.place(x=223, y=(11.2+1.2*j)*decalageY2)

        Var1 = Liste_Z[i]
        Var2 = Liste_Z[j]
        Height = Label(ws2, text=f"{Var1}"+"  ≤  "+"z"+"  ≤  "+f"{Var2}", borderwidth=3, width=w-1, relief="sunken")
        Height.place(x=345, y=(11.2+1.2*j)*decalageY2)        

    

def Calcul2():
    decalageX = 21
    decalageY = 20
    c = int(Liste_layer.get())
    z = float(Z_ent.get())
    Angle = int(Angle_ws2.get())
    
# Partie calcul
    Eps_layer = Calcul_eps_layer(z, Angle)
    Eps_L = Eps_layer[0]
    Eps_L = round(1000*float(Eps_L[0]),2)
    Eps_T = Eps_layer[1]
    Eps_T = round(1000*float(Eps_T[0]),2)
    Gamma_LT = Eps_layer[2]
    Gamma_LT = round(1000*float(Gamma_LT[0]),2)
    
# Updating the results    
    Eps_L_lbl = Label(ws2, text=f'{Eps_L}'+" mm", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_L_lbl.place(x=0, y=decalageY) 
    Eps_T_lbl = Label(ws2, text=f'{Eps_T}'+" mm", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_T_lbl.place(x=165, y=decalageY)          
    Gamma_LT_lbl = Label(ws2, text=f'{Gamma_LT}'+" mm", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_LT_lbl.place(x=330, y=decalageY)    



def Display_stresss_axe_layer():
# Creating window 3: stress calculation in each layer, in its own local axes    
    # ws2 is the window that displays strains in each layer's own axes
    global ws3
    ws3 = Toplevel(ws)
    ws3.title("Strain calculations in each layer's axes")
    n = int(Liste_nb_layer.get())
    # Center the window
    screen_x = int(ws3.winfo_screenwidth())
    screen_y = int(ws3.winfo_screenheight())
    window_x = 504
    window_y = 500
    posX = (screen_x//2) - (window_x//2)
    posY = (screen_y//2) - (window_y//2) - 75
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    ws3.geometry(geo)  

# Displaying the results
    # Column titles
    decalageX = 21
    decalageY = 20
    Eps_L = Label(ws3, text="Sigma xx:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_L.place(x=0, y=0)   
    Eps_T = Label(ws3, text="Sigma yy:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_T.place(x=165, y=0)    
    Gamma_LT = Label(ws3, text="Sigma xy:", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_LT.place(x=330, y=0)
    # Label for displaying results
    Eps_L_lbl = Label(ws3, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_L_lbl.place(x=0, y=decalageY) 
    Eps_T_lbl = Label(ws3, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Eps_T_lbl.place(x=165, y=decalageY)          
    Gamma_LT_lbl = Label(ws3, text="......", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Gamma_LT_lbl.place(x=330, y=decalageY)


# Creating the entry zones and instructions
    # Which layer is the calculation for?
    Liste_layer_lbl = Label(ws3, text="◉ Which layer?")
    Liste_layer_lbl.place(x=110, y=2.5*decalageY)    
    global Liste_layer3
    Liste_layer3 = IntVar()
    Nb_layer = []
    for i in range(n):
        Nb_layer.append(i+1)   
    Liste_layer3 = ttk.Combobox(ws3, values=Nb_layer)
    Liste_layer3.current(n-1)
    Liste_layer3.place(x=260, y=2.5*decalageY)
    
    # Angle handling
    c = int(Liste_layer3.get())
    Angle_ws3_lbl = Label(ws3, text="◉ Layer angle (in °)?")
    Angle_ws3_lbl.place(x=110, y=4*decalageY)     
    global Angle_ws3
    Angle_ws3 = IntVar()
    Angle_ws3 = Entry(ws3, text="")
    Angle_ws3.insert(0,"30")
    Angle_ws3.place(x=260, y=4*decalageY)    

    # Height z handling
    Z_lbl = Label(ws3, text="◉ Height z (in mm)?")
    Z_lbl.place(x=110, y=5.5*decalageY) 
    global Z_ent3
    Z_ent3 = DoubleVar()
    Z_ent3 = Entry(ws3)
    Z_ent3.insert(0,"2.5") # CHANGE HERE
    Z_ent3.place(x=260, y=5.5*decalageY) 

    # Entry validation button
    Validation_ws3_btn = Button(ws3, text="Validate", height=1, width=15, command=Calcul3)
    Validation_ws3_btn.place(x=201, y=7.2*decalageY)

# Block separator
    Separator = Label(ws3, text="_____________________________________________________________________________________________________")
    Separator.place(x=0, y=8.5*decalageY)


#___________________________________ Decision-support info for entry selection _______________________________________
    Title_aide = Label(ws3, text="Laminate data summary", font=("ar 10 bold", 11))
    Title_aide.place(x=150, y=9.8*decalageY)
    # Label for angles and thicknesses
    h=1
    w=17
    decalageY2 = 20
    Angle_lb = Label(ws3, text="Angles", height=h, width=w, borderwidth=2, relief="ridge")
    Angle_lb.place(x=100, y=11.2*decalageY2)   
    Thickness_lbl = Label(ws3, text="Thicknesses", height=h, width=w, borderwidth=2, relief="ridge")
    Thickness_lbl.place(x=220, y=11.2*decalageY2)
    Height_lbl = Label(ws3, text="Heights Zi", height=h, width=w, borderwidth=2, relief="ridge")
    Height_lbl.place(x=340, y=11.2*decalageY2)    

    if n==1:
        x1 = int(Angle1_ent.get())
        Angles=[x1]       
        e1 = float(Thickness1_ent.get())
        Thicknesses=[e1]         
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    elif n==2:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        Angles=[x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        Thicknesses=[e2,e1]       
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    elif n==3:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        Angles=[x3,x2,x1]     
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        Thicknesses=[e3,e2,e1]      
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
    
    elif n==4:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        Angles=[x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        Thicknesses=[e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
            
    elif n==5:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        Angles=[x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        Thicknesses=[e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
            
    elif n==6:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        x6 = int(Angle6_ent.get())
        Angles=[x6,x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        Thicknesses=[e6,e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])
            
    elif n==7:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        x6 = int(Angle6_ent.get())
        x7 = int(Angle7_ent.get())
        Angles=[x7,x6,x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        e7 = float(Thickness7_ent.get())
        Thicknesses=[e7,e6,e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    elif n==8:
        x1 = int(Angle1_ent.get())
        x2 = int(Angle2_ent.get())
        x3 = int(Angle3_ent.get())
        x4 = int(Angle4_ent.get())
        x5 = int(Angle5_ent.get())
        x6 = int(Angle6_ent.get())
        x7 = int(Angle7_ent.get())
        x8 = int(Angle8_ent.get())
        Angles=[x8,x7,x6,x5,x4,x3,x2,x1]       
        e1 = float(Thickness1_ent.get())
        e2 = float(Thickness2_ent.get())
        e3 = float(Thickness3_ent.get())
        e4 = float(Thickness4_ent.get())
        e5 = float(Thickness5_ent.get())
        e6 = float(Thickness6_ent.get())
        e7 = float(Thickness7_ent.get())
        e8 = float(Thickness8_ent.get())
        Thicknesses=[e8,e7,e6,e5,e4,e3,e2,e1]        
        var = Calcul_height()
        Liste_Z = []
        for i in range(n,-1,-1):
            Liste_Z.append(var[i])

    indices = []      
    for i in range(n):
        indices.insert(0,i+1)
      
    for i in range(n):
        j=i+1
        indic = indices[i]
        Layer = Label(ws3, text="Layer "+f'{indic}'+" :", height=h, width=13, borderwidth=2, relief="ridge")
        Layer.place(x=0, y=(11.2+1.2*j)*decalageY2)      
        
        Var = Angles[i]
        Angle = Label(ws3, text=f"{Var}"+"°", borderwidth=3, width=w-1, relief="sunken")
        Angle.place(x=100, y=(11.2+1.2*j)*decalageY2) 

        Var = Thicknesses[i]
        Thickness = Label(ws3, text=f"{Var}"+" mm", borderwidth=3, width=w-1, relief="sunken")
        Thickness.place(x=223, y=(11.2+1.2*j)*decalageY2)

        Var1 = Liste_Z[i]
        Var2 = Liste_Z[j]
        Height = Label(ws3, text=f"{Var1}"+"  ≤  "+"z"+"  ≤  "+f"{Var2}", borderwidth=3, width=w-1, relief="sunken")
        Height.place(x=345, y=(11.2+1.2*j)*decalageY2)        



def Calcul3():
    decalageX = 21
    decalageY = 20
    c = int(Liste_layer3.get())
    z = float(Z_ent3.get())
    Angle = int(Angle_ws3.get())
    
# Partie calcul

    Sigma = Calcul_stress_axe_strat(z, Angle)
    
    Sigma_xx = Sigma[0]
    Sigma_xx = round(1000*float(Sigma_xx[0]),2)
    Sigma_yy = Sigma[1]
    Sigma_yy = round(1000*float(Sigma_yy[0]),2)
    Sigma_xy = Sigma[2]
    Sigma_xy = round(1000*float(Sigma_xy[0]),2)
    
# Updating the results    
    Sigma_xx_lbl = Label(ws3, text=f'{Sigma_xx}'+" MPa", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Sigma_xx_lbl.place(x=0, y=decalageY) 
    Sigma_yy_lbl = Label(ws3, text=f'{Sigma_yy}'+" MPa", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Sigma_yy_lbl.place(x=165, y=decalageY)          
    Sigma_xy_lbl = Label(ws3, text=f'{Sigma_xy}'+" MPa", font=("ar 10 bold",10), borderwidth=2, width=decalageX, relief="sunken")
    Sigma_xy_lbl.place(x=330, y=decalageY)  

def Validation2():
# BLOCK 4 TITLE
    Title_BLOCK4 = Label(frame3, font=("ar 10 bold",10), borderwidth=2, width=30, relief="sunken", text="RESULTS DISPLAY")
    Title_BLOCK4.grid(row=35, column=4, ipady=4, pady=20)

    Separation = Label(frame3, text="____________________________________________________________________________________________________________________________________________________________________________________________________")
    Separation.grid(row=41, column=0, columnspan=8)

# Button to display Q
    Q_btn = Button(frame3, text='Display Q', command=Display_Q)
    Q_btn.grid(row=40, column=1, ipadx=32, ipady=7, padx=8)

# Button to display Q prime
    Q_prime_btn = Button(frame3, text="Display Q'", command=Display_Q_prime)
    Q_prime_btn.grid(row=40, column=2, ipadx=30, ipady=7, padx=8, pady=10)

# Button to display H
    H_btn = Button(frame3, text='Display H', command=Display_H)
    H_btn.grid(row=40, column=3, ipadx=32, ipady=7, padx=8, pady=10)

# Button to display epsilon 0 and Kappa 0
    Eps_kap0_btn = Button(frame3, text='Display epsilon 0 vector', command=Display_eps_kap0)
    Eps_kap0_btn.grid(row=40, column=4, ipady=7, padx=8, pady=10)

# Button to display strain in the laminate axes
    Eps_global_btn = Button(frame3, text='Display strains \n (laminate axes)', command=Display_eps_axe_laminate)
    Eps_global_btn.grid(row=40, column=5, padx=8, pady=10)

# Button to display strain in each layer's axes
    Eps_layer_btn = Button(frame3, text='Display strains \n (layer axes)', command=Display_eps_axe_layer)
    Eps_layer_btn.grid(row=40, column=6, padx=8, pady=10)

# Button to display STRESS in each layer's axes
    Stress_layer_btn = Button(frame3, text='Display stresses \n (layer axes)', command=Display_stresss_axe_layer)
    Stress_layer_btn.grid(row=40, column=7, ipadx=8, padx=8, pady=10)


#------------------------------------------------------------------------------------------------------------------------------




#________________________________________________ WINDOW management ______________________________________________


def main_ENG():
    global ws, screen_x, screen_y, window_x, window_y, posX, posY, geo, frame1, frame2, frame2bis, frame3, frame4, mainmenu, Menu1, Menu2, Menu3, EL_tf, ET_tf, GLT_tf, VLT_tf, Nx_tf, Ny_tf, Nz_tf, Mt_tf, Mfy_tf, Mfz_tf, Title1_lb, Coeff_mat_lb, EL_lb, ET_lb, GLT_lb, VLT_lb, Nb_layer_lb, Nb_layer, Liste_nb_layer, CL_lb, Nx_lb, Ny_lb, Nz_lb, Mt_lb, Mfy_lb, Mfz_lb, Largeur_lb, Largeur_tf, Reset_btn, Validation1_btn, Calculate_height_btn, Validation2_btn, draw_samples, Plot_eps_laminate, Tracer_eps_layer
    ws = Tk()  # This is a widget
    ws.title("Strain and stress calculation tool for composites")
    ws.config(bg='#686e70')

    # Center the window
    screen_x = int(ws.winfo_screenwidth())
    screen_y = int(ws.winfo_screenheight())
    window_x = 1200
    window_y = 800
    posX = (screen_x//2) - (window_x//2)
    posY = (screen_y//2) - (window_y//2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    ws.geometry(geo)
    #------------------------------------------------------------------------------------------------------------------------------




    #________________________________________________ FRAME management ______________________________________________
    frame1 = Frame(ws)
    frame2 = Frame(ws)
    frame2bis = Frame(ws)
    frame3 = Frame(ws)
    frame4 = Frame(ws)

    frame1.pack()
    frame2.pack()
    frame2bis.pack()
    frame3.pack()
    frame4.pack()
    #------------------------------------------------------------------------------------------------------------------------------


    #________________________________________________ MENU management ______________________________________________
    mainmenu = Menu(ws)

    # Creating menus and submenus 
    Menu1 = Menu(mainmenu)
    Menu1.add_command(label="Option 1")     # On peut ajouter des nouvelles commandes
    Menu1.add_command(label="Option 2")
    Menu1.add_separator()
    Menu1.add_command(label="Quit", command=lambda:ws.destroy())

    Menu2 = Menu(mainmenu)
    Menu2.add_command(label="Global strains", command=Draw1)
    Menu2.add_command(label="Strains by layer", command=Draw2)

    Menu3 = Menu(mainmenu)
    Menu3.add_command(label="Laminate theory")
    Menu3.add_command(label="How the tool works")


    # Creating a dropdown menu
    mainmenu.add_cascade(label="Menu 1", menu=Menu1)
    mainmenu.add_cascade(label="Graphical representations", menu=Menu2)
    mainmenu.add_cascade(label="Help", menu=Menu3)




    #________________________________________________ FRAME management ______________________________________________
    EL_tf = DoubleVar()
    ET_tf = DoubleVar()
    GLT_tf = DoubleVar()
    VLT_tf = DoubleVar()
    Nx_tf = DoubleVar()
    Ny_tf = DoubleVar()
    Nz_tf = DoubleVar()
    Mt_tf = DoubleVar()
    Mfy_tf = DoubleVar()
    Mfz_tf = DoubleVar()
    #------------------------------------------------------------------------------------------------------------------------------



    #____________________________________________  BLOCK 1 WIDGETS  ___________________________________________________
    # GENERAL BLOCK NAME
    Title1_lb = Label(frame1,
                   text="Stress and strain calculations",
                   font=("ar 10 bold", 20))
    Title1_lb.grid(row=1, column=0, columnspan=10, padx=325, pady=10)    


    #################### LEFT SUB-BLOCK ####################
    Coeff_mat_lb = Label(frame1,
                         text="Material-related coefficients",
                         font="ar 10 bold")
    Coeff_mat_lb.grid(row=2, column=1, columnspan=2, ipadx=100)

    # Material coefficient LABELS
    EL_lb = Label(
        frame1,
        text="LONGITUDINAL Young's modulus EL (in GPa):")
    EL_lb.grid(row=3, column=1)

    ET_lb = Label(
        frame1,
        text="TRANSVERSE Young's modulus ET (in GPa):")
    ET_lb.grid(row=4, column=1)

    GLT_lb = Label(
        frame1,
        text="Shear modulus GLT (in GPa):")
    GLT_lb.grid(row=5, column=1)

    VLT_lb = Label(
        frame1,
        text="Poisson's ratio VLT:")
    VLT_lb.grid(row=6, column=1)

    Nb_layer_lb = Label(
        frame1,
        text="Number of layers:")
    Nb_layer_lb.grid(row=7, column=1, rowspan=2)


    # Material coefficient ENTRIES
    EL_tf = DoubleVar()
    EL_tf = Entry(frame1)
    EL_tf.insert(0,"38")
    EL_tf.grid(row=3, column=2)

    ET_tf = DoubleVar()
    ET_tf = Entry(frame1)
    ET_tf.insert(0,"9")
    ET_tf.grid(row=4, column=2)

    GLT_tf = DoubleVar()
    GLT_tf = Entry(frame1)
    GLT_tf.insert(0,"3.6")
    GLT_tf.grid(row=5, column=2)

    VLT_tf = DoubleVar()
    VLT_tf = Entry(frame1)
    VLT_tf.insert(0,"0.32")
    VLT_tf.grid(row=6, column=2)

    Nb_layer = [1, 2, 3, 4, 5, 6, 7, 8]
    Liste_nb_layer = ttk.Combobox(frame1, values=Nb_layer)
    Liste_nb_layer.current(3)
    Liste_nb_layer.grid(row=7, column=2, rowspan=2)
    #____________



    ################ RIGHT SUB-BLOCK ################
    CL_lb = Label(frame1,
                  text="Boundary conditions",
                  font="ar 10 bold")
    CL_lb.grid(row=2, column=3, ipadx=100, columnspan=2)

    # Boundary condition LABELS
    Nx_lb = Label(
        frame1,
        text="Nx - total force (N):")
    Nx_lb.grid(row=3, column=3, sticky='e')

    Ny_lb = Label(
        frame1,
        text="Ny - total force (N):")
    Ny_lb.grid(row=4, column=3, sticky='e')

    Nz_lb = Label(
        frame1,
        text="Nz - total force (N):")
    Nz_lb.grid(row=5, column=3, sticky='e')

    Mt_lb = Label(
        frame1,
        text="Mt (in N.m):")
    Mt_lb.grid(row=6, column=3, sticky='e')

    Mfy_lb = Label(
        frame1,
        text="Mfy (in N.m):")
    Mfy_lb.grid(row=7, column=3, sticky='e')

    Mfz_lb = Label(
        frame1,
        text="Mfz (in N.m):")
    Mfz_lb.grid(row=8, column=3, sticky='e')

    Largeur_lb = Label(
        frame1,
        text="Width B of the part (mm):")
    Largeur_lb.grid(row=9, column=3, sticky='e')


    # Boundary condition ENTRIES
    Nx_tf = DoubleVar()
    Nx_tf = Entry(frame1)
    Nx_tf.insert(0,"1000")
    Nx_tf.grid(row=3, column=4, sticky='w')

    Ny_tf = DoubleVar()
    Ny_tf = Entry(frame1)
    Ny_tf.insert(0,"500")
    Ny_tf.grid(row=4, column=4, sticky='w')

    Nz_tf = DoubleVar()
    Nz_tf = Entry(frame1)
    Nz_tf.insert(0,"250")
    Nz_tf.grid(row=5, column=4, sticky='w')

    Mt_tf = DoubleVar()
    Mt_tf = Entry(frame1)
    Mt_tf.insert(0,"0")
    Mt_tf.grid(row=6, column=4, sticky='w')

    Mfy_tf = DoubleVar()
    Mfy_tf = Entry(frame1)
    Mfy_tf.insert(0,"0")
    Mfy_tf.grid(row=7, column=4, sticky='w')

    Largeur_tf = DoubleVar()
    Largeur_tf = Entry(frame1)
    Largeur_tf.insert(0,"100")
    Largeur_tf.grid(row=9, column=4, sticky='w')

    Mfz_tf = DoubleVar()
    Mfz_tf = Entry(frame1)
    Mfz_tf.insert(0,"0")
    Mfz_tf.grid(row=8, column=4, sticky='w')
    #____________
    #-----------------------------------------------------------------------------------------------------------------




    #____________________________________________  BLOCK 2 WIDGETS  ___________________________________________________

    # Reset button for General Parameters
    Reset_btn = Button(
        frame1,
        text='Clear entries',
        command=reset_entry_BLOCK1,
        width=30)
    Reset_btn.grid(row=10, column=0, columnspan=3, pady=5, sticky='e')


    # Validation button / layer creation
    Validation1_btn = Button(
        frame1,
        text='Validate',
        command=Validation1,
        width=30)
    Validation1_btn.grid(row=10, column=3, columnspan=2, pady=5, sticky='w')
    #-----------------------------------------------------------------------------------------------------------------





    #____________________________________________  BLOCK 3 WIDGETS  ___________________________________________________
    # Validation button / layer creation
    Calculate_height_btn = Button(frame2,text='Display heights Zi',command=Display_height)
    Calculate_height_btn.grid(padx=495, pady=10)

    # Validation button / layer creation
    Validation2_btn = Button(frame2,text='Validate',command=Validation2)
    Validation2_btn.grid(padx=495, pady=10, ipadx=20, ipady=5)
    #-----------------------------------------------------------------------------------------------------------------





    #____________________________________________  DRAWING CANVAS  ___________________________________________________
    def draw_samples(canvas):
        """Draw the planes for each layer and display the layer angles"""
        Z = Calcul_height()
        # Mid-plane
        x0,y0 = 0,250
        Nb_layer = int(Liste_nb_layer.get())
        f = 300/(float(Z[-1])-float(Z[0]))      # Facteur de grossissement

        if Nb_layer==1:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )    
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' ) 

        elif Nb_layer==2:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )   

        elif Nb_layer==3:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle3_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[3]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z3
            z = f*float(Z[3])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) ) 
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[3])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )

        elif Nb_layer==4:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )  
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle3_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[3]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z3
            z = f*float(Z[3])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )  
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[3])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle4_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[4]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z4
            z = f*float(Z[4])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[4])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )

        elif Nb_layer==5:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) ) 
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle3_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[3]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°") 
        # plan z3
            z = f*float(Z[3])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) ) 
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[3])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle4_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[4]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z4
            z = f*float(Z[4])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[4])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle5_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[5]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z5
            z = f*float(Z[5])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) ) 
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[5])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )        

        elif Nb_layer==6:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )  
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle3_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[3]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z3
            z = f*float(Z[3])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) ) 
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[3])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle4_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[4]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z4
            z = f*float(Z[4])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[4])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle5_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[5]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z5
            z = f*float(Z[5])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[5])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle6_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[6]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z6
            z = f*float(Z[6])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[6])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )       

        elif Nb_layer==7:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )  
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle3_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[3]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z3
            z = f*float(Z[3])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )  
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[3])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle4_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[4]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z4
            z = f*float(Z[4])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[4])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle5_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[5]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z5
            z = f*float(Z[5])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[5])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle6_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[6]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z6
            z = f*float(Z[6])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[6])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle7_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[7]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z7
            z = f*float(Z[7])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[7])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )       

        elif Nb_layer==8:
        # plan z0
            z = f*float(Z[0])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[0])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle1_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[1]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z1
            z = f*float(Z[1])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[1])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle2_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[2]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z2
            z = f*float(Z[2])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) ) 
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[2])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle3_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[3]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z3
            z = f*float(Z[3])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )   
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[3])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle4_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[4]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z4
            z = f*float(Z[4])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[4])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle5_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[5]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z5
            z = f*float(Z[5])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[5])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle6_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[6]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z6
            z = f*float(Z[6])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[6])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle7_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[7]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z7
            z = f*float(Z[7])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[7])+"mm", fill="black", font=('Helvetica 8 bold'))
            Angle = str(Angle8_ent.get())
            y_angle = (y+dy) - abs(z-f*float(Z[8]))/2
            canvas.create_text(75, y_angle, text=str(Angle)+"°")
        # plan z8
            z = f*float(Z[8])
            x, y = x0, y0-z
            dx, dy = 2000, 0
            canvas.create_line((x,y), (x+dx,y+dy), dash=(2,2) )
            canvas.create_line((x,y), (100,y+dy))
            canvas.create_text(x+25, y-8, text=str(Z[8])+"mm", fill="black", font=('Helvetica 8 bold'))
        # Mid-plane
            dx, dy = 2000, 0
            canvas.create_line((x0,y0), (x0+dx,y0+dy), dash=(2,2), fill='red' )        

    # Draw de la zone des angles
        x0, y0 = 100,250-f*Z[0]    
        x1, y1 = 100, 250+f*Z[0]
        canvas.create_line( (x0,y0), (x1,y1) )


    def Plot_eps_laminate(canvas):    
        Z = Calcul_height()
        # Mid-plane
        x0,y0 = 0,250
        Nb_layer = int(Liste_nb_layer.get())
        g = 300/(float(Z[-1])-float(Z[0]))      # Facteur de grossissement vertical

        zinf = float(Z[0])
        zsup = float(Z[-1])
        Eps_inf = 1000*Calcul_epsilon(zinf)    # Multiplication pour meilleur affichage (en mm)
        Eps_sup = 1000*Calcul_epsilon(zsup)
        # We could use absolute values if we know the strain is negative ?????????
        a, c, e = float(Eps_inf[0]), float(Eps_inf[1]), float(Eps_inf[2])
        b, d, f = float(Eps_sup[0]), float(Eps_sup[1]), float(Eps_sup[2])

        X = max(a,b,c,d,e,f, abs(a-b), abs(c-d), abs(e-f))
        m = 300/X            # Facteur de grossissement horizontal

    # Drawing Eps_xx
        x0,y0 = x0+150, y0-g*float(Z[0])
        dx, dy = m*a, 0
        x1, y1 = x0+dx, y0+dy
        dx, dy = m*(b-a), g*(Z[0]-Z[-1])
        x2, y2 = x1+dx, y1+dy   
        dx, dy = -(m*b), 0
        x3, y3 = x2+dx, y2+dy    
        canvas.create_line( (x0,y0), (x1,y1), (x2,y2), (x3,y3), (x0,y0))
        canvas.create_text(x0+20, y0+25, text="Epsilon_xx (mm)", fill="black", font=('Helvetica 8 bold'))
        canvas.create_text(x1, y1+10, text=str(round(a,1)), fill="black", font=('Helvetica 8 bold'))
        canvas.create_text(x2, y2-10, text=str(round(b,1)), fill="black", font=('Helvetica 8 bold'))

    # Drawing Eps_yy
        Negatif1 = 0
        if c<0:
            Negatif1 = abs(c)
            print("c is negative")
        Negatif2 = 0
        if d<0:
            Negatif2 = abs(d)
            print("d is negative")
        Max_epsxx = max(a,b)+Negatif1+Negatif2
        x0,y0 = 100+m*Max_epsxx+50*2, 250-g*float(Z[0])
        dx, dy = m*c, 0
        x1, y1 = x0+dx, y0+dy
        dx, dy = m*(d-c), g*(Z[0]-Z[-1])
        x2, y2 = x1+dx, y1+dy   
        dx, dy = -(m*d), 0
        x3, y3 = x2+dx, y2+dy    
        canvas.create_line( (x0,y0), (x1,y1), (x2,y2), (x3,y3), (x0,y0))
        canvas.create_text(x0+20, y0+25, text="Epsilon_yy (mm)", fill="black", font=('Helvetica 8 bold'))
        canvas.create_text(x1, y1+10, text=str(round(c,1)), fill="black", font=('Helvetica 8 bold'))
        canvas.create_text(x2, y2-10, text=str(round(d,1)), fill="black", font=('Helvetica 8 bold'))

    # Drawing Gamma_xy
        Negatif1 = 0
        if e<0:
            Negatif1 = abs(e)
            print("e is negative")
        Negatif2 = 0
        if f<0:
            Negatif2 = abs(f)
            print("f is negative")
        Max_epsyy = max(c,d) + Negatif1 + Negatif2
        x0,y0 = 100 + m*Max_epsxx + m*Max_epsyy+50*3, 250-g*float(Z[0])
        dx, dy = m*e, 0
        x1, y1 = x0+dx, y0+dy
        dx, dy = m*(f-e), g*(Z[0]-Z[-1])
        x2, y2 = x1+dx, y1+dy   
        dx, dy = -(m*f), 0
        x3, y3 = x2+dx, y2+dy    
        canvas.create_line( (x0,y0), (x1,y1), (x2,y2), (x3,y3), (x0,y0))
        canvas.create_text(x0+20, y0+25, text="Gamma_xy (mm)", fill="black", font=('Helvetica 8 bold'))
        canvas.create_text(x1, y1+10, text=str(round(e,1)), fill="black", font=('Helvetica 8 bold'))
        canvas.create_text(x2, y2-10, text=str(round(f,1)), fill="black", font=('Helvetica 8 bold'))


    def Tracer_eps_layer(canvas):
        print("We are going to draw the strains in each layer of the laminate")
        Z = Calcul_height()
        # Mid-plane
        x0,y0 = 0,250
        Nb_layer = int(Liste_nb_layer.get())
        g = 300/(float(Z[-1])-float(Z[0]))      # Facteur de grossissement vertical

        zinf = float(Z[0])
        zsup = float(Z[-1])
        Eps_inf = 1000*Calcul_epsilon(zinf)    # Multiplication pour meilleur affichage (en mm)
        Eps_sup = 1000*Calcul_epsilon(zsup)
        # We could use absolute values if we know the strain is negative ?????????
        a, c, e = float(Eps_inf[0]), float(Eps_inf[1]), float(Eps_inf[2])
        b, d, f = float(Eps_sup[0]), float(Eps_sup[1]), float(Eps_sup[2])

        X = max(a,b,c,d,e,f)
        m = 300/X            # Facteur de grossissement horizontal




    #-----------------------------------------------------------------------------------------------------------------



























    ws.config(menu=mainmenu)
    ws.mainloop()



if __name__ == "__main__":
    main_ENG()
