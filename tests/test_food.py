from selenium import webdriver
from selenium.webdriver.common.by import By
def test_01():
  driver = webdriver.Chrome()
  driver.get("https://ddiana24.github.io/food.html")
  assert "Cтраница с рецептом" == driver.title
  element = driver.find_element(By.TAG_NAME, "h1")
  page_text = element.text
  assert '"Простой бутерброд с сыром"' in page_text

  driver.quit()
