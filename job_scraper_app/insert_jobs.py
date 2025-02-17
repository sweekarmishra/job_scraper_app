from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["job_scraper"]
collection = db["jobs"]

# Job data
jobs = [
    {"title": "Python Developer", "company": "Google", "location": "Noida", "salary": "₹12,00,000", "job_url": "https://example.com/job1"},
    {"title": "Django Developer", "company": "Microsoft", "location": "Bangalore", "salary": "₹15,00,000", "job_url": "https://example.com/job2"},
    {"title": "Backend Engineer", "company": "Amazon", "location": "Hyderabad", "salary": "₹18,00,000", "job_url": "https://example.com/job3"},
]

# Insert multiple jobs
collection.insert_many(jobs)

print("Jobs inserted successfully into MongoDB!")