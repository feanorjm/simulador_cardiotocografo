# -*- coding: utf-8 -*-
#
#@author: Juan Darío Muñoz Soto
#
#@version: 2.0 
#
#@date: 02-01-2014
#
#@summary: Funciones para calcular las contracciones uterinas 
#
#@note: Modelos matematicos por: Curso 'Identificación de modelos parametricos' - Magister en Ingeniería UACh
#
#@copyright: Todos los derechos reservados por Laboratorio I+D, Alfredo Illanes, Francisco Guerra, etc
#
#@warning: All changes made in this file will be lost!
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from __future__ import division
import sys
from numpy import *
import numpy as np
import scipy as ft
import scipy 
from scipy.fftpack import fft, diff


def interseccion(Tcu,Dcu,ini,fin):
    #TCU vector con tiempos de contraccion uterina
    #DCU vector con duraciones de contraccion uterina
    #ini: inicio de CU 
    #fin: fin de CU
    #intervalo: arreglo de dos elementos que 
    fCU = Tcu + Dcu
    N = len(Tcu)
    intervalo = np.array([])
    for i in range(N):
        if fCU[i] > ini and ini > Tcu[i]:
            intervalo = np.array([ini, fCU[i]])
    return intervalo
    
'''NUEVA FUNCION PARA LA CONTRACCION *************************************************************************************************'''
def contraccion(T,tsim,u,desv,ad,rstd,fm,bandpass,mf,mfstd):
    
    auxd=0
    t=np.arange(tsim[0],tsim[1],1./fm)
    nT=len(T)
    piu0=0
    piu=np.array([])
    ttot=np.array([])
    F=1/scipy.diff(T)
    
    RT = np.ones(nT)
    D = np.ones(nT)
    A = np.ones(nT)
    Aprom = 0
    
    for j in range(0,nT):
        RT[j]=np.abs(np.random.randn())*desv[0]+u[0]
        #print RT[j], 'RT'
        D[j]=np.random.randn()*desv[1]+u[1]
        Aprom=ad*D[j]
        #print Aprom, 'amplitud'
        A[j]=np.random.randn()*desv[2]+Aprom
        #print A[j], '--->>>>>>>>'
    
    #if(len(T) == 0):
    ttot=np.arange(0,tsim[1],1/fm)
    piu=np.ones(len(ttot))
    #RT = np.ones(1)
    '''-------------------------------------------------else:
        ttot=np.arange(0,T[0],1/fm)
        #piu=RT[0]*np.ones(len(ttot)) # cambiar en caso de 
        piu=np.ones(len(ttot))
        piu[0:len(ttot)]=RT[0]'''
    
    
    '''for k in range(0,nT):
        t1=np.where((t>T[k])&(t<=(T[k]+D[k]/2)))[0]
        #print t1,'t1', len(t1) ,'largot1'
        t1=t[t1]
        if(k == nT-1):
            t2=np.where((t>(T[k]+D[k]/2)))[0]
            #print t2, 't2'
            if len(t2) == 0:
                t2 = np.array([])
            else:
                dfinal = np.array([(t2[-1])+1])
                t2 = np.concatenate([t2,dfinal])
                t2=t[t2-1]
        else:
            t2=np.where((t>(T[k]+D[k]/2))&(t<=T[k+1]))[0]
            #t2=np.where(t>(T[k]+D[k]/2))[0]
            #print t2, 't2--->',len(t2) ,'largot2'
            t2=t[t2-1]
        #t2=t[t2-1]
        
        ft=cont_exp(T[k],T[k],D[k])
        f1=cont_exp(t1,T[k],D[k])
        piu1=RT[k-1]-piu0+(A[k])*(f1-ft)/(1-ft)+piu0
        f2=cont_exp(t2,T[k],D[k])
        piu2=RT[k]+(A[k]+RT[k-1]-RT[k])*f2
        
        
        piu=np.concatenate([piu, piu1, piu2])
        
        piu0=piu[len(piu)-1]
        ttot=np.concatenate([ttot, t1, t2])-------------------------------'''
    arrayPiu = []
    for k in range(0,nT):
        t1=np.where((t>T[k])&(t<=(T[k]+D[k]/2)))[0]
        #print t1,'t1', len(t1) ,'largot1'
        t1=t[t1]
        if(k == nT-1):
            t2=np.where((t>(T[k]+D[k]/2)))[0]
            #print t2, 't2'
            if len(t2) == 0:
                t2 = np.array([])
            else:
                dfinal = np.array([(t2[-1])+1])
                t2 = np.concatenate([t2,dfinal])
                t2=t[t2-1]
        else:
            #t2=np.where((t>(T[k]+D[k]/2))&(t<=T[k+1]))[0]
            t2=np.where(t>(T[k]+D[k]/2))[0]
            #t2=np.where(t>(T[k]+D[k]/2))[0]
            #print t2, 't2--->',len(t2) ,'largot2'
            t2=t[t2-1]
        #t2=t[t2-1]
        
        ft=cont_exp(T[k],T[k],D[k])
        f1=cont_exp(t1,T[k],D[k])
        piu1=RT[k-1]-piu0+(A[k])*(f1-ft)/(1-ft)+piu0
        f2=cont_exp(t2,T[k],D[k])
        
        piu2=RT[k]+(A[k]+RT[k-1]-RT[k])*f2
        
        
        piuAux = np.concatenate([piu1, piu2])
        arrayPiu.append(piuAux)
        
    
    #piu=np.concatenate([piu, piu1, piu2])
    #piu0=piu[len(piu)-1]
    #ttot=np.concatenate([ttot, t1, t2])
    
    for i in range (0, len(arrayPiu)):
        vector = arrayPiu[i]
        #plt.plot(vector)
        #plt.show()
        largo = len(vector)
        inicio = int((T[i])*fm)
        fin = int(inicio + largo-1)
        print "largo", largo
        print "largo/fs", largo/fm
        print "inicio", inicio
        print "fin", fin
        #plt.plot(piu)
        #plt.show()
        print len(piu), "piu"
        
        inter = interseccion(T,D,inicio/250,fin/250)
        
        if len(inter)>0:
            inicio_inter = int(inter[0]*250)
            fin_inter = int(inter[1]*250)
            sig_piu_aux1 = piu[inicio_inter:fin_inter]
            fin_vector_inter = fin_inter - inicio_inter     
            sig_piu_aux2 = vector[0:fin_vector_inter]
            indice_comp1 = np.where(sig_piu_aux1>sig_piu_aux2)
            indice_concatenador = np.arange(0,len(vector))
            indice_concatenador = np.delete(indice_concatenador,indice_comp1)
            long_vec_con = len(indice_concatenador)
            comienzo = fin -long_vec_con 
            piu[comienzo:fin] = vector[indice_concatenador]
        else:
            if i == 0:
                    piu[0:inicio] = 11
            piu[inicio-1:fin] = vector
        
        '''for j in range(inicio,fin): 
            if (vector[j - inicio] > piu[j]):
                if i == 0:
                    piu[0:inicio] = 11
                piu[j] = vector[j - inicio]'''
         
    vec=np.round(fm*0.05) # % numero de muestras de vecindad de instante de contraccion
        
    for j in range (0,len(mf)):
        aux1 = mf[j]-(vec/fm)
        aux2 = mf[j]+(vec/fm)
        c = np.where((ttot >= aux1) & (ttot <= aux2))[0]
        #print c, 'c'
        p=np.mean(piu[c[0]:(c[len(c)-1])])
        print "soy RT", RT
        if (p<1.5*np.mean(RT)):
            Amf=np.random.randn()*mfstd[2]+mfstd[0]
            Dmf=np.random.rand()*mfstd[3]+mfstd[1]
            RTmf=p
            tmf=np.arange(mf[j], mf[j]+Dmf, 1/fm)
            s=Amf*(cont_exp(tmf,mf[j],Dmf))+RTmf
            #piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)]=s
            print ("hola robles")
            if len(s) > len(piu[abs(mf[j]*fm):]):
                trozo = len(piu[abs(mf[j]*fm):])
                piu[abs(mf[j]*fm):]=s[:trozo]
                print 'hola'
            else:
                if (len(s) > len(piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)])):
                    piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)+1]=s
                    #piu[abs(mf[j]*fm):] = s
                elif(len(s) == len(piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)])):
                    piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)]=s
                else:
                    piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)-1]=s
    
        
    
    if (len(piu)>1000000):
        r=np.random.randn(len(piu))
    else :
        r=np.random.randn(1000000)
    
    rf = filtbyfft(r, 100, bandpass)
    #print('r:',len(r),'rf:',len(rf))
    x=rstd/np.std(rf)
    rf=x*rf
    rf=rf[0:len(piu)]
    piu=piu+rf
    
    if len(T) == 0:
        piu = piu + 10
        
    return np.array([piu, ttot, D, A, Aprom])    
    
'''Funcion que calcula la curva de la contracción. Indispensable ************************************************************************'''
def cont_exp(t,Tn,D):
    s=np.exp(-18*(((t-Tn-D/2)**2)/D**2))
    return s    

'''**************************************************************************************************************************************'''

'''Funcion que filtra la señal de la contraccion por medio de un filtro fft *************************************************************'''
def filtbyfft(x, fs, passband):
    try:
        x
        fs
        passband
    except EOFError():
        print("3 input arguments are required")
        

    
    passband[0] = max(passband[0], 0)
    passband[1] = min(passband[1], 0.5*fs)
    
    #print('passband1',passband[0])
    #print('passband2',passband[1])

    N = len(x)
    y = np.fft.fft(x)

    lowicut = np.round(passband[0]*N/fs)
    lowmirror = N - lowicut
    #print('lowicut:',lowicut,'lowmirror:',lowmirror)

    highicut =  np.round(passband[1]*N/fs)
    highmirror = N-highicut
    #print('highicut:',highicut,'highmirror:',highmirror)
    
    for i in range(0,int(lowicut)):
        y[i]=0
    #print('largo:',len(y))
    
    for j in range(int(lowmirror), len(y)):
        y[j]=0
    #print(y)    
    #y[1:(lowicut-1) (lowmirror+1):end]=0
    y[(int(highicut)+1):(int(highmirror)-1)]=0
    

    xf = ft.ifft(y)
    #xf = xf[0]
    return xf


'''**************************************************************************************************************************************'''

def con_user(u,desv,ad,fm):
    
    RT=np.abs(np.random.randn())*desv[0]+u[0]
    print "RT",RT
        #print RT[j], 'RT'
    D=np.random.randn()*desv[1]+u[1]
    Aprom=ad*D
    #print Aprom, 'amplitud'
    A=np.random.randn()*desv[2]+Aprom
    #print A[j], '--->>>>>>>>'
    t1 = np.arange(0,(D+1/fm),1/fm)
    
    s=A*cont_exp(t1,0,D)
    
    return np.array([s, D, A, Aprom])

def CuMf(mf,ttot,mfstd,fm,desv,u):
    
    piu=np.ones(len(ttot))
    vec=np.round(fm*0.05) # % numero de muestras de vecindad de instante de contraccion
    
    RT=np.abs(np.random.randn())*desv[0]+u[0]
    
    for j in range (0,len(mf)):
        aux1 = mf[j]-(vec/fm)
        aux2 = mf[j]+(vec/fm)
        c = np.where((ttot >= aux1) & (ttot <= aux2))[0]
        #print c, 'c'
        p=np.mean(piu[c[0]:(c[len(c)-1])])
        if (p<1.5*np.mean(RT)):
            Amf=np.random.randn()*mfstd[2]+mfstd[0]
            Dmf=np.random.rand()*mfstd[3]+mfstd[1]
            RTmf=p
            tmf=np.arange(mf[j], mf[j]+Dmf, 1/fm)
            s=Amf*(cont_exp(tmf,mf[j],Dmf))+RTmf
            if len(s) > len(piu[int(mf[j]*fm):]):
                trozo = len(piu[int(mf[j]*fm):])
                piu[abs(mf[j]*fm):]=s[:trozo]
            else:
                if (len(s) > len(piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)])):
                    piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)+1]=s
                    #piu[abs(mf[j]*fm):] = s
                elif(len(s) == len(piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)])):
                    piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)]=s
                else:
                    piu[abs(mf[j]*fm):abs((mf[j]+Dmf)*fm)-1]=s
                    
    return piu