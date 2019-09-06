#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:02:56 2019

@author: macbookair
"""

#%%
#Hola nanusss, estive jugando un rato con los estilos del counturf. Por un lado podes cambiarle el estilo con el comando  plt.style.use('estilo') y podes ver los que hay en el siguiente
#link  https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html lo que hace es cambiarte el fondo y tener colores tipicos por defoult. Manteniendo el estilo tambien 
#podes cambiar los colores  importanto from matplotlib import cm y usas el comando cmap=cm.jet donde jet es ejemplo y en el link ves todas las opciones 
# https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html. 

#EL ej 2 no iba porque era lista y el np.where funciona con float(hasta que me di cuenta pasaron las elecciones ). Lo pase pero igual estan mal las condiciones porque el minimo valor es cero y estamos buscando un valor mayor a 1 que tambien sea cero. Lo hice desde esta
#otra manera que me funciona para la 1 pero nme queda lupeando eternamente para los otros. Yo ya estoy quemada si se te ocurre algo bien si no manana sera otro dia
#en los campos de vorticidad queda mucha diferencia entre las simulaciones que cuando le metes una barra unificada para poder comparar no se ve. Dani dice que hay mucha dif pero tambien dice que no le parece que el codigo este mal asi que no se. Abra que ver que les da al resto y ver que onda.
#Despues  en el 5to lo consulte con dani y habia que tirar de nuevo la magia del ds
#%% cargo librerias
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
#%%cargo las salidas del modelo para k1, k2, k3 con la funcion cargar dentro de Cargar2.py
from Cargar2 import cargar 
psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy=cargar("/Users/macbookair/Desktop/practica2/modelo_QG/out_tmp_s1/",1000,500,100,50)
psi_temp_2,vort_temp_2,psiF_2,vortF_2,QG_diag_2,QG_curlw_2,X_2,Y_2,dx_2,dy_2=cargar("/Users/macbookair/Desktop/practica2/modelo_QG/out_tmp_s2/",1000,500,100,50)
psi_temp_3,vort_temp_3,psiF_3,vortF_3,QG_diag_3,QG_curlw_3,X_3,Y_3,dx_3,dy_3=cargar("/Users/macbookair/Desktop/practica2/modelo_QG/out_tmp_s3/",1000,500,100,50)
psi_temp_4,vort_temp_4,psiF_4,vortF_4,QG_diag_4,QG_curlw_4,X_4,Y_4,dx_4,dy_4=cargar("/Users/macbookair/Desktop/practica2/modelo_QG/out_tmp_s4/",1000,500,100,50)
psi_temp_5,vort_temp_5,psiF_5,vortF_5,QG_diag_5,QG_curlw_5,X_5,Y_5,dx_5,dy_5=cargar("/Users/macbookair/Desktop/practica2/modelo_QG/out_tmp_s5/",1000,500,100,50)
#%% ejercicio 1a (evolucion de energia cinetica total) HACER IDEM
#tomo la cuarta columna de la salida QG_diag que tiene la energia cinetica para cada paso temporal (2000 pasos) en el punto central del dominio
plt.figure()
plt.plot(QG_diag[:,0],QG_diag[:,3],label="S1")
plt.plot(QG_diag_2[:,0],QG_diag_2[:,3],label="S2")
plt.plot(QG_diag_3[:,0],QG_diag_3[:,3],label="S3")
plt.plot(QG_diag_4[:,0],QG_diag_4[:,3],label="S4")
plt.plot(QG_diag_5[:,0],QG_diag_5[:,3],label="S5")
plt.xlabel("Paso temporal")
plt.ylabel("Energia cinetica")
plt.title("Evolucion de energia cinetica total")
plt.legend()
plt.savefig("ejercicio1", dpi=100)

#%%
#S1

#Queremos ver cuándo se estabiliza el modelo
Ec1=QG_diag[:,3]
Ec2=QG_diag_2[:,3]
Ec3=QG_diag_3[:,3]
Ec4=QG_diag_4[:,3]
Ec5=QG_diag_5[:,3]

k1=0
while abs(((Ec1[-1]-Ec1[k1])/Ec1[-1])*100)>=1:
    k1=k1+1 #k1  corresponde al paso a partir del cual la el cociente de energía cinética se hace menor a 1 (como lo pide el enunciado)

k2=0
while abs(((Ec2[-1]-Ec2[k1])/Ec2[-1])*100)>=1:
    k2=k2+1   
k3=0
while abs(((Ec3[-1]-Ec3[k1])/Ec3[-1])*100)>=1:
    k3=k3+1 
k4=0
while abs(((Ec4[-1]-Ec4[k1])/Ec4[-1])*100)>=1:
    k4=k4+1 
k5=0
while abs(((Ec5[-1]-Ec5[k1])/Ec5[-1])*100)>=1:
    k5=k5+1

     

#%% Ej 3

levels_psi=np.arange(-800000,10000,10000) #vector de -350000 a 0 cada 10000
#levels_psiF=np.arange()

##defino magnitudes tipicas para dimensionalizar 
L=1000000 #longitud de la cuenca
tau=0.3 #tension del viento en superficie
D=3000 #profundidad del oceano 
rho=1025 #densidad
betha=1e-11 
U=2*np.pi*tau/(rho*D*betha*L) 

###S1
psiF_dim=psiF*U*L # funcion corriente dimensionalizada (dimension m*m/s) S1
#ploteo funcion corriente S1
plt.figure()
plt.contourf(X,Y,psiF_dim,levels_psi, cmap=cm.jet)
plt.title("Campo de funcion corriente S1")
plt.colorbar()
plt.savefig("Funcion corriente S1", npi=100)

##dimesionalizo vorticidad S1

vortF_dim=vortF*U/L*1e7
#ploteo vorticidad S1
plt.figure()
plt.contourf(X,Y,vortF_dim,cmap=cm.Spectral)
plt.title("Campo de vorticidad S1")
plt.colorbar()
plt.savefig("Campo de vorticidad S1", npi=100)


###S2

#dimensionalizo funcion corriente, considero dimensiones tipicas de modelo_oceanico
psiF_2_dim=psiF_2*U*L #funcion corriente dimensionalizada (dimension m*m/s)

#ploteo funcion corriente S2
plt.figure()
plt.contourf(X_2,Y_2,psiF_2_dim,levels_psi,cmap=cm.jet)
plt.title("Campo de funcion corriente S2")
plt.colorbar()
plt.savefig("Funcion corriente S2", npi=100)

##dimesionalizo vorticidad S2

vortF_2_dim=vortF_2*U/L*1e7

#ploteo vorticidad S2
plt.figure()
plt.contourf(X,Y,vortF_2_dim,cmap=cm.Spectral )
plt.title("Campo de vorticidad S1")
plt.colorbar()
plt.savefig("Campo de vorticidad S2", npi=100)

###S3

#dimensionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
psiF_3_dim=psiF_3*U*L # funcion corriente dimensionalizada (dimension m*m/s)

#ploteo funcion corriente S3
plt.figure()
plt.contourf(X_3,Y_3,psiF_3_dim,levels_psi,cmap=cm.jet)
plt.title("Campo de funcion corriente S3")
plt.colorbar()
plt.savefig("Funcion corriente S3", npi=100)

##dimesionalizo vorticidad S2

vortF_3_dim=vortF_3*U/L*1e7

#ploteo vorticidad S2
plt.figure()
plt.contourf(X,Y,vortF_3_dim,cmap=cm.Spectral)
plt.title("Campo de vorticidad S3")
plt.colorbar()
plt.savefig("Campo de vorticidad S3", npi=100)

###S4

#dimensionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
psiF_4_dim=psiF_4*U*L # funcion corriente dimensionalizada (dimension m*m/s)

#ploteo funcion corriente S4
plt.figure()
plt.contourf(X_4,Y_4,psiF_4_dim,levels_psi,cmap=cm.jet)
plt.title("Campo de funcion corriente S4")
plt.colorbar()
plt.savefig("Funcion corriente S4", npi=100)

##dimesionalizo vorticidad S4

vortF_4_dim=vortF_4*U/L*1e7

#ploteo vorticidad S4
plt.figure()
plt.contourf(X,Y,vortF_4_dim,cmap=cm.Spectral )
plt.title("Campo de vorticidad S4")
plt.colorbar()
plt.savefig("Campo de vorticidad S4", npi=100)

###S5

#dimensionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
psiF_5_dim=psiF_5*U*L # funcion corriente dimensionalizada (dimension m*m/s)

#ploteo funcion corriente S5
plt.figure()
plt.contourf(X_5,Y_5,psiF_5_dim,levels_psi,cmap=cm.jet)
plt.title("Campo de funcion corriente S5")
plt.colorbar()
plt.savefig("Funcion corriente S5", npi=100)

##dimesionalizo vorticidad S5

vortF_5_dim=vortF_5*U/L*1e7

#ploteo vorticidad S5
plt.figure()
plt.contourf(X,Y,vortF_5_dim,cmap=cm.Spectral)
plt.title("Campo de vorticidad S5")
plt.colorbar()
plt.savefig("Campo de vorticidad S5", npi=100)


#%% Ejercicio 4
 

#S1
My=D*(np.diff(psiF_dim,n=1, axis=1))/1e6
My_central=My[25,:] #latitud numero 25
np.where(My_central[:-1] * My_central[1:] < 0 )[0]  #(6) te da la primer longitud donde cambia de signo termina el borde oeste en array (donde el transporte meridional se hace positivo)
My_borde_oeste_suma=np.sum(My_central[0:6]) #en sv
My_total_suma=np.sum(My_central) #en sv
extension_borde_oeste=np.sum(X[0:6])*20 #en m 

#S2
My_2=D*(np.diff(psiF_2_dim,n=1, axis=1))/1e6
My_2_central=My_2[25,:] #latitud numero 25
np.where(My_2_central[:-1] * My_2_central[1:] < 0 )[0]  #(5) te da la primer longitud donde cambia de signo termina el borde oeste en array (donde el transporte meridional se hace positivo)
My_2_borde_oeste_suma=np.sum(My_central[0:5]) #en sv
My_2_total_suma=np.sum(My_central) #en sv
extension_borde_oeste_2=np.sum(X[0:5])*20 #en m 

#S3
My_3=D*(np.diff(psiF_3_dim,n=1, axis=1))/1e6
My_3_central=My_3[25,:] 
np.where(My_3_central[:-1] * My_3_central[1:] < 0 )[0]  #(4)Cambia en 4 14y 16. Elijo qudatme con 5
My_3_borde_oeste_suma=np.sum(My_3_central[0:4]) #en sv
My_3_total_suma=np.sum(My_3_central) #en sv
extension_borde_oeste_3=np.sum(X[0:5])*20 #en m 

#S4
My_4=D*(np.diff(psiF_4_dim,n=1, axis=1))/1e6
My_4_central=My_4[25,:] 
np.where(My_4_central[:-1] * My_4_central[1:] < 0 )[0]  #(3)Cambia en 3 10 y 13. Elijo qudatme con 4
My_4_borde_oeste_suma=np.sum(My_4_central[0:3]) #en sv
My_4_total_suma=np.sum(My_4_central) #en sv
extension_borde_oeste_4=np.sum(X[0:3])*20 #en m 

#S5
My_5=D*(np.diff(psiF_5_dim,n=1, axis=1))/1e6
My_5_central=My_5[25,:] 
np.where(My_5_central[:-1] * My_5_central[1:] < 0 )[0]  #(17)Cambia en 1 5 y 8. Elijo qudatme con 2
My_5_borde_oeste_suma=np.sum(My_5_central[0:1]) #en sv
My_5_total_suma=np.sum(My_5_central) #en sv
extension_borde_oeste_5=np.sum(X[0:1])*20 #en m 


#acomodo informacion en tabla devuelve archivo excel
import pandas as pd
resultados4= {' ': ["Transporte meridional borde oeste [sv]","Transporte meridional total [sv]","Extension borde oeste [m]"],
     "S1":[round(My_borde_oeste_suma),round(My_total_suma),extension_borde_oeste],
     'S2':[round(My_2_borde_oeste_suma),round(My_2_total_suma),extension_borde_oeste_2],
     "S3":[round(My_3_borde_oeste_suma),round(My_3_total_suma),extension_borde_oeste_3],
     'S4':[round(My_4_borde_oeste_suma),round(My_4_total_suma),extension_borde_oeste_4],
     "S5":[round(My_5_borde_oeste_suma),round(My_5_total_suma),extension_borde_oeste_5]}

resultados4 = pd.DataFrame(data=resultados4)
resultados4.to_excel("resultados_4.xls",index=False)

#%% Ejercicio 5
from Laplaciano import Calc_del2
ds=0.1
primer_termino=((np.diff(psiF,n=1, axis=1)))[25,:]/(ds) #este es el que tuvo que tirar magia dani con ese ds que viene del .dat (gridstep)
segundo_termino=-QG_curlw[26,:]
tercer_termino=-(0.025)*Calc_del2(vortF,1)[25,:]/(ds**2)

plt.figure(33)
plt.plot(primer_termino,"r", label='Primer Termino')
plt.plot(segundo_termino,"b", label= 'Segundo Termno')
plt.plot(tercer_termino,"g", label ='Tercer Termino' )
plt.legend()
plt.savefig("EJERCICIO 5", dpi=100)



