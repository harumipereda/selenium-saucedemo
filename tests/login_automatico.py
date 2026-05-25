from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# =========================
# INICIO TIEMPO EJECUCIÓN
# =========================

inicio = time.time()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Abrir página
driver.get("https://www.saucedemo.com/")

# Usuario
usuario = "standard_user"

driver.find_element(By.ID, "user-name").send_keys(usuario)

# Contraseña
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Botón login
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# =========================
# VALIDACIÓN URL
# =========================

url_actual = driver.current_url

if "inventory.html" in url_actual:
    resultado_login = "Login exitoso"
    estado = "PASS"
else:
    resultado_login = "Login falló"
    estado = "FAIL"

print(resultado_login)

# =========================
# VALIDACIÓN TEXTO
# =========================

texto_productos = driver.find_element(By.CLASS_NAME, "title").text

if texto_productos == "Products":
    print("Texto validado correctamente")

# =========================
# FIN TIEMPO EJECUCIÓN
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
=== REPORTE AUTOMATIZACIÓN LOGIN ===

Usuario: {usuario}
Estado: {estado}
Resultado: {resultado_login}
URL actual: {url_actual}
Navegador: Chrome
Fecha: {fecha}
Tiempo ejecución: {tiempo_ejecucion} segundos
"""

with open("reporte_automatizacion_login.txt", "w", encoding="utf-8") as archivo:
    archivo.write(reporte)

print("Reporte generado correctamente")

time.sleep(5)

driver.quit()