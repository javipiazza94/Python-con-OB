# Asi se comenta en Python

# En Python se identa (se hace una sangria) para organizar el codigo

#Tipos de datos
    #A) Booleanos ---> True o False
    #B) Texto ---> str, van entrecomillas
    #C) Numericos ---> int (enteros), float (decimales), complejos

#Operadores
    #A) Aritmeticos ---> +, -, /, *, %, // (division entera), ** (exponente)
    #B) Logicos ---> AND, OR, NOT
    #C) Especiales ---> IS, IS NOT, IN, NOT IN
    #D) Asignacion ---> = (igual), += (incremento), -= (decremento), *=, /=, %=, **=, //=
    #E) Comparacion ---> == (igual que), != (no es igual que), > (mayor que), < (menor que), <=, >=
    
#Variable ---> Es un espacio de memoria que se puede cambiar durante el tiempo de ejecucion del programa
    #nombre_variable = valor
    #compone de letras, numeros y _
    #la variable es definida por el contenido y no por el contenedor
    #todas las variables son objetos
    
#Las comillas triples hacen saltos de linea
#El flujo de ejecucion va de arriba hacia abajo, menos con los bucles y funciones.

#Funciones ---> conjunto de lineas de codigo agrupadas en un bloque unitario que realizan una tarea especifica
    #Pueden devolver valores
    #Pueden tener parametros
    #Se las llama metodos cuando se definen dentro de una clase
    #Reutiliza codigo
    #Sintaxis ---> def nombre_funcion(parametros(opcional)):
        #codigo
        #return (opcional)
    #Ejecucion ---> nombre_funcion(parametros)
    #predefinidas---> vienen por defecto
    #propias ---> las creamos nosotros
    #Responden a eventos y se llaman en otros archivos
    #void ---> no se les asigna a una variable, se las llama directamente
    #Con return--> Almacenan un valor y se les puede asignar a una variable. --> def funcion = nombrevariable
    #Se declaran como def + nombrefuncion y se llaman con el nombre de la funcion
    # Pueden recibir parametros de diferentes tipos o no
    
#Listas --> Son equivalentes a los arrays, vectores y arraylists. Estructuras de datos que almacenan varios valores en la RAM en una sola unidad
    #Permite almacenar varios tipos de valores en una misma lista
    #Se pueden expandir dinamicamente
    #Sintaxis --> nombrelista = [valor1, valor2]
    #Tienen indices --> posiciones en la lista. Se empieza por el 0
    
#Tuplas --> Son listas inmutables
    #No permiten anadir, borrar, index o mover elementos dentro de una lista
    #Permite extraer porciones, pero sera una tupla nueva
    #No permiten busquedas, pero si comprueba que sus elementos estan en la tupla
    #Son mas rapidas, menos espacio en memoria, mayor optimizacion en ejecucion
    #Pueden usarse como claves en un diccionario
    #Formatean Strings
    #Sintaxis --> nombretupla = (valor1, valor2). Se puede sin parentesis
    
#Diccionarios --> Son estructuras de datos que almacemam todo tipo de valores en forma de asociacion clave(unica):valor
    #No estan ordenados
    #Se pueden almacenar tuplas, listas, otros diccionarios, ademas de otros tipos de datos
    #Se pueden alternar diferentes tipos de valores
    
#Condicionales if --> Modifica el flujo de ejecucion de un programa
    # Si se cumple (TRUE) ejecuta las instrucciones que tiene en su interior
    # Si no se cumple (FALSE) no se ejecuta y sigue la ejecucuon normal (menos si hay un else)
    # Sintaxis -->  #if condicion:
                        #codifo
                    #else:   Siempre va con un if detras, solo no
                        #codigo
    #Si no le metemos un elif el else se considera en el ultimo if, y no en todos los demas. Hace que se comporte como un solo bloque
    #No tiene condicionales switch. Apuesta por la simplicidad
    #Se pueden concadenar con operadores
    #Or == o si no
    
#Bucles --> Sirve para iterar colecciones, estructuras de datos o repetir lineas de codigo
    #Determinados = se sabe el numero de repeticiones --> for variable in elemento a recorrer
    #Indeterminados = no se sabe --> while condicion: 
    #Tiene una declaracion (repeticiones) y un codigo a ejecutar identado
    

    
    


    
    
