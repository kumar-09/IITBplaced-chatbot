# main.py
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# 1️⃣ Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# 2️⃣ Initialize OpenAI client
client = OpenAI(api_key=api_key)

# 3️⃣ Load enriched jobs data
with open("data/enriched_jobs.json", "r", encoding="utf-8") as f:
    jobs_data = json.load(f)

# 4️⃣ Simple retrieval function (can be replaced with embeddings later)
def search_jobs(query):
    results = []
    for job in jobs_data:
        combined_text = " ".join(str(v) for v in job.values() if isinstance(v, str))
        if query.lower() in combined_text.lower():
            results.append(job)
    return results

# 5️⃣ Chatbot function
def chatbot():
    print("Placement Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        # 🔍 Retrieve relevant jobs
        matched_jobs = search_jobs(user_input)
        context = ""
        if matched_jobs:
            for job in matched_jobs[:1]:  # limit to top 3 matches
                context += f"- {job.get('title', 'N/A')} at {job.get('companyName', 'N/A')}, Sector: {job.get('sector', 'N/A')}, Salary: {job.get('currency', '')} {job.get('salary', 'N/A')}\n"
                print(context)
        else:
            context = "No direct matches found in the database."

        # 💬 Send to OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful placement assistant. Use the provided job data to answer questions."},
                {"role": "user", "content": f"User question: {user_input}\nHere is some relevant job data:\n{context}"}
            ]
        )

        print("Bot:", response.choices[0].message.content, "\n")

# 6️⃣ Run the chatbot
if __name__ == "__main__":
    chatbot()
