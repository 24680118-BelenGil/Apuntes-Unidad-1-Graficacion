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
### HSV [Hue, Saturation, Value]
Basado en el sistema de color de Munsell, el cual intenta acercarse más a la manera en la que percibimos los atributos de los colores. Su espacio de color es modelado con un cono o una pirámide hexagonal inversa, y como su nombre lo indica, está definido por sus componentes:
* **H (Tono):** Es un ángulo entre 0° y 360° , donde cada valor corresponde a un color “puro” (en el espectro visible) o pigmento en la circunferencia delmodelo. Empezando con el color rojo en 0° y el verde en 120°.
* **S (Saturación):** Se relaciona con la pureza o intensidad del color, es decir, qué tanto vamos a diluir o rebajar el pigmento con un tono entre los colores blanco y negro, definido por el último componente. Donde 1 es el color puro y 0 es el tono en *V*, correspondiendo a el radio del cilindro.
* **V (Value):** Donde 0 es el color negro y 1 el blanco, haciendo referencia al factor de brillo, correspondiendo al eje del modelo.
<img width="504" height="361" alt="Captura de pantalla 2026-02-23 133317" src="https://github.com/user-attachments/assets/20db8eee-b23e-415c-af8e-ea7b784296d2" />

### HSL [Hue, Saturation, Lightness]
## 1.5. Representación y trazo de líneas y polígonos
### 1.5.1 Formatos de imagen
## 1.6. Procesamiento de mapas de bits.
# Bibliografía
