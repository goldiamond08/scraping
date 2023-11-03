from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# Initialize ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)


# Navigate to the website
driver.get(
    'https://www.paginasamarillas.es/search/all-ac/all-ma/madrid/all-is/madrid/all-ba/all-pu/all-nc/1?what=a&where=Madrid&ub=false&aprob=0.739575053332198&nprob=0.260424946667802&qc=true')  # Replace with actual URL

wait = WebDriverWait(driver, 10)

# First get the list of elements
first_divs = driver.find_elements_by_class_name('container')
print(first_divs.text)
first_div = first_divs[1]

