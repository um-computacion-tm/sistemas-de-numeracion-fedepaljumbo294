import unittest

def decimal_binario(numero):
 
    resto = ''
    while numero >1:

        resto+=str(numero%2)
        numero=numero//2
    resto+= str(numero)
    resto= resto[::-1]
          
    return resto
    
def decimal_octal(numero):
   
    resto = ''
    while numero >8:
        
        resto+=str(numero%8)
        numero=numero//8
        
    resto+= str(numero)
    resto= resto[::-1]
    
    return resto

def decimal_hexa(numero):
    
    resto=''
    while numero >=16:
        
        resto+= pasa_letras(numero)
        numero=numero//16
       
    
    resto += str(numero)
    resto= resto[::-1]
    
    return resto
def pasa_letras(numero):
    resto = ''
    letra = str(numero%16)
    if letra == '10':
        letra='A'
        resto+=str(letra)
    elif letra == '11':
        letra='B'
        resto+=str(letra)
    elif letra == '12':
        letra='C'
        resto+=str(letra)
    elif letra == '13':
        letra='D'
        resto+=str(letra)
    elif letra == '14':
        letra='E'
        resto+=str(letra)
    elif letra == '15':
        letra='F'
        resto+=str(letra)
    else:   
        resto+=str(letra)
    return resto

def binario_decimal(numero):

    resto=0
    positivo=0

    for i in range(len(numero)-1, -1, -1):
        resto+= (int(numero[i])*(2**positivo))
        positivo=positivo+1
 
    return resto        
      
def octal_decimal(numero):
    
    resto=0
    positivo=0

    for i in range(len(numero)-1, -1, -1):
        resto+= (int(numero[i])*(8**positivo))
        positivo=positivo+1        
    return resto        
        
def hexa_decimal(numero):
    
    resto=0
    positivo=0

    for i in range(len(numero)-1, -1, -1):
        if numero[i]=='A':
            resto+=10*(16**positivo)
            positivo=positivo+1
        elif numero[i]=='B':
            resto+=11*(16**positivo)
            positivo=positivo+1
        elif numero[i]=='C':
            resto+=12*(16**positivo)
            positivo=positivo+1
        elif numero[i]=='D':
            resto+=13*(16**positivo)
            positivo=positivo+1
        elif numero[i]=='E':
            resto+=14*(16**positivo)
            positivo=positivo+1
        elif numero[i]=='F':
            resto+=15*(16**positivo)
            positivo=positivo+1
        else:
            resto+= (int(numero[i])*(16**positivo))
            positivo=positivo+1    
    return resto  

def binario_octal(numero):
    aux=binario_decimal(numero)
    resto=int(decimal_octal(aux))
    return resto

def binario_hexa(numero):
    aux=binario_decimal(numero)
    resto=decimal_hexa(aux)
    return resto

def octal_hexa(numero):
    aux=octal_decimal(numero)
    resto=decimal_hexa(aux)
    return resto

def hexa_octal(numero):
    aux=hexa_decimal(numero)
    resto=int(decimal_octal(aux))
    return resto

if __name__=="__main__":
    unittest.main()