
import scrapy

# This is a spider class for scraping job postings from LinkedIn. 
class LinkedJobsSpider(scrapy.Spider):
    name = "linkedin_jobs"    # name of the spider
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%2BScientist&location=canada&geoId=&trk=public_jobs_jobs-search-bar_search-submit&start=' 
    
    # This method is called when the spider is started.
    # Send a request to the LinkedIn with the starting URL and calls the `parse_job` method to handle the response.          
    def start_requests(self):  
        first_job_on_page = 50
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})
     
    # Parse the job details from the response of LinkedIn job search API.
    def parse_job(self, response):
        first_job_on_page = response.meta['first_job_on_page'] # Get the value of the `first_job_on_page` key

        job_item = {}  # Initialize an empty dictionary for the job item
        jobs = response.css("li") # Get a list of job postings from the response

        # Print the number of job postings returned
        num_jobs_returned = len(jobs)
        print("******* Num Jobs Returned *******")
        print(num_jobs_returned)
        print('*****')
        
        # Extract the job title, job detail link, job listed time, company name, company link, and company location.
        for job in jobs:
            job_item['job_title'] = job.css("h3::text").get(default='not-found').strip()
            job_item['job_detail_link'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
            job_item['job_listed_time'] = job.css('time::text').get(default='not-found').strip()
            job_item['company_name'] = job.css('h4 a::text').get(default='not-found').strip()
            job_item['company_link'] = job.css('h4 a::attr(href)').get(default='not-found')
            job_item['company_location'] = job.css('.job-search-card__location::text').get(default='not-found').strip()
            yield job_item
        
        ### REQUEST NEXT PAGE OF JOBS ###
        # If there are more job postings to scrape, it updates the `first_job_on_page` variable 
        # and sends another request to the LinkedIn with the updated URL and metadata.
        if num_jobs_returned > 0:
            first_job_on_page = int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})