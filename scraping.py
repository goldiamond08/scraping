import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Initialize WebDriver
# Enable headless mode

chrome_options = webdriver.ChromeOptions()

# Disable JavaScript
chrome_options.add_argument('--disable-javascript')

# Disable images
chrome_options.add_argument('--blink-settings=imagesEnabled=false')

driver = webdriver.Chrome(options=chrome_options)


# Navigate to the website
driver.get(
    'https://www.paginasamarillas.es/search/all-ac/all-ma/madrid/all-is/madrid/all-ba/all-pu/all-nc/1?what=a&where=Madrid&ub=false&aprob=0.739575053332198&nprob=0.260424946667802&qc=true')

# Wait for the initial page to load


with open('C:\\Users\\goldi\\Downloads\\buisnessPhones\\phones.txt', 'w') as file:
    pass

# Loop through search pages
try:
    while True:
        # Get the current number of search results
        all_listados = driver.find_elements(By.CSS_SELECTOR, 'div.listado-item.item-ig')

        # Loop through search results on the current page
        for i in range(len(all_listados)):
            try:
                start_time = time.time()

                # Navigate through divs to find the exact span
                all_containers = driver.find_elements(By.CSS_SELECTOR,
                                                      'body.tests.srl.commonHeader.commonFooter div.container')
                first_div = all_containers[1]
                all_first_rows = first_div.find_elements(By.CSS_SELECTOR, 'div.row')
                second_div = all_first_rows[1]
                third_div = second_div.find_element(By.CSS_SELECTOR, 'div.first-content-listado')
                fourth_div = third_div.find_element(By.CSS_SELECTOR, 'div.col-lg-7.col-md-8.col-xs-12')
                fifth_div = fourth_div.find_element(By.CSS_SELECTOR, 'div.bloque-central')
                sixth_div = fifth_div.find_element(By.CSS_SELECTOR, 'div.central')
                all_listados = sixth_div.find_elements(By.CSS_SELECTOR, 'div.listado-item.item-ig')
                listLen = len(all_listados)
                seventh_div = all_listados[i]
                seventh_div_scroll = all_listados[i - 1]
                first_div_next = sixth_div.find_element(By.CSS_SELECTOR, 'div.pag2')
                second_div_next = first_div_next.find_element(By.CSS_SELECTOR, 'ul.pagination')
                next_btn = second_div_next.find_element(By.CSS_SELECTOR, 'i.fa.icon-flecha-derecha')
                eighth_div = seventh_div.find_element(By.CSS_SELECTOR, 'div.box')
                eighth_div_scroll = seventh_div_scroll.find_element(By.CSS_SELECTOR, 'div.box')
                ninth_div = eighth_div.find_element(By.CSS_SELECTOR, 'div.cabecera')
                ninth_div_scroll = eighth_div_scroll.find_element(By.CSS_SELECTOR, 'div.cabecera')
                tenth_div = ninth_div.find_element(By.CSS_SELECTOR, 'div.row')
                tenth_div_scroll = ninth_div_scroll.find_element(By.CSS_SELECTOR, 'div.row')
                eleventh_div = tenth_div.find_element(By.CSS_SELECTOR, 'div.col-xs-11.comercial-nombre')
                eleventh_div_scroll = tenth_div_scroll.find_element(By.CSS_SELECTOR, 'div.col-xs-11.comercial-nombre')
                all_rows_in_eleventh = eleventh_div.find_elements(By.CSS_SELECTOR, 'div.row')
                all_rows_in_eleventh_scroll = eleventh_div_scroll.find_elements(By.CSS_SELECTOR, 'div.row')
                twelfth_div = all_rows_in_eleventh[0]
                twelfth_div_scroll = all_rows_in_eleventh_scroll[0]
                target_span = twelfth_div.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]')
                target_span_scroll = twelfth_div_scroll.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]')

                if i > 0:
                    # Scroll the target element into view using JavaScript
                    driver.execute_script("arguments[0].scrollIntoView();", target_span_scroll)
                    # Click the element
                    target_span.click()
                else:
                    # Click the element
                    target_span.click()

                # Get the page source
                html = driver.page_source

                soup = BeautifulSoup(html, 'html.parser')
                details_div = soup.find('div', class_='contenedor')
                contact_div = details_div.find('div', class_='detalles-contacto')
                content_div = contact_div.find('div', class_='content')
                phone_span = content_div.find('span', class_='telephone')

                # Find the website anchor element
                try:
                    # Find the website anchor element
                    website_anchor = driver.find_element(By.CSS_SELECTOR, ".detalles-contacto .content a.sitio-web")
                    website_url = website_anchor.get_attribute('href')
                except NoSuchElementException:
                    # Handle the case where the website element is not found
                    website_url = "Website not available"

                name_div = details_div.find('div', class_='text-center')
                h1_div = name_div.find('h1', class_='mt-3 line-fluid')
                claim_p = soup.find('p', class_='claim pb-2')

                # Extract and print the telephone number
                try:
                    # Find the website anchor element
                    phone_number = phone_span.find('b').text
                except NoSuchElementException:
                    # Handle the case where the website element is not found
                    phone_number = "Phone number not available"

                name = h1_div.text.strip()
                claim_text = claim_p.find('a').text

                # Write to text file
                with open('C:\\Users\\goldi\\Downloads\\buisnessPhones\\phones.txt', 'a') as f:
                    f.write(f"{i +1}\n")
                    f.write(f"Name: {name}\n")
                    f.write(f"Category: {claim_text}\n")
                    f.write(f"Website: {website_url}\n")
                    f.write("Telephone Number: " + phone_number + "\n")
                    f.write(f"---------------- \n")

                current_time = time.time()
                elapsed_time = current_time - start_time
                print("index "+ str(i+1) + " logged in: " + str(elapsed_time) + "s")

                # Go back to the search results page
                driver.back()

                if i == listLen - 2:
                    next_btn.click()

            except Exception as e:
                # Handle individual result scraping exceptions
                print(f"Error scraping result {i + 1}: {str(e)}")


finally:
    # Quit the WebDriver
    print("Quitting...")
    driver.quit()
