# JSON Schema Description

- `job_title`: The title of the job posting.
- `job_detail_link`': A link to the job posting details.
- `job_listed_time`: How long ago the job posting was uploaded to LinkedIn.
- `company_name` :The name of the company posting the job on LinkedIN.
- `company_link`: A link to the company's page.
- `company_location`: The location of the company.


# JSON Schema

```json
{
  "title": "jobs",
  "description": "The job postings for a data scientist/analyst position.",
  "required": [
    "job_title",
    "job_detail_link",
    "job_listed_time",
    "company_name",
    "company_link",
    "company_location"
  ],
  "properties": {
    "job_title": {
      "type": "string",
      "description": "The title of the job posting."
    },
    "job_detail_link": {
      "type": "string",
      "format": "url",
      "description": "A link to the job posting details."
    },
    "job_listed_time": {
      "type": "string",
      "format": "date-time",
      "description": "How long ago the job posting was uploaded to LinkedIn."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the company posting the job on LinkedIN."
    },
    "company_link": {
      "type": "string",
      "format": "url",
      "description": "A link to the company's page."
    },
    "company_location": {
      "type": "string",
      "description": "The location of the company."
    }
  }
}
