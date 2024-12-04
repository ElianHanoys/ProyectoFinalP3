from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  

driver = webdriver.Chrome(service=Service('C:\\Users\\cocom\\OneDrive\\Escritorio\\chromedriver-win64\\chromedriver.exe'))
driver.get('C:\\Users\\cocom\\OneDrive\\Escritorio\\P3 PROJECT\\index.html') 

time.sleep(2)

btn_show_date = driver.find_element(By.ID, 'btnShowDate')
btn_show_date.click()
time.sleep(1)
current_date = driver.find_element(By.ID, 'currentDate')
assert "Fecha actual:" in current_date.text, "La fecha no se mostró correctamente"
driver.save_screenshot("captura_fecha.png")

btn_dark_theme = driver.find_element(By.ID, 'btnToggleDarkTheme')
btn_dark_theme.click()
time.sleep(1)
assert 'dark-theme' in driver.find_element(By.TAG_NAME, 'body').get_attribute('class'), "El tema oscuro no se activó"
driver.save_screenshot("captura_tema_oscuro.png")

btn_light_theme = driver.find_element(By.ID, 'btnToggleLightTheme')
btn_light_theme.click()
time.sleep(1)
assert 'light-theme' in driver.find_element(By.TAG_NAME, 'body').get_attribute('class'), "El tema claro no se activó"
driver.save_screenshot("captura_tema_claro.png")

name_input = driver.find_element(By.ID, 'nameInput')
greet_button = driver.find_element(By.ID, 'btnGreet')
name_input.send_keys('Elian')
greet_button.click()
time.sleep(1)
greeting_message = driver.find_element(By.ID, 'greetingMessage')
assert "¡Hola, Elian!" in greeting_message.text, "El saludo no se mostró correctamente"
driver.save_screenshot("captura_saludo.png")

num1_input = driver.find_element(By.ID, 'num1')
num2_input = driver.find_element(By.ID, 'num2')
btn_add = driver.find_element(By.ID, 'btnAdd')
btn_subtract = driver.find_element(By.ID, 'btnSubtract')
btn_multiply = driver.find_element(By.ID, 'btnMultiply')
btn_divide = driver.find_element(By.ID, 'btnDivide')


num1_input.send_keys('10')
num2_input.send_keys('5')
btn_add.click()
time.sleep(1)
calc_result = driver.find_element(By.ID, 'calcResult')
assert "Resultado: 15" in calc_result.text, "La suma no funcionó correctamente"
driver.save_screenshot("captura_suma.png")

btn_subtract.click()
time.sleep(1)
assert "Resultado: 5" in calc_result.text, "La resta no funcionó correctamente"
driver.save_screenshot("captura_resta.png")

btn_multiply.click()
time.sleep(1)
assert "Resultado: 50" in calc_result.text, "La multiplicación no funcionó correctamente"
driver.save_screenshot("captura_multiplicacion.png")

btn_divide.click()
time.sleep(1)
assert "Resultado: 2" in calc_result.text, "La división no funcionó correctamente"
driver.save_screenshot("captura_division.png")

btn_generate_random = driver.find_element(By.ID, 'btnGenerateRandom')
btn_generate_random.click()
time.sleep(1)
random_number = driver.find_element(By.ID, 'randomNumber')
assert "Número aleatorio:" in random_number.text, "El número aleatorio no se generó correctamente"
driver.save_screenshot("captura_numero_aleatorio.png")

driver.quit()
