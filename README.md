## 📑 Índice

- **[💡 Explicación de la Idea del Proyecto](#explicacion-idea-del-proyecto)**
- **[🎯 Nuestros Objetivos](#nuestros-objetivos)**
- **[🛠️ Tecnologías Usadas](#tecnologias-usadas)**
- **[🗂️ Organización](#organizacion)**
  - 📅 [Diagrama Gantt](#diagrama-gantt)
  - 🗄️ [Diagrama NoSQL](#diagrama-nosql)
- **[🌐 Página Web](#pagina-web)**
  - 🖼️ [Mockup](#mockup)
  - 📐 [Diagrama Web](#diagrama-web)
  - 🎨 [Paleta de Colores](#paleta-colores)
  - 🖌️ [Logo](#logo)
  - ⚙️ [Funcionalidades Web](#funcionalidades-web)
- **[🖥️ Proxmox](#proxmox)**
  - 🖼️ [Imagen de la Arquitectura](#imagen-arquitectura)
- **[🌐 Router](#router)**
- **[📡 DHCP](#dhcp)**
- **[🔥 Firebase](#firebase)**
- **[🔗 DNS](#dns)**
- **[🌐 NGINX (Web)](#nginx-web)**
- **[📁 FTP](#ftp)**
- **[⚙️ Instalaciones](#instalaciones)**
  - 🖥️ [Instalación de Proxmox](#instalacion-proxmox)
  - 🌐 [Instalación del Router](#instalacion-router)
  - 📡 [Instalación de DHCP](#instalacion-dhcp)
  - 🔥 [Instalación de Firebase](#instalacion-firebase)
  - 🔗 [Instalación de DNS](#instalacion-dns)
  - 🌐 [Instalación de NGINX y SSL](#instalacion-nginx)
  - 📁 [Instalación de FTP](#instalacion-ftp)


## 💡 Explicación de la Idea del Proyecto
Estamos creando una plataforma web similar a GitHub, pero enfocada exclusivamente en el campo de la ciberseguridad. Nuestro objetivo es proporcionar un espacio para que los profesionales de la seguridad informática puedan colaborar, compartir herramientas, scripts y proyectos en áreas como evaluación de vulnerabilidades y automatización de auditorías.

Una característica clave de nuestra plataforma es el uso de imágenes Docker, lo que permitirá a los usuarios crear y compartir entornos preconfigurados de manera rápida. Esto facilita la colaboración y permite replicar de forma precisa entornos seguros para pruebas de seguridad.

---

## 🎯 Nuestros Objetivos
Buscamos ofrecer una herramienta centralizada para el desarrollo en ciberseguridad, promoviendo una colaboración efectiva entre expertos y entusiastas. Al reunir recursos, herramientas y proyectos en un solo lugar, facilitamos el acceso a soluciones innovadoras y prácticas para toda la comunidad.

![Logo del proyecto](https://github.com/user-attachments/assets/222bf100-c324-4f2e-86e5-ef21598cb985)

---

## 🛠️ Tecnologías Usadas
Para este proyecto, hemos elegido tecnologías que permiten crear un entorno virtualizado y una aplicación web robusta:

### 1. Proxmox
Proxmox es una plataforma de virtualización de código abierto que permite la gestión de máquinas virtuales y contenedores, optimizando los recursos del servidor en una interfaz centralizada.

### 2. Máquinas Virtuales (VM)
Las VM permiten ejecutar varios sistemas operativos en un mismo hardware físico. Son ideales para pruebas y despliegues en entornos aislados, mejorando la seguridad y flexibilidad del sistema.

### 3. Bootstrap
Bootstrap es un framework de diseño que facilita la creación de interfaces web responsivas y modernas, con un sistema de rejilla adaptable y componentes predefinidos para un diseño atractivo y "mobile-first".

### 4. HTML (HyperText Markup Language)
HTML es el lenguaje de marcado para la creación de páginas web, proporcionando la estructura básica para el contenido mediante etiquetas interpretadas por navegadores.

### 5. CSS (Cascading Style Sheets)
CSS permite el control de la presentación y diseño de las páginas web, separando el contenido del estilo visual para facilitar el mantenimiento y mejorar la apariencia de la página.

### 6. Firebase
Firebase es una plataforma en la nube que incluye una base de datos NoSQL en tiempo real, ideal para gestionar grandes volúmenes de datos y sincronizar información de forma rápida y escalable.

### 7. Docker
Docker es una plataforma de contenedores que permite empaquetar aplicaciones y dependencias en "imágenes" reproducibles en cualquier entorno, agilizando la implementación y colaboración.

---

## 🗂️ Organización

### Nicolás Guerra
- Proxmox
- Docker
- Firebase

### Adrià Trillo
- Máquinas Virtuales (VM)
- HTML

### Edward Murphy
- CSS
- Bootstrap

---

## 📅 Diagrama Gantt
![Diagrama Gantt](https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/diagrama-grantt.png)

---

## 🗄️ Diagrama NoSQL
Como utilizamos Firebase, un tipo de base de datos NoSQL, el diagrama se ha realizado directamente en la nube de Firebase. A continuación, se muestra la estructura de colecciones, documentos y campos.

![Estructura de Firebase 1](https://github.com/user-attachments/assets/56b66400-d640-4b77-87d8-6df387f9c247)
![Estructura de Firebase 2](https://github.com/user-attachments/assets/1c5a2ee1-1f9f-4540-858a-4dd2a3334718)
![Estructura de Firebase 3](https://github.com/user-attachments/assets/4ea8488b-9647-413d-b05f-04bcfa4805bc)
![Estructura de Firebase 4](https://github.com/user-attachments/assets/b3020efc-6d73-4622-aa33-34a2ffb66727)
![Estructura de Firebase 5](https://github.com/user-attachments/assets/1ad4121e-51dd-4f97-bd8e-cfc334f9510d)
![Estructura de Firebase 6](https://github.com/user-attachments/assets/acaca4fd-4094-4c29-a917-e81d2e7d605a)

---

## 🎨 Conclusión
Estas tecnologías aseguran un entorno sólido y flexible, permitiendo el desarrollo de una aplicación web dinámica que cumple con los objetivos del proyecto.

# 🌐 Página Web

## 🎨 Mockup
La primera pantalla es de bienvenida, diseñada para captar la atención del usuario con un video de fondo que hace la página visualmente atractiva. El mensaje principal invita a explorar el foro de repositorios destacados, con un botón de llamada a la acción que lleva a los servicios. Se destacan categorías populares como **Docker**, **Hacking tools** e **ISO files**, permitiendo al usuario elegir temas de interés rápidamente. Al final, se incluyen enlaces a redes sociales e información legal, cumpliendo con normativas y facilitando la conexión con la comunidad.

La segunda pantalla permite explorar contenido a través de una barra de búsqueda con filtros. Los resultados se muestran en tarjetas visuales con imágenes, texto y enlaces, dando una vista previa clara antes de profundizar en detalles. Los filtros permiten personalizar la búsqueda, haciendo la navegación más rápida y eficiente.

La tercera pantalla está enfocada en la información del proyecto, con un carrusel de imágenes que destaca características y actualizaciones, acompañado de un bloque de texto. Además, se incluyen estadísticas importantes, como descargas y usuarios activos, mostrando el impacto y alcance del proyecto y generando confianza en los visitantes.

El diseño general está orientado a ofrecer una experiencia de usuario fluida, con una interfaz limpia y bien organizada que facilita la navegación y asegura que los usuarios encuentren la información que buscan sin sentirse abrumados.

![Mockup](https://github.com/Rusta4/Godofredos/blob/main/mokcups/conjunto-mockup%C3%A7.png)

---

## 🗺️ Diagrama Web
El mapa del sitio está estructurado en torno a la página principal (**HOME**), que actúa como nodo central para cinco secciones clave: recursos técnicos, gestión de usuarios y páginas informativas.

- **Recursos técnicos**: Incluye Hacking tools, Docker, y ISO files, enlazando a un foro de hacking, una página sobre Docker y descargas de archivos ISO.
- **Gestión de usuarios**: En la sección **INICIAR SESIÓN**, los usuarios pueden autenticarse, registrarse o recuperar contraseñas mediante un código de verificación. Además, en diferentes áreas del sitio se puede acceder al perfil de usuario, donde es posible modificar credenciales.
- **About Us**: Proporciona información sobre el sitio y permite acceder a autenticación y registro.

La estructura facilita un flujo de navegación eficiente, priorizando tanto el acceso a recursos técnicos como la administración de la cuenta de usuario de manera modular.

![Diagrama Web](https://github.com/user-attachments/assets/e90dfc7f-f809-465d-98d9-5063af0227a1)

---

## 🎨 Paleta de Colores
La paleta de colores combina blanco, gris claro, azul oscuro y verde fuerte, equilibrando simplicidad y dinamismo. 
- **Blanco**: Aporta claridad y limpieza.
- **Gris claro**: Ofrece neutralidad y elegancia.
- **Azul oscuro**: Transmite confianza y profesionalismo, ideal para entornos corporativos.
- **Verde fuerte**: Añade energía, destacando elementos clave como llamadas a la acción.

Esta combinación crea una armonía visual funcional y atractiva.

![Paleta de Colores](https://github.com/user-attachments/assets/4a00d276-8ad7-4cf6-a7fb-11ecbbd096f1)

---

## 🖼️ Logo
El primer logo ha sido seleccionado para la web, reflejando simplicidad y profesionalismo, alineado con un estilo minimalista moderno. El diseño en blanco y negro ofrece una estética limpia y elegante, fácil de integrar en diversas plataformas. El animal icónico en el logo aporta personalidad y un toque distintivo sin sobrecargar el diseño.

![Logo](https://github.com/user-attachments/assets/a8580f0e-db47-4891-bf4a-0d3fd1cccb1d)

---

## ⚙️ Funcionalidades Web
La plataforma web ofrece diversas funcionalidades destacadas en la experiencia del usuario y la administración del sitio. A continuación, se muestran las principales características de la plataforma:

![Funcionalidades Web 1](https://github.com/user-attachments/assets/37a57af5-b507-4c2a-ad87-854c6c390611)
![Funcionalidades Web 2](https://github.com/user-attachments/assets/750eb6fb-18b9-49af-bc89-a224408ab418)
![Funcionalidades Web 3](https://github.com/user-attachments/assets/abc825ac-d3d8-4b15-a1c8-1d5af8564ee5)

---

