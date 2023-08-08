#import re
#pregunta = input()
#print(pregunta.split())
#numeros = [int(numeros) for numeros in re.findall(r"-?\d+\.?\d*",pregunta)]
#print(numeros)
def main():
 print("NOTA:Si no tiene uno de estos valores,debera marcarlo en -1\n")
 print("NOTA:El -1 significa que no tenemos ese valor,es decir que es una incognita\n")
 print("NOTA:Para usar este programa debe saber redondear y identificar bien cada valor\n")
 mol_soluto = float(input("mol de soluto:"))
 masa = float(input("masa:"))
 volumen_solucion = float(input("volumen de la solucion:"))
 m = float(input("Concentracion:"))
 #p_m = float(input("Formula quimica"))
 print("\nDATOS:")
 print("mol_soluto = ", mol_soluto)
 print("volumen_solucion = ", volumen_solucion)
 print("masa = ",masa)
 print("M = ",m)
 #print("P_M = ",p_m)
 
 if m < 0:
    M(mol_soluto,volumen_solucion,masa)
 elif masa < 0:
    masas(mol_soluto,volumen_solucion,m)
 elif volumen_solucion < 0:
    volumen_soluciones(mol_soluto,m,masa)      
 elif mol_soluto < 0:
    mol_solutos(m,volumen_solucion)
 print("-------------------------------------------------------------------------")    
 main()
def mol_solutos(m,volumen_solucion):
    print()
    print("Mol de soluto = \t",  str(m) + " x " + str(volumen_solucion))
    print("=",str(m*volumen_solucion))
    #print(         "                    100")
           
def volumen_soluciones(mol_soluto,m,masa):
   print()
   if mol_soluto < 0:
    p_m = input("Introducir valor el peso atomico:")   
    print("Mol de soluto = \t",  str(masa) + " / " + str(p_m))
    print("=",str(masa/float(p_m)))
    mol_soluto = masa/float(p_m)    
   print("Volumen de la solucion = \t","         ",str(mol_soluto))
   print("             -----------------\t","=",str(mol_soluto/m))
   print("                  ",str(m))
def M(mol_soluto,volumen_solucion,masa):
    print()
    p_m = 0
    if mol_soluto < 0:
      p_m_text = input("Introducir valor el peso atomico:")
      p_m = float(p_m_text)
      mol_soluto = masa / p_m      
    print(" M = \t","         ",str(mol_soluto))
    print("             -----------------\t","=",str(mol_soluto/volumen_solucion))
    print("                  ",str(volumen_solucion))  

def masas(mol_soluto,volumen_solucion,m):
   print()
   if mol_soluto < 0:
    print("Mol de soluto = \t",  str(m) + " x " + str(volumen_solucion))
    print("=",str(m*(volumen_solucion) / 1000))  
    mol_soluto = m*(volumen_solucion) / 1000
   p_m = input("Introducir valor el peso atomico:")
   print(" masa = \t",  str(mol_soluto),"x",str(p_m),"\t","=",str(mol_soluto*float(p_m)))  

#def P_M():
#   pass
main()
    


    
     
