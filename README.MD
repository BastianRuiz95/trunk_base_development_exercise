# Trunk-Based Development
Este es un ejercicio para el electivo "Introducción a DevOps", donde deberán aplicar Trunk-Based Development para integrar código.

# Actividad
Los estudiantes deberán agruparse de a dos o tres integrantes. Luego, deberán elegir una de las siguientes funcionalidades a desarrollar.

- [ ] Calcular el promedio de un listado de valores.
- [ ] Encontrar el valor máximo dentro de un listado de valores.
- [ ] Obtener el factorial de un número según un input dado.
- [x] Calcular el área de un círculo dado el radio correspondiente.
- [ ] Comprobar si el número entregado por input es primo.
- [ ] Comprobar si una cadena de caracteres es un palíndromo.
- [ ] Ordenar un listado de valores.
- [ ] Obtener la frecuencia de los valores de una lista entregada.
- [ ] Obtener todos las palabras de un texto y colocarlas en una lista.

Cada una de estas funcionalidades debe imprimir su resultado por consola en inglés.

# Instrucciones
1. Se debe generar un archivo con su funcionalidad en la carpeta `functionalities`. Debe llevar por nombre `<nombreFuncion>.py`.
2. En el archivo `__init__.py` de la funcionalidad, deberá agregar el nombre del archivo en la lista de la variable `__all__` entre comillas dobles.
3. Se debe generar una función execute en dicho archivo donde desarrollará el problema asignado.
4. Se debe usar la función execute en el código principal (`main.py`).
5. Probar la aplicación y verificar que todo este funcionando correctamente.

# Ejecución
Para iniciar la aplicación, debe ejecutar lo siguiente en la linea de comandos:
```bash
$ python3 src/main.py
```