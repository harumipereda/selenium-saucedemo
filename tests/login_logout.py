from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Inicializar web driver
def initilize_driver():
    driver = webdriver.Edge()
    return driver

def login(driver):
    input_username = driver.find_element(By.ID, "user-name")
    # para validar que encontró el elemento print(input_username)
    # ahora con XPATH compelto /html/body/div/div/div[2]/div[2]/div/div[1]/text()[1]
    # salió mal user_name_value= driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/text()[1]")
    # entonces, se hará de otra manera, lo saqué con XPATH: //*[@id="login_credentials"]/text()[1]
    container_username = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
    # print(container_username.text)
    # Salida Accepted usernames are: standard_user etc...
    split_container_username = container_username.text.split("\n")
    # print(split_container_username)
    # Salida ['Accepted usernames are:', 'standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    user_name = split_container_username[1]
    # print(user_name)
    input_username.send_keys(user_name)
    input_password = driver.find_element(By.ID, "password")
    container_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]')
    # print(container_password.text)
    split_container_password = container_password.text.split("\n")
    password = split_container_password[1]
    input_password.send_keys(password)
    # time.sleep(2)
    # botón login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    # time.sleep(2)
    # comprobación
    return driver


def main():
    driver = initilize_driver()
    driver.get("https://www.saucedemo.com/")
    driver=login(driver)
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print("Login exitoso")
        # logout
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        time.sleep(2)
        logout_button = driver.find_element(By.ID,"logout_sidebar_link")
        logout_button.click()
        print("Logout exitoso")
        driver.quit()
    else:
        print("Login fallido")


if __name__ == "__main__":
    main()