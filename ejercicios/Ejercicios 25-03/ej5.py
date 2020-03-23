def fibo(n,a=0,b=1):                # Muestra los 10 primeros terminos de la serie de Fibonacci hasta el numero 34.
   while n!=0:                      # Mientras n sea distinto de cero , el while se ejecuta.
      return fibo(n-1,b,a+b)        # n se va disminuyendo en uno, 'a toma el valor de b y b toma el valor de a+b 
   return a                         # Cuando n sea igual a 0, se devuelve a

for i in range(0,10):               # Se imprimen los valores que devuelve la funcion fibo de los valores de n
   print(fibo(i))                   # Calculo la Serie de Fibonacci para n de 0 a 9                                