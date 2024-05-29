# -*- coding: utf-8 -*-
#
#@author: Juan Darío Muñoz Soto
#
#@version: 2.0 
#
#@date: 02-01-2014
#
#@summary: Funciones para calcular el HRV del feto
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



#Funcion que generadores de campanas en la señal FHR *********************************************************************************

def campanas(tsim,tmf,dmf,imf,fs):
    
    lon1 = np.round(fs*tsim)
    sig = np.zeros(lon1)
    
    #lon = np.array(np.round(np.multiply(dmf,fs)))
    #tMcom = np.array(np.round(np.multiply(tmf,fs)))
    lon = np.round(dmf*fs)
    tMcom = np.round(tmf*fs)
    lon2 = len(tmf)
    for i in range (0,lon2):
        var1 = tMcom[i]+lon[i]-1
        N=len(np.arange(tMcom[i],var1,1))
        t = np.linspace(0,lon[i],N)
        ds = max(t)/8
        u = max(t)/2
        l1 = len(sig[(tMcom[i]):var1]) 
        l2 = len(imf[i]*np.exp(-0.5*((t-u)/ds)**2))
        
        #print l1,l2
        if l1 == l2:
            sig[(tMcom[i]):var1] = imf[i]*np.exp(-0.5*((t-u)/ds)**2)
        else:
            a = (len(sig) - var1)
            sig[(tMcom[i]):var1] = imf[i]*np.exp(-0.5*((t[0:a]-u)/ds)**2)
        
            
    return sig

'''**************************************************************************************************************************************'''

'''Funcion para generar un mov fetal apretando un boton**********************************************************************************'''
def mov_fetal(instante, fs):
    dmf=(60 + 15*np.random.randn())
    
    #% Amplitud de los movimientos fetales 
    promA = 20 
    #%generacion del valor de la amplitud de cada movimiento fetal
    
    imf=  promA + 5*np.random.randn()
    
    #lon1 = np.round(fs*instante)
    #sig = np.zeros(lon1)
    
    lon = dmf*fs
    tMcom = instante+fs
    
    var1 = tMcom+lon # duracion de la campana
    N=len(np.arange(tMcom,var1,1)) #cantidad de elementos del vector campana
    #print(N)
    t = np.linspace(0,lon,N) #vector campana [0,1,2,3,4,5,6,7,8,9,etc]
    sig = np.zeros(len(t)) #vector de salida
    ds = max(t)/8
    u = max(t)/2
    sig[0:var1] = imf*np.exp(-0.5*((t-u)/ds)**2)
    
    return sig



'''Funcion generadora de la frec. cardiaca***********************************************************************************************'''
def HRV(fm,tsim,hrmean0,hrstd0):
    #% PARAMETROS INTERNOS
    lfhfratio = 0.1 # % Energia de LF/Energia de HF
    flo = 0.02      # % frecuencia en Hz en la cual se centra la baja frecuencia (Mayer waves)
    fhi = 1      # % frecuencia en Hz en la cual se centra la alta frecuencia (frecuencia respiratoria)
    flostd = 0.1    # % desviacion estandar de la gausseana que forma la componente de baja frecuencia (nivel de caos o de orden en baja frecuencia)
    fhistd = 0.1    # % desviacion estandar de la gausseana que forma la componente de alta frecuencia (nivel de caos o de orden en alta frecuencia)
    #% -------------------------------------------------------------------------
    
    '''lfhfratio = 0.1
    flo = 0.02
    fhi = 1.        #originales
    flostd = 0.1
    fhistd = 0.1'''
    
    tstart=tsim[0]
    tend=tsim[1]
    
    N=hrmean0*tend/60
    N=round(N+0.05*N) # % se agregan 5% mas de ciclos cardiacos
    
    #% generacion de RR inicial
    
    rr0 = rrprocess(flo,fhi,flostd,fhistd,lfhfratio,hrmean0,hrstd0,1,N)
    
    #% generacion de hrv inicial
    Frr = 1.0/rr0
    hrv0 = Frr*60.0
    
    #% paso de hrv0 a tiempo
    #[HRV0,t]=RRtime(hrv0,fm)
    val = RRtime(hrv0,fm)
    HRV0 = val[0]
    t = val[1]
    #Eliminado campanas de aqui
    '''
    spf = campanas(tend-tstart,tmf,imf,dmf,fm)
    
    spf=np.concatenate([spf,np.zeros(len(val[0])-len(spf))])
    
    
    
    HRV = spf + val[0] #-----------revisar que los datos son filas o columnas porque spf era traspuesta
    senal_HRV = HRV
    '''
    
    tiempo=t
    
    
    
    #% por el momennto
    sigmaHRV= 5*np.ones(len(val[0]))
    hrmean=hrmean0
    
    return [tiempo,sigmaHRV,HRV0,hrmean]


'''Funcion generadora de mov. Fetales ***************************************************************************************************'''
def MF(tsim, CUif, sigmahrv, NMF, fs):
    '''% CUif: señal que impide la ocurrencia de un movimiento fetal si la
    % contraccion uterina es muy fuerte
    % mfuser: listado de candidatos a movimientos fetales
    % sigmahrv: señal de varianza de hrv
    % NMF: numero promedio de movimientos fetales cada 10 min
    '''
    T = tsim
    pmfc10 = NMF
    var = 0.20*NMF
    #MFuser = mfuser
    #[lala, tmf, d, A]= mf4(T,pmfc10,var,MFuser);
    varmf4 = mf4(T,pmfc10,var)
    varhrv = sigmahrv
    cuif = CUif
    tv = 20. #%ventana de 20 segundos 
    tmf = varmf4[1]   #tmf
    dmf = varmf4[2]   #d
    imf = varmf4[3]   #A
    
    #fs = 100
    varout = MF5(varhrv,cuif,tv,tmf,dmf,imf,fs) # [Tmf,Dmf,Imf]
    
    ##print varout, varout


    return np.array([varout[0],varout[1],varout[2]])

'''**************************************************************************************************************************************'''

'''Funcion que ayuda a generar un mov fetal**********************************************************************************************'''
def mf4(T,pmfc10,var):
    T = T/60.    #transformacion de T de segundos a minutos
    ent = int(np.floor(T/10.))
    frac =  T - 10.*ent
    #Unmf = len(MFuser)
    
    '''generacion de numeros aleatorios de movimientos fetales cada 10 min.
    % Esta dividido en dos parte: parte entera (ent) y parte fraccion
    '''
    nmfT = np.zeros(ent)
    tmf = []
    d = []
    A = []
    if (ent > 0):
        for i in range(0,ent):
            nmfT[i] = np.round((np.sqrt(var))*np.random.randn() + pmfc10)
            #%nmfT[i] = round(nmfT(i));
            if (nmfT[i] < 0):
                nmfT[i] = (-1)*nmfT[i]
            
        
        nmfT[ent-1] = np.round((frac/10.)*(np.sqrt(var)*np.random.randn()+ pmfc10))
        if (nmfT[ent-1] < 0): 
            nmfT[ent-1] = (-1)*nmfT[ent-1]
        
        
        #determinación aleatoria de momentos sobre los cuales ocurren los latidos
        lontmf = 0;
        lonx = 0;
        for i in range (0,ent):
            x = (600*np.random.rand(nmfT[i]) + ((i+1)-1)*600)
            lonx = len(x)
            
            tmf[lontmf:lontmf+lonx] = x
            lontmf = len(tmf)
        
        if (nmfT[ent-1]>0):
            aa = len(tmf) + 1
            bb = aa + nmfT[ent-1] - 1
            tmf[int(aa):int(bb)] = 600*(frac/10)*np.random.rand(nmfT[ent-1]) + ent*600
        
        #sumar los movimientos fetales introducidos por el usuario (por ahora no se implementará)
        '''nmfau = len(tmf)
        if (Unmf>0):
            tmf[nmfau+1:Unmf+nmfau] = MFuser
        '''
        tmf = np.sort(tmf)
        cmf = len(tmf)  # % cantidad total de movimientos fetales
        #%% generacion de los movimientos fetales

        #%duracion de cada movimiento fetal
        d = np.zeros([len(tmf)]) 
        for i in range (0,cmf):
            d[i] =(60 + 15*np.random.randn())
        
        A = np.zeros([len(tmf)])
        #% Amplitud de los movimientos fetales 
        promA = 20 
        #%generacion del valor de la amplitud de cada movimiento fetal
        for j in range (0,cmf):
            A[j] =  promA + 5*np.random.randn()
        
    else: 
        nmfT = np.round( (T/10) * ( np.sqrt(var) * np.random.randn() + pmfc10 ))
        promA = 20
        if (nmfT > 0):
            tmf = 600*(T/10)*np.random.rand(nmfT)
            d =12.5 + 2.5*np.random.randn(nmfT)
            A =  promA + 5*np.random.randn(nmfT)
        else:
            tmf = []
            d = []
            A =  []
            
    #print(nmfT)
    #print(tmf)
    #print d ,'d'
    #print A,'A'
    
    
    return [nmfT, tmf, d, A]

'''**************************************************************************************************************************************'''

'''Funcion generadora de mov fetales 5****************************************************************************************************'''
def MF5(varhrv,cuif,tv,tmf,dmf,imf,fs):
    N1 = len(tmf)   #cantidad de latidos fetales tentativos
    j = 1.
    mf1 = 0 #variable auxiliar que ayuda a calcular una probabilidad acumulada
    mf2 = 0 #variable auxiliar que ayuda a calcular una probabilidad acumulada
    alfa = -np.log(0.5)/120.  # constante de tiempo que hace que a los 2 minutos se obtenga el Pmax/2 (120 seg)de probabilidad de que ocurra un movimiento fetal
    Tmf = []
    Dmf = []
    Imf = []
    if (N1>0):
        for i in range (0,N1):
            if (tmf[i] < 1/(fs*60.)):
                tmf[i] = 1/(fs*60.)
            
            #print(tmf[i])
            tiem_mov_fet = tmf[i]
            dur_mov_fet = dmf[i] ##modificado de dmf[i,0] --->>> dmf[i]
            int_mov_fet = imf[i]
            a = mf1
            b = mf2
            mf1 = mf2
            mf2 = tiem_mov_fet
            delta_t = (mf2-mf1)
            ini = np.floor((tiem_mov_fet-tv))
            if (ini<=0):
                ini = 1./(fs)
            
            fin = tiem_mov_fet
            u = np.floor(tiem_mov_fet*fs)
            if (u == 0):
                u = 1
            
            #print(fin)
            
            varhrvi = varhrv[u]
            pmax = pmaxvar(varhrvi)
            pacum = pmax*(1-np.exp((-delta_t)/alfa))
            cuifmax = (cuif[np.floor(ini*fs):np.floor(fin*fs)])
            if ((pacum > np.random.rand()) and (cuifmax.all() == 0)):
                Tmf.append(tiem_mov_fet)
                Dmf.append(dur_mov_fet)
                Imf.append(int_mov_fet)
                j = j+1
            else:
                mf1 = a
                mf2 = b
                cuifmax = 0.
    if (len(Tmf) == 0 ):
        Tmf = []
        Dmf = []
        Imf = []


    return [Tmf,Dmf,Imf]

'''**************************************************************************************************************************************'''

'''Otra funcion *************************************************************************************************************************'''
def rrprocess(flo, fhi, flostd, fhistd, lfhfratio, hrmean, hrstd, sfrr, n):
    w1 = 2.*np.pi*flo
    w2 = 2.*np.pi*fhi
    c1 = 2.*np.pi*flostd
    c2 = 2.*np.pi*fhistd
    sig2 = 1.
    sig1 = lfhfratio
    rrmean = 60./hrmean
    rrstd = 60.*hrstd/(hrmean*hrmean)
    
    df = sfrr/n
    #w = [0:n-1]'*2*np.pi*df;
    w = np.arange(0,n)*2.*np.pi*df
    dw1 = w-w1
    dw2 = w-w2
    Hw1 = sig1*np.exp(-0.5*(dw1/c1)**2)/np.sqrt(2*np.pi*c1**2)
    Hw2 = sig2*np.exp(-0.5*(dw2/c2)**2)/np.sqrt(2*np.pi*c2**2)
    Hw = Hw1 + Hw2
    #Hw0 = [Hw(1:n/2); Hw(n/2:-1:1)] # <----------- ver mas tarde
    Hw0 = np.concatenate([Hw[0:(n/2)], Hw[(n/2):0:-1]]) # en matlab eran 2 filas aca son dos vectores dentro del otro vector
    Sw = (sfrr/2.0)*np.sqrt(Hw0)
    #print len(Sw),'Sw'
    


    ph0 = 2.*np.pi*np.random.rand(n/2.-1) # en matlab era una columna, aca es una fila
    #print len(ph0), 'ph0'
    cero = np.array([0])
    ph = np.concatenate([cero, ph0, cero, -np.flipud(ph0)])
    #print len(ph),'ph'
    SwC = Sw * np.exp(1j*ph)
    x = (1.0/n)*((np.fft.ifft(SwC)).real)
    
    
    
    xstd = np.std(x)
    ratio = rrstd/xstd
    rr = rrmean + (x*ratio)
    
    return rr

'''**************************************************************************************************************************************'''

'''Funcion generadora de RRtime**********************************************************************************************************'''
def RRtime(HRV, fs):
    
    RR = np.array([]);
    rr0 = 60./HRV
    for k in range(0,len(rr0)-2): #revisar legth(rr0)
        ti=sum(rr0[0:k])+rr0[k+1]/2+(1./fs)
        tf=sum(rr0[0:k+1])+float(rr0[k+2]/2)
        t=np.arange(ti,tf,1./fs) #<------ entrega menos datos por el arange, no pesca el tf
        #print len(t)
        y=(rr0[k+1]-rr0[k])*(t-ti)/(tf-ti)+rr0[k] 
        #print len(y), "y"
        RR=np.concatenate([RR, y])  #concatenacion de arreglos
        #print(len(RR))
    
    t=np.arange(0,len(RR))/fs #<------ revisar que el len(RR) sea igual a length(RR)-1 en matlab
    HRV=60./RR
    
    out = np.array([HRV, t])
    return out

'''**************************************************************************************************************************************'''




'''%funcion que calcula la probabilidad maxima en funcion de la varianza de
%hrv'''

'''**************************************************************************************************************************************'''

'''Esta funcion es para algo*************************************************************************************************************'''
def pmaxvar(varhrv):
    varinf = 3  #variancion minima del hvr para que pueda ocurrir un mov fetal con la maxima probabilidad
    varsup = 7  #variancion maxima del hvr para que pueda ocurrir un mov fetal con la maxima probabilidad
    probmax=0.85
    if (varhrv > varinf and varhrv < varsup):
        pmax = probmax #bajar la probabilidad máxima de ocurrencia de un movimiento fetal
    elif (varhrv <= varinf):
        pmax = probmax*varhrv/varinf
    elif (varhrv >= varsup):
        pmax = probmax*np.exp((-0.231*2)*(varhrv - varsup));

    return pmax

'''**************************************************************************************************************************************'''