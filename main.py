import threading
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-javascript')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    'https://www.paginasamarillas.es/search/all-ac/all-ma/madrid/all-is/madrid/all-ba/all-pu/all-nc/1?what=a&where=Madrid&ub=false&aprob=0.739575053332198&nprob=0.260424946667802&qc=true')
with open('C:\\Users\\goldi\\Downloads\\buisnessPhones\\phones.txt', 'w') as file:
    pass

name = "no name yet"
claim_text = "no claim text yet"
website_url = "no url yet"
phone_number = "no phone yet"


def scrape_element(i, driver):
    j = 1
    # Scraping
    global name
    global website_url
    global claim_text
    global phone_number
    html = driver.page_source
    try:
        soup = BeautifulSoup(html, 'html.parser')
       #  print("element " + str(j) + " found at index " + str(i))
       #  j += 1
        details_div = soup.find('div', class_='contenedor')
       #  print("element " + str(j) + " found at index " + str(i))
       #  j += 1
        contact_div = details_div.find('div', class_='detalles-contacto')
       #  print("element " + str(j) + " found at index " + str(i))
       #  j += 1
        content_div = contact_div.find('div', class_='content')
       #  print("element " + str(j) + " found at index " + str(i))
       #  j += 1
        phone_span = content_div.find('span', class_='telephone')
       #  print("element " + str(j) + " found at index " + str(i))
       #  j += 1
    except NoSuchElementException:
        print("something in the initial search went wrong")

    try:
        # Find the website anchor element
        website_anchor = driver.find_element(By.CSS_SELECTOR, ".detalles-contacto .content a.sitio-web")
        website_url = website_anchor.get_attribute('href')
    except NoSuchElementException:
        website_url = "Website not available"
    print("element " + str(j) + " found at index " + str(i))
    j += 1

    name_div = details_div.find('div', class_='text-center')
    print("element " + str(j) + " found at index " + str(i))
    j += 1
    h1_div = name_div.find('h1', class_='mt-3 line-fluid')
    print("element " + str(j) + " found at index " + str(i))
    j += 1

    try:
        # claim_p = soup.find('p', class_='claim pb-2')
        claim_text = "claim_p.find('a').text"
    except NoSuchElementException:
        claim_text = "no claim text available"
    print("element " + str(j) + " found at index " + str(i))
    j += 1

    try:
        # Find the website anchor element
        phone_number = phone_span.find('b').text
    except NoSuchElementException:
        phone_number = "Phone number not available"
    print("element " + str(j) + " found at index " + str(i))
    j += 1

    name = h1_div.text.strip()


pageNumber = 1

# Loop through search pages
try:
    while True:
        # Get the current number of search results
        all_listados = driver.find_elements(By.CSS_SELECTOR, 'div.listado-item.item-ig')

        # Loop through search results on the current page
        for i in range(len(all_listados)):
            try:
                j = 1
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

                # Scroll the target element into view using JavaScript
                driver.execute_script("arguments[0].scrollIntoView();", target_span_scroll)
                # Click the element
                target_span.click()

                # Threading stuff
                thread = threading.Thread(target=scrape_element, args=(i, driver))
                thread.start()
                # Check the elapsed time in the main thread
                while thread.is_alive():
                    current_time = time.time()
                    elapsed_time = current_time - start_time

                    # If the thread takes too long (4+ seconds), stop it
                    if elapsed_time > 4:
                        print("exceeded 4 s")
                        thread.join()
                        break

                # Write to text file
                with open('C:\\Users\\goldi\\Downloads\\buisnessPhones\\phones.txt', 'a') as f:
                    f.write(f"Page {pageNumber}, element {i + 1}\n")
                    f.write(f"Name: {name}\n")
                    f.write(f"Category: {claim_text}\n")
                    f.write(f"Website: {website_url}\n")
                    f.write("Telephone Number: " + phone_number + "\n")
                    f.write(f"---------------- \n")

                current_time = time.time()
                elapsed_time = current_time - start_time
                print("index " + str(i + 1) + " logged in: " + str(elapsed_time) + "s")

                # Go back to the search results page
                driver.back()

            # Error with scraping result
            except Exception as e:
                # Handle individual result scraping exceptions
                print(f"Error scraping result {i + 1}: {str(e)}")

        pageNumber += 1

        # Check if there's a "Next" button and click it if it exists
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, 'i.fa.icon-flecha-derecha')
            driver.execute_script("arguments[0].scrollIntoView();", next_btn)
            driver.execute_script("arguments[0].click();", next_btn)
        except NoSuchElementException:
            print("No more 'Next' button. Exiting...")
            break


finally:
    # Quit the WebDriver
    print("Quitting...")
    driver.quit()
