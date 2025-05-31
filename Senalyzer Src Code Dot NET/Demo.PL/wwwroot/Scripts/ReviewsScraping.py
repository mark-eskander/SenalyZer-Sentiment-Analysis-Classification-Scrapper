#def scrape_reviews(url, api_endpoint, chromedriver_path):
#    import os
#    import sys
#    sys.path.append(r'C:\Users\LapStore\Desktop\IronPython_Lib') 
#    import requests
#    from selenium import webdriver
#    from selenium.webdriver.chrome.service import Service
#    from selenium.webdriver.common.by import By
#    from selenium.common.exceptions import NoSuchElementException
#    from time import sleep
#
#    # Verify the ChromeDriver path
#    if not os.path.isfile(chromedriver_path):
#        raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")
#
#    # Create a new service object with ChromeDriver executable path
#    service = Service(chromedriver_path)
#    
#    # Create a new instance of Chrome WebDriver with the service
#    driver = webdriver.Chrome(service=service)
#    
#    # Open the provided URL
#    driver.get(url)
#    
#    driver.maximize_window()
#    
#    try:
#        more_review_button = driver.find_element(By.XPATH, "(//a[@class='a-link-emphasis a-text-bold'])")
#        more_review_button.click()
#        reviews = []
#        for i in range(100):
#            print('Scraping page', i + 1)
#            review_elements = driver.find_elements(By.XPATH, "//span[@class='a-size-base review-text review-text-content']")
#            for review in review_elements:
#                reviews.append(review.text)
#            try:
#                next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
#                next_button.click()
#                sleep(10)
#            except NoSuchElementException:
#                print("No more pages to scrape. Stopping.")
#                break
#
#        driver.quit()
#
#        # Send the reviews to the API endpoint
#        response = requests.post(api_endpoint, json={'reviews': reviews})
#        
#        if response.status_code == 200:
#            print("Sentiment analysis results:", response.json())
#            return "Done!"  # Return a value indicating success
#        else:
#            return f"Failed to send data. Status code: {response.status_code}"
#
#    except NoSuchElementException:
#        print("The Product has no Reviews.")
#        return "No reviews found"  # Return a value indicating no reviews found
#
#def test():
#    # Example usage
#    url = "https://www.amazon.eg/%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%D8%AC-%D8%A7%D9%84%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A-%D8%AC%D9%8A%D8%AC%D8%A7%D8%A8%D8%A7%D9%8A%D8%AA-%D9%85%D9%8A%D8%AC%D8%A7%D8%A8%D9%8A%D9%83%D8%B3%D9%84-%D8%AA%D9%8A%D8%AA%D8%A7%D9%86%D9%8A%D9%88%D9%85/dp/B0CQZ1JYNY/ref=sr_1_4_sspa?crid=22BPXGXRTZ558&dib=eyJ2IjoiMSJ9.FFP80PRhuyLh6X04fEr5pXn3Mgsjn1UXKdkGbXkRvsBXZBwgjxx-FR_t3NKM2-Emw7Xbf-Dbo-6zvH91eN2Z7lieA61_pw8XTurLqXh4nkgewXcmmV_Kkqq2Vz8QTlT7XeMl9ObdoYVewATmFKa4ZYRVfEbHmtA7oi5BGfJalkn29CCQhJKNUKKIOaKdp3LufRSTFr0n7UqbtnhGXaz8bNdi54w3E17fWWzvrbjj8zw9tk-ZDpzg2JkrxQDiWvarddUscDI9cyGEEc93vNCdZl-phFWN9n8vaJvVG6ihj5I.ZD2Y1HHuqusNjXgg6zz2uVXvkeOe8ID0y-zPd72rhLc&dib_tag=se&keywords=mobile&qid=1717357211&sprefix=mobile%2Caps%2C203&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
#    api_endpoint = "https://scrapping-qc6w.onrender.com/submit-reviews"  # Update this to match your FastAPI endpoint
#    chromedriver_path = r'C:\Users\LapStore\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'
#    
#    return scrape_reviews(url, api_endpoint, chromedriver_path)  # Ensure the function returns a value
#
## Call the test function directly
#print(test())  



#import os
#import sys
#import requests
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
#from time import sleep
#
#def scrape_reviews(url, api_endpoint, chromedriver_path):
#    # Verify the ChromeDriver path
#    if not os.path.isfile(chromedriver_path):
#        raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")
#
#    # Create a new service object with ChromeDriver executable path
#    service = Service(chromedriver_path)
#    
#    # Create a new instance of Chrome WebDriver with the service
#    driver = webdriver.Chrome(service=service)
#    
#    # Open the provided URL
#    driver.get(url)
#    
#    driver.maximize_window()
#    
#    try:
#        more_review_button = driver.find_element(By.XPATH, "(//a[@class='a-link-emphasis a-text-bold'])")
#        more_review_button.click()
#        reviews = []
#        for i in range(100):
#            print('Scraping page', i + 1)
#            review_elements = driver.find_elements(By.XPATH, "//span[@class='a-size-base review-text review-text-content']")
#            for review in review_elements:
#                reviews.append(review.text)
#            try:
#                next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
#                next_button.click()
#                sleep(10)
#            except NoSuchElementException:
#                print("No more pages to scrape. Stopping.")
#                break
#
#        driver.quit()
#
#        # Send the reviews to the API endpoint
#        response = requests.post(api_endpoint, json={'reviews': reviews})
#        
#        if (response.status_code == 200):
#            print("Sentiment analysis results:", response.json())
#            return "Done!"  # Return a value indicating success
#        else:
#            return f"Failed to send data. Status code: {response.status_code}"
#
#    except NoSuchElementException:
#        print("The Product has no Reviews.")
#        return "No reviews found"  # Return a value indicating no reviews found
#
#def main():
#    if len(sys.argv) != 2:
#        print("Usage: script.py <url>")
#        return
#
#    url = sys.argv[1]
#    api_endpoint = "https://scrapping-qc6w.onrender.com/submit-reviews"
#    chromedriver_path = r'C:\Users\LapStore\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'
#    
#    result = scrape_reviews(url, api_endpoint, chromedriver_path)
#    print(result)
#
#if __name__ == "__main__":
#    main()

import os
import sys
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def scrape_reviews(url, api_endpoint, chromedriver_path):
    sys.path.append(r'C:\Users\LapStore\Desktop\IronPython_Lib')

    if not os.path.isfile(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.maximize_window()
    
    try:
        more_review_button = driver.find_element(By.XPATH, "(//a[@class='a-link-emphasis a-text-bold'])")
        more_review_button.click()
        reviews = []
        for i in range(100):
            review_elements = driver.find_elements(By.XPATH, "//span[@class='a-size-base review-text review-text-content']")
            for review in review_elements:
                reviews.append(review.text)
            try:
                next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
                next_button.click()
                sleep(10)
            except NoSuchElementException:
                break

        driver.quit()

        response = requests.post(api_endpoint, json={'reviews': reviews})
        
        if response.status_code == 200:
            result = response.json()
            return json.dumps({
                'positive_percentage': round(result['positive_percentage'], 2),
                'negative_percentage': round(result['negative_percentage'], 2)
            })
        else:
            return json.dumps({'error': 'Failed to send data. Status code: ' + str(response.status_code)})

    except NoSuchElementException:
        return json.dumps({'error': 'No reviews found'})

if __name__ == "__main__":
    url = sys.argv[1]
    api_endpoint = "https://scrapping-qc6w.onrender.com/submit-reviews"
    chromedriver_path = r'C:\Users\LapStore\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    print(scrape_reviews(url, api_endpoint, chromedriver_path))
