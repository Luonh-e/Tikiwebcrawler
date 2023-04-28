from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time

# Create an instance of Chrome driver
driver_path = "/usr/local/bin/"
browser = webdriver.Chrome(driver_path)

# Navigate to website Tiki.vn > Laptop category
browser.get("https://tiki.vn/laptop/c8095")

# Select all product items by CSS Selector
list_product_link = []
products = browser.find_elements(By.CSS_SELECTOR, ".product-item")
for product in products:
    outer_html = product.get_attribute("outerHTML")
    product_link = re.search('href="(.*?)"', outer_html).group(1)
    # product_link = "https://" + product_link
    list_product_link.append(product_link)

# Go to each product link
for product_link in list_product_link:
    print("DEBUG: " + product_link)

    # Go to product link
    try:
        browser.get("https://" + product_link)
    except:
        browser.get("https://tiki.vn" + product_link)

    # Extract product information by CSS Selector
    product_title = browser.find_elements(By.CSS_SELECTOR, ".title")[1].text
    print("DEBUG TITLE: " + product_title)

    # Extract product brand by CSS Selector then remove redundant data by Regular Expression
    # product_brand = browser.find_elements_by_css_selector(".brand-and-author")[0].get_attribute("outerHTML")
    product_brand = browser.find_elements(By.XPATH, "//a[@data-view-id='pdp_details_view_brand']")[0].text
    # product_brand = re.search('brand">(.*?)</a>', product_brand).group(1)
    print("DEBUG BRAND: " + product_brand)

    # Extract product price
    product_price = browser.find_elements(By.CSS_SELECTOR, ".product-price__current-price")[0].text
    product_price = re.search('^[\\d|\\.|\\,]+', product_price).group(0)
    print("DEBUG PRICE: " + product_price)

    # Extract product images
    image_urls = []
    image_elements = browser.find_elements(By.CLASS_NAME, '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div[1]/div[1]/div[1]/div/div/div/picture/img')
    for image_element in image_elements:
        image_src = image_element.get_attribute("src")
        image_urls.append(image_src)
    
    print(image_urls)
    
    # Extract colors

    # Extract sizes

    # Extract product details

    # Extract product description

    time.sleep(5)

# Close the browser
browser.quit()
