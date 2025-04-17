import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="QR para PDF OneDrive", layout="centered")
st.title("📄🔗 Generador de QR para PDFs en la nube")

st.markdown("""
Pega el **enlace compartido** de un archivo PDF almacenado en OneDrive, Dropbox, Google Drive u otra plataforma en la nube.  
El código QR funcionará desde cualquier celular, siempre que el enlace esté habilitado para acceso público.
Desarrollado por: Laboratorio Metalútgico / JDR - 2025
""")

# Entrada
enlace = st.text_input("🔗 Enlace compartido al archivo PDF")

if enlace:
    if not enlace.startswith("http"):
        st.error("❌ El enlace no es válido. Asegúrate de que comience con 'http'")
    else:
        try:
            # Crear el código QR
            qr = qrcode.QRCode(box_size=8, border=2)
            qr.add_data(enlace)
            qr.make(fit=True)
            imagen_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

            # Mostrar imagen del QR
            st.image(imagen_qr, caption="📱 Escanea este código QR para abrir el PDF")

            # Mostrar enlace para abrir el PDF directamente
            st.markdown(f"[📂 Abrir el PDF]({enlace})", unsafe_allow_html=True)

            # Convertir la imagen a bytes para permitir la descarga
            buffer = BytesIO()
            imagen_qr.save(buffer, format="PNG")
            buffer.seek(0)

            # Botón para descargar
            st.download_button(
                label="⬇️ Descargar QR como imagen",
                data=buffer,
                file_name="QR_PDF.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"❌ Error al generar el código QR: {e}")

