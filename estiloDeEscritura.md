# Estilo de escritura
## Convención de nombres
Cada lenguaje de programación tiene su propia convención en como debemos de nombrar nuestras variablas, métodos, clases y otros elemento de nuestro _código_. La convención de codificación es un conjunto de normas para un lenguaje de programación especifico que recomienda estilos de programación, __buenas prácticas y métodos__ para mantener el aspecto del _código_. 
Estas convenciones incluyen:

* organización de archivos
* indentación
* comentarios
* declaraciones de variables
* espacios en blanco
* llaves de apertura y cierre.

Se les recomienda a los desarrolladores para ayudar a mejorar la legibilidad del código y facilitar el mantenimiento del software. Las principales razones de la existencia de estas, son para __reducir los esfuerzos a la hora de leer y entender código__, de esta manera nos centramos en revisar los puntos más importantes de nuestro código.

# Tipos de convenciones de nombres (Técnicas de naming):
- [CamelCase 🐫][1]
- [snake_case 🐍][2]
- [kebab-case 🍢][3]
- [Train-Case 🚂][4]
- [l33t][5]
- [Notación Húngara][6]

## CamelCase 🐫
El nombre se debe a que las mayúsculas a lo largo de una palabra en CamelCase se asemejan a las jorobas de un camello.
Existen dos tipos de CamelCase:
* UpperCamelCase: cuando la primera letra de cada palabra es mayúscula. Ejemplo _EscuelaDeCódigo_
* lowerCamelCase: igual que la anterior con la excepción de que la primera letra es minúscula. Ejemplo: _escuelaDeCódigo_

Esta técnica es muy usada, se usa en #hasTags, en nombres de empresas como: iPod, eBay, BlackBerry, MySpace, YouTube y PayPal, y para nombrar variables en muchos lenguajes de programación.
Ejemplo:Java, JavaScript, C, PHP, Dart, Python etc.  

**Java**
```Java
int soyUnaVariable;
public class SoyUnaClase{}
public soyUnMetodo(){}
```  

**Pyhon**
```Python
soyUnaVariable = 0
def soyUnMetodo():
class SoyUnaClase:
```

## snake_case 🐍
Snake case es la técnica que compone las palabras separadas por barra baja (underscore) en vez de espacios y con la primera letra de cada palabra en minúscula. Por ejemplo _escuela_de_codigo_

Este  tipo  de  convención  se  utiliza  en  nombres  de  variables  y  funciones  de  lenguajes,particularmente asociado con C. Aunque también lenguajes como Ruby y Python lo han adoptado. Igual que el CamelCase existen variedades, por ejemplo todas las letras en  mayusculas  de  denomina  **SCREAMING_SNAKE_CASE**  utilizado  para definir constantes.  

**Java**
```Java
// SCREAMING_SNAKE_CASE
int SOY_UNA_CONSTANTE;
```  

**Pyhon**
```Python
# nombre de archivos
from mi_archivo import mi_metodo
soy_una_variable = 0
def soy_un_metodo():

```


## kebab-case 🍢
Kebab case, o kebab-case, es una convención de nomenclatura de variables de programación en la que un desarrollador reemplaza los espacios entre palabras con un guión.

El término proviene de la técnica asociada a una brocheta. La brocheta perfora varios trozos de distintos alimentos. En el código, el guión representa la brocheta y mantiene varias palabras juntas para describir el significado de un recurso.

Aquí hay tres ejemplos de la convención de nomenclatura de casos de kebab:
* nombre-variable-descriptivo
* ARCHIVO-DE-TEXTO-INTERESANTE (SCREAM-KEBAB)
* nomenclatura-convenciones-página-web

        NOTA:Muy utilizado en lenguajes funcionales y scripts de terminal.

```json
{
  "name": "proyectoreactjs",
  "version": "0.1.0",
  "private": true,
  "homepage": "/",
  "dependencies": {
    "bootstrap": "^4.4.1",
    "jquery": "^3.4.1",
    "popper.js": "^1.16.0",
    "react": "^16.12.0",
    "react-dom": "^16.12.0",// Formato 'Kebab Case' 
    "react-router": "^5.1.2", // Formato 'Kebab Case' 
    "react-router-dom": "^5.1.2", // Formato 'Kebab Case' 
    "react-scripts": "3.1.1"
  }, 
...
...
...
// URL con Formato 'Kebab Case' 
https://infoedcmvc.my.canva.site/alfonso6z-modulos-pc-tipos-de-datos
 

```
### Problemas con el caso de kebab
El mayor problema con el caso de kebab radica principalmente en el uso de un guión. Muchos lenguajes de programación interpretarán el guión como un __signo menos__ y, sin querer, crean errores de software que son difíciles de aislar y solucionar.


# Train-Case 🚂
Es una variedad del kebab-case o snake_case, pero cada palabra con la primera letra en mayúsculas. Ejemplo: _Escuela-De-Código_ y _Escuela_De_Código_


# l33t
[Leet](https://en.wikipedia.org/wiki/Leet) (o “1337”), también conocido como eleet o leetspeak, es una nomenclatura usada por algunas comunidades y usuarios de diferentes medios de internet.  

Utiliza algunos caracteres para reemplazar a otros en formas que juegan en la similitud a través de la reflexión u otra semejanza. Por ejemplo, las ortografías de leet de la palabra leet incluyen 1337 y l33t. Ejemplo: _3$cu314D3C0D160_

---
Al colectivo de hackers [Cult of the Dead Cow](https://en.wikipedia.org/wiki/Cult_of_the_Dead_Cow) se le atribuye la acuñación original del término, en sus archivos de texto de esa época. Una teoría es que se desarrolló para anular los filtros de texto creados por [BBS](https://es.wikipedia.org/wiki/Bulletin_Board_System) o los operadores del sistema Internet Relay Chat para foros de mensajes para desalentar la discusión de temas prohibidos, como cracking y hackeo .Los errores ortográficos creativos y las palabras derivadas del arte ASCII también eran una forma de intentar indicar que uno estaba bien informado sobre la cultura de los usuarios de computadoras.

Algunos consideran que los emoticons y el arte ASCII , como las caras sonrientes, son __leet__, mientras que otros sostienen que leet consiste únicamente en el cifrado de palabras simbólicas. Las variantes de leet se han utilizado con fines de censura durante muchos años; por ejemplo, _"@ $$"_ y _"$ #! +"_ se ven con frecuencia para hacer que una palabra parezca censurada para el ojo inexperto pero obvia para una persona familiarizada con _leet_.

[600613](https://www.google.es/?hl=xx-hacker&gws_rd=cr&ei=dGw4We-MGZC1UobrnIgH) tiene una versión de su buscador en honor a esta nomenclatura.

---


## Notación Húngara
La notación húngara es un sistema que intenta hacer que nombrar cosas sea un poco más fácil. Es posible que te encuentres con la notación húngara al explorar un código base existente (Lenguajes no tipados ).  

La notación húngara es una convención sobre la denominación de identificadores. Se aplica principalmente a la denominación de variables, pero también puede cubrir la denominación de funciones. La notación es un intento de formalizar cómo el nombre de una variable puede indicar su tipo o propósito.

Usando la notación húngara, todos los nombres de variables comienzan con un grupo de letras con un significado acordado. Estas letras suelen ser una abreviatura del tipo de variable. Por ejemplo, la letra __l__ podría representar un número entero __long__. La abreviatura __str__  representa una cadena.

### ¿Es realmente húngaro?
¡Sí, la notación húngara fue, de hecho, inventada por un húngaro! Charles Simonyi era un empleado de Microsoft cuando inventó el término.

A diferencia de la mayoría de los otros idiomas occidentales, los nombres húngaros ordenan primero el apellido, seguido del nombre de pila. El término notación húngara puede hacer referencia a este hecho, o puede ser simplemente una feliz coincidencia. Podría haber sido más natural para Simonyi debido a su idioma nativo.

Ejemplo: 
En un lenguaje de tipado debil, como JavaScript, Python o PHP, las variables pueden adoptar diferentes tipos según el valor que tengan. En lugar de nombrar una variable simplemente _edad_, la notación húngara incluye un prefijo que representa el tipo de esa variable.

```JavaScript
iEdad = 13;
strNombre = "Alfonso";
bInscrito = true;
```
### Algunos Prefijos de la nótación húngara
|Prefijo|Escribe|Ejemplo|
|:-:|:-:|:-:|
|b|boolean|bAcceso| 
|c|char|cInicial| 
|str|string|strNombre| 
|i|int|iRueda| 
|f|float|fPromedio|
|C|class|CPersona|
|{class Persona}|objeto|personaLider|

[1]:#camelcase-🐫
[2]:#snakecase-🐍
[3]:#kebab-case-🍢
[4]:#train-case-🚂
[5]:#l33t
[6]:#notación-húngara