import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get HTML content of a webpage
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve webpage:", response.status_code)
        return None

# Function to scrape job details from Indeed
def scrape_jobs(job_title, location, num_pages=1):
    base_url = "https://in.indeed.com/jobs"
    job_list = []
    
    for page in range(0, num_pages * 10, 10):  # Each page has 10 results
        url = f"{base_url}?q={job_title}&l={location}&start={page}"
        print(f"Scraping: {url}")
        
        html = get_html(url)
        if not html:
            continue
        
        soup = BeautifulSoup(html, "html.parser")
        job_cards = soup.find_all("div", class_="job_seen_beacon")  # Corrected class for job postings
        
        for job in job_cards:
            title_tag = job.find("h2", class_="jobTitle")
            company_tag = job.find("span", class_="companyName")
            location_tag = job.find("div", class_="companyLocation")
            salary_tag = job.find("div", class_="salary-snippet")  # Salary if available
            
            title = title_tag.text.strip() if title_tag else "N/A"
            company = company_tag.text.strip() if company_tag else "N/A"
            location = location_tag.text.strip() if location_tag else "N/A"
            salary = salary_tag.text.strip() if salary_tag else "Not mentioned"

            job_list.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Salary": salary
            })

    return job_list

# Main function
if __name__ == "__main__":
    job_title = "Python Developer"
    location = "Noida, Uttar Pradesh"
    
    jobs = scrape_jobs(job_title, location, num_pages=2)  # Scrape 2 pages
    if jobs:
        df = pd.DataFrame(jobs)
        df.to_csv("indeed_jobs.csv", index=False)
        print("Jobs scraped successfully and saved to indeed_jobs.csv")
    else:
        print("No jobs found. Please check if Indeed has changed its structure.")