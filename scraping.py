# -SCRAPING-
from telnetlib import EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main import driver

# Wait a bit for JavaScript to load the page
driver.implicitly_wait(10)

# Get the page source
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

details_div = soup.find('div', class_='contenedor')

contact_div = details_div.find('div', class_='detalles-contacto')

content_div = contact_div.find('div', class_='content')

phone_span = content_div.find('span', class_='telephone')

wait = WebDriverWait(driver, 10)
website_anchor = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".detalles-contacto .content a.sitio-web")))

name_div = details_div.find('div', class_='text-center')
h1_div = name_div.find('h1', class_='mt-3 line-fluid')

claim_p = soup.find('p', class_='claim pb-2')

# Extract and print the telephone number
phone_number = phone_span.find('b').text
name = h1_div.text.strip()
website_url = website_anchor.get_attribute('href')
claim_text = claim_p.find('a').text

# Write to text file

with open('C:\\Users\\goldi\\Downloads\\buisnessPhones\\phones.txt', 'w') as f:
    f.write("")  # Clears the file

with open('C:\\Users\\goldi\\Downloads\\buisnessPhones\\phones.txt', 'a') as f:
    f.write(f"Name: {name}\n")
    f.write(f"Category: {claim_text}\n")
    f.write(f"Website: {website_url}\n")
    f.write("Telephone Number: " + phone_number + "\n")
    f.write(f"----------------")

driver.quit()
