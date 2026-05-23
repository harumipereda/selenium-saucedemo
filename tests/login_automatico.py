from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Abrir página
driver.get("https://www.saucedemo.com/")

# Usuario, standard_user es el usuario de prueba para login exitoso
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Contraseña, secret_sauce es la contraseña de prueba para login exitoso
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Botón login
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# =========================
# VALIDACIÓN URL
#Si muestra: inventory.html significa que el login fue exitoso, de lo contrario, el login falla
#https://www.saucedemo.com/inventory.html
# =========================

url_actual = driver.current_url

if "inventory.html" in url_actual:
    print("Login exitoso")
else:
    print("Login falló")

# =========================
# VALIDACIÓN TEXTO
#Products de la página en código muestra así:
#<span class="title" data-test="title">Products</span>
# =========================

texto_productos = driver.find_element(By.CLASS_NAME, "title").text

if texto_productos == "Products":
    print("Texto validado correctamente")

time.sleep(5)

driver.quit()