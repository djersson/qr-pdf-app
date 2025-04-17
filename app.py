import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR para PDF OneDrive", layout="centered")
st.title("📄🔗 Generador de QR para PDFs en la nube")

st.markdown("""
Pega el **enlace compartido** de un archivo PDF almacenado en OneDrive, Dropbox, Google Drive u otra plataforma en la nube.  
El código QR funcionará desde cualquier celular, siempre que el enlace esté habilitado para acceso público.
""")

# Entrada
link = st.text_input("🔗 Enlace compartido al archivo PDF")

if link:
    if not link.startswith("http"):
        st.error("❌ El enlace no es válido. Asegúrate de que comience con 'http'")
    else:
        try:
            # Crear QR
            qr = qrcode.QRCode(box_size=8, border=2)
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            # Mostrar QR
            st.image(img, caption="📱 Escanea este código QR para abrir el PDF")

            # Botón para abrir el link
            st.markdown(f"[📂 Abrir el PDF]({link})", unsafe_allow_html=True)

            # Botón para descargar el QR
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            st.download_button(
                label="⬇️ Descargar QR como imagen",
                data=buffer,
                file_name="QR_PDF.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"❌ Error al generar el código QR: {e}")