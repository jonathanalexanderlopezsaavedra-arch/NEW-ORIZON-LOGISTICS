
from flask import Flask, render_template_string, request, redirect, url_for, flash
from email.message import EmailMessage
from pathlib import Path
import smtplib
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# RUTAS DEL PROYECTO
BASE_DIR = Path(__file__).resolve().parent
CARPETA_IMAGES = BASE_DIR / "static" / "images"
CARPETA_IMAGES.mkdir(parents=True, exist_ok=True)


@app.route("/")
def inicio():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NEW ORIZON LOGISTICS S.A.C.</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html {
                scroll-behavior: smooth;
            }

            body {
                font-family: Arial, sans-serif;
                background: #FFFFFF;
                color: #024D64;
            }

            header {
                background: #000000;
                padding: 15px 7%;
                display: flex;
                align-items: center;
                justify-content: space-between;
                flex-wrap: wrap;
                gap: 20px;
            }

            .logo-imagen {
                max-width: 210px;
                max-height: 85px;
                width: auto;
                height: auto;
                display: block;
                object-fit: contain;
            }

            nav {
                display: flex;
                gap: 22px;
                flex-wrap: wrap;
            }

            nav a {
                color: #FFFFFF;
                text-decoration: none;
                font-size: 14px;
                font-weight: bold;
            }

            nav a:hover {
                color: #87A4BA;
            }

            .imagen-portada {
                display: block;
                width: 100%;
                height: auto;
            }

            .portada {
                background: #EAF4F8;
                padding: 65px 8%;
                text-align: center;
            }

            .portada h1 {
                font-size: 42px;
                margin-bottom: 20px;
            }

            .portada p {
                font-size: 19px;
                line-height: 1.6;
                max-width: 700px;
                margin: auto;
            }

            .boton {
                display: inline-block;
                margin-top: 25px;
                background: #A61731;
                color: #FFFFFF;
                padding: 14px 25px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }

            .boton:hover {
                background: #C52B45;
            }

            section {
                padding: 70px 8%;
                text-align: center;
            }

            section h2 {
                font-size: 32px;
                margin-bottom: 20px;
                color: #024D64;
            }

            section p {
                line-height: 1.7;
            }

            /* SERVICIOS */

            .servicios {
                background: #EAF4F8;
            }

            .descripcion-servicios {
                max-width: 850px;
                margin: 0 auto 35px;
                color: #444444;
                font-size: 16px;
                line-height: 1.8;
            }

            .tarjetas {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 25px;
    max-width: 1200px;
    margin: 35px auto 0;
}

.tarjeta:nth-child(1),
.tarjeta:nth-child(2),
.tarjeta:nth-child(3) {
    grid-column: span 2;
}

.tarjeta:nth-child(4) {
    grid-column: 2 / span 2;
}

.tarjeta:nth-child(5) {
    grid-column: 4 / span 2;
}

            .tarjeta {
                background: #FFFFFF;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(0,0,0,0.09);
                text-align: left;
                transition: transform 0.3s ease,
                            box-shadow 0.3s ease;
            }

            .tarjeta:hover {
                transform: translateY(-6px);
                box-shadow: 0 9px 24px rgba(0,0,0,0.15);
            }

            .tarjeta img {
                width: 100%;
                height: 220px;
                object-fit: cover;
                display: block;
            }

            .tarjeta-contenido {
                padding: 24px;
            }

            .tarjeta h3 {
                margin-bottom: 14px;
                color: #A61731;
                font-size: 21px;
                line-height: 1.4;
            }

            .tarjeta p {
                color: #555555;
                font-size: 15px;
                line-height: 1.7;
            }

            /* CONTACTO */

            .contacto-titulo {
                background: #EAF4F8;
                padding: 55px 8% 35px;
                text-align: center;
            }

            .contacto-titulo h2 {
                color: #024D64;
                font-size: 34px;
                margin-bottom: 12px;
            }

            .contacto-titulo p {
                color: #555555;
                line-height: 1.6;
            }

            footer {
                background: #024D64;
                color: #FFFFFF;
                padding: 55px 7% 0;
            }

            .footer-contenido {
                display: grid;
                grid-template-columns: 1.2fr 1fr 1.2fr;
                gap: 40px;
                max-width: 1400px;
                margin: auto;
                padding-bottom: 45px;
            }

            .footer-columna h3 {
                color: #FFFFFF;
                font-size: 21px;
                margin-bottom: 25px;
                padding-bottom: 12px;
                border-bottom: 2px solid #A61731;
            }

            .footer-columna p {
                font-size: 14px;
                line-height: 1.8;
                margin-bottom: 13px;
                color: #EAF4F8;
            }

            .footer-columna a {
                color: #FFFFFF;
                text-decoration: none;
            }

            .footer-columna a:hover {
                color: #FFB6C1;
            }

            /* FORMULARIO */

            .formulario {
                display: flex;
                flex-direction: column;
                gap: 13px;
            }

            .formulario input,
            .formulario textarea {
                width: 100%;
                padding: 13px;
                border: 1px solid #D5E1E5;
                border-radius: 5px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                outline: none;
            }

            .formulario input:focus,
            .formulario textarea:focus {
                border-color: #A61731;
            }

            .formulario textarea {
                min-height: 110px;
                resize: vertical;
            }

            .formulario button {
                background: #A61731;
                color: #FFFFFF;
                border: none;
                padding: 15px;
                border-radius: 5px;
                font-size: 15px;
                font-weight: bold;
                cursor: pointer;
            }

            .formulario button:hover {
                background: #C52B45;
            }

            .mensaje {
                background: #FFFFFF;
                color: #024D64;
                padding: 12px;
                border-radius: 5px;
                margin-bottom: 15px;
                font-size: 14px;
                line-height: 1.5;
            }

            /* REDES SOCIALES */

            .redes {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
                margin-top: 20px;
            }

            .redes a {
                background: #FFFFFF;
                color: #024D64;
                padding: 10px 13px;
                border-radius: 5px;
                font-size: 13px;
                font-weight: bold;
            }

            .redes a:hover {
                background: #A61731;
                color: #FFFFFF;
            }

            /* MAPA */

            .mapa {
                width: 100%;
                height: 290px;
                border: 0;
                border-radius: 7px;
                margin-bottom: 15px;
            }

            .boton-mapa {
                display: inline-block;
                background: #A61731;
                padding: 11px 17px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
            }

            /* WHATSAPP */

            .whatsapp {
                position: fixed;
                bottom: 22px;
                right: 22px;
                width: 58px;
                height: 58px;
                border-radius: 50%;
                background: #25D366;
                color: #FFFFFF;
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                font-size: 29px;
                font-weight: bold;
                box-shadow: 0 4px 12px rgba(0,0,0,0.25);
                z-index: 1000;
            }

            .whatsapp:hover {
                transform: scale(1.08);
            }

            /* DERECHOS */

            .footer-final {
                border-top: 1px solid rgba(255,255,255,0.25);
                padding: 22px 10px;
                text-align: center;
            }

            .footer-final p {
                font-size: 13px;
                color: #EAF4F8;
                line-height: 1.8;
            }

            /* TABLETS */

            @media (max-width: 950px) {
    .tarjetas {
        grid-template-columns: repeat(2, 1fr);
    }

    .tarjeta:nth-child(1),
    .tarjeta:nth-child(2),
    .tarjeta:nth-child(3),
    .tarjeta:nth-child(4),
    .tarjeta:nth-child(5) {
        grid-column: auto;
    }

    .footer-contenido {
        grid-template-columns: 1fr 1fr;
    }

    .footer-columna:first-child {
        grid-column: 1 / -1;
    }
}

            /* CELULARES */

@media (max-width: 700px) {
    header {
        justify-content: center;
    }

    nav {
        justify-content: center;
        gap: 13px;
    }

    nav a {
        font-size: 12px;
    }

    .portada h1 {
        font-size: 30px;
    }

    .logo-imagen {
        max-width: 180px;
    }

    .tarjetas {
        grid-template-columns: 1fr;
        gap: 25px;
    }

    .tarjeta:nth-child(1),
    .tarjeta:nth-child(2),
    .tarjeta:nth-child(3),
    .tarjeta:nth-child(4),
    .tarjeta:nth-child(5) {
        grid-column: auto;
    }

    .tarjeta img {
        height: 210px;
    }

    .footer-contenido {
        grid-template-columns: 1fr;
        gap: 35px;
    }

    .footer-columna:first-child {
        grid-column: auto;
    }

    .contacto-titulo h2 {
        font-size: 28px;
    }
}
        </style>
    </head>

    <body>

        <!-- ENCABEZADO -->

        <header>
            <img
                class="logo-imagen"
                src="{{ url_for('static', filename='images/NEW_ORIZON_logo_recortado_fondo_negro.png') }}"
                alt="NEW ORIZON LOGISTICS S.A.C."
            >

            <nav>@
                <a href="#inicio">Inicio</a>
                <a href="#nosotros">Nosotros</a>
                <a href="#servicios">Servicios</a>
                <a href="#trabajo">Bolsa de trabajo</a>
                <a href="#contacto">Contacto</a>
            </nav>
        </header>

        <!-- PORTADA -->

        <img
            class="imagen-portada"
            src="{{ url_for('static', filename='images/portada.jpeg') }}"
            alt="Portada de NEW ORIZON LOGISTICS S.A.C."
        >

        <div class="portada" id="inicio">
            <h1>Conectamos el mundo con soluciones logísticas</h1>

            <p>
                Soluciones de transporte y logística para conectar
                negocios con nuevas oportunidades.
            </p>

            <a href="#servicios" class="boton">
                Conoce nuestros servicios
            </a>
        </div>

        <!-- NOSOTROS -->

        <section id="nosotros">
            <h2>Sobre nosotros</h2>

            <p>
                Bienvenidos a NEW ORIZON LOGISTICS S.A.C.
                Estamos preparando una nueva forma de conectar
                personas, empresas y destinos.
            </p>
        </section>

        <!-- SERVICIOS -->

        <section class="servicios" id="servicios">
            <h2>Nuestros servicios</h2>

            <p class="descripcion-servicios">
                Ofrecemos soluciones logísticas integrales para
                acompañar tus operaciones de comercio internacional,
                desde el origen hasta el destino de tu mercancía.
            </p>

            <div class="tarjetas">

                <!-- SERVICIO 1: MARITIMO -->

                <div class="tarjeta">
                    <img
                        src="{{ url_for('static', filename='images/maritimo.jpeg') }}"
                        alt="Transporte marítimo de mercancías"
                    >

                    <div class="tarjeta-contenido">
                        <h3>Flete Internacional Marítimo – LCL / FCL</h3>

                        <p>
                            Coordinamos el transporte marítimo de carga
                            consolidada y contenedores completos,
                            ofreciendo alternativas logísticas adaptadas
                            al volumen, origen y destino de cada operación.
                        </p>
                    </div>
                </div>

                <!-- SERVICIO 2: AEREO -->

                <div class="tarjeta">
                    <img
                        src="{{ url_for('static', filename='images/aereo.jpeg') }}"
                        alt="Transporte aéreo internacional"
                    >

                    <div class="tarjeta-contenido">
                        <h3>Flete Internacional Aéreo</h3>

                        <p>
                            Gestionamos soluciones de transporte aéreo
                            internacional para mercancías que requieren
                            agilidad, planificación y coordinación
                            eficiente en cada etapa del envío.
                        </p>
                    </div>
                </div>

                <!-- SERVICIO 3: ADUANAS -->

                <div class="tarjeta">
                    <img
                        src="{{ url_for('static', filename='images/aduanas.jpeg') }}"
                        alt="Agenciamiento de aduanas"
                    >

                    <div class="tarjeta-contenido">
                        <h3>Agenciamiento de Aduanas</h3>

                        <p>
                            Coordinamos los procesos de despacho aduanero
                            y la gestión documentaria necesaria para
                            facilitar las operaciones de importación y
                            exportación, en coordinación con agentes
                            especializados.
                        </p>
                    </div>
                </div>

                <!-- SERVICIO 4: SEGURO -->

                <div class="tarjeta">
                    <img
                        src="{{ url_for('static', filename='images/seguro.jpeg') }}"
                        alt="Seguro internacional de carga"
                    >

                    <div class="tarjeta-contenido">
                        <h3>Seguro Internacional de Carga</h3>

                        <p>
                            Coordinamos alternativas de seguro para
                            brindar protección a tu mercancía durante
                            el transporte internacional, de acuerdo
                            con las condiciones y coberturas disponibles.
                        </p>
                    </div>
                </div>

                <!-- SERVICIO 5: Transporte Terrestre -->

                <div class="tarjeta">
                    <img
                        src="{{ url_for('static', filename='images/terrestre.jpeg') }}"
                        alt="Transporte local de mercancías"
                    >

                    <div class="tarjeta-contenido">
                        <h3>Transporte terrestre</h3>

                        <p>
                            Gestionamos el traslado de mercancías desde
                            puertos, terminales y almacenes hasta el
                            destino indicado, coordinando unidades y
                            operadores según los requerimientos de
                            cada carga.
                        </p>
                    </div>
                </div>

            </div>
        </section>

        <!-- BOLSA DE TRABAJO -->

        <section id="trabajo">
            <h2>Bolsa de trabajo</h2>

            <p>
                Próximamente podrás conocer nuestras oportunidades
                laborales y formar parte de NEW ORIZON LOGISTICS S.A.C.
            </p>
        </section>

        <!-- CONTACTO -->

        <div class="contacto-titulo" id="contacto">
            <h2>Estamos aquí para ayudarte</h2>

            <p>
                Comunícate con NEW ORIZON LOGISTICS S.A.C.
                y conoce nuestras soluciones logísticas.
            </p>
        </div>

        <footer>

            <div class="footer-contenido">

                <!-- COLUMNA 1: FORMULARIO -->

                <div class="footer-columna">
                    <h3>Envíanos un mensaje</h3>

                    {% with mensajes = get_flashed_messages() %}
                        {% for mensaje in mensajes %}
                            <div class="mensaje">{{ mensaje }}</div>
                        {% endfor %}
                    {% endwith %}

                    <form class="formulario"
                          action="/enviar-mensaje"
                          method="POST">

                        <input
                            type="text"
                            name="nombre"
                            placeholder="Nombres y apellidos"
                            maxlength="100"
                            required
                        >

                        <input
                            type="email"
                            name="correo"
                            placeholder="Correo electrónico"
                            maxlength="150"
                            required
                        >

                        <input
                            type="tel"
                            name="celular"
                            placeholder="Número de celular"
                            maxlength="25"
                            required
                        >

                        <input
                            type="text"
                            name="empresa"
                            placeholder="Nombre de empresa"
                            maxlength="120"
                        >

                        <input
                            type="text"
                            name="cargo"
                            placeholder="Cargo"
                            maxlength="100"
                        >

                        <textarea
                            name="mensaje"
                            placeholder="Escribe tu mensaje..."
                            maxlength="3000"
                            required
                        ></textarea>

                        <button type="submit">
                            ENVIAR MENSAJE
                        </button>

                    </form>
                </div>

                <!-- COLUMNA 2: EMPRESA -->

                <div class="footer-columna">
                    <h3>NEW ORIZON LOGISTICS S.A.C.</h3>

                    <p>
                        <strong>Dirección:</strong><br>
                        Mz. H Lt. 17, Asociación Montecarlo,
                        San Martín de Porres, Lima, Perú.
                    </p>

                    <p>
                        <strong>Teléfono:</strong><br>
                        <a href="tel:+51907225733">
                            907 225 733
                        </a>
                    </p>

                    <p>
                        <strong>WhatsApp:</strong><br>
                        <a href="https://wa.me/51923754292?text=Hola%2C%20deseo%20informaci%C3%B3n%20y%20una%20cotizaci%C3%B3n%20sobre%20sus%20servicios%20log%C3%ADsticos.%20%C2%A1Gracias%21"
                           target="_blank">
                            923 754 292
                        </a>
                    </p>

                    <p>
                        <strong>Correo empresarial:</strong><br>
                        <a href="mailto:operaciones@neworizonlogistics.com">
                            operaciones@neworizonlogistics.com
                        </a>
                    </p>

                    <p>
                        <strong>Horario de atención:</strong><br>
                        Lunes a viernes<br>
                        9:00 a. m. – 6:00 p. m.
                    </p>

                    <p>
                        <strong>Síguenos en nuestras redes:</strong>
                    </p>

                    <div class="redes">
                        <a href="https://www.facebook.com/search/top?q=New%20Orizon%20Logistics"
                           target="_blank">Facebook</a>

                        <a href="https://www.instagram.com/"
                           target="_blank">Instagram</a>

                        <a href="https://www.tiktok.com/search?q=New%20Orizon%20Logistics"
                           target="_blank">TikTok</a>
                    </div>
                </div>

                <!-- COLUMNA 3: MAPA -->

                <div class="footer-columna">
                    <h3>Encuéntranos</h3>

                    <p>
                        Visítanos en nuestras oficinas.
                        Estamos ubicados en San Martín de Porres, Lima.
                    </p>

                    <iframe
                        class="mapa"
                        src="https://maps.google.com/maps?q=Mz.%20H%20Lt.%2017%20Asociacion%20Montecarlo%20San%20Martin%20de%20Porres%20Lima&t=&z=15&ie=UTF8&iwloc=&output=embed"
                        loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade"
                        allowfullscreen>
                    </iframe>

                    <a
                        class="boton-mapa"
                        href="https://maps.app.goo.gl/4d9h5vwpnNtVtk667"
                        target="_blank">
                        VER UBICACIÓN EN GOOGLE MAPS
                    </a>
                </div>

            </div>

            <div class="footer-final">
                <p>
                    NEW ORIZON LOGISTICS S.A.C.
                </p>

                <p>
                    © 2026 - Conectamos oportunidades. Coordinamos soluciones.
                </p>
            </div>

        </footer>

        <!-- BOTÓN FLOTANTE DE WHATSAPP -->

       <!-- BOTÓN FLOTANTE DE WHATSAPP -->

<a
    class="whatsapp"
    href="https://wa.me/51923754292?text=Hola%2C%20deseo%20informaci%C3%B3n%20y%20una%20cotizaci%C3%B3n%20sobre%20sus%20servicios%20log%C3%ADsticos.%20%C2%A1Gracias%21"
    target="_blank"
    aria-label="Contactar por WhatsApp">

    <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 32 32"
        width="34"
        height="34"
        fill="white">

        <path d="M16 2.5a13.4 13.4 0 0 0-11.5 20.3L2.7 30l7.4-1.9A13.5 13.5 0 1 0 16 2.5zm0 24.5c-2.2 0-4.3-.6-6.1-1.8l-.4-.2-4.4 1.2 1.2-4.3-.3-.5A11 11 0 1 1 16 27z"/>

        <path d="M22.1 18.7c-.3-.2-2-1-2.3-1.1-.3-.1-.5-.2-.7.2-.2.3-.8 1.1-1 1.3-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.6-.7-.6h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.2 3.1 1.4 3.3c.2.2 2.3 3.5 5.6 4.8 3.3 1.3 3.3.9 3.9.9.6-.1 2-.8 2.3-1.6.3-.8.3-1.5.2-1.6-.1-.1-.3-.2-.6-.4z"/>
    </svg>

</a>
        </a>

    </body>
    </html>
    """)


@app.route("/enviar-mensaje", methods=["POST"])
def enviar_mensaje():

    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    celular = request.form.get("celular", "").strip()
    empresa = request.form.get("empresa", "").strip()
    cargo = request.form.get("cargo", "").strip()
    mensaje = request.form.get("mensaje", "").strip()

    if not nombre or not correo or not celular or not mensaje:
        flash("Completa todos los campos obligatorios.")
        return redirect(url_for("inicio") + "#contacto")

    if len(nombre) > 100 or len(correo) > 150 or len(mensaje) > 3000:
        flash("Uno de los campos supera el límite permitido.")
        return redirect(url_for("inicio") + "#contacto")

    servidor = os.environ.get("MAIL_SERVER")
    puerto = int(os.environ.get("MAIL_PORT", "587"))
    usuario = os.environ.get("MAIL_USERNAME")
    clave = os.environ.get("MAIL_PASSWORD")
    usar_tls = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"

    if not servidor or not usuario or not clave:
        flash(
            "El formulario está preparado, pero falta configurar "
            "el servicio de correo. Comunícate directamente con nosotros."
        )
        return redirect(url_for("inicio") + "#contacto")

    try:
        correo_mensaje = EmailMessage()

        correo_mensaje["Subject"] = "Nueva consulta desde NEW ORIZON"
        correo_mensaje["From"] = usuario
        correo_mensaje["To"] = "operaciones@neworizonlogistics.com"
        correo_mensaje["Reply-To"] = correo

        correo_mensaje.set_content(f"""
NUEVA CONSULTA - NEW ORIZON LOGISTICS S.A.C.

Nombre: {nombre}
Correo: {correo}
Celular: {celular}
Empresa: {empresa}
Cargo: {cargo}

Mensaje:
{mensaje}
""")

        with smtplib.SMTP(servidor, puerto, timeout=20) as smtp:
            smtp.ehlo()

            if usar_tls:
                smtp.starttls()
                smtp.ehlo()

            smtp.login(usuario, clave)
            smtp.send_message(correo_mensaje)

        flash("¡Mensaje enviado correctamente! Gracias por contactarnos.")

    except Exception:
        app.logger.exception("Error al enviar el correo de contacto.")
        flash(
            "No se pudo enviar el mensaje en este momento. "
            "Por favor, inténtalo nuevamente o contáctanos por WhatsApp."
        )

    return redirect(url_for("inicio") + "#contacto")


if __name__ == "__main__":
    app.run(debug=True)
