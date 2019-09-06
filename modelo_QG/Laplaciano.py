#bplist00—_WebMainResource’	
#_WebResourceData_WebResourceMIMEType_WebResourceTextEncodingName^WebResourceURL_WebResourceFrameNameOÛ<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">""" 
#C√°lculo del laplaciano

#INPUTS
#array_2D: numpy array de dos dimensiones
#ds: paso espacial 

#"""

def Calc_del2(array_2D, ds):

    #Cargamos las librerias necesarias
    import numpy as np   
    del2 = np.zeros(array_2D.shape, float)
    del2[1:-1, 1:-1] = (array_2D[1:-1,2:] + array_2D[1:-1,:-2] + array_2D[2:,1:-1] + array_2D[:-2,1:-1] - 4.*array_2D[1:-1,1:-1])/(ds*ds)
    return del2
