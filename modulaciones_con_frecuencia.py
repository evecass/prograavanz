
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.widgets import Slider, TextBox, Button


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

points = 2000
bits = 20

type_of_modulation = 2

# Bit Rate inicial
bit_rate = 1000       # bits por segundo

# Frecuencia de la portadora
frecuencia_portadora = 8000   # Hz


# ==========================================================
# DATOS
# ==========================================================

data = [0] * bits

for i in range(bits):
    data[i] = random.randint(0, 1)


# ==========================================================
# CÁLCULOS DE BIT RATE Y BAUD RATE
# ==========================================================

def bits_por_simbolo():

    # ASK, OOK, FSK y BPSK son binarias
    return 1


def calcular_baud_rate():

    M = 2 ** bits_por_simbolo()

    return bit_rate / math.log2(M)


def tiempo_de_bit():

    return 1 / bit_rate


def tiempo_de_simbolo():

    baud = calcular_baud_rate()

    return 1 / baud


# ==========================================================
# TIEMPO TOTAL DE LA TRANSMISIÓN
# ==========================================================

def tiempo_total():

    return bits * tiempo_de_bit()


# ==========================================================
# VECTOR DE TIEMPO
# ==========================================================

def crear_tiempo():

    total = tiempo_total()

    return [
        i * total / (points - 1)
        for i in range(points)
    ]


# ==========================================================
# PORTADORA
# ==========================================================

portadora_x = [0] * points
portadora_y = [0] * points


def portadora():

    global portadora_x
    global portadora_y

    portadora_x = crear_tiempo()

    for i in range(points):

        t = portadora_x[i]

        # Frecuencia real en Hz
        portadora_y[i] = math.sin(
            2 * math.pi * frecuencia_portadora * t
        )


# ==========================================================
# MODULANTE
# ==========================================================

modulante_x = [0] * points
modulante_y = [0] * points


def modulante():

    global modulante_x
    global modulante_y

    modulante_x = crear_tiempo()

    modulante_y = [0] * points

    Tbit = tiempo_de_bit()

    for i in range(points):

        t = modulante_x[i]

        numero_bit = int(t / Tbit)

        if numero_bit >= bits:
            numero_bit = bits - 1

        modulante_y[i] = data[numero_bit]


# ==========================================================
# MODULADA
# ==========================================================

modulada_x = [0] * points
modulada_y = [0] * points


# ==========================================================
# ASK
# ==========================================================

def ask():

    global modulada_x
    global modulada_y
    global type_of_modulation

    type_of_modulation = 1

    print("tipo de modulación: ASK")

    for i in range(points):

        t = modulante_x[i]

        modulada_x[i] = t

        if modulante_y[i] == 1:

            modulada_y[i] = portadora_y[i]

        else:

            modulada_y[i] = portadora_y[i] / 2


# ==========================================================
# PSK
# ==========================================================

def psk():

    global modulada_x
    global modulada_y
    global type_of_modulation

    type_of_modulation = 2

    print("tipo de modulación: PSK")

    for i in range(points):

        t = modulante_x[i]

        modulada_x[i] = t

        if modulante_y[i] == 1:

            modulada_y[i] = portadora_y[i]

        else:

            modulada_y[i] = math.sin(
                2 * math.pi * frecuencia_portadora * t
                + math.pi
            )


# ==========================================================
# OOK
# ==========================================================

def ook():

    global modulada_x
    global modulada_y
    global type_of_modulation

    type_of_modulation = 3

    print("tipo de modulación: OOK")

    for i in range(points):

        t = modulante_x[i]

        modulada_x[i] = t

        if modulante_y[i] == 1:

            modulada_y[i] = portadora_y[i]

        else:

            modulada_y[i] = 0


# ==========================================================
# FSK
# ==========================================================

def fsk():

    global modulada_x
    global modulada_y
    global type_of_modulation

    type_of_modulation = 4

    print("tipo de modulación: FSK")

    frecuencia_fsk_0 = frecuencia_portadora
    frecuencia_fsk_1 = frecuencia_portadora * 2

    for i in range(points):

        t = modulante_x[i]

        modulada_x[i] = t

        if modulante_y[i] == 1:

            modulada_y[i] = math.sin(
                2 * math.pi * frecuencia_fsk_1 * t
            )

        else:

            modulada_y[i] = math.sin(
                2 * math.pi * frecuencia_fsk_0 * t
            )


# ==========================================================
# SELECCIÓN DE MODULACIÓN
# ==========================================================

def modulation_type(val):

    global type_of_modulation

    if val == 1:

        ask()

    elif val == 2:

        psk()

    elif val == 3:

        ook()

    elif val == 4:

        fsk()


# ==========================================================
# CREAR SEÑALES INICIALES
# ==========================================================

portadora()
modulante()
modulation_type(type_of_modulation)


# ==========================================================
# FIGURA
# ==========================================================

fig = plt.figure(figsize=(12, 9))

plt.subplots_adjust(
    left=0.10,
    right=0.95,
    bottom=0.19,
    top=0.76,
    hspace=0.60
)


# ==========================================================
# VENTANA DEL DOMINIO DE LA FRECUENCIA
# ==========================================================

fig_frecuencia = plt.figure(figsize=(10, 5))
fig_frecuencia.canvas.manager.set_window_title(
    "Dominio de la frecuencia"
)

ax_frecuencia_fft = fig_frecuencia.add_subplot(1, 1, 1)

ax_frecuencia_fft.set_title("Espectro de frecuencia")
ax_frecuencia_fft.set_xlabel("Frecuencia (Hz)")
ax_frecuencia_fft.set_ylabel("Magnitud")
ax_frecuencia_fft.grid(True)


# ==========================================================
# GRÁFICA PORTADORA
# ==========================================================

ax1 = fig.add_subplot(3, 1, 1)

linea_portadora, = ax1.plot(
    portadora_x,
    portadora_y
)

ax1.set_title("Portadora")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Amplitud")
ax1.grid(True)


# ==========================================================
# GRÁFICA MODULANTE
# ==========================================================

ax2 = fig.add_subplot(3, 1, 2)

linea_modulante, = ax2.plot(
    modulante_x,
    modulante_y
)

ax2.set_title("Modulante")
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Bit")
ax2.set_ylim(-0.2, 1.2)
ax2.grid(True)


# ==========================================================
# GRÁFICA MODULADA
# ==========================================================

ax3 = fig.add_subplot(3, 1, 3)

linea_modulada, = ax3.plot(
    modulada_x,
    modulada_y
)

ax3.set_title("Señal modulada")
ax3.set_xlabel("Tiempo (s)")
ax3.set_ylabel("Amplitud")
ax3.grid(True)


# ==========================================================
# INFORMACIÓN
# ==========================================================

texto_informacion = fig.text(
    0.5,
    0.965,
    "",
    ha="center",
    va="center",
    fontsize=11
)


def nombre_modulacion():

    if type_of_modulation == 1:
        return "ASK"

    elif type_of_modulation == 2:
        return "PSK"

    elif type_of_modulation == 3:
        return "OOK"

    elif type_of_modulation == 4:
        return "FSK"


def actualizar_informacion():

    nombre = nombre_modulacion()

    br = bit_rate

    baud = calcular_baud_rate()

    tb = tiempo_de_bit()

    ts = tiempo_de_simbolo()

    texto_informacion.set_text(
        f"{nombre}   |   "
        f"Bit Rate: {br:.0f} bit/s   |   "
        f"Baud Rate: {baud:.0f} baud   |   "
        f"Tb: {tb * 1000:.3f} ms   |   "
        f"Ts: {ts * 1000:.3f} ms"
    )


# ==========================================================
# ACTUALIZAR GRÁFICA DEL DOMINIO DE LA FRECUENCIA
# ==========================================================

def actualizar_frecuencia_fft():
    # Si no hay señal, no hacemos nada
    if len(modulada_y) == 0:
        return

    # Vector de tiempo actual
    tiempo = np.array(modulada_x)

    # Señal modulada
    señal = np.array(modulada_y)

    # Número de muestras
    N = len(señal)

    # Paso de tiempo promedio
    if N > 1:
        dt = np.mean(np.diff(tiempo))
    else:
        return

    # Frecuencia de muestreo
    fs = 1 / dt

    # FFT: solamente frecuencias positivas
    espectro = np.fft.rfft(señal)

    frecuencias = np.fft.rfftfreq(N, d=dt)

    # Magnitud normalizada
    magnitud = np.abs(espectro) / N

    # Corregir amplitud para el espectro de un solo lado
    if N > 1:
        magnitud[1:-1] *= 2

    # Actualizar la gráfica
    ax_frecuencia_fft.clear()

    ax_frecuencia_fft.plot(
        frecuencias,
        magnitud
    )

    ax_frecuencia_fft.set_title(
        f"Espectro de frecuencia - {nombre_modulacion()}"
    )

    ax_frecuencia_fft.set_xlabel("Frecuencia (Hz)")
    ax_frecuencia_fft.set_ylabel("Magnitud (u. a.)")
    ax_frecuencia_fft.grid(True)

    # Mostrar desde 0 Hz hasta Nyquist
    ax_frecuencia_fft.set_xlim(-1000, fs / 2)

    ax_frecuencia_fft.relim()
    ax_frecuencia_fft.autoscale_view(
        tight=False,
        scalex=False,
        scaley=True
    )

    fig_frecuencia.canvas.draw_idle()


# ==========================================================
# BOTONES DE MODULACIÓN
# ==========================================================

ax_ask = fig.add_axes(
    (0.10, 0.84, 0.10, 0.055)
)

ax_psk = fig.add_axes(
    (0.22, 0.84, 0.10, 0.055)
)

ax_ook = fig.add_axes(
    (0.34, 0.84, 0.10, 0.055)
)

ax_fsk = fig.add_axes(
    (0.46, 0.84, 0.10, 0.055)
)


b_ask = Button(ax_ask, "ASK")
b_psk = Button(ax_psk, "PSK")
b_ook = Button(ax_ook, "OOK")
b_fsk = Button(ax_fsk, "FSK")


# ==========================================================
# ACTUALIZAR MODULACIÓN
# ==========================================================

def actualizar_ask(event):

    global type_of_modulation

    type_of_modulation = 1

    modulation_type(type_of_modulation)

    linea_modulada.set_xdata(modulada_x)
    linea_modulada.set_ydata(modulada_y)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


def actualizar_psk(event):

    global type_of_modulation

    type_of_modulation = 2

    modulation_type(type_of_modulation)

    linea_modulada.set_xdata(modulada_x)
    linea_modulada.set_ydata(modulada_y)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


def actualizar_ook(event):

    global type_of_modulation

    type_of_modulation = 3

    modulation_type(type_of_modulation)

    linea_modulada.set_xdata(modulada_x)
    linea_modulada.set_ydata(modulada_y)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


def actualizar_fsk(event):

    global type_of_modulation

    type_of_modulation = 4

    modulation_type(type_of_modulation)

    linea_modulada.set_xdata(modulada_x)
    linea_modulada.set_ydata(modulada_y)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


b_ask.on_clicked(actualizar_ask)
b_psk.on_clicked(actualizar_psk)
b_ook.on_clicked(actualizar_ook)
b_fsk.on_clicked(actualizar_fsk)


# ==========================================================
# SLIDER DE FRECUENCIA
# ==========================================================

ax_frecuencia = fig.add_axes(
    [0.20, 0.075, 0.60, 0.025]
)

slider_frecuencia = Slider(
    ax_frecuencia,
    "Portadora (Hz)",
    1000,
    20000,
    valinit=frecuencia_portadora,
    valstep=100
)


# ==========================================================
# SLIDER DE BIT RATE
# ==========================================================

ax_bitrate = fig.add_axes(
    [0.20, 0.035, 0.60, 0.025]
)

slider_bitrate = Slider(
    ax_bitrate,
    "Bit Rate",
    100,
    5000,
    valinit=bit_rate,
    valstep=100
)


# ==========================================================
# ACTUALIZAR FRECUENCIA
# ==========================================================

def actualizar_frecuencia(val):

    global frecuencia_portadora

    frecuencia_portadora = slider_frecuencia.val

    portadora()

    modulation_type(type_of_modulation)

    linea_portadora.set_xdata(portadora_x)
    linea_portadora.set_ydata(portadora_y)

    linea_modulada.set_xdata(modulada_x)
    linea_modulada.set_ydata(modulada_y)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


slider_frecuencia.on_changed(
    actualizar_frecuencia
)


# ==========================================================
# ACTUALIZAR BIT RATE
# ==========================================================

def actualizar_bitrate(val):

    global bit_rate

    bit_rate = slider_bitrate.val

    # Volvemos a construir el eje temporal
    portadora()
    modulante()

    modulation_type(type_of_modulation)

    # Actualizar portadora
    linea_portadora.set_xdata(
        portadora_x
    )

    linea_portadora.set_ydata(
        portadora_y
    )

    # Actualizar modulante
    linea_modulante.set_xdata(
        modulante_x
    )

    linea_modulante.set_ydata(
        modulante_y
    )

    # Actualizar modulada
    linea_modulada.set_xdata(
        modulada_x
    )

    linea_modulada.set_ydata(
        modulada_y
    )

    # Ajustar límites de tiempo
    limite = tiempo_total()

    ax1.set_xlim(0, limite)
    ax2.set_xlim(0, limite)
    ax3.set_xlim(0, limite)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


slider_bitrate.on_changed(
    actualizar_bitrate
)


# ==========================================================
# CAJA DE CÓDIGO
# ==========================================================

ax_codigo = fig.add_axes(
    [0.20, 0.005, 0.60, 0.025]
)

entrada_codigo = TextBox(
    ax_codigo,
    "Código:",
    initial="".join(map(str, data))
)


# ==========================================================
# ACTUALIZAR CÓDIGO
# ==========================================================

def actualizar_codigo(text):

    global data
    global bits

    nuevo_codigo = ""

    for numero in text:

        if numero in "01":

            nuevo_codigo += numero

    if len(nuevo_codigo) == 0:

        return

    data = [
        int(numero)
        for numero in nuevo_codigo
    ]

    bits = len(data)

    portadora()
    modulante()

    modulation_type(
        type_of_modulation
    )

    linea_portadora.set_xdata(
        portadora_x
    )

    linea_portadora.set_ydata(
        portadora_y
    )

    linea_modulante.set_xdata(
        modulante_x
    )

    linea_modulante.set_ydata(
        modulante_y
    )

    linea_modulada.set_xdata(
        modulada_x
    )

    linea_modulada.set_ydata(
        modulada_y
    )

    limite = tiempo_total()

    ax1.set_xlim(0, limite)
    ax2.set_xlim(0, limite)
    ax3.set_xlim(0, limite)

    actualizar_informacion()
    actualizar_frecuencia_fft()

    fig.canvas.draw_idle()


entrada_codigo.on_submit(
    actualizar_codigo
)


# ==========================================================
# INFORMACIÓN INICIAL
# ==========================================================

actualizar_informacion()
actualizar_frecuencia_fft()

limite_inicial = tiempo_total()

ax1.set_xlim(0, limite_inicial)
ax2.set_xlim(0, limite_inicial)
ax3.set_xlim(0, limite_inicial)


# ==========================================================
# MOSTRAR
# ==========================================================

plt.show()
