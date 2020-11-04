import numpy as np
archive=open("estadisticas.txt","w")
def separar(x,sistol,diasto):
    partes=x.split("/")
    sistol.append(int(partes[0]))
    diasto.append(int(partes[1]))
def esta(lista1,examen1,mes1,lista2,examen2,mes2):
    for o in range(len(lista1)):
        if not lista1[o] in lista2:                    
            lista2.append(lista1[o]) 
            examen2.append(examen1[o])
            mes2.append(mes1[o])           
        if lista1[o] in lista2:
            x=lista2.index(lista1[o])
            examen2[x]=examen1[o]
            mes2[x]=mes1[o]
matriz=np.zeros([12,3])
año=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
tipo=[]
valor_normal=[]
valor_alterado=[]
diagnostico=[]
rut=[]   
paciente=[]
genero=[]
edad=[]
rut1=[]
mes=[]  
examenes1=[]  
resultado=[]
paci=open("pacientes.txt","r")
linea=paci.readline().strip()
rut40_masc=[]
rut40_feme=[]
while linea!="":
    partes=linea.split(",")
    rut.append(partes[0])
    paciente.append(partes[1])
    genero.append(partes[2])
    edad.append(int(partes[3]))
    if int(partes[3])>40:
        if partes[2]=="M":
            rut40_masc.append(partes[0])
        else:
            rut40_feme.append(partes[0])    
    linea=paci.readline().strip()    
paci.close
exame=open("examenes.txt","r")
linea=exame.readline().strip()
alterado=[]
normal=[]
while linea!="":    
    partes=linea.split(",") 
    tipo.append(partes[0])
    valor_normal.append(partes[1])
    valor_alterado.append(partes[2])
    diagnostico.append(partes[3])
    if partes[0]=="P":
        alterado.append(partes[2])
        normal.append(partes[1])   
    linea=exame.readline().strip()
exame.close
regis=open("registro.txt","r")
linea=regis.readline().strip()
while linea!="":
    partes=linea.split(",")   
    if partes[0]=="O":
        linea=regis.readline().strip()
    else:     
        rut1.append(partes[0])
        mes.append(partes[1])
        examenes1.append(partes[2])
        resultado.append(partes[3])  
        linea=regis.readline().strip()   
suma=0
for i in mes:
    x=año.index(i)
    y=tipo.index(examenes1[suma])
    suma+=1
    matriz[x][y]+=1
R_presion=[]
R_curva=[]
R_colesterol=[]
M_presion=[]
M_curva=[]
M_colesterol=[]  
for i in range(len(examenes1)):
     if examenes1[i]=="P":
         R_presion.append(resultado[i])
         M_presion.append(mes[i])
     if examenes1[i]=="G":
         R_curva.append(resultado[i])
         M_curva.append(mes[i])
     if examenes1[i]=="C":
         R_colesterol.append(resultado[i])
         M_colesterol.append(mes[i])
archive.write("*A*\n")
archive.write("Presión Arterial\n")
for f in range(len(año)):
    g=0
    archive.write(año[f])
    archive.write(",")
    archive.write(str(int(matriz[f][g])))
    archive.write("\n")
archive.write("Colesterol\n")   
for j in range(len(año)):
    g=2
    archive.write(año[j])
    archive.write(",")
    archive.write(str(int(matriz[j][g])))
    archive.write("\n")
archive.write("Curva de Tolerancia a la Glucosa\n")    
for k in range(len(año)):    
    g=1
    archive.write(año[k])
    archive.write(",")
    archive.write(str(int(matriz[k][g])))
    archive.write("\n") 
normal_sistol=[]
alterado_sistol=[]
normal_diasto=[]
alterado_diasto=[] 
sistol=[]
diasto=[]
for i in R_presion:
    separar(i,sistol,diasto)
separar(alterado[0],alterado_sistol,alterado_diasto)
separar(normal[0],normal_sistol,normal_diasto)
archive.write("*B*\n")   
for j in range(len(tipo)):
    if tipo[j]=="P":        
        archive.write("Presión Arterial\n")         
        for i in año:
            cont1=0
            cont2=0
            cont3=0
            c=0            
            for h in range(len(M_presion)):                
                if  M_presion[h]==i:                    
                    if alterado_sistol[j]<=sistol[h] or alterado_diasto[j]<=diasto[h]:                         
                         cont1+=1                    
                    elif normal_sistol[j]>=sistol[h] or normal_diasto[j]>=diasto[h]:                                                 
                         cont2+=1                   
                    else:
                         cont3+=1
                c=cont1+cont2+cont3               
            if c!=0:
                pro1=cont1*100/c
                pro2=cont2*100/c
                pro3=cont3*100/c
            else:
                pro1=0
                pro2=0
                pro3=0        
            archive.write(i)
            archive.write(",")
            archive.write(str(int(round(pro2)))+"%"+",")        
            archive.write(str(int(round(pro3)))+"%"+",")        
            archive.write(str(int(round(pro1)))+"%")
            archive.write("\n")
    if tipo[j]=="C":    
        archive.write("Colesterol\n")
        for i in año:
            cont1=0
            cont2=0
            cont3=0
            c=0
            for h in range(len(M_colesterol)):                
                 if M_colesterol[h]==i:                     
                     if (int(valor_alterado[j]))<=int(R_colesterol[h]):                         
                         cont1+=1                     
                     elif (int(valor_normal[j]))>=int(R_colesterol[h]):                         
                         cont2+=1                     
                     else:
                         cont3+=1
                 c=cont1+cont2+cont3                 
            if c!=0:
                pro1=cont1*100/c
                pro2=cont2*100/c
                pro3=cont3*100/c
            else:
                pro1=0
                pro2=0
                pro3=0            
            archive.write(i)
            archive.write(",")
            archive.write(str(int(round(pro2)))+"%"+",")            
            archive.write(str(int(round(pro3)))+"%"+",")            
            archive.write(str(int(round(pro1)))+"%")
            archive.write("\n")                        
for j in range(len(tipo)):              
    if tipo[j]=="G":        
        archive.write("Curva de Tolerancia a la Glucosa\n")               
        for i in año:
            cont1=0
            cont2=0
            cont3=0
            c=0
            for h in range(len(M_curva)):              
                 if M_curva[h]==i:                   
                     if (int(valor_alterado[j]))<=int(R_curva[h]):                       
                         cont1+=1                   
                     elif (int(valor_normal[j]))>=int(R_curva[h]):                       
                         cont2+=1                   
                     else:
                         cont3+=1
                 c=cont1+cont2+cont3               
            if c!=0:
                pro1=cont1*100/c
                pro2=cont2*100/c
                pro3=cont3*100/c
            else:
                pro1=0
                pro2=0
                pro3=0
            archive.write(i)
            archive.write(",")
            archive.write(str(int(round(pro2)))+"%"+",")          
            archive.write(str(int(round(pro3)))+"%"+",")          
            archive.write(str(int(round(pro1)))+"%")
            archive.write("\n")
rut_curva=[] 
examenes_curva=[]
mes_curva=[]
rut_curva2=[]               
examenes_curva2=[] 
mes_curva2=[]         
rut_coles=[]
examenes_coles=[]
mes_coles=[]
rut_coles2=[]
examenes_coles2=[] 
mes_coles2=[]
rut_pre=[]
examenes_pre=[]
mes_pre=[]
rut_pre2=[]
examenes_pre2=[]
mes_pre2=[]
sisto11=[]
diasto11=[]
for i in range(len(examenes1)):
    if examenes1[i]=="P":
        rut_pre.append(rut1[i])
        examenes_pre.append(resultado[i])
        mes_pre.append(mes[i])
    if examenes1[i]=="G":
        rut_curva.append(rut1[i])
        examenes_curva.append(resultado[i])
        mes_curva.append(mes[i])       
    if examenes1[i]=="C":
        rut_coles.append(rut1[i])
        examenes_coles.append(resultado[i])
        mes_coles.append(mes[i])
esta(rut_curva,examenes_curva,mes_curva,rut_curva2,examenes_curva2,mes_curva2)        
esta(rut_coles,examenes_coles,mes_coles,rut_coles2,examenes_coles2,mes_coles2)
esta(rut_pre,examenes_pre,mes_pre,rut_pre2,examenes_pre2,mes_pre2)
for u in range(len(examenes_pre2)):
    separar(examenes_pre2[u],sisto11,diasto11)              
con2=0    
con33=0  
con25=0
con35=0
con45=0     
con55=0
for j in range(len(tipo)):   
    if tipo[j]=="P":
        for i in range(len(sisto11)):
            if int(sisto11[i])<=int(normal_sistol[0]) or int(diasto11[i])<=int(normal_diasto[0]):
                con45+=1
            else:
                con55+=1
    if tipo[j]=="G":
        for i in range(len(examenes_curva2)):
            if int(examenes_curva2[i])<=int(valor_normal[j]):              
                con2+=1
            else:
                con33+=1
    if tipo[j]=="C":
        for i in range(len(examenes_coles2)):
            if int(examenes_coles2[i])<=int(valor_normal[j]):              
                con25+=1
            else:
                con35+=1           
total12=con2+con33  
total13=con25+con35 
total14=con45+con55  
archive.write("*C*\n")
archive.write("Presión Arterial\n")
archive.write(str(int(round(con45*100/total14)))+"%")
archive.write("\n")       
archive.write("Colesterol\n")
archive.write(str(int(round(con25*100/total13)))+"%")
archive.write("\n")      
archive.write("Curva de Tolerancia a la Glucosa\n")
archive.write(str(int(round(con2*100/total12)))+"%")
archive.write("\n")
matriz_H=np.zeros([len(rut),len(año)])
matriz_F=np.zeros([len(rut),len(año)])
normal_P=[]  
normal_G=[]
normal_C=[]
alterado_G=[]
alterado_C=[]  
for k in range(len(tipo)):
    if tipo[k]=="P":
        normal_P.append(valor_normal[k])
    if tipo[k]=="G":
        normal_G.append(valor_normal[k])
        alterado_G.append(valor_alterado[k])
    if tipo[k]=="C":
        normal_C.append(valor_normal[k])
        alterado_C.append(valor_alterado[k])      
contador_hombres=0  
contador_mujeres=0 
rut_mujeres=[]   ###3 puesto demas   
for s in range(len(rut)):
    if genero[s]=="M":
        contador_hombres+=1
    elif genero[s]=="F":    
        contador_mujeres+=1     
for i in range(len(rut_curva2)):
    if int(examenes_curva2[i])>int(normal_G[0]):
        x=rut.index(rut_curva2[i])
        if int(edad[x])>40:
            if genero[x]=="M":
                y=año.index(mes_curva2[i])
                matriz_H[x][y]+=1
            elif genero[x]=="F":             
                y=año.index(mes_curva2[i])
                matriz_F[x][y]+=1         
for i in range(len(rut_coles2)):
    if int(examenes_coles2[i])>int(normal_C[0]):
        x=rut.index(rut_coles2[i])
        if int(edad[x])>40:
            if genero[x]=="M":
                y=año.index(mes_coles2[i])
                matriz_H[x][y]+=1
            elif genero[x]=="F":             
                y=año.index(mes_coles2[i])
                matriz_F[x][y]+=1                       
for i in range(len(rut_pre2)): 
    if int(sisto11[i])>int(normal_sistol[0]) or int(diasto11[i])>int(normal_diasto[0]):
        x=rut.index(rut_pre2[i])
        if int(edad[x])>40:
            if genero[x]=="M":
                y=año.index(mes_pre2[i])
                matriz_H[x][y]+=1
            elif genero[x]=="F":
                y=año.index(mes_pre2[i])
                matriz_F[x][y]+=1
rut_hombres=[] #puesto demas
conta_hombres=0
for fila in range(len(rut)):
    suma=0
    for col in range(len(año)):
        suma=suma+matriz_H[fila][col]
    if suma>=2:
        rut_hombres.append(rut[fila]) #puesto demas
        conta_hombres+=1
conta_mujeres=0
for fila in range(len(rut)):
    suma=0
    for col in range(len(año)):
        suma=suma+matriz_F[fila][col]
    if suma>=2:
        rut_mujeres.append(rut[fila]) # acacacacacsgfgs
        conta_mujeres+=1
archive.write("*D*\n")
archive.write("Mujeres"+" "+str(round(conta_mujeres*100/contador_mujeres))+"%")
archive.write("\n")
archive.write("Hombres"+" "+str(round(conta_hombres*100/contador_hombres))+"%")
archivo=open("diagnosticos.txt","w")
archivo.write("Presión Arterial\n")
for i in año:
    archivo.write(i)  
    archivo.write("\n")
    for j in range(len(rut_pre)):
        if mes_pre[j]==i:         
            archivo.write(rut_pre[j])
            x=rut.index(rut_pre[j])
            archivo.write(",")
            archivo.write(paciente[x])
            archivo.write(",")
            if sistol[j]<=normal_sistol[0] and diasto[j]<=normal_diasto[0]:
                archivo.write("NORMAL")
                archivo.write("\n")
            elif (diasto[j]>normal_diasto[0] and diasto[j]<alterado_diasto[0]) or (sistol[j]>normal_sistol[0] and sistol[j]<alterado_sistol[0]):
                archivo.write("PRECAUCIÓN")
                archivo.write("\n")
            elif sistol[j]>=alterado_sistol[0] or diasto[j]>=alterado_diasto[0] :
                archivo.write("HIPERTENSIÓN")
                archivo.write("\n")               
archivo.write("Colesterol\n")
for i in año:
    archivo.write(i)  
    archivo.write("\n")
    for j in range(len(rut_coles)):
        if mes_coles[j]==i:
            archivo.write(rut_coles[j])
            x=rut.index(rut_coles[j])
            archivo.write(",")
            archivo.write(paciente[x])
            archivo.write(",")
            if int(R_colesterol[j])<=int(normal_C[0]):
                archivo.write("NORMAL")
                archivo.write("\n")
            elif int(R_colesterol[j])<int(alterado_C[0]) and int(R_colesterol[j])>int(normal_C[0]):
                archivo.write("PRECAUCIÓN")
                archivo.write("\n")
            elif int(R_colesterol[j])>=int(alterado_C[0]):
                 archivo.write("RIESGOSO")
                 archivo.write("\n")                     
archivo.write("Curva de Tolerancia a la Glucosa\n")              
for i in año:
    archivo.write(i)  
    archivo.write("\n")
    for j in range(len(rut_curva)):
        if mes_curva[j]==i:
            archivo.write(rut_curva[j])
            x=rut.index(rut_curva[j])
            archivo.write(",")
            archivo.write(paciente[x])
            archivo.write(",")
            if int(R_curva[j])<=int(normal_G[0]):
                archivo.write("NORMAL")
                archivo.write("\n")
            elif int(R_curva[j])<int(alterado_G[0]) and int(R_curva[j])>int(normal_G[0]):
                archivo.write("PRECAUCIÓN")
                archivo.write("\n")
            elif int(R_curva[j])>=int(alterado_G[0]):
                 archivo.write("DIABETES")
                 archivo.write("\n")              
archivo.close()



    