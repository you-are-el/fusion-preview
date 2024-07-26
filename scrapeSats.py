from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This assumes chromedriver is in your system PATH
driver = webdriver.Chrome()

def collect_data_while_scrolling(url, output_file):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # Wait for the table to be present
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
    
    collected_data = set()  # Use a set to avoid duplicates
    seen_rows = set()

    try:
        while True:
            # Collect data
            table = driver.find_element(By.TAG_NAME, 'table')
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            rows = tbody.find_elements(By.TAG_NAME, 'tr')
            
            for row in rows:
                try:
                    row_id = row.get_attribute('data-index')
                    if row_id not in seen_rows:
                        cells = row.find_elements(By.TAG_NAME, 'td')
                        if len(cells) >= 4:
                            divs = cells[3].find_elements(By.TAG_NAME, 'div')
                            for div in divs:
                                sat_number = div.text
                                if sat_number.isdigit():
                                    collected_data.add(sat_number)
                                    break
                        seen_rows.add(row_id)
                except Exception as e:
                    print(f"Error processing row: {e}")
            
            print(f"Found {len(rows)} rows in the table.")
            print(f"Number of seen rows: {len(seen_rows)}")
            print(f"Collected data size: {len(collected_data)}")
            print(f"Collected Data: {list(collected_data)}")

            # Wait for a short period to allow for manual scrolling
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped by user")

    finally:
        driver.quit()
        # Write collected data to a file
        with open(output_file, 'w') as file:
            file.write(str(list(collected_data)))
        print(f"Data written to {output_file}")

# URL of the page to scrape
url = 'https://magiceden.io/ordinals/marketplace/rare-sats?attributes=%257B%2522Satributes%2522%253A%255B%257B%2522value%2522%253A%2522Palindrome%2522%252C%2522label%2522%253A%2522Palindrome%2522%252C%2522floor%2522%253A1e-8%257D%255D%252C%2522year%2522%253A%255B%257B%2522traitType%2522%253A%2522year%2522%252C%2522value%2522%253A%25222011%2522%252C%2522count%2522%253A0%252C%2522floor%2522%253A0%252C%2522image%2522%253A%2522%2522%252C%2522label%2522%253A%25222011%2522%252C%2522total%2522%253A0%257D%255D%257D&search='
output_file = 'collected_data.txt'
collect_data_while_scrolling(url, output_file)