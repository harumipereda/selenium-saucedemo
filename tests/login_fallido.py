from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# =========================
# INICIO TIEMPO
# =========================

inicio = time.time()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# =========================
# ABRIR PÁGINA
# =========================

driver.get("https://www.saucedemo.com/")

# =========================
# LOGIN INCORRECTO
# =========================

usuario = "usuario_falso"

driver.find_element(By.ID, "user-name").send_keys(usuario)

driver.find_element(By.ID, "password").send_keys("clave_falsa")

driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# =========================
# VALIDAR MENSAJE ERROR
# =========================

mensaje_error = driver.find_element(By.CLASS_NAME, "error-message-container").text

if "Epic sadface" in mensaje_error:
    estado = "PASS"
    resultado = "Mensaje de error mostrado correctamente"
else:
    estado = "FAIL"
    resultado = "No se mostró mensaje error"

print(resultado)

# =========================
# TIEMPO EJECUCIÓN
# =========================

fin = time.time()

tiempo_ejecucion = round(fin - inicio, 2)

# =========================
# FECHA
# =========================

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# =========================
# REPORTE TXT
# =========================

reporte = f"""
=== REPORTE LOGIN FALLIDO ===

Usuario: {usuario}
Estado: {estado}
Resultado: {resultado}
Mensaje encontrado: {mensaje_error}
Fecha: {fecha}
Tiempo ejecución: {tiempo_ejecucion} segundos
"""

with open("reporte_login_fallido.txt", "w", encoding="utf-8") as archivo:
    archivo.write(reporte)

print("Reporte generado correctamente")

time.sleep(5)

driver.quit()