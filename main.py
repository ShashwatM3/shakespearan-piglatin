from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

app = FastAPI(title="Fun OpenAI API")

# Allow requests from all origins (for simplicity)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Fun OpenAI API!"}

@app.get("/piglatin")
def piglatin(query: str = Query(..., description="Input text")):
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
          {"role": "system", "content": "Respond to all input text into Pig Latin."},
          {"role": "user", "content": query}
      ],
    )
    answer = completion.choices[0].message.content
    return {"query": query, "answer": answer}

@app.get("/shakespeare")
def shakespeare(query: str = Query(..., description="Input text")):
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
          {"role": "system", "content": "Respond to all input text into Shakespearean English."},
          {"role": "user", "content": query}
      ],
    )
    answer = completion.choices[0].message.content
    return {"query": query, "answer": answer}