# Clases Python 2024

**pycheck** es un comprobador de ejercicios escritos en Python.

### **Instalación**

```bash
$ pip install git+http://get.pycheck.es
```

Es necesario tener instalado git: [¿Cómo instalar git?](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git) Si no funciona con `python` prueba con `python3`

Si todo ha ido bien, deberías poder ejecutar la herramienta de la siguiente manera:

```bash
$ pycheck
```

Asegúrate de que se localizan los ejecutables: [¿Cómo configurar el PATH?](https://realpython.com/add-python-to-path/)

### **Versión**

```bash
$ pycheck --version
```

### **Actualización**

```bash
$ pycheck update
```

### **Documentación**

Permite abrir la documentación del proyecto directamente en un navegador web:

```bash
$ pycheck docs
```

### **Enunciado**

Cada ejercicio tiene un **identificador** asociado. Una vez que lo sepamos podremos realizar una serie de acciones sobre el mismo. Supongamos que vamos a trabajar con un ejercicio cuyo identificador es `sum`.

Para ver el enunciado del ejercicio ejecutamos lo siguiente:

```bash
$ pycheck show sum
```

![https://pycheck.es/static/docs/images/pycheck-show.png](https://pycheck.es/static/docs/images/pycheck-show.png)

Esto nos muestra:

1. Un **título** del ejercicio. *En el encabezado del marco*.
2. Una **descripción** del ejercicio: *Texto Markdown*.
3. Una lista de **casos de comprobación**. *Los casos de comprobación están numerados `#` y se puede hacer referencia a ellos de manera individual*.

### **Plantilla**

Para empezar a trabajar necesitamos la plantilla del ejercicio. La podemos generar de la siguiente manera:

```bash
$ pycheck template sum
```

Esto generará un fichero `sum.py` en la carpeta de trabajo con el siguiente contenido:

```bash
# ********************
# LA SUMA MÁS SENCILLA
# ********************


def run(a: int, b: int) -> int:
    result = 'tu código aquí'
    return result


if __name__ == '__main__':
    run(3, 4)
```

> ℹ️ Nuestro código debe empezar en la línea 7.

### **Arranque**

Existe una forma de mostrar la descripción del ejercicio y crear la plantilla, todo de una vez. Para ello usamos el siguiente comando de "arranque":

```bash
$ pycheck boot sum
```

### **Comprobación**

Una vez que hayamos escrito nuestro código sobre la plantilla `sum.py` podemos ver si supera los casos de comprobación. Para ello hacemos:

```bash
$ pycheck check sum
```

Resultado erróneo:

![https://pycheck.es/static/docs/images/pycheck-check1.png](https://pycheck.es/static/docs/images/pycheck-check1.png)

Resultado correcto:

![https://pycheck.es/static/docs/images/pycheck-check2.png](https://pycheck.es/static/docs/images/pycheck-check2.png)

Es posible lanzar un único caso de comprobación. Supongamos que sólo queremos comprobar el caso número 1:

```bash
$ pycheck check -n1 sum
```

Esta opción es muy interesante para poder depurar nuestro código.

### **Ejecución**

Si queremos ejecutar el ejercicio con argumentos propios, podemos hacerlo pasando dichos argumentos desde línea de comandos:

```bash
$ pycheck run sum 1 9
10
```

Es muy importante tener en cuenta que, en la mayoría de situaciones, los argumentos por línea de comandos deben pasarse entrecomillados:

```bash
$ pycheck run sum 1 9
$ pycheck run sum "1" "9"$ pycheck run sum -- 1 -1  # Usar -- para números negativos$ pycheck run sum 3.21 4.56

$ pycheck run sum hola mundo  # 2 argumentos distintos$ pycheck run sum "Hola mundo"  # Un único argumento
$ pycheck run sum True
$ pycheck run sum "True"
$ pycheck run sum "[1, 2, 3]"  # listas$ pycheck run sum "{'a': 1, 'b': 2}"  # diccionarios
```

La documentacion compartida en este repo fue creada por Sergio Delgado Quintero y esta publicada en:
[pycheck.es](https://pycheck.es/)

Formando parte del curso:
[aprendepython.es](https://aprendepython.es/)
