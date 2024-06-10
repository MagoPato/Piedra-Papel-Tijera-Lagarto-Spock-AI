<h1>Piedra, Papel, Tijera, Lagarto, Spock con Inteligencia Artificial</h1>

  <h2>Requisitos</h2>
    <p>Para ejecutar este proyecto, necesitas tener instalados los siguientes paquetes de Python:</p>
   <ul>
        <li><code>numpy</code></li>
        <li><code>tensorflow</code></li>
        <li><code>tkinter</code></li>
  </ul>
    <p>Puedes instalarlos usando <code>pip</code>:</p>
    <pre><code>pip install numpy tensorflow</code></pre>

  <h2>Descripción del Proyecto</h2>

  <h3>Lógica del Juego</h3>
    <p>El juego incluye cinco opciones: piedra, papel, tijera, lagarto y spock. Cada opción puede ganar contra dos otras opciones y perder contra otras dos, siguiendo estas reglas:</p>
   <ul>
        <li><strong>Piedra</strong> aplasta tijera y lagarto.</li>
        <li><strong>Papel</strong> cubre piedra y desaprueba a Spock.</li>
        <li><strong>Tijera</strong> corta papel y decapita lagarto.</li>
        <li><strong>Lagarto</strong> come papel y envenena a Spock.</li>
        <li><strong>Spock</strong> aplasta piedra y rompe tijera.</li>
    </ul>

  <h3>Inteligencia Artificial</h3>

  <h4>Creación del Modelo</h4>
   <p>El modelo LSTM se crea utilizando TensorFlow y se compone de dos capas LSTM y una capa densa final con una activación softmax para predecir las probabilidades de cada una de las cinco opciones.</p>

   <h4>Entrenamiento del Modelo</h4>
   <p>El modelo se entrena usando el historial de jugadas. Cada jugada se convierte en un vector de longitud 5. Utilizamos secuencias de cinco jugadas anteriores para predecir la próxima jugada. Este enfoque secuencial permite que el modelo capture patrones en las decisiones del jugador.</p>

   <h3>Interfaz Gráfica de Usuario (GUI)</h3>

  <p>La GUI permite al usuario seleccionar una de las cinco opciones y muestra el resultado del juego después de cada jugada. Los botones de las opciones están deshabilitados temporalmente mientras se actualiza el juego y se entrena el modelo. La interfaz está diseñada para ser intuitiva y fácil de usar, proporcionando una experiencia de juego agradable.</p>

  <h3>Flujo del Juego</h3>

   <ol>
        <li><strong>Inicio del Juego:</strong> El usuario selecciona una opción entre piedra, papel, tijera, lagarto y spock.</li>
        <li><strong>Actualización de la Jugada:</strong> La elección del usuario se convierte en un vector, y la IA predice su jugada utilizando el modelo LSTM.</li>
        <li><strong>Determinación del Ganador:</strong> Se determina el ganador basándose en las reglas del juego.</li>
        <li><strong>Entrenamiento del Modelo:</strong> La jugada del usuario y la predicción de la IA se agregan al historial, y el modelo se entrena de nuevo con este historial.</li>
        <li><strong>Visualización del Resultado:</strong> Se muestra el resultado del juego en la GUI.</li>
    </ol>

  <h2>Ejecución</h2>

  <p>Para ejecutar el juego, simplemente corre el script en tu entorno Python. Aparecerá una ventana con botones para cada opción del juego. Selecciona tu jugada y la IA responderá con su propia elección. El resultado del juego se mostrará en la etiqueta de la ventana.</p>

   <p>¡Disfruta jugando y viendo cómo la IA mejora con cada jugada!</p>

   <h2>Cómo Contribuir</h2>

  <p>Si deseas contribuir a este proyecto, puedes hacerlo de las siguientes maneras:</p>
   <ol>
        <li><strong>Reportar Errores:</strong> Abre un issue en GitHub para reportar cualquier error que encuentres.</li>
        <li><strong>Solicitar Funciones:</strong> Si tienes ideas para nuevas funciones, siéntete libre de abrir un issue con tus sugerencias.</li>
        <li><strong>Hacer Pull Requests:</strong> Si has realizado mejoras o correcciones, puedes enviar un pull request para que se revisen e integren en el proyecto.</li>
    </ol>

  <h2>Licencia</h2>

   <p>Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, siempre y cuando se mencione la autoría original.</p>
