from flask import Flask, render_template_string, request, redirect, url_for, flash
from email.message import EmailMessage
from pathlib import Path
import smtplib
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "clave-temporal-desarrollo")

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
        <meta name="google-site-verification" content="_nflRzVJg-8Be9vrd76cF4XgiQyeoAG71vheiwRZ8HY">

        <title>NEW ORIZON LOGISTICS S.A.C. | Agencia de Carga Internacional</title>

        <meta name="description" content="NEW ORIZON LOGISTICS S.A.C. ofrece servicios de carga internacional marítima y aérea, agenciamiento de aduanas, seguro de carga y transporte terrestre en Perú.">

 
\        <style>
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
                transition: color 0.3s ease;
            }

            nav a:hover {
                color: #87A4BA;
            }

            /* PORTADA */

            .portada {
                background: #EAF4F8;
                padding: 75px 8%;
                text-align: center;
            }

            .portada-contenido {
                max-width: 900px;
                margin: auto;
            }

            .portada h1 {
                font-size: 42px;
                margin-bottom: 20px;
                color: #024D64;
            }

            .portada p {
                font-size: 19px;
                line-height: 1.7;
                max-width: 700px;
                margin: auto;
                color: #444444;
            }

            .boton-principal {
                display: inline-block;
                margin-top: 25px;
                background: #A61731;
                color: #FFFFFF;
                padding: 14px 25px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                transition: background 0.3s ease;
            }

            .boton-principal:hover {
                background: #C52B45;
            }


            /* PORTADA PRINCIPAL ADAPTABLE */

            .portada-fondo {
                position: relative;
                width: 100%;
                overflow: hidden;
            }

            @media (min-width: 769px) {
                .portada-fondo {
                    max-height: 52vw;
                }
            }

            .portada-imagen {
                display: block;
                width: 100%;
                height: auto;
                object-fit: contain;
                object-position: center;
            }

            .portada {
                position: absolute;
                inset: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: flex-start;
                padding: 35px clamp(25px, 7vw, 100px);
                box-sizing: border-box;
                background: linear-gradient(
                    90deg,
                    rgba(0, 0, 0, 0.42),
                    rgba(0, 0, 0, 0.10)
                );
                text-align: left;
            }

            .portada-contenido {
                width: 58%;
                max-width: 650px;
                margin: 0;
            }

            .portada h1 {
                color: #FFFFFF;
                font-size: clamp(25px, 2.5vw, 34px);
                line-height: 1.2;
                margin: 0 0 12px;
                text-shadow: 0 2px 8px rgba(0,0,0,0.5);
            }

            .portada p {
                color: #FFFFFF;
                font-size: clamp(13px, 1.1vw, 16px);
                line-height: 1.5;
                max-width: 480px;
                margin: 0;
                text-shadow: 0 1px 6px rgba(0,0,0,0.5);
            }

            .portada-frase {
                position: absolute;
                left: clamp(25px, 7vw, 100px);
                bottom: 18px;
                max-width: 430px;
                color: #FFFFFF;
                font-size: clamp(13px, 1.3vw, 17px);
                font-weight: 600;
                line-height: 1.4;
                text-shadow: 0 2px 7px rgba(0,0,0,0.55);
            }

            /* SECCIONES GENERALES */

            .seccion {
                padding: 70px 8%;
                text-align: center;
            }

            .seccion h2 {
                font-size: 32px;
                margin-bottom: 20px;
                color: #024D64;
            }

            .seccion p {
                line-height: 1.7;
            }

            /* NOSOTROS */

            .nosotros-intro {
                max-width: 850px;
                margin: 0 auto 35px;
                color: #555555;
                font-size: 16px;
                line-height: 1.8;
            }

            .nosotros-tarjetas {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 25px;
                max-width: 1050px;
                margin: 0 auto;
                text-align: left;
            }

            .nosotros-tarjeta {
                background: #EAF4F8;
                border-top: 5px solid #024D64;
                border-radius: 9px;
                padding: 28px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.07);
            }

            .nosotros-tarjeta h3 {
                color: #A61731;
                font-size: 23px;
                margin-bottom: 14px;
            }

            .nosotros-tarjeta p {
                color: #444444;
                font-size: 15px;
                line-height: 1.8;
            }

            .valores {
                max-width: 1050px;
                margin: 25px auto 0;
                background: #FFFFFF;
                border-top: 5px solid #A61731;
                border-radius: 9px;
                padding: 28px;
                text-align: left;
                box-shadow: 0 4px 15px rgba(0,0,0,0.07);
            }

            .valores h3 {
                color: #A61731;
                font-size: 23px;
                margin-bottom: 18px;
            }            .valores-lista {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 16px 25px;
                margin-top: 18px;
            }

            .valor {
                color: #444444;
                font-size: 15px;
                line-height: 1.7;
            }

            .valor strong {
                color: #024D64;
            }

            /* SERVICIOS */

            .servicios {
                background: #EAF4F8;
            }

            .seccion-descripcion {
                max-width: 850px;
                margin: 0 auto 35px;
                color: #444444;
                font-size: 16px;
                line-height: 1.8;
            }

            .servicios-grid {
                display: grid;
                grid-template-columns: repeat(6, 1fr);
                gap: 25px;
                max-width: 1200px;
                margin: 35px auto 0;
            }

            .servicio {
                grid-column: span 2;
                background: #FFFFFF;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(0,0,0,0.09);
                text-align: left;
                transition: transform 0.3s ease,
                            box-shadow 0.3s ease;
            }

            .servicio:nth-child(4) {
                grid-column: 2 / span 2;
            }

            .servicio:nth-child(5) {
                grid-column: 4 / span 2;
            }

            .servicio:hover {
                transform: translateY(-6px);
                box-shadow: 0 9px 24px rgba(0,0,0,0.15);
            }

            .servicio img {
                width: 100%;
                height: 220px;
                object-fit: cover;
                display: block;
            }

            .servicio h3 {
                margin: 20px 20px 12px;
                color: #A61731;
                font-size: 21px;
                line-height: 1.4;
            }

            .servicio p {
                padding: 0 20px 24px;
                color: #555555;
                font-size: 15px;
                line-height: 1.7;
            }

            /* BOLSA DE TRABAJO */

            .bolsa {
                background: #FFFFFF;
            }

            .bolsa p {
                max-width: 800px;
                margin: 0 auto 15px;
                color: #555555;
                font-size: 16px;
            }

            /* CONTACTO */

            .contacto {
                background: #EAF4F8;
            }

            .contacto h2 {
                margin-bottom: 35px;
            }

            .footer-columnas {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 30px;
                max-width: 1300px;
                margin: auto;
                text-align: left;
            }

            .footer-columna {
                background: #024D64;
                color: #FFFFFF;
                padding: 25px;
                border-radius: 9px;
            }

            .footer-columna h3 {
                color: #FFFFFF;
                font-size: 21px;
                margin-bottom: 20px;
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
                overflow-wrap: anywhere;
            }

            .footer-columna a:hover {
                color: #FFB6C1;
            }

            /* FORMULARIO */

            .contacto-formulario {
                display: flex;
                flex-direction: column;
                gap: 13px;
                max-width: 750px;
                margin: 35px auto 0;
                padding: 30px;
                background: #FFFFFF;
                border-radius: 10px;
                text-align: left;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }

            .contacto-formulario h3 {
                color: #024D64;
                font-size: 23px;
                margin-bottom: 10px;
                text-align: center;
            }

            .contacto-formulario label {
                color: #024D64;
                font-weight: bold;
                font-size: 14px;
            }

            .contacto-formulario input,
            .contacto-formulario textarea {
                width: 100%;
                padding: 13px;
                border: 1px solid #D5E1E5;
                border-radius: 5px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                outline: none;
            }

            .contacto-formulario input:focus,
            .contacto-formulario textarea:focus {
                border-color: #A61731;
            }

            .contacto-formulario textarea {
                min-height: 110px;
                resize: vertical;
            }

            .contacto-formulario button {
                background: #A61731;
                color: #FFFFFF;
                border: none;
                padding: 15px;
                border-radius: 5px;
                font-size: 15px;
                font-weight: bold;
                cursor: pointer;
            }

            .contacto-formulario button:hover {
                background: #C52B45;
            }

                        /* MENSAJES */

            .mensaje {
                background: #FFFFFF;
                color: #024D64;
                padding: 12px;
                border-radius: 5px;
                margin: 15px auto;
                max-width: 750px;
                font-size: 14px;
                line-height: 1.5;
            }

            /* REDES SOCIALES */

            .redes {
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
                margin-top: 12px;
            }

            .redes a {
                color: #FFFFFF;
                text-decoration: none;
                font-weight: bold;
            }

            .redes a:hover {
                color: #87A4BA;
            }

            /* MAPA */

            .mapa {
                width: 100%;
                height: 220px;
                border: 0;
                border-radius: 8px;
                margin-top: 15px;
            }

            .boton-mapa {
                display: inline-block;
                background: #A61731;
                color: #FFFFFF;
                padding: 10px 18px;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 12px;
                font-weight: bold;
            }

            .boton-mapa:hover {
                background: #C52B45;
            }

            /* WHATSAPP */

            .whatsapp {
                position: fixed;
                right: 20px;
                bottom: 20px;
                width: 58px;
                height: 58px;
                background: #25D366;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 999;
                box-shadow: 0 3px 10px rgba(0,0,0,0.25);
                transition: transform 0.3s ease;
            }

            .whatsapp:hover {
                transform: scale(1.1);
            }

            .whatsapp svg {
                width: 32px;
                height: 32px;
                fill: #FFFFFF;
            }

            /* PIE DE PÁGINA */

            .footer-final {
                background: #013747;
                color: #FFFFFF;
                text-align: center;
                padding: 20px;
                font-size: 13px;
            }

            /* DISEÑO PARA TABLETS Y CELULARES */

            @media (max-width: 900px) {
                .footer-columnas {
                    grid-template-columns: 1fr 1fr;
                }

                .footer-columna:last-child {
                    grid-column: 1 / -1;
                }
            }

            @media (max-width: 768px) {
                .portada-imagen {
                    display: block;
                    width: 100%;
                    height: auto;
                    object-fit: contain;
                    object-position: center;
                }

                .portada {
                    position: absolute;
                    inset: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: flex-start;
                    justify-content: center;
                    padding: 20px;
                    box-sizing: border-box;
                    background: linear-gradient(
                        90deg,
                        rgba(0, 0, 0, 0.45),
                        rgba(0, 0, 0, 0.12)
                    );
                    text-align: left;
                }

                .portada-contenido {
                    width: 85%;
                    max-width: 430px;
                    margin: 0;
                }

                .portada h1 {
                    font-size: clamp(19px, 5vw, 25px);
                    line-height: 1.2;
                    margin-bottom: 9px;
                }

                .portada p {
                    font-size: 13px;
                    line-height: 1.4;
                    margin: 0;
                }

                .portada-frase {
                    position: absolute;
                    left: 20px;
                    bottom: 12px;
                    transform: none;
                    width: 85%;
                    max-width: 430px;
                    margin: 0;
                    font-size: 12px;
                    line-height: 1.35;
                    text-align: left;
                }

                header {
                    flex-direction: column;
                    padding: 15px;
                }

                .logo-imagen {
                    max-width: 180px;
                }

                nav {
                    justify-content: center;
                    gap: 12px;
                }

                nav a {
                    font-size: 13px;
                }

                .seccion {
                    padding: 45px 18px;
                }

                .seccion h2 {
                    font-size: 27px;
                }

                .nosotros-tarjetas {
                    grid-template-columns: 1fr;
                }

                .valores-lista {
                    grid-template-columns: 1fr;
                }

                .servicios-grid {
                    grid-template-columns: 1fr;
                }

                .servicio,
                .servicio:nth-child(4),
                .servicio:nth-child(5) {
                    grid-column: auto;
                }

                .footer-columnas {
                    grid-template-columns: 1fr;
                }

                .footer-columna:last-child {
                    grid-column: auto;
                }

                .contacto-formulario {
                    padding: 20px;
                }

                .whatsapp {
                    width: 54px;
                    height: 54px;
                    right: 15px;
                    bottom: 15px;
                }
            }

            @media (max-width: 400px) {
                .portada h1 {
                    font-size: 25px;
                }

                nav {
                    gap: 10px;
                }

                nav a {
                    font-size: 12px;
                }
            }

        </style>
    </head>

        <body>

        <header>
            <a href="#inicio">
                <img
                    src="{{ url_for('static', filename='images/NEW_ORIZON_logo_recortado_fondo_negro.png') }}"
                    alt="NEW ORIZON LOGISTICS S.A.C."
                    class="logo-imagen"
                >
            </a>

            <nav>
                <a href="#inicio">Inicio</a>
                <a href="#nosotros">Nosotros</a>
                <a href="#servicios">Servicios</a>
                <a href="#bolsa">Bolsa de trabajo</a>
                <a href="#contacto">Contacto</a>
            </nav>
        </header>

        <main>

            <!-- PORTADA -->

<div class="portada-fondo">

    <img
        class="portada-imagen"
        src="{{ url_for('static', filename='images/portada.jpeg') }}"
        alt="NEW ORIZON LOGISTICS"
    >

    <section class="portada" id="inicio">

        <div class="portada-contenido">

            <h1>
                Tu carga, en buenas manos,<br>
                de origen a destino.
            </h1>

            <p>
                Seguridad, eficiencia y confianza en cada operación logística.
            </p>

        </div>

        <div class="portada-frase">
            Conectamos oportunidades. Coordinamos soluciones.
        </div>

    </section>

</div>

            <!-- NOSOTROS -->

            <section class="seccion nosotros" id="nosotros">

                <h2>CONÓCENOS</h2>

                <div class="nosotros-intro">
                    <p>
                        NEW ORIZON LOGISTICS nace de la experiencia en el sector logístico y de la identificación de oportunidades para mejorar la gestión del comercio internacional.
                    </p>

                    <p>
                        Impulsada por la confianza de clientes que apostaron por este proyecto, surge con el propósito de brindar soluciones logísticas personalizadas, eficientes y confiables, construyendo relaciones comerciales basadas en el compromiso y la transparencia.
                    </p>
                </div>

                <div class="nosotros-tarjetas">

                    <div class="nosotros-tarjeta">
                        <h3>Nuestra misión</h3>
                        <p>
                            Brindar soluciones logísticas integrales que faciliten las operaciones de comercio internacional de nuestros clientes, ofreciendo atención personalizada, coordinación eficiente y compromiso en cada etapa del proceso.
                        </p>
                    </div>

                    <div class="nosotros-tarjeta">
                        <h3>Nuestra visión</h3>
                        <p>
                            Consolidarnos como una empresa logística reconocida por su confiabilidad, calidad de servicio y capacidad de conectar negocios con oportunidades en los mercados internacionales.
                        </p>
                    </div>

                </div>

                <div class="valores">
                    <h3>Nuestros valores</h3>
                    <p>
                        Compromiso, confianza, transparencia, responsabilidad y eficiencia en cada operación logística.
                    </p>
                </div>

            </section>

            <!-- SERVICIOS -->

            <section class="seccion servicios" id="servicios">

                <h2>NUESTROS SERVICIOS</h2>

                <p class="seccion-descripcion">
                    Brindamos soluciones logísticas para acompañar tus operaciones
                    de comercio internacional.
                </p>

                <div class="servicios-grid">

                    <div class="servicio">
                        <img src="{{ url_for('static', filename='images/maritimo.jpeg') }}"
                             alt="Flete Internacional Marítimo">

                        <h3>Flete Internacional Marítimo – LCL / FCL</h3>

                        <p>
                            Coordinamos el transporte marítimo de carga consolidada y
                            contenedores completos, ofreciendo alternativas logísticas
                            adaptadas al volumen, origen y destino de cada operación.
                        </p>
                    </div>

                    <div class="servicio">
                        <img src="{{ url_for('static', filename='images/aereo.jpeg') }}"
                             alt="Flete Internacional Aéreo">

                        <h3>Flete Internacional Aéreo</h3>

                        <p>
                            Gestionamos soluciones de transporte aéreo internacional
                            para mercancías que requieren agilidad, planificación y
                            coordinación eficiente en cada etapa del envío.
                        </p>
                    </div>

                    <div class="servicio">
                        <img src="{{ url_for('static', filename='images/aduanas.jpeg') }}"
                             alt="Agenciamiento de Aduanas">

                        <h3>Agenciamiento de Aduanas</h3>

                        <p>
                            Coordinamos los procesos de despacho aduanero y la gestión
                            documentaria necesaria para facilitar las operaciones de
                            importación y exportación, en coordinación con agentes
                            especializados.
                        </p>
                    </div>

                    <div class="servicio">
                        <img src="{{ url_for('static', filename='images/seguro.jpeg') }}"
                             alt="Seguro Internacional de Carga">

                        <h3>Seguro Internacional de Carga</h3>

                        <p>
                            Coordinamos alternativas de seguro para brindar protección
                            a tu mercancía durante el transporte internacional, de
                            acuerdo con las condiciones y coberturas disponibles.
                        </p>
                    </div>

                    <div class="servicio">
                        <img src="{{ url_for('static', filename='images/terrestre.jpeg') }}"
                             alt="Transporte Terrestre">

                        <h3>Transporte Terrestre</h3>

                        <p>
                            Gestionamos el traslado de mercancías desde puertos,
                            terminales y almacenes hasta el destino indicado,
                            coordinando unidades y operadores según los requerimientos
                            de cada carga.
                        </p>
                    </div>

                </div>

            </section>

            <!-- BOLSA DE TRABAJO -->

            <section class="seccion bolsa" id="bolsa">

                <h2>BOLSA DE TRABAJO</h2>

                <p>
                    ¿Te gustaría formar parte de nuestro equipo?
                    En NEW ORIZON LOGISTICS estamos interesados en conocer
                    personas comprometidas y con ganas de crecer profesionalmente.
                </p>

                <p>
                    Envíanos tu información y tu currículum al correo:
                </p>

                <a href="mailto:operaciones@neworizonlogistics.com"
                   class="boton-principal">
                    Enviar currículum
                </a>

            </section>

                        <!-- CONTACTO -->

            <section class="seccion contacto" id="contacto">

                <h2>CONTÁCTANOS</h2>

                <div class="footer-columnas">

                    <div class="footer-columna">

                        <h3>Información de contacto</h3>

                        <p>
                            <strong>Dirección:</strong><br>
                            Mz. H Lt. 17, Asociación Montecarlo,
                            San Martín de Porres, Lima, Perú.
                        </p>

                        <p>
                            <strong>Teléfono:</strong>
                            <a href="tel:+51907225733">907 225 733</a>
                        </p>

                        <p>
                            <strong>WhatsApp:</strong>
                            <a href="https://wa.me/51923754292?text=Hola%2C%20deseo%20informaci%C3%B3n%20y%20una%20cotizaci%C3%B3n%20sobre%20sus%20servicios%20log%C3%ADsticos.%20%C2%A1Gracias%21"
                               target="_blank">
                                923 754 292
                            </a>
                        </p>

                        <p>
                            <strong>Correo:</strong>
                            <a href="mailto:operaciones@neworizonlogistics.com">
                                operaciones@neworizonlogistics.com
                            </a>
                        </p>

                        <p>
                            <strong>Horario:</strong><br>
                            Lunes a viernes: 9:00 a. m. – 6:00 p. m.
                        </p>

                    </div>

                    <div class="footer-columna">

                        <h3>Encuéntranos</h3>

                        <iframe
                            class="mapa"
                            src="https://www.google.com/maps?q=Mz.%20H%20Lt.%2017%20Asociaci%C3%B3n%20Montecarlo%20San%20Mart%C3%ADn%20de%20Porres%20Lima&output=embed"
                            loading="lazy"
                            allowfullscreen>
                        </iframe>

                        <a class="boton-mapa"
                           href="https://maps.app.goo.gl/4d9h5vwpnNtVtk667"
                           target="_blank">
                            Ver ubicación
                        </a>

                    </div>

                    <div class="footer-columna">

                        <h3>Síguenos</h3>

                        <p>New Orizon Logistics</p>

                        <div class="redes">

                            <a href="https://www.facebook.com/search/top?q=New%20Orizon%20Logistics"
                               target="_blank">Facebook</a>

                            <a href="https://www.instagram.com/"
                               target="_blank">Instagram</a>

                            <a href="https://www.tiktok.com/search?q=New%20Orizon%20Logistics"
                               target="_blank">TikTok</a>

                        </div>

                    </div>

                </div>

                <!-- FORMULARIO -->

                <form class="contacto-formulario"
                      action="/enviar-mensaje"
                      method="POST">

                    <h3>Envíanos un mensaje</h3>

                    <label for="nombre">Nombre completo</label>
                    <input type="text" id="nombre" name="nombre"
                           placeholder="Escribe tu nombre" required>

                    <label for="correo">Correo electrónico</label>
                    <input type="email" id="correo" name="correo"
                           placeholder="ejemplo@correo.com" required>

                    <label for="telefono">Teléfono</label>
                    <input type="tel" id="telefono" name="telefono"
                           placeholder="Tu número de contacto">

                    <label for="mensaje">Mensaje</label>
                    <textarea id="mensaje" name="mensaje" rows="5"
                              placeholder="Cuéntanos cómo podemos ayudarte"
                              required></textarea>

                    <button type="submit">Enviar mensaje</button>

                </form>

            </section>

        </main>

        <!-- PIE DE PÁGINA -->

        <footer class="footer-final">
            <p>
                © 2026 NEW ORIZON LOGISTICS S.A.C.
                Todos los derechos reservados.
            </p>
        </footer>

        <!-- BOTÓN WHATSAPP -->

        <a class="whatsapp"
           href="https://wa.me/51923754292?text=Hola%2C%20deseo%20informaci%C3%B3n%20y%20una%20cotizaci%C3%B3n%20sobre%20sus%20servicios%20log%C3%ADsticos.%20%C2%A1Gracias%21"
           target="_blank"
           aria-label="Contactar por WhatsApp">

            <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 .5C7.45.5.5 7.45.5 16c0 2.73.72 5.29 1.98 7.51L.5 31.5l8.2-1.95A15.43 15.43 0 0 0 16 31.5c8.55 0 15.5-6.95 15.5-15.5S24.55.5 16 .5zm0 28.3c-2.35 0-4.65-.63-6.65-1.83l-.48-.29-4.86 1.16 1.2-4.74-.31-.49A12.75 12.75 0 1 1 16 28.8zm7-9.55c-.38-.19-2.24-1.1-2.59-1.23-.35-.13-.6-.19-.85.19-.25.38-.97 1.23-1.19 1.48-.22.25-.44.28-.82.09-.38-.19-1.6-.59-3.05-1.89-1.13-1.01-1.9-2.26-2.12-2.64-.22-.38-.02-.58.17-.77.17-.17.38-.44.57-.66.19-.22.25-.38.38-.63.13-.25.06-.47-.03-.66-.09-.19-.85-2.05-1.17-2.81-.31-.74-.62-.64-.85-.65h-.73c-.25 0-.66.09-1.01.47-.35.38-1.32 1.29-1.32 3.15s1.35 3.65 1.54 3.9c.19.25 2.66 4.06 6.45 5.69.9.39 1.6.62 2.15.79.9.29 1.72.25 2.37.15.72-.11 2.24-.91 2.56-1.79.32-.88.32-1.63.22-1.79-.09-.16-.34-.25-.72-.44z"/>
            </svg>

        </a>

    """)


# SITEMAP

@app.route("/sitemap.xml")
def sitemap():

    contenido = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://new-orizon-logistics.onrender.com/</loc>
            <changefreq>weekly</changefreq>
            <priority>1.0</priority>
        </url>
    </urlset>
    """

    return app.response_class(
        contenido,
        mimetype="application/xml"
    )


# ROBOTS

@app.route("/robots.txt")
def robots():

    contenido = """User-agent: *
Allow: /

Sitemap: https://new-orizon-logistics.onrender.com/sitemap.xml
"""

    return app.response_class(
        contenido,
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(debug=True)
