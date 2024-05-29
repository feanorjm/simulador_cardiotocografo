# -*- coding: utf-8 -*-
#
#@author: Juan Darío Muñoz Soto
#
#@version: 2.0 
#
#@date: 02-01-2014
#
#@summary: Funciones para calcular las desaceleraciones 
#
#@note: Modelos matematicos por: Curso 'Identificación de modelos parametricos' - Magister en Ingeniería UACh
#
#@copyright: Todos los derechos reservados por Laboratorio I+D, Alfredo Illanes, Francisco Guerra, etc
#
#@warning: All changes made in this file will be lost!
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from __future__ import division
import numpy as np
import sys
import math
import scipy as ft
import pywt

def rampa(T,tr,Ts): 
    N = np.round(T/Ts) 
    Nr = np.round(tr/Ts) 
    ramp = np.zeros(N) 
    k = Nr 
    while k < N: 
        ramp[k] = Ts*(k-Nr) 
        k = k + 1 
    return ramp


'''Funcion para la Desaceleración Temprana (DIP 1)'''
def DIP1(Tc,Dc,Ac,Aprom,fs):

    Idprom=-30.
    c1=Idprom/Aprom
    va1=abs(np.random.randn()*0.05+0.3)
    va3=abs(np.random.randn()*0.01+0.1)
    Pr=0.4
    Pl=0.4
    Pe=0.2
    
    Di=Tc+(np.random.randn())*3+5
    Df=Tc+Dc-np.random.randn()*3-5
    
    
    kf=np.round(fs*(Df-Di))
    D1=kf-1
    km=D1/2
    Id=c1*Ac
    D2=va1*D1
    va2=abs(np.random.randn()*0.01+D2/2) 
    kd=km-va2
    ka=kd+D2
    
    RLE=np.random.rand()
    if ((RLE>=0)&(RLE<0.4)):
        Aka=Id
        Akd=Id-va3*Id
    elif((RLE>=0.4)&(RLE<0.8)):
        Akd=Id
        Aka=Id-va3*Id
    else:
        Aka=Id
        Akd=Id
    
    
    
    k1=np.arange(1,kd+1)
    k2=np.arange(kd+1,ka+1)
    k3=np.arange(ka+1,kf+1)
    x1=1.
    x2=kd
    x3=ka
    x4=kf
    y1=0.
    y2=Akd
    y3=Aka
    y4=0.
    dip1=((y2-y1)/(x2-x1))*(k1-x1)+y1
    dip2=((y3-y2)/(x3-x2))*(k2-x2)+y2
    dip3=((y4-y3)/(x4-x3))*(k3-x3)+y3
    dip=np.concatenate([dip1, dip2, dip3])

    return np.array([dip, Di])


'''Funcion para la Desaceleración Tardía (DIP 2)'''
def DIP2(Tc,Dc,Ac,Tprof,Aprom,fs, hrmean):
    
    des = hrmean - Tprof
    if(des < 10):
        T = 60 + 10*np.random.rand()
    else:
        T = 60 + ((des-10)/35)*40 + 10*np.random.rand()
    t0 = 0
    t1 = 15 - 5*np.random.rand()
    t2 = T/2 + 5 + 15*np.random.rand()
    t3 = T
    b0 = 0
    b1 = des*(1 - np.random.rand())
    b2 = des 
    b3 = 0
    
    tdi = np.random.randn()*10+20
    Di=(Tc+Dc/2)+tdi
    Ts = 1/250
    
 
    T = float(T)
    #t0,t1,t2,t3,b0,b1,b2,Ts = float(t0), float(t1),float(t2),float(t3), float(b0), float(b1), float(b2), float(Ts)  
    m1 = (b1-b0)/(t1-t0) #pendiente de desaceleracion de la dip
    m2 = (b2-b1)/(t2-t1) #pendiente de aceleracion de la dip
    m3 = (b3-b2)/(t3-t2)
    # bajada
    rampa0 = m1*rampa(T,t0,Ts)
    rampa1 = m1*rampa(T,t1,Ts)
    # subida 1 (sube poco)
    rampa2 = m2*rampa(T,t1,Ts)
    rampa3 = m2*rampa(T,t2,Ts)
    # ultima subida
    rampa4 = m3*rampa(T,t2,Ts)
   
    dip = -(rampa0 - rampa1 + rampa2 - rampa3 + rampa4  + b0)
        
        
        
    return np.array([dip,Di])

'''Funcion para la Desaceleración Variable (DIP 3)'''





def DIP3(Tc, Dc, Tdur, Tprof, hrmean): 
    
    des = hrmean - Tprof
    T = Tdur
    t0 = 0
    t1 = 10 - 5*np.random.rand()
    t2 = T/2 + 5 + 15*np.random.rand()
    t3 = T
    b0 = 0
    b1 = des
    b2 = b1 - 10 - 15*np.random.rand()
    b3 = 0
    
    tdi = np.random.randn()*10+20
    Di=(Tc+Dc/2)+tdi
    Ts = 1/250
    
    if(Tdur > 60):
        T = float(T)
        #t0,t1,t2,t3,b0,b1,b2,Ts = float(t0), float(t1),float(t2),float(t3), float(b0), float(b1), float(b2), float(Ts)  
        m1 = (b1-b0)/(t1-t0) #pendiente de desaceleracion de la dip
        m2 = (b2-b1)/(t2-t1) #pendiente de aceleracion de la dip
        m3 = (b3-b2)/(t3-t2)
        # bajada
        rampa0 = m1*rampa(T,t0,Ts)
        rampa1 = m1*rampa(T,t1,Ts)
        # subida 1 (sube poco)
        rampa2 = m2*rampa(T,t1,Ts)
        rampa3 = m2*rampa(T,t2,Ts)
        # ultima subida
        rampa4 = m3*rampa(T,t2,Ts)
       
        dip = -(rampa0 - rampa1 + rampa2 - rampa3 + rampa4  + b0)
        

    else:
        T = float(T) 
        #t0,t1,t2,t3,b0,b1,b2,b3,Ts = float(t0), float(t1),float(t2),float(t3), float(b0), float(b1), float(b2), float(Ts) 
        m1 = (b1-b0)/(t1-t0) #pendiente de desaceleracion de la dip 
        m2 = (b2-b1)/(t3-t2) #pendiente de aceleracion de la dip
    
        rampa1 = m1*rampa(T,t0,Ts) 
        rampa2 = m1*rampa(T,t1,Ts) 
        rampa3 = m2*rampa(T,t2,Ts) 
        rampa4 = m2*rampa(T,t3,Ts) 
        dip = -(rampa1-rampa2 +rampa3 - rampa4 + b0)
        
        
    return np.array([dip,Di])


'''Funcion para la Desaceleración Desaceleracion prolongada (Dip4)'''

def DIP4(Tc, Dc, Tdur, Tprof, hrmean): 
    
    des = hrmean - Tprof
    T = Tdur
    t0 = 0
    t1 = 10 - 5*np.random.rand()
    t2 = 0.7*T + 15*np.random.rand()
    t3 = T
    b0 = 0
    b1 = des
    b2 = b1 - 10 - 15*np.random.rand()
    b3 = 0
    
    tdi = np.random.randn()*10+20
    Di=(Tc+Dc/2)+tdi
    Ts = 1/250
    
    T = float(T)
    #t0,t1,t2,t3,b0,b1,b2,Ts = float(t0), float(t1),float(t2),float(t3), float(b0), float(b1), float(b2), float(Ts)  
    m1 = (b1-b0)/(t1-t0) #pendiente de desaceleracion de la dip
    m2 = (b2-b1)/(t2-t1) #pendiente de aceleracion de la dip
    m3 = (b3-b2)/(t3-t2)
    # bajada
    rampa0 = m1*rampa(T,t0,Ts)
    rampa1 = m1*rampa(T,t1,Ts)
    # subida 1 (sube poco)
    rampa2 = m2*rampa(T,t1,Ts)
    rampa3 = m2*rampa(T,t2,Ts)
    # ultima subida
    rampa4 = m3*rampa(T,t2,Ts)
   
    dip = -(rampa0 - rampa1 + rampa2 - rampa3 + rampa4  + b0)
        
        
    return np.array([dip,Di])


'''Generador de las DIPs'''

def DIPgenerator(Tc,Ttipo,Dc,Ac,Aprom,t,fs, Tdur, Tprof, hrmean):
    '''print Tc
    print Ttipo
    print Dc
    print Ac
    print Aprom
    print len(t)
    print fs'''
    
    print 'valores de la Duracion para cada caso: ', Tdur
    print 'valores de la profundidad para cada caso: ', Tprof
    
    N=len(t)
    dips=np.zeros(N)
    h=np.zeros(N)
    #rrint=cumtrapz(rr)
    for k in range (0,len(Ttipo)):
        a=1./fs
        if (Ttipo[k]==1): #Precoz
            #var = [dip,Di]
            var=DIP1(Tc[k],Dc[k],Ac[k],Aprom,fs)
            b=np.where((t>=var[1]-a)&(t<=var[1]+a))[0]
            onpulso=b[0]
            porcion = len(dips[onpulso:])
            if (porcion < len(var[0])):
                dips[onpulso:]=(var[0])[0:porcion]
                h[onpulso:]=np.hanning(porcion)
            else:
                dips[onpulso:(onpulso+len(var[0]-1))]=var[0]
                h[onpulso:(onpulso+len(var[0]))]=np.hanning(len(var[0]))
        
        elif (Ttipo[k]==2):  #Tardía
            #var = [dip,Di]
            var=DIP2(Tc[k],Dc[k],Ac[k],Tprof[k],Aprom,fs,hrmean)
            b=np.where((t>=var[1]-a)&(t<=var[1]+a))[0]
            if len(b) >0 :
                onpulso=b[0]
                porcion = len(dips[onpulso:])
                if (porcion < len(var[0])):
                    dips[onpulso:]=(var[0])[0:porcion]
                    h[onpulso:]=np.hanning(porcion)
                else:
                    dips[onpulso:(onpulso+len(var[0]-1))]=var[0]
                    h[onpulso:(onpulso+len(var[0]))]=np.hanning(len(var[0]))
                
        elif (Ttipo[k]==3): #Variable
            #var = [dip,Di]
            #var=DIP3(Tc[k],Dc[k],Ac[k],Aprom,fs, Tprof[k])
            var=DIP3(Tc[k],Dc[k],Tdur[k],Tprof[k],hrmean)
            b=np.where((t>=var[1]-a)&(t<=var[1]+a))[0]
            if (len(b)) >0 :
                onpulso=b[0]
                porcion = len(dips[onpulso:])
                if (porcion < len(var[0])):
                    dips[onpulso:]=(var[0])[0:porcion]
                    h[onpulso:]=np.hanning(porcion)
                else:
                    dips[onpulso:(onpulso+len(var[0]-1))]=var[0]
                    h[onpulso:(onpulso+len(var[0]))]=np.hanning(len(var[0]))
                    
        elif (Ttipo[k]==4): #Variable
            #var = [dip,Di]
            #var=DIP3(Tc[k],Dc[k],Ac[k],Aprom,fs, Tprof[k])
            var=DIP4(Tc[k],Dc[k],Tdur[k],Tprof[k],hrmean)
            b=np.where((t>=var[1]-a)&(t<=var[1]+a))[0]
            if (len(b)) >0 :
                onpulso=b[0]
                porcion = len(dips[onpulso:])
                if (porcion < len(var[0])):
                    dips[onpulso:]=(var[0])[0:porcion]
                    h[onpulso:]=np.hanning(porcion)
                else:
                    dips[onpulso:(onpulso+len(var[0]-1))]=var[0]
                    h[onpulso:(onpulso+len(var[0]))]=np.hanning(len(var[0]))
        
        #incluir la aceleracion aca mismo
        # para ello pasar pmf a RR y de ahi sumarlo
        # en el intervalo a rr0 y actualizar rr
        
    return np.array([dips,h])

def analisiswav(sig,tipo):

    coef= pywt.wavedec(sig, tipo, level=12)
    tendencia = pywt.upcoef('a', coef[0], tipo, level=12, take = len(sig))
    return  tendencia



