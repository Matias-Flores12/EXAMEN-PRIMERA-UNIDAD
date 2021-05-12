#ejercicio 1
def notafinalMUFA():
  print("la nota final es")
  #variable
  notafinalMUFA = 0.00
  #datos de entrada
  U1=float(input("ingrese nota de la primera unidad: "))
  U2=float(input("ingrese nota de la segunda unidad: "))
  U3=float(input("ingrese nota de la tercera unidad: "))
  TF=float(input("ingrese nota del trabajo final: "))
  #proceso
  if 0<=U1<=20 and 0<=U2<=20 and 0<=U3<=20 and 0<=TF<=20:
    notafinalMUFA=(U1*(20*0.2)/20+U2*(20*0.15)/20+U3*(20*0.15)/20+TF*(20*0.5)/20)
    #datos de salida
    print("\nla nota final es:", notafinalMUFA)
  else:
    print("\ningrese bien los datosd, las notas solo estan comprendido de 0 a 20")
#notafinalMUFA()



#ejercicio 2
def bonoprofesorMUFA():
  print("Calcularel bono de acuerdo a su puntuacion")
  #variables
  bonoObtenidoMUFA = 0.00
  #datos de dentrada
  puntos=int(input("ingrese puntos obtenidos: "))
  SMinimo=float(input("ingrese el salario minimo: "))
  #proceso
  if puntos>=50 and puntos<=100:
    bonoObtenidoMUFA=SMinimo*0.1
  elif puntos>=101 and puntos<=150:
    bonoObtenidoMUFA=SMinimo*0.4
  elif puntos>=151:
    bonoObtenidoMUFA=SMinimo*0.7
  #datos de salida
  print("el bono que recibira es: ", bonoObtenidoMUFA)
#bonoprofesorMUFA()



#ejercicio 3
def dosisdevacunacovid19MUFA():
  print("tipo de dosis de vacuna que se debe aplicar")
  #variable
  TipodevacunaMUFA = ""
  F = "FEMENINO"
  M = "MASCULINO"
  #datos de entrada
  edad=int(input("digitar la edad de la persona: "))
  sexo= input("digitar el sexo de la persona: ")
  #proceso
  if sexo=='FEMENINO' or sexo=='MASCULINO':
    if edad>=70 and sexo=='FEMENINO' or sexo=='MASCULINO':
      TipodevacunaMUFA="C"
    elif 16<=edad<=69 and sexo=='FEMENINO':
      TipodevacunaMUFA="B"
    elif 16<=edad<=69 and sexo=='MASCULINO':
      TipodevacunaMUFA="A"
    elif edad<16 and sexo=='FEMENINO' or sexo=='MASCULINO':
      TipodevacunaMUFA="A"
    #datos de salida
  print("el tipo de vacuna que la persona debe recibir es: ", TipodevacunaMUFA)
#dosisdevacunacovid19MUFA()



#ejercicio 4
def operacionaritmeticaMUFA():
  print("operacione aritmetica")
  #variable
  resultado= 0
  #datos de entrada
  numero1=float(input("ingrese el primer numero: "))
  numero2=float(input("ingrese el segundo numero: "))
  operacion= input("ingrese la operacion: ")
  #proceso
  if operacion=='+':
    resultado=numero1+numero2
  elif operacion=='-':
    resultado=numero1-numero2
  elif operacion=='/':
    resultado=numero1/numero2
  elif operacion=='*':
    resultado=numero1*numero2
  elif operacion=='^':
    resultado=numero1**numero2
  else:
    resultado="la operacion es incorrecta"
  #datos de salida
  print("el resultado es: ",resultado)
#operacionaritmeticaMUFA()


#ejercicio 5
def algoritmodeejercicosresueltos(): 
  print("Prueba de los ejercios realizados anteriormente")
  #variable
  NumerodeEjercicio = 0
  #datos de entrada
  NumerodeEjercicio=int(input("Ingresar el numero de ejercicio a realizar: "))
  if NumerodeEjercicio>=2 and NumerodeEjercicio<=3:
    if NumerodeEjercicio==2:
      def bonoprofesorMUFA():
        print("Calcularel bono de acuerdo a su puntuacion")
        #variables
        bonoObtenidoMUFA = 0.00
        #datos de dentrada
        puntos=int(input("ingrese puntos obtenidos: "))
        SMinimo=float(input("ingrese el salario minimo: "))
        #proceso
        if puntos>=50 and puntos<=100:
          bonoObtenidoMUFA=SMinimo*0.1
        elif puntos>=101 and puntos<=150:
          bonoObtenidoMUFA=SMinimo*0.4
        elif puntos>=151:
          bonoObtenidoMUFA=SMinimo*0.7
        #datos de salida
        print("el bono que recibira es: ", bonoObtenidoMUFA)
      bonoprofesorMUFA()
    elif  NumerodeEjercicio==3:
      def dosisdevacunacovid19MUFA():
        print("tipo de dosis de vacuna que se debe aplicar")
        #variable
        TipodevacunaMUFA = ""
        F = "FEMENINO"
        M = "MASCULINO"
        #datos de entrada
        edad=int(input("digitar la edad de la persona: "))
        sexo= input("digitar el sexo de la persona: ")
        #proceso
        if sexo=='FEMENINO' or sexo=='MASCULINO':
          if edad>=70 and sexo=='FEMENINO' or sexo=='MASCULINO':
            TipodevacunaMUFA="C"
          elif 16<=edad<=69 and sexo=='FEMENINO':
            TipodevacunaMUFA="B"
          elif 16<=edad<=69 and sexo=='MASCULINO':
            TipodevacunaMUFA="A"
          elif edad<16 and sexo=='FEMENINO' or sexo=='MASCULINO':
            TipodevacunaMUFA="A"
          #datos de salida
        print("el tipo de vacuna que la persona debe recibir es: ", TipodevacunaMUFA)
      dosisdevacunacovid19MUFA()
#Datos de salida
print("ejecutar el ejercicio realizado: " ,algoritmodeejercicosresueltos)
algoritmodeejercicosresueltos()