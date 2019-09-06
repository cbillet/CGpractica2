#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:41:45 2019

@author: nadia
"""

#%% cargo librerias
import numpy as np
from matplotlib import pyplot as plt
#%%cargo las salidas del modelo para k1, k2, k3 con la funcion cargar dentro de Cargar2.py
from Cargar2 import cargar 
psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica2/modelo_QG/out_tmp_s1/",1000,500,100,50)
psi_temp_2,vort_temp_2,psiF_2,vortF_2,QG_diag_2,QG_curlw_2,X_2,Y_2,dx_2,dy_2=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica2/modelo_QG/out_tmp_s2/",1000,500,100,50)
psi_temp_3,vort_temp_3,psiF_3,vortF_3,QG_diag_3,QG_curlw_3,X_3,Y_3,dx_3,dy_3=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica2/modelo_QG/out_tmp_s3/",1000,500,100,50)
psi_temp_4,vort_temp_4,psiF_4,vortF_4,QG_diag_4,QG_curlw_4,X_4,Y_4,dx_4,dy_4=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica2/modelo_QG/out_tmp_s4/",1000,500,100,50)
psi_temp_5,vort_temp_5,psiF_5,vortF_5,QG_diag_5,QG_curlw_5,X_5,Y_5,dx_5,dy_5=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica2/modelo_QG/out_tmp_s5/",1000,500,100,50)
#%% ejercicio 1a (evolucion de energia cinetica total) HACER IDEM
#tomo la cuarta columna de la salida QG_diag que tiene la energia cinetica para cada paso temporal (2000 pasos) en el punto central del dominio
plt.figure()
plt.plot(QG_diag[:,0],QG_diag[:,3],label="k1")
plt.plot(QG_diag_2[:,0],QG_diag_2[:,3],label="k2")
plt.plot(QG_diag_3[:,0],QG_diag_3[:,3],label="k3")
plt.xlabel("paso temporal")
plt.ylabel("energia cinetica")
plt.title("Evolucion de energia cinetica total")
plt.legend()
plt.savefig("ejercicio1a", dpi=100)

#%%
#S1
en_cin=QG_diag[:,3]
en_cin_abs_i=[]
for i in range(len(en_cin)):
    en_cin_abs_i.append(np.abs((en_cin[-1]-en_cin[i])/en_cin[-1])*100)

for j in range(len(en_cin)):
    k=en_cin_abs_i[j]<1 & en_cin_abs_i[j]==np.min(en_cin_abs_i)

np.where(en_cin_abs_i<1 & np.min(en_cin_abs_i)) 
     
     

plt.plot(QG_diag[:,0],en_cin)
plt.axvline(x=147,"r")
        
