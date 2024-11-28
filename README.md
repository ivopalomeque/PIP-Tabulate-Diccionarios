# PIP (Como npm pero para python)
### PIP es un sistema de gestión de paquetes utilizado para instalar y administrar bibliotecas de software escritas en Python.
### PIP es una herramienta que viene incluida, de forma predeterminada, junto al lenguaje Python desde hace ya varios años. Sin embargo, si necesitamos instalarlo por separado
### Descargamos get-pip.py desde https://bootstrap.pypa.io/get-pip.py
### Una vez instalado, PIP se utiliza desde la línea de comandos o terminal definiendo el nombre de estaherramienta, seguido de la palabra install y, por último, el nombre del paquete o dependencia a instalar.

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 191621.png" width="600"/></a>
	</p>
</div>

### Una vez instalado, PIP se utiliza desde la línea de comandos o terminal definiendo el nombre de esta herramienta, seguido de la palabra install y, por último, el nombre del paquete o dependencia a instalar.

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 191640.png" width="600"/></a>
	</p>
</div>

### Sus comandos más comunes, son:
#### pip install dependencia: para instalar una dependencia en nuestro proyecto
#### pip uninstall dependencia: si queremos quitar alguna dependencia instalada previamente
#### pip install --upgrade dependencia: para actualizar a la última versión
#### pip list: si deseamos ver las dependencias instaladas previamente

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 192115.png" width="600"/></a>
	</p>
</div>

# Tabulate (Para crear tablas en consola)

### Tabulate es un módulo Python en formato de librería el cual nos permite imprimir tablas legibles en la consola a partir de listas de datos o estructuras de datos como diccionarios. 
### Para instalarlo, ejecutamos el siguiente comando en la terminal:

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193233.png" width="600"/></a>
	</p>
</div>

### Instalada la dependencia tabulate, debemos inicializarla en el proyecto donde deseamos utilizarla, importando la misma de la siguiente forma:

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193349.png" width="600"/></a>
	</p>
</div>

#### Luego, si queremos visualizar información desde una lista simple, debemos primero reconvertirla a una estructura tabular, la cual debe incluir índices para una mejor visualización. Veamos un ejemplo:

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193436.png" width="600"/></a>
	</p>
</div>

#### Finalmente, podemos imprimir los datos a visualizar, utilizando diferentes posibles formatos de salida.
#### Entre ellos tenemos a:
- keys
- html
- github
- predeterminado

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193639.png" width="600"/></a>
	</p>
</div>

#### Los formatos predeterminado y keys tienen una estructura similar, por lo tanto casi que no veremos diferencias sustanciales entre ellos.

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193743.png" width="600"/></a>
	</p>
</div>

#### Los formatos html entrega una estructura de tabla HTML con encabezado y cuerpo:

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193833.png" width="600"/></a>
	</p>
</div>

#### El formato github estructura una tabla algo más completa que las anteriores, utilizando el formato markdown para su armado:

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 193928.png" width="600"/></a>
	</p>
</div>

# Diccionarios
### Los diccionarios en Python son estructuras de datos que almacenan pares clave-valor. Son muy versátiles y se utilizan ampliamente debido a su capacidad para almacenar y recuperar datos de manera eficiente.
### En un diccionario, cada elemento está representado por una clave única y su valor correspondiente
#### Dentro de las principales características que encontramos en un diccionario, podemos destacar:
- estructura clave-valor
- claves únicas
- mutabilidad
- heterogeneidad

<div>
	<p>
		<a><img src="./img/Captura de pantalla 2024-11-28 194124.png" width="600"/></a>
	</p>
</div>

#### En este ejemplo, el diccionario estudiante tiene claves como "nombre", "edad", "cursos" y "puntuacion", y cada una tiene su respectivo valor asociado (pares clave-valor).
#### Podemos acceder a los valores de un diccionario utilizando la sintaxis de corchetes [] y la clave:

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194213.png" width="600"/></a>
    </p>
</div>

#### Aquí tenemos un ejemplo de un diccionario de productos electrónicos, algo más elaborado y cercano a las estructuras de datos que estuvimos manejando a lo largo de la diplomatura.

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194350.png" width="600"/></a>
    </p>
</div>

#### Para listar este diccionario, debemos iterarlo primero para armar un diccionario de lista simple, eliminando sus propiedades (clave). Las mismas deben ser representadas en una tupla, como encabezado de la tabla a mostrar:

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194426.png" width="600"/></a>
    </p>
</div>

#### Aquí tenemos un ejemplo de una función que nos permite listar dicho diccionario de datos. Separamos los encabezados en una tupla, y los productos en una lista para luego imprimir todo utilizando tabulate

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194504.png" width="600"/></a>
    </p>
</div>

#### Aquí tenemos el resultado de combinar, en una función, una estructura de diccionario de datos junto con la librería tabulate, para representar la información a visualizar utilizando el formato de representación markdown.

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194536.png" width="600"/></a>
    </p>
</div>

# Importar y Exportar

### Python nos permite modular la estructura de nuestras aplicaciones, generando en archivos separados contenido que tengamos que implementar.
### Esto nos permite estructurar mejor nuestras aplicaciones, separando en capas la lógica, los datos, y el resto de funcionalidades necesarias para nuestra app

#### Por ejemplo, podemos crear un archivo llamado diccionario.py y, en este, definir nuestro diccionario de productos, tal como muestra la siguiente imagen:

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194705.png" width="600"/></a>
    </p>
</div>

#### Luego, desde nuestro archivo principal, podemos importar este diccionario referenciando primero el nombre del archivo y luego el nombre de la variable que deseamos importar:

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194751.png" width="600"/></a>
    </p>
</div>

#### Finalmente podemos hacer uso del diccionario previamente importado dentro de cualquier función Python que necesitemos utilizarlo.

<div>
    <p>
        <a><img src="./img/Captura de pantalla 2024-11-28 194833.png" width="600"/></a>
    </p>
</div>