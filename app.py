import streamlit as st

st.set_page_config(page_title="Feliz Cumpleaños Kely", layout="wide")

# Rutas remotas de archivos (debes subir estos a GitHub y usar los links RAW)
video_url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/static/videos/fondo.mp4"
imagen_url = "https://github.com/isaitj24/streamlit_kely/blob/main/kely.jpg"

html = f"""
<style>
body {{
  margin: 0;
  overflow: hidden;
  font-family: 'Segoe UI', sans-serif;
}}

video {{
  position: fixed;
  top: 0; left: 0;
  min-width: 100%;
  min-height: 100%;
  z-index: -1;
  object-fit: cover;
}}

.center {{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(0,0,0,0.5);
  color: white;
  padding: 40px;
  border-radius: 20px;
  text-align: center;
  z-index: 5;
}}

img {{
  margin-top: 20px;
  max-width: 320px;
  border-radius: 20px;
  border: 5px solid #ffb3e6;
  box-shadow: 0 0 25px #ff80bf;
  animation: float 3s ease-in-out infinite;
}}

@keyframes float {{
  0%, 100% {{ transform: translateY(0); }}
  50% {{ transform: translateY(-10px); }}
}}

.item {{
  position: absolute;
  width: 90px;
  height: 90px;
  font-size: 2.8em;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  animation: fall linear infinite;
  transition: transform 0.3s;
}}

.item:hover {{
  transform: scale(1.3);
}}

.fixed {{
  animation-play-state: paused !important;
  z-index: 1000;
  background: rgba(255,255,255,0.9);
  border-radius: 15px;
  padding: 10px;
  font-size: 1em;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
}}

@keyframes fall {{
  0% {{ transform: translateY(-500px) rotate(0deg); opacity: 1; }}
  100% {{ transform: translateY(120vh) rotate(360deg); opacity: 0.5; }}
}}

.mensaje-final {{
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.2em;
  width: 80%;
  max-width: 700px;
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 0 15px rgba(0,0,0,0.1);
  color: #4a148c;
  font-weight: 500;
  animation: fadeIn 3s ease-in-out;
}}

@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(-20px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
</style>

<video autoplay loop muted>
  <source src="{video_url}" type="video/mp4">
</video>

<div class="center">
  <h1>🌷 ¡Feliz 21° Cumpleaños, Kely! 🌷</h1>
  <img src="{imagen_url}" alt="Foto de Kely">
</div>

<div class="mensaje-final">
  Hoy celebro el día en que el mundo recibió a la persona más increíble que he conocido.  
  Gracias por llenar mi vida de luz, ternura, ocurrencias y alegría.  
  Que este nuevo año traiga bendiciones, aventuras, sueños cumplidos y millones de sonrisas.  
  ¡Te amo con todo mi corazón, Kely! 💖🎂
</div>

<script>
const iconos = ["💌", "🎈", "🌷", "✨", "💝", "🎀", "🌟", "🎊", "🎶", "💫"];
const mensajes = [
  "Tu sonrisa es mi paz diaria 😄",
  "¿Recuerdas nuestro primer abrazo? Fue mágico ✨",
  "Cada día contigo es mi regalo favorito 🎁",
  "¿Si hoy pudieras pedir un deseo… cuál sería? 💭",
  "Mi corazón late con tu nombre 💘",
  "Eres arte con forma de persona 🎨",
  "¿Qué viaje soñado te gustaría hacer conmigo? 🧳",
  "No hay nadie como tú, Kely 💐",
  "Hoy, mañana y siempre: tú 💍",
  "Gracias por hacerme mejor 💞",
  "¿Qué canción te recuerda a nosotros? 🎵",
  "Eres mi lugar favorito para quedarme 🌙",
  "¿Te imaginas lo que estaremos celebrando dentro de 10 años? 🥂",
  "Tu risa vale más que mil estrellas 🌠",
  "¡Contigo todo tiene sentido! 💫",
];

function crearItem() {{
  const el = document.createElement('div');
  el.className = 'item';
  el.innerText = iconos[Math.floor(Math.random() * iconos.length)];
  const lado = Math.random() < 0.5 ? 'left' : 'right';
  el.style[lado] = (Math.random() * 13 + 12) + 'vw';
  el.style.animationDuration = (Math.random() * 4 + 7) + 's';

  el.addEventListener('click', () => {{
    if (!el.classList.contains('fixed')) {{
      el.classList.add('fixed');
      el.innerText = mensajes[Math.floor(Math.random() * mensajes.length)];
    }}
  }});

  document.body.appendChild(el);
}}

setInterval(() => {{
  if (document.querySelectorAll('.item').length < 40) {{
    crearItem();
  }}
}}, 400);
</script>
"""

st.components.v1.html(html, height=800)
