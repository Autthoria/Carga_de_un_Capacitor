import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configurar el puerto serie (ajusta COM3 si es necesario)
ser = serial.Serial("COM3", 9600, timeout=1)

# Lista para almacenar los datos
valores = []

# Función para actualizar la gráfica
def actualizar_grafica(i):
    if ser.in_waiting > 0:  # Si hay datos disponibles
        dato = ser.readline().decode("utf-8").strip()
        print(f"Dato recibido: {dato}")  # Mostrar el dato recibido
        try:
            voltaje = float(dato)  # Convertir el valor a flotante
            valores.append(voltaje)  # Agregar el voltaje a la lista
            valores[:] = valores[-1000:]  # Mantener solo los últimos 1000 datos

            # Imprimir los valores de voltaje para depuración
            print(f"Voltaje: {voltaje:.2f} V")
            
            plt.cla()  # Limpiar la gráfica
            plt.plot(valores, label="Voltaje del capacitor")
            plt.ylim(0, 5)  # Ajustar la escala del eje Y para voltaje de 0 a 5V
            plt.xlim(0, 1000)
            plt.xlabel("Tiempo")
            plt.ylabel("Voltaje (V)")  # Etiqueta en voltios
            plt.legend()

            # Mostrar el último valor de voltaje en la gráfica
            plt.text(400, 4.5, f'{voltaje:.2f} V', fontsize=12, color='red', ha='center')

        except ValueError:
            pass  # Ignorar datos incorrectos

# Configurar la animación en tiempo real
fig = plt.figure()
ani = animation.FuncAnimation(fig, actualizar_grafica, interval=100)

# Mostrar la gráfica
plt.show()

# Cerrar la conexión al cerrar la ventana
ser.close()
