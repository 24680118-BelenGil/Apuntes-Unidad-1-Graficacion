# Unidad 1. Introducción a la graficación por computadora
La graficación es la rama de la informática que se encarga de la creación, manipualción y representación de imágenes mediante el uso de sistemas computacionales. Esta combina conocimientos de matemáticas, programación, física y diseño para generar imágenes digitales que pueden visualizarse en pantallas, imprimirse o utilizarse en entornos interactivos.
## 1.1. Historia y evolución de la graficación por computadora
### 📌 Primeros avances (años 1950–1960)
* En el Massachusetts Institute of Technology (MIT) se desarrollaron los primeros sistemas gráficos.
* En 1963, Ivan Sutherland creó Sketchpad, considerado el primer programa de diseño asistido por computadora (CAD).
*Se utilizaban pantallas de tubo de rayos catódicos (CRT).

### 📌 Décadas de 1970–1980
* Se desarrollan algoritmos para trazar líneas y polígonos.
* Aparecen las primeras tarjetas gráficas.
* Se popularizan los videojuegos como Pong.
* Nacen empresas como Silicon Graphics, especializadas en hardware gráfico.

### 📌 Década de 1990
* Surgen APIs gráficas como OpenGL y DirectX.
* Avances importantes en gráficos 3D.
* Se estrenan películas con animación digital como Toy Story de Pixar Animation Studios.

### 📌 Actualidad
* Uso de GPUs avanzadas.
* Realidad virtual y aumentada.
* Motores gráficos como Unreal Engine y Unity.
* Renderizado en tiempo real y trazado de rayos (Ray Tracing).

## 1.2. Áreas de aplicación
Es un campo multidisciplinario donde todos los especialistas comparten un mismi objetivo "mostrar un mundo a través de una ventana", algunas areas de aplicación son:
* **Industria del entretenimiento:** Creación de películas o caricaturas sintéticas, publicidad, efectos visuales y videojuegos.
* **Ingeniería Mecánica:** Diseño de prototipos virtuales de partes mecánicas para su construcción,
utilizando sistemas CAD/CAM (Computer-Aided Design/ Computer-Aided Manufacturing).
* **Arquitectura:** Uso del software CAD para la creación de planos de alguna estructura
arquitectónica, visualizaciones de espacios antes y después de una construcción planeada.
* **Diseño:** Diseño y creación de productos, haciendo uso de sistemas CAD/CAM.
* **Patrimonio cultural:** Reconstrucciones virtuales de templos, monumentos, piezas antiguas, o
bien, reconstrucciones hipotéticas de escenas.
* **Medicina:** Simulaciones virtuales de cirugías para entrenamiento y visualización de
datos dados por algún instrumento de diagnóstico.
## 1.3. Aspectos matemáticos de la graficación
La graficación por computadora se fundamenta en principios matemáticos que permiten representar objetos, transformarlos y visualizarlos en una pantalla. Estos aspectos matemáticos garantizan precisión, realismo y eficiencia en la generación de imágenes digitales.
### Sistemas de coordenadas
Para representar objetos en el espacio se utilizan sistemas de coordenadas:
* Coordenadas cartesianas (x, y) en gráficos 2D.
* Coordenadas cartesianas (x, y, z) en gráficos 3D.
Cada punto en la pantalla se define mediante valores numéricos que determinan su posición exacta.
### Geometría analítica
La geometría analítica permite describir líneas, curvas y superficies mediante ecuaciones matemáticas.
### Álgebra lineal y matrices
Las matrices se utilizan para realizar transformaciones como:
* Traslación
* Rotación
* Escalamiento
* Reflexión
### Transformaciones geométricas
Las transformaciones permiten modificar la posición, tamaño y orientación de los objetos.
* **Traslación:** Cambia la posición.
* **Escalamiento:** Cambia el tamaño.
* **Rotación:** Gira el objeto.
* **Cizallamiento:** Deforma la figura.
Estas transformaciones se realizan mediante operaciones matemáticas aplicadas a cada punto del objeto.
### Cálculo y funciones
El cálculo diferencial e integral que decriben movimientos y efectos visuales con mayor realismo, se utilizan en:
* Modelado de curvas y superficies.
* Animaciones suaves.
* Cálculo de iluminación y sombras.
* Interpolaciones.
### Geometría computacional
Se encarga del estudio de algoritmos para resolver problemas geométricos como:
* Intersección de líneas.
* Detección de colisiones.
* Relleno de polígonos.
* Recorte de figuras.
## 1.4. Modelos de color: RBG, CMY, HSV y HSL
Los modelos de color son sistemas matemáticos que permiten representar los colores mediante combinaciones numéricas. Son fundamentales en la graficación por computadora, ya que determinan cómo se generan, visualizan y manipulan los colores en distintos dispositivos.
### RBG [Red, Green, Blue]
Conocido como Additive Color Model o modelo natural, combinan las intensidades de los tres colores primarios (Rojo, Verde y Azul), para obtener un color. Su espacio de color puede ser representado por el cubo unitario [0, 1] × [0, 1] × [0, 1], asignandose el color negro al
origen (0, 0, 0), y conforme la intensidad de los colores incremente se llega al
color blanco en (0, 0, 0) al moverse a lo largo de los ejes.

<img width="455" height="332" alt="Captura de pantalla 2026-02-23 130221" src="https://github.com/user-attachments/assets/e166da72-2ea4-4144-8925-fb4dc723515e" />

Se utilizan 8-bits por componente, por lo que cada uno puede representar hasta 256 valores diferentes. 
### CMY [Cyan, Magenta, Yellow]
Es un modelo sustractivo, utilizado principalmente en impresión. Utiliza los tres colores primarios cian, magenta y amarillo.
* **Cian:** Puede describirse como una combinación de verde y azul, cuando se refleja la luz, este absorbe el componente rojo y refleja el verde y azul.
* **Magenta:** Esta resta la componente verde de la luz incidente.
* **Amarillo:** Resta la componente azul.

En el modelo CMY, la posición espacial (I, I, 1 ) representa el negro, se restan todos los componentes de la luz incidente, el (0, 0, 0) origen representa la luz blanca. Si se utilizan cantidades iguales de cada uno de los colores primarios, se obtienen las sombras de gris, situadas a lo largo de la diagonal principal del cubo.
Una combinación de cian y magenta produce luz azul, porque las componentes roja y verde de la luz incidente se absorven. De forma similar, una combinación de tinta cian y amarilla produce luz verde, mientras que una combinación de tinta magenta y amarilla nos da la luz roja. 

<img width="265" height="250" alt="image" src="https://github.com/user-attachments/assets/619e0f2e-bc38-4ff3-b1be-54645ce95646" />

### HSV [Hue, Saturation, Value]
Basado en el sistema de color de Munsell, el cual intenta acercarse más a la manera en la que percibimos los atributos de los colores. Su espacio de color es modelado con un cono o una pirámide hexagonal inversa, y como su nombre lo indica, está definido por sus componentes:
* **H (Tono):** Es un ángulo entre 0° y 360° , donde cada valor corresponde a un color “puro” (en el espectro visible) o pigmento en la circunferencia del modelo. Empezando con el color rojo en 0° y el verde en 120°.
* **S (Saturación):** Se relaciona con la pureza o intensidad del color, es decir, qué tanto vamos a diluir o rebajar el pigmento con un tono entre los colores blanco y negro, definido por el último componente. Donde 1 es el color puro y 0 es el tono en *V*, correspondiendo a el radio del cilindro.
* **V (Value):** Donde 0 es el color negro y 1 el blanco, haciendo referencia al factor de brillo, correspondiendo al eje del modelo.
  
<img width="504" height="361" alt="Captura de pantalla 2026-02-23 133317" src="https://github.com/user-attachments/assets/20db8eee-b23e-415c-af8e-ea7b784296d2" />

### HSL [Hue, Saturation, Lightness]
Basado en parámetros intuitivos de color es el sistema utilizado por Tektronix Corporation. Este espacio de color tiene la representación de doble cono sus tres parámetros se denominan: 
* **Tono (H):** Es un ángulo entre 0° y 360° , donde cada valor corresponde a un color “puro” o pigmento en la circunferencia del modelo. El magenta estará a 60°. el rojo a 120° y el cian a 180". Los colores complementarios estarán separados 180° en este doble cono. 
* **Saturación (S):** Especifica la pureza de un color. Este parámetro varía entre 0 y 1.0
y los colores puros son aquellos para los que .V = 1.0 y L = 0.5. A medida que S disminuye, se añade más blanco a un color. La escala de grises se encuentra en S = 0. 
* **Claridad (L):** El eje vertical en este modelo se denomina claridad, L. Para L = 0, tendremos el negro, mientras que el blanco se encontrará en L = 1.0. Los valores de escala de grises se encuentran a lo largo del eje L y los colores puros están en el plano L - 0.5. 

<img width="396" height="572" alt="Captura de pantalla 2026-02-23 140857" src="https://github.com/user-attachments/assets/c006ecef-c17a-4fb7-bff6-ab0afdeb6391" />

## 1.5. Representación y trazo de líneas y polígonos
En la graficación por computadora, las imágenes se construyen a partir de primitivas geométricas básicas, principalmente puntos, líneas y polígonos. Estas primitivas son la base para generar figuras más complejas en gráficos 2D y 3D.
### *Representación de líneas*
Una línea en matemáticas es una sucesión infinita de puntos, pero en gráficos por computadora se representa mediante una secuencia discreta de píxeles en una pantalla.

Su representación matemática es *y = mx + b*.

Donde *m* es la pendiente y *b* la intersección con el eje Y.

Para dibujar líneas eficientemente se emplean algoritmos específicos:

**1. Algoritmo DDA (Digital Differential Analyzer)**
* Calcula incrementos pequeños en X y Y.
* Es sencillo pero puede presentar errores acumulativos por redondeo.
  
**2. Algoritmo de Bresenham**
* Utiliza únicamente operaciones enteras.
* Es más rápido y preciso.
* Determina qué píxel encender en cada paso.
  
### *Representación de polígonos*
Un polígono es una figura plana formada por segmentos de línea que conectan varios vértices.

Su definición matemática es *P = {(X1,Y1), (X2,Y2),...,(Xn,Yn)}*

Cada par de puntos consecutivos forma un lado del polígono.

**Tipos de polígonos en gráficos**
* **Convexos:** Todos sus ángulos internos son menores a 180°.
* **Cóncavos:** Tienen al menos un ángulo interno mayor a 180°.
* **Regulares:** Todos sus lados y ángulos son iguales.
  
**Relleno de polígonos**
* **Scan-line (línea de barrido):** Rellena el polígono línea por línea.
* **Flood Fill:** Rellena desde un punto interior hasta alcanzar los bordes.

**Practicas**
Los siguientes links muestran practicas para reforzar el trazo de líneas y polígonos.

***Polígono 2D***

https://github.com/24680118-BelenGil/Practica-1-Pol-gono-.git

***Flor de vidad***

https://github.com/24680118-BelenGil/Practica-2.Graficaci-n.git

### 1.5.1 Formatos de imagen
Los formatos de imagen son estructuras digitales que permiten almacenar, organizar y codificar información gráfica dentro de un archivo. Estos formatos determinan cómo se guardan los píxeles, el tipo de compresión utilizada, la profundidad de color y la calidad final de la imagen.

***📌 1. Formatos Raster (Mapa de Bits)***
Una imagen raster está formada por una matriz de píxeles organizada en filas y columnas. Cada píxel contiene información de color.

Matemáticamente se representa como: *I(x,y) = (R, G, B)*

Estas dependen de la resolución, pierden calidad al ampliarse pero son ideales para fotografías.

*Principales formatos*

**BMP (Bitmap):** No utiliza compresión por lo que conserva toda la información original, pero sus archivos son de gran tamaño.

**JPEG (Joint Photographic Experts Group):** Reduce el tamaño eliminando infromación poco importante, es ideal para forografías digitales.

**PNG (Portable Network Graphics):** A diferencia de JPEG, usa compresion pero no elimina información de la imagen, permite transparencias y es excelente para gráficos, logotipos e imágenes web.

**GIF (Graphics Interchange Format):** Soporta animaciones pero se limita a 256 colores, es ideal para íconos y animaciones.

**TIFF (Tagged Image File Format):** Usa compresión sin perdida y de alta calidad.

***📌 2. Formatos Vectoriales***

Compuestas por ecuaciones matemáticas que describen líneas, curvas y polígonos, no pierden calidad al escalarse, su tamaño es menor y son ideales para logotipos, planos y diseño técnico.

*Formato principal*

***SVG (Scalable Vector Graphics):*** Esta basado en XML, es ecalable sin pérdida de calidad y compatible con navegadores web.
## 1.6. Procesamiento de mapas de bits.
manipulación matemática de una imagen digital formada por píxeles, con el objetivo de mejorarla, analizarla o transformarla.

Una imagen digital raster puede representarse como una función: 
*I(x,y)*

Donde:
* **x** = coordenada horizontal
* **y** = coordenada vertical
* **I** = intensidad o valor de color del píxel

***📌 1. Tipos de procesamiento***
* **Procesamiento puntual:** Se modifica cada píxel de forma independiente.
* **Procesamiento espacial:** El nuevo valor del píxel depende de los píxeles vecinos.
* **Transformaciones geométricas:** Las transformaciones geométricas modifican la posición, orientación o tamaño de una imagen sin alterar directamente los valores de color de los píxeles.
* **Segmentación de imágenes:** Dividir una imagen en regiones o áreas con características similares, como color, textura o intensidad.
* **Detección de bordes:** Identifica cambios bruscos de intensidad en una imagen. Los bordes representan los límites de los objetos.
## Bibliografía
* (N.d.). Wordpress.com. Retrieved February 23, 2026, from https://ingenieriayeducacion.wordpress.com/wp-content/uploads/2013/12/graficosporcomputadorayopengl.pdf
* La graficación, ___________________________________________________________________ Lección 1. 1-Breve Historia Dde. (n.d.). UNIDAD I.- INTRODUCCIÓN A LA GRAFICACIÓN POR COMPUTADORA. Wordpress.com. Retrieved February 23, 2026, from https://iscitver2011.wordpress.com/wp-content/uploads/2011/02/1-1breve-historia-de-la-graficacion.pdf
* (N.d.). Wdfiles.com. Retrieved February 23, 2026, from https://aliamondano-eo.wdfiles.com/local--files/libro-graficos-1-0/graficos-1.0.pdf
* (N.d.-b). Proyectodescartes.org. Retrieved February 23, 2026, from https://proyectodescartes.org/iCartesiLibri/PDF/GraficacionComputadora.pdf
# Unidad 2. Graficación 2D
La graficación en dos dimensiones constituye una base fundamental en el campo de la computación gráfica, ya que permite representar objetos en un plano cartesiano mediante el uso de coordenadas (x, y). A través de algoritmos matemáticos y estructuras de datos, es posible manipular, transformar y visualizar figuras geométricas en pantallas digitales.

Este campo es ampliamente utilizado en áreas como:
* Diseño gráfico
* Desarrollo de videojuegos
* Interfaces gráficas (GUI)
* Animación digital
* Sistemas CAD
## 2.1. Transformación bidimensional.
Operaciones matemáticas que permiten modificar la geometría de un objeto. Estas transformaciones no alteran la estructura interna del objeto (salvo en el caso del escalamiento no uniforme o el sesgado), sino que cambian su posición o apariencia en el plano.

Un objeto en gráficos 2D se representa como un conjunto de puntos o vértices, por lo tanto, cualquier transformación se aplica a cada punto de forma individual.
### 2.1.1. Traslación.
La traslación es una transformación que consiste en desplazar un objeto de una posición a otra dentro del plano sin modificar su forma, tamaño ni orientación. Es una de las transformaciones más simples y más utilizadas, ya que representa el movimiento básico de los objetos.

Desde el punto de vista matemático, la traslación se realiza sumando un vector de desplazamiento a las coordenadas originales de cada punto. Esto significa que todos los puntos del objeto se mueven la misma distancia y en la misma dirección.

Es una transformación rígida, lo que significa que:
* No cambia la forma
* No cambia el tamaño
* No altera los ángulos

📌 Forma vectorial:

𝑃′= 𝑃 + 𝑇

Donde:

P = (x, y) y T = (Tx, Ty)

📌 Propiedades:
* Conserva paralelismo
* Conserva distancias
* Es reversible
### 2.1.2. Escalamiento.
Transformación que modifica el tamaño de un objeto, este puede alterar las proporciones de la figura dependiendo de los factores utilizados.
📌 Tipos:

🔹 Escalamiento uniforme

Mantiene proporciones

Sx = Sy

🔹 Escalamiento no uniforme

* Deforma la figura
* Puede estirar o comprimir

📌 Consideraciones importantes:

Si Sx o Sy < 1 → reducción

Si Sx o Sy > 1 → ampliación

Si es negativo → refleja el objeto

Una consideración importante es que el escalamiento normalmente se realiza respecto al origen del sistema de coordenadas. Sin embargo, si se desea escalar respecto a otro punto, es necesario trasladar el objeto al origen, aplicar el escalamiento y posteriormente regresarlo a su posición original.
### 2.1.3. Rotación.
Transformación que permite girar un objeto alrededor de un punto específico, generalmente el origen del sistema de coordenadas. Esta transformación cambia la orientación del objeto, pero no su forma ni su tamaño.

x′=xcosθ−ysinθ

y′=xsinθ+ycosθ​

La rotación depende de un ángulo, que puede medirse en grados o radianes. Un aspecto importante es el sentido de la rotación: si es en sentido antihorario, se considera positiva, mientras que si es en sentido horario, se considera negativa.

Al igual que la traslación, la rotación es una transformación rígida, ya que conserva distancias y ángulos. Sin embargo, su implementación puede ser más compleja, especialmente cuando se rota respecto a un punto distinto del origen, lo cual requiere realizar transformaciones adicionales.
### 2.1.4. Sesgado.
Transformación que inclina un objeto en una dirección determinada, provocando una deformación en su forma ya que no conserva los ángulos, por lo que altera la geometría del objeto.
## 2.2.Representación matricial de las transformaciones bidimensionales.
En la computación gráfica, las transformaciones se representan comúnmente mediante matrices, ya que esto permite realizar cálculos de forma más eficiente y sistemática.

Para utilizar matrices, se emplea el concepto de coordenadas homogéneas, que consiste en añadir una tercera componente a cada punto. Esto permite representar todas las transformaciones, incluyendo la traslación, como multiplicaciones matriciales.

Una de las principales ventajas de la representación matricial es la posibilidad de combinar múltiples transformaciones en una sola operación. Esto se logra mediante la multiplicación de matrices, lo que facilita la implementación en programas y motores gráficos.

Es importante considerar que el orden en el que se multiplican las matrices afecta el resultado final. Por ejemplo, no es lo mismo rotar un objeto y luego trasladarlo, que trasladarlo primero y después rotarlo.

## 2.3. Trazo de líneas curvas.
Las curvas son fundamentales en la graficación 2D, ya que permiten representar formas suaves y naturales que no pueden lograrse únicamente con líneas rectas.
### 2.3.1. Bézier.
Ampliamente utilizadas en gráficos por computadora debido a su simplicidad y flexibilidad. Estas curvas se definen mediante un conjunto de puntos llamados puntos de control.

📌 Tipos:

* Lineal (2 puntos)
* Cuadrática (3 puntos)
* Cúbica (4 puntos, más común)

Una característica importante es que la curva no necesariamente pasa por todos los puntos de control, sino que se aproxima a ellos, lo que permite un mayor control sobre la forma.

Las curvas de Bézier pueden ser lineales, cuadráticas o cúbicas, dependiendo del número de puntos de control. Las cúbicas son las más utilizadas en aplicaciones prácticas, ya que ofrecen un buen equilibrio entre control y complejidad.
### 2.3.2. B-spline.
Las curvas B-Spline son una generalización de las curvas de Bézier y ofrecen mayor flexibilidad y control. Una de sus principales ventajas es el control local, lo que significa que modificar un punto de control solo afecta una parte de la curva, en lugar de toda la forma.

## 2.4. Fractales
Los fractales son estructuras geométricas que presentan autosimilitud, es decir, que sus partes son similares al todo, independientemente de la escala. Estos objetos se generan mediante procesos matemáticos iterativos o recursivos, lo que les permite tener una complejidad prácticamente infinita.
## 2.5. Uso y creación de fuentes de texto.
Elementos fundamentales en la representación de texto en sistemas gráficos. Estas fuentes pueden ser de tipo bitmap o vectorial.

Las fuentes bitmap están formadas por píxeles y pueden perder calidad al escalarse, mientras que las fuentes vectoriales se basan en curvas matemáticas, lo que permite escalarlas sin pérdida de calidad.

En la creación de fuentes, se utilizan curvas de Bézier para definir la forma de cada carácter. Además, se consideran aspectos como el espaciado entre letras (kerning) y las métricas de los caracteres.
## Bibliografía
* (N.d.). Wordpress.com. Retrieved February 23, 2026, from https://ingenieriayeducacion.wordpress.com/wp-content/uploads/2013/12/graficosporcomputadorayopengl.pdf
* (N.d.). Wdfiles.com. Retrieved February 23, 2026, from https://aliamondano-eo.wdfiles.com/local--files/libro-graficos-1-0/graficos-1.0.pdf
* (N.d.-b). Proyectodescartes.org. Retrieved February 23, 2026, from https://proyectodescartes.org/iCartesiLibri/PDF/GraficacionComputadora.pdf

