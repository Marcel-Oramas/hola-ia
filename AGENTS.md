
# Especificación: PolyglotTalk - Tu Tutor de Idiomas Inteligente

## 1. Problema y usuario
- **Problema**: Muchas personas que estudian un nuevo idioma (Inglés, Alemán, Japonés) no tienen con quién practicar conversaciones del día a día de manera fluida y sin sentir la presión o vergüenza de equivocarse. Además, las aplicaciones tradicionales son muy rígidas y no dan feedback adaptado al contexto de la charla.
- **Usuario**: Estudiantes de idiomas de nivel básico a intermedio que quieren ganar confianza y soltura.
- **Solución IA**: El LLM actúa como un compañero de conversación empático que adapta su lenguaje y analiza las respuestas del usuario para indicarle de manera constructiva cómo mejorar su gramática y vocabulario.

## 2. Qué hace la app
PolyglotTalk es una aplicación web interactiva que permite al usuario simular conversaciones cotidianas en inglés, alemán o japonés con un tutor de Inteligencia Artificial. Tras cada respuesta del usuario, la IA continúa la conversación de manera natural y, en paralelo, proporciona un pequeño recuadro con feedback inmediato que resalta errores gramaticales o sugiere formas más naturales de expresarse.

## 3. Entradas y salidas
- **Entrada del usuario**:
  - Selección del idioma (Inglés, Alemán, Japonés).
  - Selección del rol/escenario (ej. "Pedir café en una cafetería").
  - Entrada de texto con su respuesta en el chat. Ej: *"I want order a coffee black please"*
- **Salida de la app**:
  - Respuesta interactiva del tutor en el idioma seleccionado: *"Sure! I can help you with that. Would you like any milk or sugar with your black coffee?"*
  - Bloque de feedback pedagógico: *"Feedback: 'I want order' es incorrecto. Lo correcto sería decir 'I want to order' o de forma más natural 'I would like to order'. ¡Buen intento!"*

## 4. Qué pieza de IA usa
- Usaremos la API de Gemini (por ejemplo, `gemini-2.5-flash-lite` o `gemini-2.5-flash`) mediante el SDK oficial de Google.
- **Justificación**: Gemini posee capacidades multilingües sobresalientes, especialmente en inglés, alemán y japonés, y es extremadamente rápido y económico para aplicaciones de chat interactivo con análisis de texto simultáneo.

## 5. Restricciones
- Coste de desarrollo e infraestructura cero (utilizando el plan gratuito o créditos iniciales de Google AI Studio).
- Ninguna API Key expuesta directamente en el código del frontend.
- Interfaz sencilla e intuitiva utilizando Streamlit en la Ruta A.

## 6. Criterios de aceptación
1. El usuario puede seleccionar entre Inglés, Alemán y Japonés al iniciar la sesión.
2. El tutor de IA responde contextualmente al escenario propuesto sin salirse del personaje.
3. Cada respuesta del usuario recibe una corrección explícita de errores ortográficos, gramaticales o de naturalidad en una sección visualmente diferenciada del chat.
4. La interfaz limpia el cuadro de texto tras enviar cada mensaje y mantiene el historial de la conversación activo.

