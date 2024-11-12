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


# 🖥️ Proxmox

## 🏗️ Imagen de la Arquitectura
Nuestra arquitectura se basa en una red virtual, compuesta por un cliente (**MV CLIENTE**) que se conecta a Firebase a través de una máquina virtual que funciona como router (**MV ROUTER**) y un router físico conectado a Internet. Este enrutador tiene una dirección IP pública dinámica (100.77.20.X), permitiendo la conexión a Internet.

**MV ROUTER** administra dos interfaces:
- **VMBR0**: Interfaz externa con IP pública (100.77.20.120) conectada al router físico.
- **VMBR1**: Interfaz interna con IP privada (10.20.40.1), que permite la comunicación local con el cliente (IP 10.20.40.2).

Esta configuración de dos redes permite al cliente acceder a servicios externos, como Firebase, mediante una infraestructura combinada virtual y física. La estructura se implementa de la siguiente manera:

![Arquitectura Proxmox](https://github.com/user-attachments/assets/fe519f3a-bd52-4966-bbc3-93b77aabf96b)

---

# 🌐 Router
La incorporación de un router es fundamental para el proyecto, ya que permite conectar la red interna a Internet. Para lograr esto, configuramos dos adaptadores:
1. Uno para conectar con una red que tenga acceso a Internet.
2. Otro para la comunicación interna.

Con **iptables**, habilitamos el reenvío de paquetes, permitiendo a los dispositivos de la red interna acceder a Internet a través del router.

---

# 📶 DHCP
El servidor **DHCP** facilita la asignación de direcciones IP en la red de forma automática, simplificando la configuración. Al definir un rango de direcciones disponibles y configurar el tiempo de concesión, el servidor **DHCP** asegura que cada dispositivo reciba una IP única, evitando conflictos.

---

# ☁️ Firebase
**Firebase Database** es una base de datos NoSQL en la nube, que almacena datos en formato JSON y sincroniza en tiempo real con los clientes conectados. Utilizamos Firebase para almacenar la base de datos, permitiendo consultas a través de scripts en formato JSON para la web.

**Ventajas de Firebase**:
- Sincronización en tiempo real.
- Escalabilidad y estructura flexible.
- Seguridad configurable y almacenamiento offline.

Ideal para aplicaciones de chat, sistemas de gestión de contenido y juegos multijugador, ofreciendo una experiencia fluida incluso sin conexión a Internet.

---

# 🌐 DNS
Un servidor **DNS** es crucial para la resolución de nombres de dominio, facilitando el acceso al proyecto web mediante nombres de dominio en lugar de direcciones IP. 

**Funciones del DNS**:
- Traduce nombres de dominio a IPs para mejorar la accesibilidad.
- Ofrece redundancia, aumentando la disponibilidad.
- Administra registros como A, CNAME y MX, esenciales para la configuración de correos y otros servicios.

---

# 🌐 NGINX (Web)
**NGINX** es un servidor web y proxy inverso que gestiona solicitudes HTTP, balanceo de carga y terminación SSL. Su arquitectura asíncrona permite manejar múltiples conexiones simultáneamente, ideal para aplicaciones de alto tráfico.

**Funciones de NGINX**:
- Optimiza el rendimiento y reduce la latencia.
- Se integra con bases de datos, servidores de aplicaciones y herramientas de caché.
- Configura reglas de redirección, compresión de archivos y seguridad.

En este proyecto, usamos **NGINX** para alojar el código de la web, permitiendo el acceso de usuarios remotos.

---

# 📂 FTP
**FTP** es un protocolo fundamental para la transferencia de archivos entre cliente y servidor. Permite cargar y descargar archivos, facilitando la gestión de contenido en servidores web.

**Ventajas de FTP**:
- Simple y compatible con varios sistemas operativos.
- Transferencia de archivos grandes y reanudación de cargas.
- Seguridad mediante credenciales y la variante SFTP para cifrado de datos.

FTP será utilizado para almacenar y gestionar archivos que los usuarios puedan descargar.

---

# ⚙️ Instalaciones

## 🛠️ Instalación de Proxmox
Aquí se encuentra la información sobre la instalación de **Proxmox** que hemos realizado en el proyecto.

### 🔗 IP's de Proxmox (Interna y Externa)



<h2>⚙️ Configuración Netplan Cliente</h2> <p>Hemos creado una <b>red interna</b> en Proxmox 🖧, para manejar la conectividad de las VM. Esta es la configuración del <b>Cliente</b>, donde asignamos la IP <b>10.20.40.2/24</b>. También configuramos la puerta de enlace con la IP del router <b>10.20.40.1/24</b>.</p> <img src="https://github.com/user-attachments/assets/2eab6a67-2fdb-49d8-b8ac-9dbb79721d44" alt="Netplan Cliente" width="900" height="400" /> <h2>🛠️ Configuración Netplan Router</h2> <p>Hemos añadido un <b>router virtual</b> en Proxmox, que actúa como punto central para gestionar el tráfico de la red interna y mantener la comunicación hacia el exterior 🌐.</p> <img src="https://github.com/user-attachments/assets/85217131-03cd-4772-a3a0-dcf624145ae9" alt="Netplan Router" width="900" height="500" /> <h2>🔄 Conexión Entre Máquinas</h2> <p>Las interfaces de red en el router y el cliente están configuradas para que las máquinas virtuales puedan conectarse entre sí y con el router. Para verificar, realizamos pings entre las máquinas y desde el router a Google.com para asegurar conectividad hacia el exterior ✅.</p> <img src="https://github.com/user-attachments/assets/f95da3ba-bfc4-4488-a961-08f3ab36d132" alt="Prueba de Conexión" width="1100" height="600" /> <h2>🔥 Configuración de IPTables</h2> <p>Para configurar reglas de firewall y redirección de tráfico, utilizamos IPTables y modificamos <code>/etc/sysctl.conf</code> activando <b>net.ipv4.ip_forward=1</b>, lo cual permite que el router reenvíe tráfico entre interfaces de red 🔄.</p> <img src="https://github.com/user-attachments/assets/d062a00a-aaae-4e64-a2c4-17988b710dc6" alt="IPTables Configuración" width="900" height="600" /> <br> <p>Aplicamos el comando <code>sudo sysctl -p</code> para actualizar los cambios y añadimos reglas para permitir tráfico entre interfaces:</p> <pre><code>sudo iptables -A FORWARD -i ens19 -o ens18 -j ACCEPT</code></pre> <img src="https://github.com/user-attachments/assets/980bf8bf-f41f-4b93-a915-bccffde9d45e" alt="Reglas IPTables" width="600" height="300" /> <br> <p>Para garantizar la comunicación bidireccional, aplicamos la siguiente regla:</p> <pre><code>sudo iptables -A FORWARD -i ens18 -o ens19 -m state --state ESTABLISHED,RELATED -j ACCEPT</code></pre> <p>Guardamos los cambios con <code>sudo iptables-save</code> y confirmamos la conectividad externa con ping desde el cliente 🌍.</p> <img src="https://github.com/user-attachments/assets/eccf8c13-227f-44d6-901c-a7e328effdb8" alt="Prueba de Conexión Cliente" width="1200" height="400" /> <h2>📌 Reglas Permanentes</h2> <p>Para que las reglas de IPTables persistan después de reiniciar, instalamos <code>iptables-persistent</code>:</p> <pre><code>sudo apt install iptables-persistent -y</code></pre> <img src="https://github.com/user-attachments/assets/f7bc6414-ad7c-4fba-8651-15f21ec70b74" alt="Persistencia IPTables" width="900" height="400" /> <h2>📡 Configuración QEMU Cliente</h2> <p>En la máquina cliente, instalamos <code>qemu-guest-agent</code> para mejorar la administración de la VM en Proxmox:</p> <pre><code>sudo apt install qemu-guest-agent</code></pre> <img src="https://github.com/user-attachments/assets/aba1ca56-4c0f-403b-9ad9-fdb9fe35e1ad" alt="QEMU Cliente" width="1000" height="500" />
<h1 id="Instalación Router">🚀 Instalación del Router</h1> <p>La configuración principal del router implica ajustar el netplan e IPTables.</p> <h2>🔧 Configuración de ens19</h2> <p>La interfaz <b>ens19</b> tiene conexión al exterior con la IP <b>100.77.20.20</b> para asegurar una IP fija sin DHCP.</p> <img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/netplan-ens19.png" alt="Configuración ens19" width="468" height="239" /> <h2>🔧 Configuración de ens18</h2> <p>La interfaz <b>ens18</b> conecta con la red interna <b>10.20.40.0/24</b> usando como gateway la IP de la red real <b>100.77.20.1</b>.</p> <img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/netplan-ens18.png" alt="Configuración ens18" width="513" height="238" /> <h2>📜 Resultado Final del Netplan del Router</h2> <img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/netplan-router-all.png" alt="Netplan Final Router" width="635" height="525" /> <h2>⚙️ IPTables y Forwarding</h2> <p>Para que los clientes internos accedan a Internet, configuramos <code>/etc/sysctl.conf</code> activando <b>net.ipv4.ip_forward=1</b>.</p> <img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/sysctl
Estas son las IPs en los bridges de nuestra red. La interfaz **VMBR0** y **VMBR1** están configuradas en el router, mientras que solo **VMBR1** se usa en el cliente, definiendo así la red interna.

![IPs Proxmox](https://github.com/user-attachments/assets/d3b779ba-4444-4fef-8b57-d859c45d2e1b)


Aquí tienes el contenido estructurado y con emojis:

---

<h2>📝 Archivo sysctl.conf</h2>
<p>La primera configuración es en el archivo <code>/etc/sysctl.conf</code>, donde descomentaremos la línea <b>net.ipv4.ip.forward=1</b> para permitir el reenvío de tráfico entre las diferentes interfaces de red. 🔄</p>
<img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/sysctl-cong.png" alt="LOGO-GODO" width="247" height="93" />

<h2>🌐 Conexión de la Red Interna con el Exterior</h2>
<p>Una vez realizada esta configuración, utilizaremos IPTables para permitir que el tráfico de la red interna fluya hacia el exterior a través de la red especificada:</p>
<pre>
<code><b>sudo iptables -A FORWARD -i ens19 -o ens18 -j ACCEPT</b></code>
</pre>

<p>Además, añadimos una regla para permitir que las respuestas a las solicitudes que se originan desde la red interna puedan regresar sin problemas. Esto asegura una comunicación bidireccional eficiente.</p>
<pre>
<code><b>sudo iptables -A FORWARD -i ens18 -o ens19 -m state --state ESTABLISHED,RELATED -j ACCEPT</b></code>
</pre>

<p>Luego, reiniciamos el router y comprobamos la conexión con el comando:</p>
<pre>
<code><b>ping 8.8.8.8</b></code>
</pre>
<img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/ping-nginx.png" alt="LOGO-GODO" width="509" height="175" />

<h2>📌 Reglas Permanentes</h2>
<p>Para mantener las reglas de IPTables después de reiniciar el sistema, instalamos el paquete <code>iptables-persistent</code>:</p>
<pre>
<code><b>sudo apt install iptables-persistent -y</b></code>
</pre>

---

<h1 id="Instalación DHCP">📡 Instalación del DHCP</h1>
<p>Ahora que el router está configurado, es momento de instalar y configurar el servicio DHCP para asignar IPs automáticamente a los clientes que se añadan en el proyecto.</p>

<h2>🔄 Actualización del Sistema e Instalación del Servicio DHCP</h2>
<p>Nos aseguramos de que el router esté actualizado y procedemos a instalar el DHCP con los comandos:</p>
<pre>
<code><b>sudo apt update && sudo apt upgrade -y</b></code>
</pre>
y
<pre>
<code><b>sudo apt install isc-dhcp-server</b></code>
</pre>

<h2>⚙️ Configuración de dhcpd.conf</h2>
<p>Una vez instalado el servicio DHCP, vamos al archivo de configuración en <code>/etc/dhcp/dhcpd.conf</code> para declarar la siguiente configuración:</p>

<ul>
<li><b>Rango de IPs</b></li>
<li><b>Gateway de la red interna</b></li>
<li><b>IP del servidor DNS</b></li>
<li><b>Nombre de dominio</b> (Godofredo.com)</li>
<li><b>Resolución inversa del DNS</b></li>
</ul>

<h2>📋 Direcciones Estáticas por MAC</h2>
<p>Para evitar problemas de cambio de IPs en algunos servidores, hemos configurado direcciones estáticas por MAC. Así, el DHCP asignará siempre la misma dirección IP a los servidores específicos.</p>
<p>Para esto, indicamos el nombre del servidor, su MAC address, y la IP que el DHCP debe asignarle:</p>
<img src="https://github.com/Rusta4/Godofredos/blob/main/fotos_memoria/mac-dhcp.png" alt="LOGO-GODO" width="380" height="299" />

<h2>♻️ Reinicio y Estado del Servidor DHCP</h2>
<p>Para aplicar la configuración, reiniciamos el servidor DHCP y verificamos su estado:</p>
<pre>
<code><b>sudo systemctl restart isc-dhcp-server</b></code>
</pre>
<p>y</p>
<pre>
<code><b>sudo systemctl status isc-dhcp-server</b></code>
</pre>

---

<h1 id="Instalación Firebase">☁️ Instalación Firebase</h1>

<h2>🚀 Funcionamiento Interno</h2>
<p>Primero, instalamos una máquina Ubuntu y la actualizamos ejecutando el comando:</p>
<pre>
<code><b>sudo apt update && sudo apt upgrade -y</b></code>
</pre>

<p>A continuación, instalamos Node.js, asegurándonos de tener la versión más reciente y compatible:</p>
<pre>
<code><b>sudo apt-get install nodejs -y</b></code>
</pre>

<p>Para gestionar las versiones de Node.js y npm, utilizamos fnm (Fast Node Manager):</p>
<pre>
<code>
# Instalar fnm
<b>curl -fsSL https://fnm.vercel.app/install | bash</b>
# Activar fnm
<b>source ~/.bashrc</b>
# Instalar Node.js
<b>fnm use --install-if-missing 20</b>
# Verificar versión de Node.js
<b>node -v # debería mostrar `v20.18.0`</b>
# Verificar versión de npm
<b>npm -v # debería mostrar `10.8.2`</b>
</code>
</pre>

<h2>💻 Instalación de NPM y Firebase Tools</h2>
<p>Luego, instalamos npm, que es necesario para instalar <b>firebase-tools</b>:</p>
<pre>
<code><b>sudo apt install npm -y</b></code>
</pre>

<p>Con npm instalado, procedemos a instalar Firebase Tools:</p>
<pre>
<code><b>npm install -g firebase-tools</b></code>
</pre>

<h2>🔍 Verificación y Login en Firebase</h2>
<p>Verificamos la instalación de Firebase comprobando la versión:</p>
<pre>
<code><b>firebase --version</b></code>
</pre>
<img src="https://github.com/user-attachments/assets/dedc83ef-6b2c-475f-9a1a-43854b50cc0b" alt="LOGO-GODO" width="800" height="200" />

<p>Para iniciar sesión, usamos el siguiente comando:</p>
<pre>
<code><b>firebase login --no-localhost</b></code>
</pre>
<img src="https://github.com/user-attachments/assets/b6d07467-ddda-4377-ac9b-f4bc4284e849" alt="LOGO-GODO" width="800" height="100" />

<h2>🚀 Inicialización y Visualización de Proyectos</h2>
<p>Inicializamos Firebase en el proyecto con el comando:</p>
<pre>
<code><b>firebase init</b></code>
</pre>
<img src="https://github.com/user-attachments/assets/4e502ffc-d1b1-4d7f-8934-62c71aebd739" alt="LOGO-GODO" width="1000" height="500" />

<p>Para ver los proyectos disponibles, usamos:</p>
<pre>
<code><b>firebase projects:list</b></code>
</pre>

<h3>📂 Más Comandos Firebase en Ubuntu</h3>
<p>Luego de configurar Firebase, subimos los archivos HTML a la carpeta <code>public</code> y lanzamos el hosting para tener el sitio en línea con la base de datos integrada.</p>
<img src="https://github.com/user-attachments/assets/f75b8951-c442-4734-97a4-f8ae2b5dd3aa" alt="LOGO-GODO" width="1000" height="500" />
<img src="https://github.com/user-attachments/assets/519e8939-ee60-4a38-ae6b-e80cbfb70cdd" alt="LOGO-GODO" width="1000" height="500" />
