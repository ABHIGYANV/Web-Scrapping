import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Function to scrape the details of a project
def scrape_project_details(driver, project_url):
    driver.get(project_url)
    time.sleep(3)  # Allowing some time for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Extracting project details
    details = {}
    details['GSTIN No'] = soup.find('div', text='GSTIN No.').find_next_sibling('div').text.strip()
    details['PAN No'] = soup.find('div', text='PAN No.').find_next_sibling('div').text.strip()
    details['Name'] = soup.find('div', text='Name').find_next_sibling('div').text.strip()
    details['Permanent Address'] = soup.find('div', text='Permanent Address').find_next_sibling('div').text.strip()
    
    return details

# Function to scrape the list of projects under the Registered section
def scrape_registered_projects():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # To run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    
    # Navigating to the website
    driver.get("https://hprera.nic.in/PublicDashboard")
    time.sleep(3)  # Allowing some time for the page to load
    
    # Navigating to the Registered section
    driver.find_element_by_link_text('Registration').click()
    time.sleep(1)
    driver.find_element_by_link_text('Real Estate Project').click()
    time.sleep(1)
    driver.find_element_by_link_text('Search Projects').click()
    time.sleep(1)
    driver.find_element_by_link_text('Registered').click()
    time.sleep(3)
    
    # Scraping project details
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    project_items = soup.find_all('div', class_='col-sm-12 col-md-6 col-lg-4 mb-4')

    registered_projects = []
    for project in project_items[:5]:
        project_link = project.find('a')['href']
        project_details = scrape_project_details(driver, project_link)
        registered_projects.append(project_details)
    
    driver.quit()
    
    return registered_projects

# Main function to run the scraper
def main():
    registered_projects = scrape_registered_projects()
    
    # Displaying the results
    for idx, project in enumerate(registered_projects, 1):
        print(f"Project {idx}:")
        for key, value in project.items():
            print(f"{key}: {value}")
        print()

if __name__ == "__main__":
    main()
