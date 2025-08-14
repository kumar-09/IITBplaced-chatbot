import json
import os

# Load data
def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

departments = load_json("data/departments.json")
specializations = load_json("data/specializations.json")
sectors = load_json("data/sectors.json")
programs = load_json("data/programs.json")
jobs = load_json("data/jobs.json")

# Helper functions
def get_department_by_id(dep_id):
    return next((d for d in departments if d["id"] == dep_id), None)

def get_specializations_by_department(dep_id):
    return [s for s in specializations if s["departmentId"] == dep_id]

def get_sector_by_id(sector_id):
    return next((s for s in sectors if s["id"] == sector_id), None)

def get_jobs_by_sector_name(sector_name):
    matching_sectors = [s for s in sectors if sector_name.lower() in s["name"].lower()]
    sector_ids = {s["id"] for s in matching_sectors}
    return [j for j in jobs if j.get("sectorId") in sector_ids]

# Chat loop
def chatbot():
    print("📢 College Placement Chatbot (offline) — type 'exit' to quit")
    while True:
        query = input("\nYou: ").strip().lower()
        if query == "exit":
            break
        
        # Example rules
        if "data science" in query:
            results = get_jobs_by_sector_name("Data Science")
            print(f"Found {len(results)} job(s) in Data Science sector:")
            for r in results[:5]:
                print("-", r["title"], "at", r["company"]["name"])
        
        elif "specialization" in query and "aerospace" in query:
            dept = next((d for d in departments if "aerospace" in d["name"].lower()), None)
            if dept:
                specs = get_specializations_by_department(dept["id"])
                print(f"Specializations in {dept['name']}:")
                for s in specs:
                    print("-", s["name"])
            else:
                print("No matching department found.")
        
        else:
            print("Sorry, I don't understand yet. Try asking about jobs, sectors, or specializations.")

chatbot()
