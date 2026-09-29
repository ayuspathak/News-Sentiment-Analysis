from imports import *

def scrape_sports(url, driver_path='chromedriver.exe'):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)

    # Wait until the page is fully loaded
    WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Initialize lists to store scraped data
    titles = []
    links = []

    try:
        wait = WebDriverWait(driver, 20)
        
        if url == "https://www.indiatoday.in/search/sports":
            divs = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'B1S3_content__wrap__9mSB6')))
            for div in divs:
                try:
                    h3_tag = div.find_element(By.TAG_NAME, 'h3')
                    titles.append(h3_tag.text)
                    link = h3_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    links.append(link)
                except NoSuchElementException:
                    continue
        
        elif url == "https://indianexpress.com/section/technology/":
            ul_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'article-list')))
            li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
            for li in li_elements:
                try:
                    h3_tag = li.find_element(By.TAG_NAME, 'h3')
                    titles.append(h3_tag.text)
                    link = h3_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    links.append(link)
                except NoSuchElementException:
                    continue
        elif url == "https://indianexpress.com/section/entertainment/":
            divs = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'articles')))
            for div in divs:
                try:
                    h2_tag = div.find_element(By.CLASS_NAME, 'title')
                    titles.append(h2_tag.text)
                    link = h2_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    links.append(link)
                except NoSuchElementException:
                    continue
        else:
            divs = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'articles')))
            for div in divs:
                try:
                    h2_tag = div.find_element(By.TAG_NAME, 'h2')
                    titles.append(h2_tag.text)
                    link = h2_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    links.append(link)
                except NoSuchElementException:
                    continue
    
    except TimeoutException:
        print("Elements not found using CLASS_NAME. Trying XPath.")
        try:
            divs = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="B1S3_B1__s3_widget__1S13T"]')))
            for div in divs:
                try:
                    h3_tag = div.find_element(By.TAG_NAME, 'h3')
                    titles.append(h3_tag.text)
                    link = h3_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    links.append(link)
                except NoSuchElementException:
                    continue
        except TimeoutException:
            print("Elements not found using XPath.")
    
    # Close the WebDriver
    driver.quit()
    
    return titles, links

# Usage example
# url = "https://indianexpress.com/section/technology/"
# titles, links = scrape_sports(url)
# print("Titles:", titles)
# print("Links:", links)
