
import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="PolyglotTalk - Tutor de Idiomas", page_icon="🗣️", layout="centered")

# Título y descripción
st.title("🗣️ PolyglotTalk")
st.subheader("Tu Tutor de Idiomas Inteligente")
st.write("Practica conversaciones de la vida real en inglés, alemán o japonés con feedback constructivo al instante.")

# Sidebar para selección de idioma y escenario
st.sidebar.header("Configuración del Tutor")
idioma = st.sidebar.selectbox("Selecciona el idioma:", ["Inglés 🇬🇧", "Alemán 🇩🇪", "Japonés 🇯🇵"])
escenario = st.sidebar.selectbox("Selecciona un escenario:", [
    "Pedir café en una cafetería",
    "Hacer el check-in en un hotel",
    "Preguntar por direcciones en la calle"
])

# Inicializar historial de chat en el estado de Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensaje de bienvenida del Tutor simulando la IA (Versión 0)
    bienvenidas = {
        "Inglés 🇬🇧": "Hello! I will be your tutor today. Let's practice ordering coffee. What would you like to have?",
        "Alemán 🇩🇪": "Hallo! Ich bin dein Lehrer heute. Lass uns üben, Kaffee zu bestellen. Was möchtest du trinken?",
        "Japonés 🇯🇵": "こんにちは！今日の講師です。カフェでの注文を練習しましょう。何になさいますか？"
    }
    st.session_state.messages.append({"role": "assistant", "content": bienvenidas[idioma], "feedback": None})

# Reiniciar chat si cambia el idioma o escenario
if st.sidebar.button("Reiniciar Conversación"):
    st.session_state.messages = []
    st.rerun()

# Mostrar historial de chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        # Si el mensaje del usuario tiene feedback simulado, mostrarlo en una caja amigable
        if msg.get("feedback"):
            st.info(f"💡 **Feedback Pedagógico:** {msg['feedback']}")

# Entrada de chat para el usuario
if user_input := st.chat_input("Escribe tu respuesta aquí..."):
    # Mostrar el mensaje del usuario
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generar Feedback Simulado y Respuesta de la IA para Versión 0
    feedback_simulado = ""
    next_response = ""
    
    if "inglés" in idioma.lower():
        feedback_simulado = "Tu frase es comprensible. Intenta usar 'I would like to order...' en lugar de estructuras directas para sonar más natural y cortés."
        next_response = "Great choice! Would you like that with sugar or milk?"
    elif "alemán" in idioma.lower():
        feedback_simulado = "¡Buen intento! Recuerda capitalizar los sustantivos como 'Kaffee'. Podrías decir: 'Ich möchte einen Kaffee bestellen'."
        next_response = "Sehr gut! Möchten Sie Milch oder Zucker dazu?"
    else:
        feedback_simulado = "Gramática excelente. En situaciones cotidianas, usar la forma cortés '〜をお願いします' (o-negai shimasu) es perfecto."
        next_response = "かしこまりました。お飲み物はホットですか、アイスですか？"

    # Añadir entrada de usuario al historial
    st.session_state.messages.append({"role": "user", "content": user_input, "feedback": feedback_simulado})
    
    # Añadir respuesta de IA al historial
    st.session_state.messages.append({"role": "assistant", "content": next_response, "feedback": None})
    
    # Recargar la app para actualizar la interfaz
    st.rerun()
