-- SQLite
SELECT company_name, job_title ,company_location, job_listed_time
FROM preprocessed_jobs
WHERE company_location = "Toronto"
AND job_listed_time < 7;