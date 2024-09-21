# Import necessary libraries for web scraping and data handling
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set browser options
options = Options()
options.headless = False # Set to True for headless mode (browser runs in the background)
#options.add_argument('window-size=1920x1080')

# Define the Audible Bestsellers URL and path to ChromeDriver
website = "https://www.audible.com/adblbestsellers?ref_pageloadid=not_applicable&ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=3c510bf6-cff4-47d1-bb27-1ba091ebb823&pf_rd_r=RVYH286Y8AH5KQAM0AQ9&pageLoadId=xgivS6OYW5vqk6AH&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482"
path = "/Users/saichaitanya/Downloads/chromedriver-mac-arm64/chromedriver" # Update with your ChromeDriver path

# Start Chrome browser session using Selenium
driver = webdriver.Chrome(path)
# driver = webdriver.Chrome(path, options=options)
driver.get(website)
driver.maximize_window()

# Find pagination element to determine the number of pages
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)

# Initialize empty lists to store audiobook data
titles = []
authors = []
runtime = []

# Loop through all pages and scrape data
current_page = 1
while current_page <= last_page:
    time.sleep(2) # Implicit wait of 2 seconds to allow the page to fully load

    # Wait for the product container to load using an explicit wait
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container")))
    # container = driver.find_element_by_class_name("adbl-impression-container")

    # Find all product elements on the current page
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH,'.//li[contains(@class, "productListItem")]')))
    # products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

    # Loop through each product and extract the title, author, and runtime
    for product in products:
        titles.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-pub-break-word")]').text)
        authors.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        runtime.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

    current_page += 1
    # Try to find and click the "Next" button to move to the next page
    try:
        next_page_button = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page_button.click()
    except:
        pass

# Close the browser session once all pages have been scraped
driver.quit()

df_books = pd.DataFrame({'title': titles, "authors": authors, 'runtime': runtime})
df_books.to_csv("books_bestsellers.csv", index=False)

