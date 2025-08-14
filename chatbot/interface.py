# interface.py
import json
from chatbot.processor import JobProcessor
from chatbot.models import JobEnriched

class JobInterface:
    def __init__(self, sectors_path):
        self.processor = JobProcessor(sectors_path)

    def process_jobs(self, jobs):
        enriched_jobs = []
        for job in jobs:
            enriched = self.processor.process_job(job)
            enriched_jobs.append(JobEnriched(**enriched).dict())
        return enriched_jobs
